from lispeval import *
from parser import *

def eval(x, env=global_env):
	"Evaluate the given expression in the given environment"
	if isinstance(x, Sym):	#reference to variable
		return env[x]
	elif not isinstance(x, List):	#const literal
		return x
	elif x[0] == 'quote':		#(quote exp)
		(_,exp) = x
		return exp
	elif x[0] == 'if':		#(if test conseq alt)
		(_,test,conseq,alt) = x
		exp = (conseq if eval(test,env) else alt)
		return eval(exp,env)
	elif x[0] == 'define':		#(define var exp)
		(_,var,exp) = x
		env[var] = eval(exp,env)
	else:
		proc = eval(x[0], env)
		args = [eval(arg,env) for arg in x[1:]]
		return proc(*args)

