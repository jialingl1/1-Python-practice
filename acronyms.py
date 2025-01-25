# ask the user what acronym they want
acronym = input("What acronym do you want to add?\n")

#ask user for the definition
definition = input("What is the definition?\n")


#open the file
# found = False

with open('acronyms.txt') as file:
    for line in file:
        if acronym in line:
            print(line)
            found = True
            break

if not found:
    print("The acronym does not exist") 

# write the new acronym and definition to the file
