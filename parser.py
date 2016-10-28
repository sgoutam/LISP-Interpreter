from lispeval import *

def tokenize(chars):
	"Creates a list of tokens"
	return chars.replace('(',' ( ').replace(')',' ) ').split()

def parse(program):
	"Begin parsing from here"
	return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
	"Validate the list of tokens generated"
	if len(tokens) == 0:
		raise SyntaxError('Unexpected EOF while reading')
	token = tokens.pop(0)
	if token == '(':
		L = []
		while tokens[0] != ')':
			L.append(read_from_tokens(tokens))
		tokens.pop(0)  #removes the ')' token
		return L
	elif token == ')':
		raise SyntaxError('Unexpected )')
	else:
		return atom(token)

def atom(token):
	"Convert the tokens generated into atoms for the Interpreter"
	try:
		return int(token)
	except ValueError:
		try:
			return float(token)
		except ValueError:
			return Sym(token)
