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


	def check_palindrome(self):


		p1 = self.head
		p2 = self.head

		ct = 0


		#found mid point
		while p2 is not None and p2.next is not None:

			p1 = p1.next
			p2  = p2.next.next

			ct += 1

		mid = p1
		prev = mid

		#reverse half list from midpoint
		while mid is not None:

			next = mid.next
			mid.next = prev
			prev = mid
			mid = next

		head1 = self.head 
		head2 = prev

		#compare both before half and reversed list
		while ct != 0:

			if head1.value != head2.value:

				return False

			head1 = head1.next
			head2 = head2.next

			ct -= 1

		return True


			



		

list1 = SingleList()

list1.head = Node("1")

e2 = Node("2")
e3 = Node("3")
e4 = Node("2")
e5 = Node("1")

list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5





list1.printlist()


print(list1.check_palindrome())

