# product of list as user oriented and number as default argument
def product(number_list, number=2):
    num = int(input("Enter the size of your list: "))
    
    for i in range(num):
        digit = int(input(f"Enter digit {i+1} in the list: "))
        number_list.append(digit)
        
    new_list = []
    for i in number_list:
        new_list.append(i * number)
        
    return new_list

number_list = []

print("The product of the list is:", product(number_list, number=5))

    