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


def middle_delete(head):

	p1 = head
	p2 = head
	prev = p1

	while p2 is not None and p2.next is not None:

		prev = p1
		p1 = p1.next
		p2 = p2.next.next


	prev.next = p1.next

	



list1 = SingleList()

list1.head = Node("One")

e2 = Node("Four")

list1.head.next = e2




list1.printlist()


middle_delete(list1.head)


list1.printlist()
