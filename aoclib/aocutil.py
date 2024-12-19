
def puzzleinput():
	import sys
	return (line for line in map(str.strip, sys.stdin) if line)

