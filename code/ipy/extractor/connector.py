import sqlite3 as slt

def get_db(name_str='../../data/pseudo_prime.db'): 
	conny = slt.connect(name_str)
	return conny

def get_db_iasc(name_str='../../data_iasc/pseudo_prime.db'): 
        conny = slt.connect(name_str)
        return conny
