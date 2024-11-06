

#	nString = str(n)
#	nLen = len(str(n))
#	nString.isdecimal()



#'{:,.2f}'.format(n)
#'{:_.2f}'.format(n)
#'{:,}'.format(n)

#input read: allows 60_2248 automatically

#use apply for pd.DataFrame??

def big5(numb):
	s = str(numb)
	l = [x for x in s if x in '1234567890']
	for x in reversed(range(len(s))[::5]):
		l.insert(-x, '_')
	l = ''.join(l[1:])
	return ('-'+l if numb < 0 else l)

#df.val.apply(readable.set_us_numeric)


def big5_lambda_double(axes):
	return(axes.apply(lambda x: big5(int(x)*2)))

def set_us_numeric(m):
	return('{:,.2f}'.format(m))
