from tokens.tokenizer import TokensRepo

class Symbol:
	def print(self, level = 0):
		print("---"*level+"-> Empty")

class Factory:
	def makeSymbol():
		if TokensRepo.getInstance().hasNext():
			return None
		return Symbol()
