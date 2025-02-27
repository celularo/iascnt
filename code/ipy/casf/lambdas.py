def fpt27_lucas(mers=127):
	info = ('dev.celularo','from.2024-12-13',
                        'cha.2025-02-05')
	#g[0](g[1])
	start = 4
	return (lambda x : (x*x-2) % mers,start,info)

def fpt23_mersenne():
	info = ('dev.celularo',
                        'from.2024-12-13',
                        'cha.2025_02_05')
	return (lambda x: pow(2,x)-1,info)

def ias1_restquotient(num,cls=60_22483_59169):
	info = ('dev.celularo',
                        'from.2024-12-29',
                        'cha.2025-02-05')
	return(lambda x : num - (x*cls),info)


