import sqlite3 as slt
import pandas as pd
from format import readable
import extractor.connector, extractor.dbframes
import datetime as dt
import report.input

class iascDB:
    def __init__(self) -> None:
        coi = extractor.connector.get_db_iasc()
        self.primes: DataFrame = pd.read_sql_query("select * from primes",coi)
        self.frequency: DataFrame = pd.read_sql_query("select * from frequency",coi)
        self.frequency_psp2: DataFrame = pd.read_sql_query("select * from frequency_psp2",coi)
        self.psp: DataFrame = pd.read_sql_query("select * from psp",coi)
        self.spsp: DataFrame = pd.read_sql_query("select * from spsp",coi)
        self.psp_base_bundles: DataFrame = pd.read_sql_query("select * from psp_base_bundles",coi)
        self.report_oltp: DataFrame = pd.read_sql_query("select * from report_oltp",coi)
        self.bases_spsp_sets: DataFrame = pd.read_sql_query("select * from bases_spsp_sets",coi)
        self.spsp_top: DataFrame = pd.read_sql_query("select * from spsp_top",coi)
        self.report: DataFrame = pd.read_sql_query("select * from report",coi)
        self.decomps: DataFrame = pd.read_sql_query("select * from decomps",coi)
        self.projects_p: DataFrame = pd.read_sql_query("select * from projects_p",coi)
        self.projects_f: DataFrame = pd.read_sql_query("select * from projects_f",coi)
        self.projects_c: DataFrame = pd.read_sql_query("select * from projects_c",coi)
        self.conni: Connection = coi
        self.lstprof: List = self.projects_f['0'].to_list()
        self.lstprop: List = self.projects_p['0'].to_list()

    def input_projects_f(self,num: str) -> None:
        L=(num,str(dt.datetime.utcnow()))
        AR=[L]
        rfra=pd.DataFrame(AR)
        report.input.update_projects_f(self.conni,rfra)

    def input_decomps(self,deco: str,facto: str) -> None:
        L=(deco,facto,str(dt.datetime.utcnow()))
        AR=[L]
        rfra=pd.DataFrame(AR)
        report.input.update_decomps(self.conni,rfra)

class masterDB:
    def __init__(self) -> None:
        coi = extractor.connector.get_db()
        self.primes: DataFrame = pd.read_sql_query("select * from primes",coi)
        self.bressoud_p18: DataFrame = pd.read_sql_query("select * from bressoud_p18",coi)
        self.bressoud_p18_psp_2: DataFrame = pd.read_sql_query("select * from bressoud_p18_psp_2",coi)
        self.psp: DataFrame = pd.read_sql_query("select * from psp",coi)
        self.spsp: DataFrame = pd.read_sql_query("select * from spsp",coi)
        self.psp_base_bundles: DataFrame = pd.read_sql_query("select * from psp_base_bundles",coi)

class trialDB:
    def __init__(self) -> None:
        coi = extractor.connector.get_db_trial()
        self.pseudo_trials: DataFrame = pd.read_sql_query("select * from pseudo_trials",coi)
