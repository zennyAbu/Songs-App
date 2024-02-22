from connect import * 

def update_songs():
  try:
    # SongID is a primary key field
    songID = int(input("Enter the SongID to update a record: "))
    dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")
    
    # fetchone fetches a unique(one) record
    row = dbCursor.fetchone()
    # None is a single object to check if a value is present
    if row == None:
      print(f"No record with the SongID {songID} exists")
    else:
      fieldname = input("Enter the field (Artist, Title, Genre) to update: ").title()
      fieldValue = input(f"Enter the value for {fieldname}: ")
            
      dbCursor.execute(f"UPDATE songs SET {fieldname} = ? WHERE SongID = ?", (fieldValue, songID))
      dbCon.commit()
  
  except sql.OperationalError as e:
        print(f"Failed because: {e}")
  except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
  
  finally:
    print("DB operation performed")

if __name__ == "__main__":
  update_songs()
      