#!/usr/bin/env python
from count import correct, error
import random, time
import sys
class Remem:
	mask = 10
	length = 5
	sleep = 3
	def __init__(self):
		pass
	def game(self):
		while True:	
			numbers = []
			for i in range(self.length):
				a = random.randrange(self.mask)
				numbers.append(a)
			print numbers
			time.sleep(self.sleep)
			for i in range(20):
				print '\n',
			print 'answer:'
			try:
				answer = int(raw_input())
			except Exception as ex:
				print ex
				sys.exit()
			else:
				pass
			r = sum(numbers)
			if r==answer:
				print '\n'
				correct()
			else:
				print '\n'
				error()
				print 'shoule be: ', r
			numbers = []
			
if __name__ == '__main__':
	remem = Remem()
	remem.game()

