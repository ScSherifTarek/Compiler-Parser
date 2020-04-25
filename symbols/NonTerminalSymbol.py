class NonTerminalSymbol:
	def __init__(self, title, *children):
		self.title = title
		self.children = children

	def print(self, level = 0	):
		print("---"*level+"->"+self.title+": ")
		for child in self.children:
			child.print(level = level+1)