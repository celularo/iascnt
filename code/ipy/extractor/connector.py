import sqlite3 as slt

def get_db(name_str='../../data/pseudo_prime.db'): 
	conny = slt.connect(name_str)
	return conny

