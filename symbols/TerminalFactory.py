from .TerminalSymbol import TerminalSymbol
from .TerminalChecker import TerminalChecker
from tokens.tokenizer import Token, TokensRepo

class TerminalFactory:
	def makeSymbol(tokenName):
		if TerminalChecker.willConsume(tokenName):
			return TerminalSymbol(TokensRepo.getInstance().consume())

		return None