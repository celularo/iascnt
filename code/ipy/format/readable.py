# 60_22483_59169
def big5(n_int):
	s = str(n_int)
	l = [x for x in s]
	for x in reversed(range(len(s))[::5]):
		l.insert(-x, '_')
	l = ''.join(l[1:])
	return ('-'+l if n_int < 0 else l)

# 59,169.00
def set_us_numeric(m):
	return('{:,.2f}'.format(m))
