
current_movies = {'The Hangover': '11:00pm',
                  'LOTR': "10:00pm",
                  'Beauty and the Beast': '9:00am'}

print('these are the current movies: ')

for key in current_movies:
    print (key)

movie = input('Which movie would you like know about?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print('Your requested movie is not available.')
else:
    print(movie, 'is playing at: ', showtime)