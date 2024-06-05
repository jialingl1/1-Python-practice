
contacts = {
    'number': '4',
    'students': [
        {'name': 'Harry', 'email': 'harry@email.com'},
        {'name': 'Hermione', 'email': 'hermione@email.com'},
        {'name': 'Ron', 'email': 'ron@email.com'},
        {'name': 'Dumbledore', 'email': 'dumbledore@email.com'}
    ]
}

print('Student emails:')

for student in contacts['students']:
    print(student['email'])