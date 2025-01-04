#recursive
def lule29_0(mers=127):
	info = ('id.lule29', 'vers.0','dev.celularo',
                        'from.2024-12-13',
                        'cha.2024-12-13')
	#g[0](g[1])
	start = 4
	return (lambda x : (x*x-2) % mers,start,info)

#derivatives
def mers_0():
	info = ('id.mers', 'vers.0','dev.celularo',
                        'from.2024-12-13',
                        'cha.2024-12-13')
	return (lambda x: pow(2,x)-1,info)

#divide
def dividix_0(num,cls=60_22483_59169):
	info = ('id.dividix', 'vers.0','dev.celularo',
                        'from.2024-12-29',
                        'cha.2024-12-29')
	return(lambda x : num - (x*cls),info)



