from collections import defaultdict
import argparse
VERBOSITY_LEVEL = 0


META = '''
E -> EE
E -> LR

A -> ~
O -> -
Q -> >

L -> AO

R -> QA
R -> QP
R -> QS

P -> AA

S -> IL
I -> JU
U -> ~
U -> AN
N -> CU
C -> ,
J -> {
L -> }
'''


def get_input():
	global VERBOSITY_LEVEL
	parser = argparse.ArgumentParser()
	parser.add_argument("--grammar", required=True, help="file containing production rules")
	parser.add_argument("string", help="string or file to be validated")
	parser.add_argument('--verbose', '-v', action='count', default=0, help="validate production rules and print parsing results")
	args = parser.parse_args()

	VERBOSITY_LEVEL = args.verbose
	GRAMMAR = open(args.grammar).read()

	try:
		STRING = open(args.string).read()
	except:
		STRING = args.string

	return STRING, GRAMMAR


def validate(string, grammar):
	global VERBOSITY_LEVEL

	def multisplit(s):
		words = []; word = []
		for e in s:
			if e == ' ' or e == '\n':
				if word:
					words.append("".join(word))
					word = []
			else:
				word.append(e)
		return words


	ORIGIN = ""
	def parse():
		nonlocal ORIGIN
		global VERBOSITY_LEVEL
		words = multisplit(grammar)
		ORIGIN = words[0]
		d = defaultdict(set)

		for k in range(0, len(words), 3):
			pre = words[k]; post = words[k+2]
			
			if post[0] == "{" and post[-1] == "}":
				for e in post[1:-1].split(','):
					d[e].add(pre)
			else:
				d[post].add(pre)
		return d


	PRODUCTIONS = parse()
	def pset(s1, s2):
		ps = []
		for post, pre in PRODUCTIONS.items():
			if len(post) == 2 and post[0] in s1 and post[1] in s2:
				ps.append(pre)
		return set().union(*ps)


	def valid(string):	
		string = string.replace(' ','').replace('\n','')
		n = len(string)
		M = [ [PRODUCTIONS[string[i]].union(PRODUCTIONS["~"]) if i == j else None for i in range(n)] for j in range(n) ]

		for k in range(1, n):
			for i in range(n-k):
				j = i+k
				M[i][j] = set().union(*[ pset(M[i][d], M[d+1][j]) for d in range(i, j) ])

		return ORIGIN in M[0][n-1]

	if VERBOSITY_LEVEL:
			VERBOSITY_LEVEL = 0
			L = []
			for key, val in PRODUCTIONS.items():
				L += [ v + " -> " + key for v in val ] 
			print("<parsing grammar>")
			print("\n".join(L))

			if validate(grammar, META):
				print("<grammar is valid>")
				print()
			else:
				raise Exception("Grammar is invalid!")

	
	return valid(string)


# Driver code
valid = "valid" if validate(*get_input()) else "invalid"
print( f"String is {valid}" )