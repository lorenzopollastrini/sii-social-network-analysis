import dwave_networkx as dnx
from dwave.system import DWaveSampler, EmbeddingComposite

from drawing import draw_min_vertex_cover, draw_structural_imbalance
from loader import load_data


G = load_data()

sampler = EmbeddingComposite(DWaveSampler())

# Minimum vertex cover
min_vertex_cover = dnx.min_vertex_cover(G, sampler, label='Harry Potter - Minimum Vertex Cover')
print(f'Minimum vertex cover: {min_vertex_cover}')
draw_min_vertex_cover(G, min_vertex_cover)

# Structural imbalance
frustrated_edges, colors = dnx.structural_imbalance(G, sampler, label='Harry Potter - Structural Imbalance')
print('Structural imbalance: ', len(frustrated_edges), 'violations out of', len(G.edges), 'edges')
draw_structural_imbalance(G, colors)
