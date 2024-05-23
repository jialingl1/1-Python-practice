
expenses = [10.80, 8, 21, 9, 15]


#comment: one way for adding all expenses using a for in loop
#sum = 0

#for x in expenses:
#    sum = sum + x

#print('You spent $', sum, sep='')


#comment 2: a cleaner way to add expenses using the sum function
total = sum(expenses)

print('You spent $', total, sep='')