from connect import *
 
def delete_asong():
    try:
        #check if the song id exists
        songID  = int(input("Enter the SongID to delete arecord : "))
        dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")
 
        row = dbCursor.fetchone()
 
        if row == None:
            print(f"SongID {songID} does not exits")
        else:
            dbCursor.execute("DELETE FROM songs WHERE SongID = ?", (songID,))
            dbCon.commit()
            print(f"The record {songID} deleted from the songs table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")

if __name__ == "__main__":   
    delete_asong()