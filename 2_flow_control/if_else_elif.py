#if, else, and elif

name = 'Alice'

if name == 'Alice': #condition statement
    print('Hi, Alice')
print('Done')

#this condition will return False
name = 'Bob'

if name == 'Alice': #condition statement
    print('Hi, Alice')
print('Done')

#condition returns True
password = 'swordfish'
if password == 'swordfish':
    print('Access granted')
else:
    print('Access denied')

#elif block executes if it is true and all previous conditions have been false
#else is at the end, executes if all previous conditions have been false
name = 'Bob'
age = 3000
if name == 'Alice':
    print(Hi, Alice)
elif age < 12:
    print('You are a child!')
elif age > 1000:
    print('Hello Lich')
#though age is also > 100, will not go that far bc the age > 1000 has already been called
elif age > 100:
    print('Are you a Lich?')


#truthy and falsey values
print('Enter a name: ')
name = input()
#if name: 
#this checks to see if the empty string (no name) is present. if so, then will return false, and go to the else statement 
# not ideal way to check, can be more explicit, so something like the below is better
if name != '':
    print('Thank you.')
else:
    print('You did not enter a name.')

# 0 and 0.0 are considered falsey, all other truthy
print('This is what returns when 0 is passed to bool: ' + str(bool(0)))
print('This is what returns when 0.0 is passed to bool: ' + str(bool(0.0)))
print('This is what returns when 42 is passed to bool: ' + str(bool(42)))
#you can see which values are Truthy or Falsey by passing them to bool()
