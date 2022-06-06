# 1. Basic - PRint all integers from 0 -> 150 

for x in range(151):
    print(x)


# 2. Multiples of Fives - Print all the mutliples of 5 from 5 to 1,000

for x in range(5, 1001):
    if x % 5 == 0:
        print(x)


# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for x in range (1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range (0, 500001):
    if x % 2 != 0:
        sum = sum + x
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for x in range (2018,0,-4):
    print(x)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 1
highNum = 100
mult = 6

for x in range (lowNum,highNum):
    if x % mult == 0:
        print(x)