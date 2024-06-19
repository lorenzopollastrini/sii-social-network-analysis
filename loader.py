import csv
import os

import networkx as nx


def load_data():
    G = nx.Graph()

    dataset_directory = 'dataset'
    relations_file_path = os.path.join(dataset_directory, 'relations.csv')

    with open(relations_file_path) as relations:
        reader = csv.reader(relations)

        next(reader)  # Skip header

        for row in reader:
            u, v, sign = row
            if sign == '+':
                G.add_edge(u, v, sign=1)
            elif sign == '-':
                G.add_edge(u, v, sign=-1)

    return G