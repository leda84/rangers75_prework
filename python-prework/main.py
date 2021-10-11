#Question 1
def hello_name(user_name):
    print('Hello ' + user_name + '!')

hello_name('Christopher')

#Question 2
#print all odd numbers between 1 and 100
def add100():
    print([value for value in range(1,100,2)])

#add100()

#print first 100 odd numbers
def first_100():
    numbers = list(range(0,201))
    for number in numbers:
        if number % 2 != 0:
            print(number)
#first_100()

#Question 3 write a function that returns the max number in a given list
def max_num(a_list):
    max_value = max(a_list)
    return max_value

print(max_num([2,3,5,8,9]))

#Question 4 write a function to return if a given year is a leap year

def is_leap_year(a_year):
    """
        Return true or false whether a given year is a leap year.
    """
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2019)
is_leap_year(2028)

#question 5 write a function to check if numbers in the given list are consecutive

def is_consecutive(a_list):
    """
        Figure out if all numbers in the given list are consecutive
    """
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

print(is_consecutive([1,2,3,4,5,7]))
print(is_consecutive([1,2,3,4,5,6]))

def is_consecutive2(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i+1]:
            i+=1
        else:
            status = False
            break
    print(status)

is_consecutive2([3,4,5,6])
is_consecutive2([1,5,2,3])
