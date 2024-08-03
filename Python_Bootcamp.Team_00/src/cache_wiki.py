import argparse
import asyncio
import json
import logging
import logging.config
import os
from urllib.parse import quote, unquote

import aiohttp
import networkx as nx  # type: ignore[import-untyped]
import py2neo  # type: ignore[import-untyped]
from bs4 import BeautifulSoup  # type: ignore[import-untyped]
from dotenv import load_dotenv

logger = logging.getLogger("cache_wiki")
lock = asyncio.Lock()


def setup_logging():
    with open("logging_config.json", "r") as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)


class WikiParser:
    wiki_base_link: str = "https://en.wikipedia.org"

    def __init__(
        self,
        base_article: str,
        deep: int = 3,
        *,
        is_directed: bool = True,
    ) -> None:
        if deep < 0:
            raise ValueError("The value of 'deep' must be greater than or equal to 0")

        self.base_article = base_article
        self.deep = deep

        self.collected_data: set[str] = set()
        self.graph = nx.DiGraph() if is_directed else nx.Graph()
        self.__links_collected: int = 0
        self.max_links = 1000
        self.k_workers = 10 if deep < 2 else 40
        self.queue: asyncio.Queue = asyncio.Queue()
        self.semaphore = asyncio.Semaphore(int(self.k_workers * 0.5))

    def name_article_to_url(self, articl_name: str) -> str:
        return (
            self.wiki_base_link
            + "/wiki/"
            + quote(articl_name.replace(" ", "_"), encoding="utf-8")
        )

    def url_to_name_article(self, url: str) -> str:
        return unquote(url.split("/")[-1].replace("_", " "))

    def _extract_relative_links(self, html_data: str):
        soup = BeautifulSoup(html_data, "html.parser")

        start_tag = soup.find("span", {"id": "See_also", "class": "mw-headline"})
        if start_tag is None:
            title = soup.find("title").text
            logger.info(f"Not found links {title}")
            return []

        end_tag = start_tag.parent.next.find_next("span", {"class": "mw-headline"})
        relative_links = []
        for tag in start_tag.find_all_next():
            if tag == end_tag:
                break
            if tag.name == "a" and tag.get("href", "").startswith("/wiki/"):
                relative_links.append(tag.get("href"))
        return relative_links

    def _get_full_links(self, relative_links: list[str]) -> list[str]:
        links = list(
            map(
                lambda relative_link: self.wiki_base_link + relative_link,
                relative_links,
            )
        )
        return links

    async def get_links_from_url(self, url: str) -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()

                logger.info(f"Start extract data from {url=}")

                relative_links = self._extract_relative_links(html)
                links = self._get_full_links(relative_links)

                logger.info(f"Extracred {len(relative_links)} links {url=}")

                return links

    def _update_graph(self, main_url: str, urls: list[str]):
        main_name_article = self.url_to_name_article(main_url)
        self.__links_collected += len(urls)

        self.collected_data.add(main_name_article)
        self.graph.add_node(main_name_article)
        self.graph.add_edges_from(
            [(main_name_article, self.url_to_name_article(url)) for url in urls]
        )

    async def fetch_worker(self):
        logger.debug(f"Created worker {asyncio.current_task().get_name()}")
        while True:
            url, deep = await self.queue.get()
            if self.__links_collected >= self.max_links:
                self.queue.task_done()
                continue
            try:
                urls = await self.get_links_from_url(url)
                self._update_graph(main_url=url, urls=urls)

                for url in urls:
                    if deep == 0 or url in self.collected_data:
                        continue
                    if self.__links_collected >= self.max_links:
                        break
                    await self.queue.put((url, deep - 1))
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                logger.error(f"Failed to fetch {url}: {e}")
            except Exception as e:
                logger.exception(f"Unexpected error occurred while fetching {url}: {e}")
            finally:
                self.queue.task_done()

    async def _fetch_urls(self, url, deep):
        await self.queue.put((url, deep))

        workers = [
            asyncio.create_task(self.fetch_worker(), name=f"worker-{i + 1}")
            for i in range(self.k_workers)
        ]

        await self.queue.join()

        for worker in workers:
            worker.cancel()
            logger.debug(f"Stoped worker-{worker.get_name()}")

    async def run(self):
        logger.info("Start processing")
        await self._fetch_urls(
            self.name_article_to_url(self.base_article), deep=self.deep
        )
        logger.info(f"Number of pages processed = {self.__links_collected}")
        self.save_data()

    def save_data(self):
        load_dotenv()
        save_path = os.getenv("WIKI_FILE", "wiki.json")
        if not (save_path := os.getenv("WIKI_FILE")):
            logger.info(
                "WIKI_FILE env variable must be set. Geting WIKI_FILE from wiki.json"
            )
            save_path = "wiki.json"

        with open(save_path, "w") as f:
            f.write(json.dumps(nx.node_link_data(pareser.graph), indent=4))


def save_graph_in_db(
    graph: nx.Graph | nx.DiGraph,
    url: str = "bolt://localhost:7687",
    auth: tuple[str, str] = ("neo4j", "password"),
):
    # View the result of saving the graph `http://localhost:7474`
    # `MATCH (n)-[r]->(m) RETURN n, r, m` - start execution in the neo4j runline

    connect = py2neo.Graph(url, auth=auth)
    connect.delete_all()

    for node in graph.nodes:
        connect.create(py2neo.Node("Node", name=node))

    for edge in graph.edges:
        node1 = connect.nodes.match("Node", name=edge[0]).first()
        node2 = connect.nodes.match("Node", name=edge[1]).first()
        relationship = py2neo.Relationship(node1, "CONNECTS_TO", node2)
        connect.create(relationship)


def get_args() -> tuple[str, int, bool]:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-p", type=str, default="Harry Potter", required=False)
    arg_parser.add_argument("-d", type=int, default=3, required=False)
    arg_parser.add_argument("-s", type=bool, default=False, required=False)
    args = arg_parser.parse_args()

    return args.p, args.d, args.s


if __name__ == "__main__":
    setup_logging()
    base_article, deep, is_save_db = get_args()
    pareser = WikiParser(
        base_article=base_article,
        deep=deep,
        is_directed=True,
    )
    asyncio.run(pareser.run())

    if is_save_db:
        save_graph_in_db(graph=pareser.graph)
