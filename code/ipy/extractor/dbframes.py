import pandas as pd
from format import readable
import datetime as dt


def get_schema(con):
	frame = pd.read_sql_query("select * from sqlite_schema",con)
	print(frame.axes,'\nShape:',frame.shape)
	return (frame,frame.tbl_name)

def tbl_plain(con,tbl_str):
	frame = pd.read_sql_query("select * from " + tbl_str,con)
	print(frame.axes,'\nShape:',frame.shape)
	return frame

def spsp_group_con_bases(con):
	frame = pd.read_sql_query("with CAST_tab as "+
			"(select *, CAST(base as decimal)  base1 from spsp) "+
			"select val, count() ct_bases, group_concat(base1 ORDER BY base1 asc) "+
			"for_bases from CAST_tab group by val order by ct_bases desc",con)
	frame['val_num'] = frame.val.apply(readable.big5)
	frame['report_dtu'] = str(dt.datetime.utcnow())
	print(frame.axes,'\nShape:',frame.shape)
	return frame

def spsp_group_con_spsps(con):
	frame = pd.read_sql_query("with bases_enum as( "+
			"with CAST_tab as "+
			"(select *, CAST(base as decimal) base1 from spsp) "+
			"select val, count() ct_bases, group_concat(base1 ORDER BY "+
			"base1 asc) for_bases from CAST_tab group by val order by "+
			"ct_bases desc) "+
			"select ct_bases, for_bases, count() ct_vals, "+
			"group_concat(val ORDER BY val asc) by_vals "+
			"from bases_enum group by ct_bases, for_bases order by "+
			"ct_bases desc,ct_vals desc",con)
	print(frame.axes,'\nShape:',frame.shape)
	return frame
