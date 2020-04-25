from .NonTerminalSymbol import NonTerminalSymbol
from .VarDeclFactory import VarDeclFactory
from .FunDeclFactory import FunDeclFactory

class DeclFactory:
	def makeSymbol():
		varDecl = VarDeclFactory.makeSymbol()
		if varDecl:
			return NonTerminalSymbol("VarDecl", varDecl)

		funDecl = FunDeclFactory.makeSymbol()
		if funDecl:
			return NonTerminalSymbol("FunDecl", funDecl)

		return None