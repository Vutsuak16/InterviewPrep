class Node:

	def __init__(self,value):

		self.value = value
		self.next = None


class SingleList:

	def __init__(self):
		self.head = None

	def insert_at_end(self,value):

		node = Node(value)

		if self.head == None:

			self.head = node
			return

		curr = self.head

		while curr.next is not None:

			curr = curr.next

		curr.next = node

		return

	def printlist(self):

		curr = self.head

		while curr is not None:

			print(curr.value)
			curr = curr.next
		
		print()
		print()

	def del_node(self, value):

		curr = self.head

		if curr == None:
			return

		if curr.value == value:

			self.head  = curr.next
			return


		else:

			prev = None

			while curr is not None:

				if curr.value == value:
					break

				prev = curr
				curr = curr.next

			if curr == None:

				return #value not found

			prev.next = curr.next

			curr = None

			return


list1 = SingleList()

list1.head = Node("One")

e2 = Node("Two")
e3 = Node("Three")
e4 = Node("Four")
e5 = Node("Five")

list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

list1.printlist()

print()
print()

list1.insert_at_end("Six")

list1.printlist()

print()
print()

list1.del_node("Six")

list1.printlist()

print()
print()


list1.del_node("Four")

list1.printlist()

print()
print()












