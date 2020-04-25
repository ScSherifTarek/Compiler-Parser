from .NonTerminalSymbol import NonTerminalSymbol
from .DeclFactory import DeclFactory
from .DeclListDashFactory import DeclListDashFactory

class DeclListFactory:
	def makeSymbol():
		decl = DeclFactory.makeSymbol()
		if(decl == None):
			return None

		declListDash = DeclListDashFactory.makeSymbol()
		if(declListDash == None):
			return None

		return NonTerminalSymbol("DeclList", decl, declListDash)