import readsongs, addsongs, updatesongs, deletesong, search

def read_file(file_path): # file_path is a parameter/variable
  try:
    with open(file_path) as readfile:
      rf = readfile.read()
    return rf
  except FileNotFoundError as nf:
    print(f"file not found: {nf}")
# Testing file path
# print(read_file("pt9_10Db\menuOptions.txt"))

def songs_menu():
  option = 0 # intialising/assign the option variable with an integer value 0
  optionsList = ["1","2","3","4","5","6"]
  # call the read_file function and assign to a variable
  menu_choices = read_file("pt9_10Db\menuOptions.txt")
  
  # repeat the menu options until the user selects to quit
  while option not in optionsList:
    print(menu_choices) # print the menu_choices variable because it is a function
    # re-assign the option variable a string value
    option = input("Enter an option from the menu choice above: ")
    
    # check if the input provided in options variable is not outside of 1,2,3,4,5,6
    if option not in optionsList:
      print(f"{option} is not a valid choice! ")
  
  return option

# testing
# print(songs_menu())

# create and use a boolean flag variable
mainProgram = True # toggle to false to exit out of the while loop

while mainProgram: # while True
  # call the songs_menu function and assign to a varaible(main_menu)
  main_menu = songs_menu()
  
  # use match case # same as switch in JS
  match main_menu:
    case "1": # call the readsong file and the function display all songs
      readsongs.all_songs()
    case "2":
      addsongs.insert_songs()
    case "3":
      updatesongs.update_songs()
    case "4":
      deletesong.delete_asong()
    case "5":
      search.search_song()
    case _:
      mainProgram = False # set to fasle to exit the menu

input("Press enter to exit...................")