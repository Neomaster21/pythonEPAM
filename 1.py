from math import sqrt
#first task
print "THE FIRST TASK (A)"
string_1 = str(raw_input("Input string no less then 10 symbols:"))

if len(string_1)<10:
    while len(string_1)<10:
        print "Error!"
        string_1 = str(raw_input("Input string no less then 10 symbols: \n"))
else:
    print "Good boy"

print string_1[0:4]
print string_1[len(string_1)-4:]
print string_1[len(string_1)/2-1]
print string_1[2:8]
print len(string_1), len(string_1)/2


#second task
print "THE SECOND TASK"
massiv = str(raw_input("Enter the 6 members separating them with a comma \n"))
a = massiv.split(",")
if len(a)>6 or len(a)<1:
    print "Enter 6 members!"
    while True:
        massiv = str(raw_input("Enter the 6 members separating them with a comma \n"))
        a = massiv.split(",")
        if len(a)==6: break;

print a[3]
for i in range(-1,-len(a)-1,-1):
    print a[i],

summa = 0
for i in a:
    summa += int (i)
else:
    print summa

print "Average: ", summa/len(a)

summa_dev = 0
for i in a:
    deviation = int(i) - summa / len(a)
    print deviation
    summa_dev += deviation**2

print "Mean square deviation: ", sqrt(summa_dev/len(a))


#seconds task (a)
print "THE SECOND TASK (A)"
massiv = str(raw_input("Enter the members separating them with a comma \n"))
a = massiv.split(",")

summary = 0
for i in a:
    summary +=i

print "Summary of all numbers: ", summary
print "Average: ", summary/len(a)

for i in a:
    summary +=i
    deviation = int(i) - summary / len(a)
    summa_dev += deviation ** 2
    print "Deviation: ", deviation

print "Mean square deviation: ", sqrt(summa_dev/len(a))


#The fourth task (a)
print "THE FOURTH TASK"
for i in range(501):
    if i%7==0 and i!=0:
        print i


#The fifth task (a)
print "THE FIFTH TASK"
massiv = str(raw_input("Enter the members separating them with a comma \n"))
a = massiv.split(",")
for i in a:
    if int(i)%2!=0 and int(i)!=0:
        print int(i)*2
