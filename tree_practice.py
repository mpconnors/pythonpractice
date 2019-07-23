#binary tree

class Node(object):
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class Stack(object):
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()

	def is_empty(self):
		return len(self.items) == 0

	def peek(self):
		if not self.is_empty():
			return self.items[-1].data

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)

class Queue(object):
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()

	def is_empty(self):
		if len(self.items) == 0:
			return True
		return False

	def peek(self):
		if not self.is_empty():
			return self.items[-1].data

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)



class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def printTree(self, travType):
		if travType == "preOrder":
			return self.preOrderPrint(tree.root, "")
		if travType == "inOrder":
			return self.inOrderPrint(tree.root, "")
		if travType == "postOrder":
			return self.postOrderPrint(tree.root, "")
		if travType == "levelOrder":
			return self.levelOrderPrint(tree.root)
		if travType == "reverselevelOrder":
			return self.reverseLevelOrderPrint(tree.root)

		return print("Traversal type "+ travType + " is not supported")

	#Root->Left->Right
	def preOrderPrint(self, start, traversal):
		if start:
			traversal += (str(start.data)+ "--")
			traversal = self.preOrderPrint(start.left, traversal)
			traversal = self.preOrderPrint(start.right, traversal)
		return traversal

	#print L->Root->R
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

	def levelOrderPrint(self, start):
		if start is None:
			return
		q = Queue()
		q.enqueue(start)
		traversal = ""

		while len(q) > 0:
			traversal += (str(q.peek())+"-")
			node = q.dequeue()
			if node.left:
				q.enqueue(node.left)
			if node.right:
				q.enqueue(node.right)
		return 

	def reverseLevelOrderPrint(self, start):
		 if start is None:
		 	return
		 q = Queue()
		 s = Stack()

		 q.enqueue(start)
		 traversal = ""

		 while len(q) > 0:
		 	node = q.dequeue()
		 	s.push(node)

		 	if node.right:
		 		q.enqueue(node.right)
		 	if node.left:
		 		q.enqueue(node.left)
		 while len(s) > 0:
		 	node = s.pop()
		 	traversal += (str(node.data)+ "-")
		 return traversal

	def height(self, node):
		if node is None:
			return -1
		left_height = self.height(node.left)
		right_height = self.height(node.right)

		return 1 + max(left_height, right_height)

	def size(self):
		if self.root is None:
			return 0
		s = Stack()
		s.push(self.root)
		size = 1
		while s:
			node = s.pop()
			if node.left:
				size += 1
				s.push(node.left)
			if node.right:
				size += 1
				s.push(node.right)
		return size

	def size_rec(self, node):
		if node is None:
			return 0
		return 1 + self.size_rec(node.left) + self.size_rec(node.right)





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.printTree("reverselevelOrder"))
print(str(tree.height(tree.root.left)))
print(str(tree.size()))
print(str(tree.size_rec(tree.root)))


