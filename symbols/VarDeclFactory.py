from .NonTerminalSymbol import NonTerminalSymbol
from .TerminalFactory import TerminalFactory
from tokens.tokenizer import Token
from .TypeSpecFactory import TypeSpecFactory
from .VarDeclDashFactory import VarDeclDashFactory

class VarDeclFactory:
	def makeSymbol():
		typeSpec = TypeSpecFactory.makeSymbol()
		if typeSpec == None:
			return None

		ident = TerminalFactory.makeSymbol(Token.ID)
		if ident == None:
			return None

		varDeclDash = VarDeclDashFactory.makeSymbol()
		if varDeclDash:
			return None

		return NonTerminalSymbol("VarDecl", typeSpec, ident, varDeclDash)