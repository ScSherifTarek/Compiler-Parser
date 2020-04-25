from symbols.ProgramFactory import ProgramFactory
from symbols.NonTerminalSymbol import NonTerminalSymbol
from tokens.reader import reader
from tokens.tokenizer import TokensRepo


def init():
	tokens = reader()
	tokensRepo = TokensRepo.getInstance()
	for token in tokens:
		tokensRepo.addToken(token)


def main():
	init()
	program = ProgramFactory.makeSymbol()
	tokensRepo = TokensRepo.getInstance()
	if program == None or tokensRepo.isEmpty():
		print("Syntax Error")
	else:
		program.print()

main()