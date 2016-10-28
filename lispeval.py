Sym = str
List = list
Num = (int, float)
Env = dict

def standard_env():
	import math, operator as op
	env = Env()
	env.update(vars(math))
	env.update({
		'+':op.add, '-':op.sub, '*':op.mul, '/':op.div,
		'>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq,
		'abs': abs,
		'append': op.add,
		'apply': apply,
		'begin': lambda *x: x[-1],
		'car': lambda x: x[0],
		'cdr': lambda x: x[1:],
		'cons': lambda x,y: [x]+y,
		'eq?' : op.is_,
		'equal?': op.eq,
		'length': len,
		'list': lambda *x: list(x),
		'list?': lambda x: isinstance(x,list),
		'map': map,
		'max': max,
		'min': min,
		'not': op.not_,
		'null?': lambda x: x == [],
		'number?': lambda x: isinstance(x, Num),
		'procedure?': callable,
		'round': round,
		'symbol?': lambda x: isinstance(x, Sym),
	})
	return env

global_env = standard_env()


