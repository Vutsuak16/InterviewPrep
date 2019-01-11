class Node:

	def __init__(self,value):

		self.value = value
		self.next = None

class SingleList:

	def __init__(self):

		self.head = None

	def printlist(self):

		start = self.head

		while start is not None:

			print(start.value)
			start = start.next
		
		print()
		print()


	def insert_at_end(self, value):

		start = self.head

		while start.next is not None:

			start = start.next
		
		start.next = Node(value)


def print_from_last_iter(k, head):

	p1 = head
	p2 = head


	for i in range(k):

		if p1 == None:
			return

		p1 = p1.next

	while p1 is not None:

		p1 = p1.next
		p2 = p2.next

	print(p2.value)

	



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


print_from_last_iter(1, list1.head)