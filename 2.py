from some_name import Factorial, MSS #The third task

#The first task
print Factorial(5)
print Factorial(5.2)
print

#The second task
test_list = [1,2,3,4,5,6,7,8,9]
print "Mean square deviation: %s \n" % round(MSS(test_list),2)

#The fourth task
with open('Other files/SomeText.txt', 'r') as inf:
    for line in inf:
        print "Entire string: %s" %line,
        print "Part of string from 3 to 7 char: %s \n" %line[2:6]

#The fifth task
PATH = str(raw_input("Input path to file... \n"))
array =[]
with open(PATH, 'r') as inf:
    for line in inf:
        array.append(int(line))
print "\nRead sequence:", array
print "Mean square deviation: %s \n" % round(MSS(array),2)