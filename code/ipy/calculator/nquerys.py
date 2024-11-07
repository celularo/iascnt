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
def algo0(b,frame,m):
	l=frame.shape[0]
	b_=b
	basis = []
	for i in range(l):
		basis.append(b)
		b=b*b % (m)
	frame['worker0'] = basis*frame.clock0
	frame['worker1'] = frame.worker0.replace(0,1)
	mexpo_val = np.product(frame.worker1)%m
	k=1
	for i in frame.worker1:
		k=k*i % m
	return(frame.applymap(readable.big5),
		'numpy result : ' + str(mexpo_val),
		'result : ' + str(k),
		'import0 : ' + str(b_),
		'import1 : ' + readable.big5(sum(frame.clock3)),
		'import2 : ' + readable.big5(m))

## querys decimal data

