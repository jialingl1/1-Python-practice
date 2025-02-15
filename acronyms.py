def find_acronym():
    look_up = input("What acronym would you like to look up?\n")

    found = False
    with open('acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
    if not found:
        print("The acronym does not exist")


def add_acronym():
    # ask the user what acronym they want
    acronym = input("What acronym do you want to add?\n")

    #ask user for the definition
    definition = input("What is the definition?\n")


    #open the file
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

    # write the new acronym and definition to the file

#add main function
        
def main():
    #ask user if they want to add or find a function
    choice = input("Do you want to find(F) or add (A) an acrinym?\n")
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

#call main function
main() 
