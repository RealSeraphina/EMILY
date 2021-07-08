#!/usr/bin/env python3

import sys
from termcolor import colored, cprint

def displayEmily(emilyFile):	
	with open(emilyFile) as emily:
		for line in emily:
		#	print(line, end = ' ')
			cprint(line, 'magenta', end = ' ')

def main():
	displayEmily("/home/pi/EMILY/emily_ascii.txt")

if __name__ == '__main__':
	main()	
