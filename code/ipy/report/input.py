
def update_report_tab(con,report_frame):
	report_frame.to_sql('report',con,if_exists = 'replace')
