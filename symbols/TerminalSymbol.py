class TerminalSymbol:
	def __init__(self, token = None):
		self.token = token

	def print(self, level = 0):
		print("---"*level+"->"+self.token.value)