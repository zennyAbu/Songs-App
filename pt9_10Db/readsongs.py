from connect import *

def all_songs():
  try:
    # try to execute the sql statemrnt below
    dbCursor.execute("SELECT * FROM songs")
    
    # allsongs = dbCursor.execute("SELECT * FROM songs").fetchall()
    
    # fetch all selected data(rows)
    allsongs = dbCursor.fetchall() # fetchall fetches all the records(rows) from the table
    
    if allsongs:
      # format output
      print("SongID | Title | Artist | Genre")
      print("-" * 50)
      
      for aSong in allsongs:
        print(f"{aSong[0]:<2} | {aSong[1]:<10} | {aSong[2]:<20} | {aSong[3]:<7}")
    else:
      print("No songs found in the songs table")
  
  except sql.OperationalError as e:
        print(f"Failed because: {e}")
  except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
  
  finally:
    print("DB operation performed")

if __name__ == "__main__":    
  all_songs()