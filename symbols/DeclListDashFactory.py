from .NonTerminalSymbol import NonTerminalSymbol
from .DeclFactory import DeclFactory
from .Empty import Factory as EmptyFactory

class DeclListDashFactory:
	def makeSymbol():
		decl = DeclFactory.makeSymbol()
		if(decl == None):
			return makeWithEmpty()

		declListDash = DeclListDashFactory.makeSymbol()
		if(declListDash == None):
			return makeWithEmpty()

		return NonTerminalSymbol("DeclList", decl, declListDash)

	def makeWithEmpty():
		empty = EmptyFactory.makeSymbol()
		
		if empty:
			return NonTerminalSymbol("DeclListDash", empty)

		return None