
import numpy as np
import pandas as pd
import math
from format import readable



### b i n a r y

#parts
def list_parts_bin_d(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/2)
	return Lparts

# representation
def list_bin(n):
	Lbin = [int(x) for x in bin(n).split('b')[1]]
	revLbin = [x for x in reversed(Lbin)]
	return Lbin

# representation reversed
def list_bin_rev(n):
        Lbin = [int(x) for x in bin(n).split('b')[1]]
        revLbin = [x for x in reversed(Lbin)]
        return revLbin

# powers
def list_2pows_d(len):
	Lpows = []
	k=0
	while k < len:
		Lpows.append(int(math.pow(2,k)))
		k = k+1
	return Lpows

# frame
def frame0(n):
	dicty = {
		'clock0' : list_bin_rev(n),
		'clock1' : list_parts_bin_d(n),
		'clock2' : list_2pows_d(len(list_bin(n)))}
	df = pd.DataFrame(data = dicty)
	df['clock3'] = df.clock0 * df.clock2
	return(df)

### d e c i m a l

# parts
def list_parts_dec(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/10)
	return Lparts

# multiples
def list_multis_dec(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/10)
	return Lparts

# representation
def list_dec(n):
	Ldec = [int(x) for x in str(n)]
	revLdec = [x for x in reversed(Ldec)]
	return Ldec

# representation reversed
def list_dec_rev(n):
        Ldec = [int(x) for x in str(n)]
        revLdec = [x for x in reversed(Ldec)]
        return revLdec

# powers
def list_10pows(len):
	Lpows = []
	k=0
	while k < len:
		Lpows.append(int(math.pow(10,k)))
		k = k+1
	return Lpows

# frame
def frame1(n):
	dicty = {
		'clock0' : list_dec_rev(n),
		'clock1' : list_parts_dec(n),
		'clock2' : list_10pows(len(list_dec(n)))}
	df = pd.DataFrame(data = dicty)
	df['clock3'] = df.clock0 * df.clock2
	return(df)

