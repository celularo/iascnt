#base package for code-as-frame displays

import numpy as np
import pandas as pd
import math
import format.readable
import casf.lambdas as lambdas

# rows
def show_n(max=None):
	pd.set_option('display.max_rows', max)


def ias2_segmentproduct(dj,col_ind,a,b,n):
	info = ('dev.celularo',
                        'from.2024-11-15',
                        'cha.2025-02-05')
	f=1
	for i in dj[col_ind][a:b]:
		f= f*i %n
	return (f,info)

def ias1_crossproduct(z,w=0):
	info = ('dev.celularo',
			'from.2024-11-15',
			'cha.2025-02-05')
	pi=1
	for i in str(z)[w:]:
		pi *= int(i)
	return (pi,info)

def fpt9_euclid(n,k,v=500_00000):
	info = ('dev.celularo',
                        'from.2024-11-12',
                        'cha.2025-02-05')
	def f():
		return (lambda x : (x[1],x[2],x[1] % x[2]))
	c=[]
	c.append((n,k,n%k))
	for i in range(v):
		try: c.append(f()(c[i]))
		except(ZeroDivisionError,IndexError) as error:
			#fine v was sufficient
			info = (info,error)
			return(pd.DataFrame(c),info)
			break
	return (pd.DataFrame(c),info)

def fpt65_pollard(n,const,start,v=5_00000,sh=5):
	info = ('dev.celularo',
                        'from.2024-11-14',
                        'cha.2025-02-05')
	def f():
                return (lambda x : (x[0]+1,(x[1]*x[1] + 1)%n))
	def res():
		return(lambda x: x.append(x[len(x)-1]))
	c=[]
	c.append((0,start))
	C=[]
	D=[]
	D.append(0)
	for i in range(v):
		try:
			F=f()(c[i])
			c.append(F)
		except(ZeroDivisionError,IndexError) as error:
				#fine v was sufficient
				info = (info,error)
		if bin(F[0])[:4] == '0b11':
			C.append(F)
			if ias1_crossproduct(bin(F[0])[2:])[0] == 1:
				D.append(F[1])
			else:
				res()(D)
	dj = pd.DataFrame(C)
	dj[2] = dj[0].apply(bin)
	dj[3] = D[1:]
	dj[4] = (dj[1] - dj[3]) %n
	dj[5] = [x if x != 0 else 1 for x in dj[4]]
	return (dj,info)



def fpt65_A_pollard(n,const,start,v=500,sh=5):
	info = ('dev.celularo',
			'from.2025-01-18',
			'cha.2025-02-05')
	AR=[[]]
	x=start
	c=const
	i=1
	m=1
	b=False
	B=False
	l=1
	q=0
	r=0
	brent=0
	tar=1
	AR
	while (i < v):
	    y=(x*x+c)%n
	    if (i==pow(2,m)-1):
	        b=True
	    if (i==(pow(2,l+1)-pow(2,l-1))):
	        B=True
	    if (b):
	        s=q
	        q=x
	    if (B):
	        r=x
	        brent=s-r
	        tar = (tar*brent)%n
	    AR.append([i,x,y,m,b,l,B,q,r,s,brent,tar])
	    i+=1
	    x=y
	    if(i==pow(2,m)):
	        b=False
	        m+=1
	    if(i==pow(2,l+1)):
	        B=False
	        l+=1
	fra=pd.DataFrame(data=AR)
	return(fra,info)

def fpt27_lucas(n=31):
	info = ('dev.celularo',
                        'from.2025-01-17',
                        'cha.2025-02-06')
	p=pow(2,n)-1
	condi=((p%2)==1,(p>=3))
	exit=n-2
	c=[[p,4,0,n,exit,condi]]
	for i in range(n-1):
		try: c.append([format.readable.big5(p),lambdas.fpt27_lucas(p)[0](c[i][1]),lambdas.fpt23_mersenne()[0](i+2)])
		except(ZeroDivisionError,IndexError) as error:
			#fine v was sufficient
			info = (info,error)
			return(pd.DataFrame(c),info)
			break
	return (pd.DataFrame(c),info)
#
def fpt68_pollard(n=2047,c=29,v=69):
	info = ('dev.celularo',
		'from.2025-01-18','cha.2025-02-06')
	i=0
	m=1
	mMin1=0
	gn =1
	condi = math.gcd(n,c)
	assu=(condi==1)
	A=[[]]
	A.append([n,i,m,mMin1,gn,assu])
	for u in range(v):
		i+=1
		m=pow(c,i,n)
		mMin1=m-1
		gn=math.gcd(mMin1,n)
		A.append([n,i,m,mMin1,gn])
	return(pd.DataFrame(A),info)

def ias4_modularpow(b,iframe,m):
	frame = pd.DataFrame.copy(iframe)
	l=frame.shape[0]
	b_=b
	basis = []
	for i in range(l):
		basis.append(b)
		b=b*b % (m)
	frame['value0'] = basis*frame.iter0
	frame['value1'] = frame.value0.replace(0,1)
	mexpo_val = np.product(frame.value1)%m
	k=1
	for i in frame.value1:
		k=k*i % m
	return(	k,format.readable.big5(k),
		frame.applymap(format.readable.big5),
		'numpy result : ' + str(mexpo_val),
		str(b_))


def ias10_pspbases(rng=int(160_00000_00000),dpth=15,b=(2,3,5,7)) :
	c = []
	for i in range(dpth):
		k = 2*i+1
		if (rng - k) % 5 !=0:
			c.append(format.readable.big5(rng - k))
	d= [ias4_modularpow(b[0],ias5_binaryframe(int(x)-1),int(x))[0] for x in c]
	e= [ias4_modularpow(b[1],ias5_binaryframe(int(x)-1),int(x))[0] for x in c]
	f= [ias4_modularpow(b[2],ias5_binaryframe(int(x)-1),int(x))[0] for x in c]
	g= [ias4_modularpow(b[3],ias5_binaryframe(int(x)-1),int(x))[0] for x in c]
	dicty = { 'iter0' : c , 'value0' : d, 'value1' : e, 'value2' : f,
		'value3' : g }
	df = pd.DataFrame(data= dicty)
	return df


def ias5_binaryframe(n):
	dicty = {
		'iter0' : ias8_binarylist(n),
		'iter1' : ias6_binarylist(n),
		'iter2' : ias9_binarylist(len(ias7_binarylist(n)))}
	df = pd.DataFrame(data = dicty)
	df['iter3'] = df.iter0 * df.iter2
	return(df)

def ias6_binarylist(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/2)
	return Lparts

def ias7_binarylist(n):
	Lbin = [int(x) for x in bin(n).split('b')[1]]
	revLbin = [x for x in reversed(Lbin)]
	return Lbin

def ias8_binarylist(n):
        Lbin = [int(x) for x in bin(n).split('b')[1]]
        revLbin = [x for x in reversed(Lbin)]
        return revLbin

def ias9_binarylist(len):
	Lpows = []
	k=0
	while k < len:
		Lpows.append(int(math.pow(2,k)))
		k = k+1
	return Lpows

def ias3_spspbases(n,stage=1,b=(2,3,5,7)):
	k= int(0.5*(n-1))
	reva= []
	for j in range(len(b)):
		reva.append(ias4_modularpow(b[j],ias5_binaryframe(k),n)[0])
	return (reva, [format.readable.big5(x) for x in reva])

