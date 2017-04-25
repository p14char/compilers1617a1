
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
	
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --

		sys.stdout.write(line)

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --

