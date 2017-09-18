import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,5),(1,3),(1,2),(1,4),(4,5)])

def main():
	d = nx.coloring.greedy_color(G, strategy=nx.coloring.strategy_largest_first)
	print d
	
main()
