from collections import deque

#############################
# stack data structure

class stack:
	def __init__ (self):
		self.cont = deque()
	def push(self,val):
		self.cont.append(val)
	def pop (self):
		return self.cont.pop()
	def lass_item (self):
		return self.cont[-1]
	def is_empty(self):
		return len(self.cont) == 0