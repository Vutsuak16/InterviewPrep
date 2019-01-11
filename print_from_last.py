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


	def insert_at_end(self, value):

		start = self.head

		while start.next is not None:

			start = start.next
		
		start.next = Node(value)


def print_from_last( k , head):	QAZ

	if head == None:
		return 0

	index = print_from_last(k , head.next) + 1

	if index == k :
		print(head.value)

	return index




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


print_from_last(5, list1.head)