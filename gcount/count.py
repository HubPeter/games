#!/usr/bin/env python
import random, time
a = b = 0
rsum = usum = 0
def correct():
	print '\n',\
		'             *\n'+\
		' *        *\n'+\
		'  *   *\n'+\
		'   *'
def error():
	print \
		'*       *\n'+\
		'  *   *\n'+\
		'    *\n'+\
		'  *   *\n'+\
		'*       *'

opChar = '+'
def add( oper='+', mask=10):
	while True:
		try:
			a = random.randrange(mask)
			b = random.randrange(mask)
			if oper=='+':
				rsum = a+b
			elif oper=='-':
				rsum = a-b
			elif oper=='*':
				rsum = a*b
			elif oper=='/':
				rsum = a/b
			else:
				error()
				break
			print '	', a, '\n', '	', b
			usum = raw_input()
			if int(usum)==rsum:
				correct()
			else:
				error()
				print 'Answer:',rsum,'\n'
			#time.sleep(1)
		except Exception as ex:
			print ex
			break

def main():
	print 'Command + - * / (q)uit:'
	op = raw_input().strip()
	if op=='+' or op=='-' or op=='*' or op=='/':
		print 'mask: '
		try:
			mask = int(raw_input())
		except Exception as ex:
			print ex
			sys.exit()
		add(op, mask)
	elif op=='q':
		print 'Bye'
	else:
		print 'Bye'

if __name__=='__main__':
	main()
