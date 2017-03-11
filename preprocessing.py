# preprocessing
import pandas as pd
import sys
import numpy as np

def main(size):
	"""
	Metoda na pouzitie sliding window
	"""
	
	all_csv = pd.read_csv("all2.csv", dtype={'x':np.int16, 'y':np.int16, 'z':np.int16,'movement':np.int8, 'user':np.int8})
	#print(all_csv)
	# print (all_csv.dtypes)
	# return

	start = 0
	index_increment=size+start-1
	end = index_increment

	slidedataframe = pd.DataFrame()
	iteration=1
	mycolumns=[]
	prev_movement=all_csv.ix[end,4]
	prev_userid=all_csv.ix[end,5]
	counter_100k = 1
	out_file = "sliding{}.csv"
	while (all_csv.shape[0]-1 > end):
		movement = all_csv.ix[end,4]
		userid = all_csv.ix[end,5]
		if (prev_movement != movement) or (prev_userid != userid):
			start=end
			end=start+index_increment
			prev_movement=movement
			prev_userid=userid
			continue
		tmp = all_csv.ix[start:end,1:4]
		tmp = tmp.stack().to_frame().T
		prev_movement=movement
		prev_userid=userid

		if iteration == 1:
			mycolumns=['{}_{}'.format(*c) for c in tmp.columns]
			iteration=2
		tmp.columns = mycolumns
       	# print (tmp.columns)
		tmp['movement'] = movement
		tmp['user'] = userid
		tmp[['movement','user']]=tmp[['movement','user']].astype(np.int8)

		slidedataframe = slidedataframe.append(tmp)
		start += 1
		end += 1
		# if end == 100:
		#     print (slidedataframe.dtypes)
		#     break
		if (end % 1000 == 0):
			print(end)
			# print(slidedataframe)
			# break
		if (end % 100000 == 0):
			# save to csv
			slidedataframe.to_csv(out_file.format(counter_100k),sep=',')
			slidedataframe = pd.DataFrame()
			counter_100k+=1

	# vypis posledneho dataframe-u
	slidedataframe.to_csv(out_file.format(counter_100k), sep=',')




if __name__ == '__main__':
    sliding_window_size=50
    main(sliding_window_size)