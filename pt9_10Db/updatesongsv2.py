from connect import *

def update_all_fields():
  try:
    songID = int(input("Enter the SongID of the record to update: "))
    dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")
    
    row = dbCursor.fetchone()
    if row == None: # None is a singleton object that checks if a value is present
      print(f"No record with SongID {songID} exists.")
    
    else:
      # get the values to update the respective fields
      sTitle = input("Enter the song Title: ")
      sArtist = input("Enter the song Artist: ")
      sGenre = input("Enter the song Genre: ")
      
      # execute the sql statment to update respective fields
      dbCursor.execute("UPDATE songs SET Title = ?, Artist = ?, Genre = ? WHERE SongID = ?", (sTitle, sArtist,sGenre,songID))
      dbCon.commit()
      
      #print the details of the updated record
      print(f"The record {songID} updated in the songs table")
  except sql.OperationalError as e:
        print(f"Failed because: {e}")
  except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
  
  finally:
    print("DB operation performed")

update_all_fields()