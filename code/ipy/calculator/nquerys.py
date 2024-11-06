import numpy as np
import pandas as pd
import math
from format import readable 

## show more rows
def show_n(max=None):
	pd.set_option('display.max_rows', max)

## querys binary data

# mod exp of basis / exponent / modulus
# re_va : frame, numpys response, true value,given basis, given exponent
def get_mexpo_result(b,frame,m):
	l=len(frame.driver)
	b_=b
	basis = []
	for i in range(l):
		basis.append(b)
		b=b*b % (m)
	frame['basis'] = basis*frame.driver
	frame['result'] = frame.basis.replace(0,1)
	mexpo_val = np.product(frame.result)%m
	k=1
	for i in frame.result:
		k=k*i % m
	return(frame.applymap(readable.big5),str(mexpo_val)+'numpy',k,b_,readable.big5(sum(frame.repr)))

## querys decimal data

