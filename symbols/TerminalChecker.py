from tokens.tokenizer import Token, TokensRepo

class TerminalChecker:
	@staticmethod
	def willConsume(tokenName):
		tokensRepo = TokensRepo.getInstance()
		if tokensRepo.isEmpty():
			return False

		token = tokensRepo.getNext()
		if token.name == tokenName:
			return True

		return False