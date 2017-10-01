import networkx as nx

class graphColour():	
	@staticmethod
	def colour(nodes, edges):
		G=nx.Graph()
		G.add_nodes_from(nodes)
		G.add_edges_from(edges)
			
		return nx.coloring.greedy_color(G, strategy=nx.coloring.strategy_largest_first)
		
