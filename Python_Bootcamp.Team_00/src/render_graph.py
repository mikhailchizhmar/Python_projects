import os
import json
import networkx
import nx_altair
import matplotlib.pyplot as plt
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    if os.getenv("WIKI_FILE"):
        wiki_path = os.getenv("WIKI_FILE")
    else:
        print("WIKI_FILE env variable must be set. Geting WIKI_FILE from wiki.json")
        wiki_path = "wiki.json"
    try:
        graph = json.load(open(wiki_path, "r"))
        graph = networkx.node_link_graph(graph)
        nodes = list(graph.nodes())
        size = [graph.degree(node) for node in nodes]

        networkx.draw(
            graph,
            nodelist=nodes,
            node_size=size,
            with_labels=True,
            font_size=0.3,
            width=0.01,
        )

        plt.savefig("wiki_graph.png", dpi=1200)

        for idx, node in enumerate(graph.nodes()):
            graph.nodes[node]["size"] = graph.degree(node)

        plt.rcParams["figure.figsize"] = [7, 7]

        html = nx_altair.draw_networkx(
            graph,
            node_size="size",
            font_size=0.3,
            width=0.01,
            node_tooltip=["size"],
        )
        html.save("wiki_graph.html")
    except Exception as e:
        print(f"Error while script running:\n{e}\nTerminate")
