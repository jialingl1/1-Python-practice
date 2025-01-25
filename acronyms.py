# ask the user what acronym they want
acronym = input("What acronym do you want to add?\n")

#ask user for the definition
definition = input("What is the definition?\n")


#open the file
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')

# write the new acronym and definition to the file
