import numpy as np
import pandas as pd
import math
from format import readable
from calculator import nquerys
from extractor import nframes

# rows
def show_n(max=None):
	pd.set_option('display.max_rows', max)

###  b i n a r y

# modular exponentiation
def algo0(b,iframe,m):
	frame = pd.DataFrame.copy(iframe)
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
	return(	k,readable.big5(k),
		frame.applymap(readable.big5),
		'numpy result : ' + str(mexpo_val),
		str(b_))



# psp in eer
def algo1(rng=int(160_00000_00000),dpth=15,b=(2,3,5,7)) :
	c = []
	for i in range(dpth):
		k = 2*i+1
		if (rng - k) % 5 !=0:
			c.append(readable.big5(rng - k))
	d= [nquerys.algo0(b[0],nframes.frame0(int(x)-1),int(x))[0] for x in c]
	e= [nquerys.algo0(b[1],nframes.frame0(int(x)-1),int(x))[0] for x in c]
	f= [nquerys.algo0(b[2],nframes.frame0(int(x)-1),int(x))[0] for x in c]
	g= [nquerys.algo0(b[3],nframes.frame0(int(x)-1),int(x))[0] for x in c]
	dicty = { 'clock0' : c , 'worker0' : d, 'worker1' : e, 'worker2' : g,
		'worker3' : g }
	df = pd.DataFrame(data= dicty)
	return df

#spsp
def algo2(n,stage=1,b=(2,3,5,7)):
	k= int(0.5*(n-1))
	reva= []
	for j in range(len(b)):
		reva.append(nquerys.algo0(b[j],nframes.frame0(k),n)[0])
	return (reva, [readable.big5(x) for x in reva])

### d e c i m a l

#manu modulus
def algo3(m,nu):
	dg = nframes.frame1(m).sort_values(by='clock2',ascending = False)
	w = []
	for a in dg.clock1.tolist():
		w.append((math.floor(a/nu),a%nu))
	dg['work1'] = w
	v =  dg.clock0.tolist()[1:]
	fini = [0]
	v= v + fini
	dg['work2'] = v
	return (dg,v)
