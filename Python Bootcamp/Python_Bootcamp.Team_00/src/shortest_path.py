import argparse
import json
import os
from dotenv import load_dotenv
from collections import deque


def load_graph(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data = json.load(f)

    graph = {}
    for node in data["nodes"]:
        graph[node["id"]] = []

    for link in data["links"]:
        graph[link["source"]].append(link["target"])

    return graph


def bfs_shortest_path(
    graph: dict, start: str, goal: str, non_directed: bool
) -> tuple[list[str], int] | tuple[None, None]:
    if start not in graph or goal not in graph:
        return None, None

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path, len(path) - 1

        visited.add(current)

        neighbors = graph[current]

        if non_directed:
            for node, edges in graph.items():
                if current in edges:
                    neighbors.append(node)

        for n in neighbors:
            if n not in visited:
                queue.append((n, path + [n]))

    return None, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from", dest="start", type=str, required=True, help="Start page"
    )
    parser.add_argument("--to", dest="end", type=str, required=True, help="End page")
    parser.add_argument(
        "--non-directed",
        dest="nd",
        action="store_true",
        help="Treats links as non-directed",
    )
    parser.add_argument("-v", action="store_true", help="Prints path")
    args = parser.parse_args()

    load_dotenv()
    wiki_file = os.getenv("WIKI_FILE", "wiki.json")
    if not os.path.exists(wiki_file):
        print("database not found")
        exit()

    graph = load_graph(wiki_file)
    path, length = bfs_shortest_path(graph, args.start, args.end, args.nd)

    if path is None:
        print("path not found")
    else:
        if args.v:
            print(" -> ".join(f"'{node}'" for node in path))
        print(length)


if __name__ == "__main__":
    main()
    # python shortest_path.py --from "Harry Potter" --to "Portal:Schools" -v
    # 3
    # python shortest_path.py --from "Harry Potter" --to "Harry Potter" -v
    # 0
    # python shortest_path.py --from "Harry Potter" --to "Iyashikei" -v --non-directed
    # 4
    # python shortest_path.py --from "The Worst Witch" --to "Slice of life" -v
    # 2
    # python shortest_path.py --from "Mary Poppins (book series)" --to "Harry Potter" -v --non-directed
    # 1
    # python shortest_path.py --from "Mary Poppins (book series)" --to "Harry Potter" -v
    # path not found
