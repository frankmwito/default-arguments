# return a list of numbers in a range given the starting as the default argument = 1

def range_of(end, start = 1):
    for i in range (start, end):
        print(i)
    
print("Your range in numbers is", range_of(end= int(input("Enter the ending number: ")), start= 1))