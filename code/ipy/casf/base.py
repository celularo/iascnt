#base package for code-as-frame products

import numpy as np
import pandas as pd
import math
import format.readable

# rows
def show_n(max=None):
	pd.set_option('display.max_rows', max)


# saddle
def saddle(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/10)
	Ldec = [int(x) for x in str(n)]
	revLdec = [x for x in reversed(Ldec)]
	Lpows = []
	k=0
	while k < len(Ldec):
		Lpows.append(int(math.pow(10,k)))
		k = k+1
	dicty = {
		'iter0' : revLdec,
		'iter1' : Lparts,
		'iter2' : Lpows}
	df = pd.DataFrame(data = dicty)
	df['iter3'] = df.iter0 * df.iter2
	return(df,'dev.celularo', 'from.2024-11-12','cha.2024-11-12')


# olanova24
def olanova24(m,nu):
	dg = saddle(m)[0].sort_values(by='iter2',ascending = False)
	w = []
	for a in dg.iter1.tolist():
		w.append((math.floor(a/nu),a%nu))
	dg['value1'] = w
	v =  dg.iter0.tolist()[1:]
	fini = [0]
	v= v + fini
	dg['value2'] = v
	return (dg,'dev.celularo', 'from.2024-11-12','cha.2024-11-12')

