class Stack:

	def __init__(self):

		self.items = []

	def peek(self):

		return self.items[-1]

	def push(self,value):

		self.items.append(value)

	def pop(self):

		return self.items.pop()l 

	def isEmpyty():

		return self.items == []

	def size(self):

		return len(self.items)

