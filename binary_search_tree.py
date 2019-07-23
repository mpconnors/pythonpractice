class Node(object):
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class BST(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(data, self.root)

	def _insert(self, data, cur_node):
		 if data < cur_node.data:
		 	if cur_node.left is None:
		 		cur_node.left = Node(data)
		 	else:
		 		self._insert(data, cur_node.left)
		 elif data > cur_node.data:
		 	if cur_node.right is None:
		 		cur_node.right = Node(data)
		 	else:
		 		self._insert(data, cur_node.right)
		 else:
		 	print("data is already in Binary Search Tree")

	def find(self, data):
		if self.root:
			is_found = self._find(data, self.root)
			if is_found:
				return True
			return False
		else:
			return None

	def _find(self, data, cur_node):
		if data > cur_node.data and cur_node.right:
			return self._find(data, cur_node.right)
		elif data < cur_node.data and cur_node.left:
			return self._find(data, cur_node.left)
		if data == cur_node.data:
			return True


	def printTree(self, travType):
		if travType == "preOrder":
			return self.preOrderPrint(bst.root, "")
		if travType == "inOrder":
			return self.inOrderPrint(bst.root, "")
		if travType == "postOrder":
			return self.postOrderPrint(bst.root, "")

		return print("Traversal type "+ travType + " is not supported")
	def preOrderPrint(self, start, traversal):
		if start:
			traversal += (str(start.data)+ "--")
			traversal = self.preOrderPrint(start.left, traversal)
			traversal = self.preOrderPrint(start.right, traversal)
		return traversal
	def inOrderPrint(self, start, traversal):
		if start:
			traversal = self.inOrderPrint(start.left, traversal)
			traversal += (str(start.data) + "->")
			traversal = self.inOrderPrint(start.right, traversal)
		return traversal
	def postOrderPrint(self, start, traversal):
		#L->R->Root
		if start:
			traversal = self.inOrderPrint(start.left, traversal)
			traversal = self.inOrderPrint(start.right, traversal)
			traversal += (str(start.data) + "->")
		return traversal

bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(50)
bst.insert(26)
bst.insert(13)
bst.insert(77)
print(bst.printTree("inOrder"))
print(bst.find(16))

