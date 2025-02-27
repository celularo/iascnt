import numpy as np
import pandas as pd
import datetime as dt
import format.readable


def collect_test_lists(frame):
	frame = frame[frame.ct_bases>=4]
	tab = frame.pivot_table(index = ['for_bases','val','val_num','report_dtu'],
				values = 'ct_bases',aggfunc = 'sum').sort_index(ascending=False)
	print(frame.axes,'\nShape:',frame.shape)
	return tab

def show_n(max=None):
	pd.set_option('display.max_rows', max)

#def trial_max_n(primes_frame,max=2000,n=3215031751):
def ias1_primetrial(primes_frame,max=2000,n=3215031751):
	frame1 = primes_frame[primes_frame.val < max]
	frame1['moduloval'] = n%frame1['val']
	frame2=frame1.sort_values(by=['moduloval','val'])
	print(frame2.axes,'\nShape:',frame2.shape)
	return frame2

