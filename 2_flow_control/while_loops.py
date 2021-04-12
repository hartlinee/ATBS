#while loops

spam = 0
#iterates 5 times
while spam < 5:
    print('Hello world')
    spam = spam +1

#while block should be used to recheck the condition, where an if only checks once

#input validation, technically 
name = ''
while name != 'your name':
    print('Please enter a name: ')
    name = input()
print('Thank you')

#this will cause an infinite loop bc of the validation
name = ''
while True: #causes the infinite loop
    print('Please enter a name: ')
    name = input()
    if name == 'your name':
        break #causes the the execution to leave the loop without re-checking the condition
print('Thank you')

#continue 
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue #this jumps back up to the start of the loop and rechecks the condition, so the print is never called for 3
    print('spam is ' + str(spam))