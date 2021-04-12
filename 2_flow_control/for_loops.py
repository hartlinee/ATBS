#for loops iterate a specific amount of times

print('My name is ')
i = 0
#while i < 5: 
#for is more concise here, while requires an extra line at bottom
for i in range(5): #range is up to and not including end point
    print('Jimmy Five Times ' + str(i))
    #i = i + 1

#range(10) returns range(0,10)
#range(start, stop)
#range(12, 16) starts at 12 and goes up to 15
#range can be called with three arguments, range(start, stop, step argument)
    #step argument is how much you are counting by, (count by twos, count by -1 to count down etc)

total = 0
for num in range(101):
    total = total + num
print(total)

