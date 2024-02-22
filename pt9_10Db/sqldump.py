from connect import *
from readsongs import *

def dump_data():
  # opens the file
  with open("pt9_10Db/songs.sql") as df:
    # reads the open file and save its contents to sqlInsertScript variable
    sqlInsertScript = df.read()
    
    # write the content found/stored in the sqlInsertScript variable
    dbCursor.executescript(sqlInsertScript)
    # now call the all_sngs function from the readsongs file to display updated records
    all_songs()

dump_data()