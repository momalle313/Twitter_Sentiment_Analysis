#!/usr/bin/python
import sys
import os
import pandas as pd

### Michael O'Malley, Michael Burke
### Machine Learning
### Semster Project
### Tweet Parser

# Run main
if __name__ == "__main__":

	# Read in training data
	if len(sys.argv) != 2:
		print "Please state file you'd like to clean."
		sys.exit()
	elif not os.path.isfile(str(sys.argv[1])):
		print "The given file does not exist."
		sys.exit(1)
	else:
		data = pd.read_csv(str(sys.argv[1]), sep='\n\n')

print data
