""""
by: Jean Prinston
This is a DEMO explaining how to use Git command line tools
12/4/23
"""""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def display_even_numbers(stop):
    """
    this function displays all even numbers to the "stop" parameter
    - non-inclusive
    """
    for number in range(stop):
        if number % 2 == 0:
            print(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    display_even_numbers(100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
