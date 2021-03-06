#!/usr/bin/python
import sys
import os
import re
import pandas as pd
import numpy as np
import math
import json
import glob

def main():
	##### check argument #####
	if len(sys.argv)<2:
		sys.exit("ERROR: not enough arguments\nUSAGE ./magma_expPlot.py <filedir>")

	##### get command line arguments #####
	filedir = sys.argv[1]
	if re.match(".+\/$", filedir) is None:
		filedir += '/'

	### get files ###
	files = glob.glob(filedir+"/magma_exp*.out")

	out = []
	for f in files:
		dat = pd.read_table(f, delim_whitespace=True, comment="#", dtype=str, usecols=["COVAR", "P"])
		dat = np.array(dat)
		dat = dat[dat[:,1].astype(float).argsort()]
		dat = np.c_[dat, range(0,len(dat))]
		dat = dat[dat[:,0].argsort()]
		dat = np.c_[dat, range(0,len(dat))]
		c = re.match(r'.*magma_exp_(.*)\.gcov.out', f)
		for l in dat:
			out.append([c.group(1), l[0], float(l[1]), l[2], l[3]])

	print json.dumps(out)
if __name__ == "__main__": main()
