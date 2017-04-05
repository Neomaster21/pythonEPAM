from math import sqrt
#Factorial (1)
def Factorial (number):
    if number%1!=0:
        return "It is not integer!"
    else:
        summary = 1
        for i in range(1,number+1):
            summary *=i
        return summary

#Mean square deviation (2)
def MSS (members):
    "Input some list of number and get Mean Square Deviation"
    SUMMARY = 0
    summary_dev = 0
    COUNT_OF_MEMBRES = len(members)
    for i in members:
        SUMMARY +=i
    AVERAGE = SUMMARY/COUNT_OF_MEMBRES
    for i in members:
        deviation = int(i) - AVERAGE
        summary_dev += deviation ** 2
    return sqrt(summary_dev / COUNT_OF_MEMBRES)