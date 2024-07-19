"""
The program asks the user what number they would like to find in the list. It then searches through the list for the number.
"""

def binary_search(list,n):
    """
    Searches through a list of integers using binary search. Also prints each step.
    """
    list.sort()
    min = 0
    max = len(list) - 1
    middle = 0
    steps = 0

    while min <= max:
        print(f"Step {steps}: {str(list[min:max + 1])}")
        steps += 1
        middle = (min + max)//2

        if n == list[middle]:
            return middle
        elif n > list[middle]:
            min = middle + 1
        else:
            max = middle - 1
    return -1
        
            

my_list = [0,342,275,30,49,69,24,1,3,5,7,15,18]

#starts program
while True:
    try:
        target = int(input("What number would you like to find? "))
        break
    except ValueError:
        print("Only integers are accepted. Try again")

answer = binary_search(my_list, target)

if answer == -1:
    print("The number could not be found in the list.")
else:
    print(f"The number is at index {answer}")

