#creating a simple graph

class Graph(object):
	def __init__(self):
		self.nodes = {}

	def add_node(self, node):
		if node.name not in self.nodes.keys():
			self.nodes[node.name] = [node.edges, node.data]
		else:
			print("Node "+node.name+" already in graph")

	#pass in the names of the two nodes to be connected by an edge. Bidriectional.		
	def add_edge(self, node1, node2):
		if node2.name in node1.edges or node1.name in node2.edges:
			print("Node "+node1.name+" and "+node2.name+" are already connected by an edge")
		else:
			node1.edges.append(node2.name)
			node2.edges.append(node1.name)
			print("Added edge between "+node1.name+"--"+node2.name)


	def print_graph(self):
		for node in self.nodes.keys():
			print(node+ " ** Edges= " + str(self.nodes[node][0]) + " ** Data= " + str(self.nodes[node][1]))

class Node(object):
	def __init__(self, data=None, name=None):
		self.data = data
		self.edges = []
		self.name = name


g = Graph()
n0 = Node(12, "a")
n1 = Node(3456, "b")
n2 = Node(39, "c")
n3 = Node(1, "d")
n4 = Node(7, "e")
n5 = Node(9, "a")
g.add_node(n0)
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_node(n5)
g.add_edge(n0,n4)
g.add_edge(n0,n3)
g.add_edge(n2,n3)
g.add_edge(n5,n2)
g.print_graph()