from tokens.tokenizer import TokensRepo

class Symbol:
	def print(self):
		return

class Factory:
	def makeSymbol():
		if TokensRepo.getInstance().hasNext():
			return None
		return Symbol()
