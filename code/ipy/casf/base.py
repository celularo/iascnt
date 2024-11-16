#base package for code-as-frame products

import numpy as np
import pandas as pd
import math
import format.readable

# rows
def show_n(max=None):
	pd.set_option('display.max_rows', max)

# mod products column segments
def segmoco_0(dj,col_ind,a,b,n):
	info = ('id.segmoco', 'vers.0','dev.celularo',
                        'from.2024-11-15',
                        'cha.2024-11-15')
	f=1
	for i in dj[col_ind][a:b]:
		f= f*i %n
	return (f,info)

#cropro
def cropro_0(z,w=0):
	info = ('id.cropro', 'vers.0','dev.celularo',
			'from.2024-11-15',
			'cha.2024-11-15')
	pi=1
	for i in str(z)[w:]:
		pi *= int(i)
	return (pi,info)

#crosu
def crosu_0(z,w=0):
        info = ('id.crosu', 'vers.0','dev.celularo',
                        'from.2024-11-15',
                        'cha.2024-11-15')
        su=0
        for i in str(z)[w:]:
                su += int(i)
        return (su,info)


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
def olanova24_0(m,nu):
	dg = saddle(m)[0].sort_values(by='iter2',ascending = False)
	w = []
	for a in dg.iter1.tolist():
		w.append((math.floor(a/nu),a%nu))
	dg['value1'] = w
	v =  dg.iter0.tolist()[1:]
	fini = [0]
	v= v + fini
	dg['value2'] = v
	info = [('id.olanova24', 'vers.0','dev.celularo',
                        'from.2024-11-12',
                        'cha.2024-11-14')]
	return (dg,info)

# progupusad
def progupusad_0(n,k,v=500_00000):
	info = ('id.progupusad', 'vers.0','dev.celularo',
                        'from.2024-11-12',
                        'cha.2024-11-14')
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

#pro
def pro_0(n,const,start,v=5_00000,sh=5):
	info = ('id.pro', 'vers.0','dev.celularo',
                        'from.2024-11-14',
                        'cha.2024-11-16')
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
			if cropro_0(bin(F[0])[2:])[0] == 1:
				D.append(F[1])
			else:
				res()(D)
	dj = pd.DataFrame(C)
	dj[2] = dj[0].apply(bin)
	dj[3] = D[1:]
	#l = [x for x in dj[1][sh:]]
	#while len(l) <= len(range(v)):
	#	l.append(0)
	#dj[3] = l
	dj[4] = (dj[1] - dj[3]) %n
	dj[5] = [x if x != 0 else 1 for x in dj[4]]
	return (dj,info)

#lassomoon
def lassomoon_0(v=5_00000):
	info = ('id.lassomoon', 'vers.0','dev.celularo',
			'from.2024-11-15',
			'cha.2024-11-16')
	def f():
		return (lambda x : str(x)[2:]) #x.split('b')[1])
	def u():
		return( lambda x : cropro_0(x)[0])
	def l():
		return( lambda x : crosu_0(x)[0])
	def l_():
		return( lambda x : crosu_0(x,2)[0])

	c=range(v)
        #c.append((n,k,n%k))
#        for i in range(v):
#                try: c.append(f()(c[i]))
#                except(ZeroDivisionError,IndexError) as error:
#                        #fine v was sufficient
#                        info = (info,error)
#                        return(pd.DataFrame(c),info)
#                        break
	dj = pd.DataFrame(c)
	dj[1] = dj[0].apply(bin)
	dj[2] = dj[1].apply(f())
	dj[3] = dj[2].apply(u())
	dj[4] = dj[2].apply(l())
	dj[5] = dj[2].apply(l_())
	m=[1 if x == 2 else 0 for x in dj[4]]
	p=[1 if x == 0 else 0 for x in dj[5]]
	dj[6] = pd.Series.multiply(pd.Series(m),pd.Series(p))
	return (dj,info)


#template
def tmpl_0(n,s,v=5_00000):
        info = ('id.tmpl', 'vers.0','dev.celularo',
                        'from.2024-mm-dd',
                        'cha.2024-mm-dd')
        def f():
                return (lambda x : x)
        c=[]
        #c.append((n,k,n%k))
        for i in range(v):
                try: c.append(f()(c[i]))
                except(ZeroDivisionError,IndexError) as error:
                        #fine v was sufficient
                        info = (info,error)
                        return(pd.DataFrame(c),info)
                        break
        return (pd.DataFrame(c),info)
