import matplotlib.pyplot as plt
import networkx as nx


def draw_min_vertex_cover(G, min_vertex_cover):
    node_color = [1 if v in min_vertex_cover else 0 for v in G.nodes]

    # Only draw edges with an endpoint outside the minimum vertex cover
    edgelist = [(u, v) for u, v in G.edges if (u not in min_vertex_cover) or (v not in min_vertex_cover)]

    plt.figure(figsize=(15, 15))
    nx.draw(
        G,
        pos=nx.bipartite_layout(sorted(G, key=int), sorted(min_vertex_cover, key=int)),
        with_labels=True,
        edgelist=edgelist,
        node_color=node_color,
        cmap=plt.get_cmap('PuOr'),
        font_color='whitesmoke'
    )
    plt.savefig('min_vertex_cover.png')


def draw_structural_imbalance(G, colors):
    node_color = [colors[v] for v in G.nodes]

    frustrated_edgelist = []
    for u, v in G.edges:
        if colors[u] != colors[v] and G[u][v]['sign'] > 0:
            frustrated_edgelist.append((u, v))
        elif colors[u] == colors[v] and G[u][v]['sign'] < 0:
            frustrated_edgelist.append((u, v))
    frustrated_edge_color = [G[u][v]['sign'] for u, v in frustrated_edgelist]

    plt.figure(figsize=(10, 10))
    nx.draw(
        G,
        pos=nx.circular_layout(sorted(sorted(G, key=int), key=lambda node: colors[node])),
        with_labels=True,
        edgelist=frustrated_edgelist,
        node_color=node_color,
        cmap=plt.get_cmap('PuOr'),
        edge_color=frustrated_edge_color,
        edge_cmap=plt.get_cmap('RdYlGn'),
        font_color='whitesmoke'
    )
    plt.savefig('structural_imbalance.png')
