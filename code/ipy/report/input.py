
def update_report_tab(con,report_frame):
	report_frame.to_sql('report',con,if_exists = 'replace')

def update_spsp_top(con,report_frame):
        report_frame.to_sql('spsp_top',con,if_exists = 'replace')

def update_bases_spsp_sets(con,report_frame):
        report_frame.to_sql('bases_spsp_sets',con,if_exists = 'replace')

