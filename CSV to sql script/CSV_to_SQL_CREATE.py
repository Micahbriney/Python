import os
import csv
import glob
import pandas as pd
import numpy as np
from pathlib import Path
from pandas.api.types import is_string_dtype


  ## 
  #
  # Program will take in one csv file in the same directory
  #   and output an CREATE TABLE script like the ones below.
  # Unsure what will happen when more than one file is in directory
  #
  #
  #      CREATE TABLE albums (
  #      	AId INTEGER,
  #      	Title VARCHAR(30),
  #      	Year INTEGER,
  #      	Type: type of recording (studio, live, etc.)
  #      	Label: label (record company) that released the album
  #      );
  #
  ##

for filename in glob.glob('*.csv'): # open a csv file. One or many???
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        data = pd.read_csv(f)    ## read cvs into data

with open("Create.txt", "w") as ff:
   
   df = pd.DataFrame(data) # create dataframe, index(rows) and headers/columns
   hd = df.columns
   
   
   ##
   #
   # For testing purposes to see what the output will be
   #
   ##
   
   
   fname = filename.rsplit('.',1)[0]
   print('CREATE TABLE', fname, '(')
   for index in hd:
       print('\t' + index.strip() + ' ', end = '')
       print('VARCHAR(30),' if df.dtypes[index] == object else 'FLOAT,' if df.dtypes[index] == np.float64 else 'INTEGER,')
   print('\tPRIMARY KEY()\n);')

    
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
    
   fname = filename.rsplit('.',1)[0]
   print('CREATE TABLE', fname, '(', file=ff)
   for index in hd:
       print('\t' + index.strip() + ' ', end = '', file=ff)
       print('VARCHAR(30),' if df.dtypes[index] == object else 'INTEGER,', file=ff)
   print('\tPRIMARY KEY()\n);', file=ff) 

  
ff.close()
f.close()
