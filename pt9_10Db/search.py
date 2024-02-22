from connect import *
def search_song():
        try:
                #ask for the field to search by
            field = input("Search by SongID, Title, Artist, Genre: ")
 
            if field == "SongID":
                # search by songID
                idInput = int(input("Enter SongID: "))
                dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (idInput,))
                row = dbCursor.fetchone()
 
                if row is None:
                    # if the songID entered is not in the table
                    print(f"No record with SongID {idInput} exists")
                else:
                    # if the songID entered is exiata in the table
                    for aSong in row:
                        print(aSong)
 
            elif field in ["Title", "Artist", "Genre"]:
                # search by Title, Artist, Genre
                strInput= input(f"Enter the value for the field {field}: ")
                #SELECT * FROM songs WHERE "Title", "Artist", "Genre"  LIKE "Dance" or "MJ" or "Rap"?
                # dbCursor.execute("SELECT * FROM songs WHERE ? LIKE ?", (field,strInput))
                dbCursor.execute(f"SELECT * FROM songs WHERE {field} LIKE '%{strInput}%'")
 
                rows = dbCursor.fetchall()
                if not rows:
                    print(f"No record with field {field} matching '{strInput} ")
                else:
                    # display all matched records for the search field
                    for records in rows:
                        print(records)
 
            else: # where the search input is not  SongID, Title, Artist, Genre
                print(f"Search field {field} invalid !")
        except sql.OperationalError as e:
            print(f"Failed because: {e}")
        except sql.ProgrammingError as pe:
            print(f"Not working because: {pe}")
        finally:
            print("DB operation performed")

if __name__ == "__main__":
    search_song()
    