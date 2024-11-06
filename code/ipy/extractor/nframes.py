### b i n a r y

import numpy as np
import pandas as pd
import math
from format import readable 


#parts list
def list_parts_bin_d(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/2)
	return Lparts

# representation List
def list_bin(n):
	Lbin = [int(x) for x in bin(n).split('b')[1]]
	revLbin = [x for x in reversed(Lbin)]
	return Lbin

# representation List reversed 
def list_bin_rev(n):
        Lbin = [int(x) for x in bin(n).split('b')[1]]
        revLbin = [x for x in reversed(Lbin)]
        return revLbin

# powers list
def list_2pows_d(len):
	Lpows = []
	k=0
	while k < len:
		Lpows.append(int(math.pow(2,k)))
		k = k+1
	return Lpows

# frame
def frame_bin(n):
	dicty = {'parts_d' : list_parts_bin_d(n),
		'driver' : list_bin_rev(n),
		'powers_d' : list_2pows_d(len(list_bin(n)))}
	df = pd.DataFrame(data = dicty)
	df['terms_d'] = df.driver * df.powers_d
	return(df)

### d e c i m a l 

# parts list
def list_parts_dec(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/10)
	return Lparts

# multiples list
def list_multis_dec(n):
	Lparts = []
	k=n
	while k>=1:
		Lparts.append(k)
		k=math.floor(k/10)
	return Lparts

# representation List
def list_dec(n):
	Ldec = [int(x) for x in str(n)]
	revLdec = [x for x in reversed(Ldec)]
	return Ldec

# representation List reversed 
def list_dec_rev(n):
        Ldec = [int(x) for x in str(n)]
        revLdec = [x for x in reversed(Ldec)]
        return revLdec

# powers list
def list_10pows(len):
	Lpows = []
	k=0
	while k < len:
		Lpows.append(int(math.pow(10,k)))
		k = k+1
	return Lpows

# frame
def frame_dec(n):
	dicty = {'parts' : list_parts_dec(n),
		'driver' : list_dec_rev(n),
		'powers' : list_10pows(len(list_dec(n)))}
	df = pd.DataFrame(data = dicty)
	df['terms'] = df.driver * df.powers
	return(df)

