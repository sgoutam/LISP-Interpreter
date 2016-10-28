#!/usr/bin/env python
from eval import *

def repl( prompt = 'lisp.py>' ):
	"Read-Eval-Print-Loop"
	while True:
		val = eval(parse(raw_input(prompt)))
		if val is not None:
			print(dispstr(val))

def dispstr(exp):
	"Convert python object into LISP object"
	if isinstance(exp, list):
		return '(' + ' '.join(map(dispstr,exp))+ ')'
	else:
		return str(exp)

while(1):
	repl()

