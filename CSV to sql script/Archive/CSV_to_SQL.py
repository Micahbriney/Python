import os
import csv
import glob
import pandas as pd
import numpy as np
from pathlib import Path


  ## 
  #
  # Program will take in one csv file in the same directory
  #   and output an INSERT script like the ones below.
  # Unsure what will happen when more than one file is in directory
  #
  #
  #    INSERT INTO tasks(title, priority)
  # VALUES
  # 	('My first task', 1),
  # 	('It is the second task',2),
  # 	('This is the third task of the week',3);
  #
  ##

for filename in glob.glob('*.csv'): # open a csv file. One or many???
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        data = pd.read_csv(f)    ## read cvs into data

with open("Insert.txt", "w") as ff:
   
   df = pd.DataFrame(data) # create dataframe, index(rows) and headers/columns
   hd = df.columns
   
   
   ##
   #
   # For testing purposes to see what the output will be
   #
   ##
   
   
   fname = filename.rsplit('.',1)[0]
   print('\tINSERT INTO', fname, '(', end = '')
   print( *hd, sep=',', end = '')
   print(')')
   print('VALUES')
   for index, row in df.iterrows() :
       print('\t(', end = '')
       for i in range(df.shape[1]) :
           print('' if df.dtypes[i] == np.int64 else '\'', end = '')
           print(row[i], end = '')
           print('' if df.dtypes[i] == np.int64 else '\'', end = '')
           print(',' if i < (df.shape[1] - 1) else ')', end = '')
       print( ',' if index < (len(df.index) - 1) else ';')
    
    
   ##
   #
   # Output to file ff
   #
   # file = 'filename' you can output the stdout to a file
   # end = '' remove /n added at end of print statements
   # df.shape returns num of (rows, cols)
   # range(df.shape[1]) returns num of cols. Changes range df.shape to an int
   # 
   ##
    
   fname = filename.rsplit('.',1)[0]    # extract csv filename before '.'
   print('\tINSERT INTO', fname, '(', end = '', file=ff )
   print( *hd, sep=',', end = '', file=ff)   # iterate headers. stdout >file
   print(')', file=ff)
   print('VALUES', file=ff)
   for index, row in df.iterrows() :    # iterrate rows
       print('\t(', end = '', file=ff)  # formatting with tab
       for i in range(df.shape[1]) :    # iterate though all column's rows
           print('' if df.dtypes[i] == np.int64 else '\'', end = '', file=ff)
           print(row[i], end = '', file=ff) # stdout 1 (row, col) at a time
           print('' if df.dtypes[i] == np.int64 else '\'', end = '', file=ff)
           print(',' if i < (df.shape[1] - 1) else ')', end = '', file=ff) #fmt
       print( ',' if index < (len(df.index) - 1) else ';', file=ff) # fmtting

  
ff.close()
f.close()
