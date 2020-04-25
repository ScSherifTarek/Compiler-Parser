from .NonTerminalSymbol import NonTerminalSymbol
from .DecListFactory import DecListFactory

class ProgramFactory:
	def makeSymbol():
		decList = DecListFactory.makeSymbol()

		if(decList == None):
			return None

		return NonTerminalSymbol("Program", decList)