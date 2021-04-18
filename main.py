"""This program has no general theme. It is simply a combination of
everything I have learned this semester in the class."""

import math

__author__ = 'Jose Nodarse'


def get_square_root(a, b):
    """This function takes in two numbers and cubes them, then adds one and
    takes the square root.
    :param a: First number to be cubed
    :param b: Second number to be cubed
    :return: A integer is returned
    """
    cube_plus_1 = (a ** 2 + b ** 3) + 1
    square_root = math.sqrt(cube_plus_1)
    return square_root


def get_diameter(radius):
    """ This function takes in a number and multiplies it times two.
    :param radius: The radius which is a number
    :return: The diameter of a circle for the given radius
    """
    diameter = (radius * 2)
    return diameter


def get_area(radius):
    """This function takes in a number, squares it, then multiplies it time pi.
    :param radius: The radius which is a number
    :return: The area of a circle for the given radius
    """
    area = math.pi * radius ** 2
    return area


def get_smaller(num1, num2):
    """This function takes in two numbers and compares them. The smaller one
    assigned to the variable smaller.
    :param num1: Any number
    :param num2: Any number
    :return: The smaller of the two numbers
    """
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    return smaller


def get_good_input():
    """This function is meant to test whether the user can follow directions.
    The user is asked to input a whole number, it the user does not, the
    function lets them know and asks for input again until a whole number is
    given.
    :return: Valid is returned once a whole number is given.
    """
    got_good_input = False
    while got_good_input == False:
        try:
            (input("Please enter a whole number: "))
            got_good_input = True
        except ValueError:
            print("That was not a a whole number. Please try again.")
    good = "Valid"
    return good


# noinspection PyUnboundLocalVariable
def find_average():
    """

    :return:
    """
    number = False
    while number == False:
        try:
            num1 = int(input("Enter number: "))
            number = True
        except ValueError:
            print("That was not an acceptable number. Please input a "
                  "whole number.")
    sum2 = 0
    divisor = 0
    # noinspection PyUnboundLocalVariable
    while num1 != 0:
        sum2 += num1
        divisor += 1
        num1 = int(input())
    else:
        average1 = (sum2 / divisor)
    return average1


# noinspection PyUnboundLocalVariable
def find_sum():
    """

    :return:
    """
    total = 0
    for x in range(5):
        sum1 = False
        while sum1 == False:
            try:
                num_1 = int(input("Enter a number: "))
                sum1 = True
            except ValueError:
                print("That was not an acceptable number. Please input a "
                      "whole number.")
        total += num_1
    sum1 = total
    return sum1


def try_boo_op():  # Boolean Operator "and", "or"
    """This function is meant to implement boolean operators. It asks for a
    two numbers within a specific range.
    :return: If both numbers are within the parameters then Valid is output.
    If one number is within the parameters then Partially Valid is output.
    Lastly, if both numbers are outside the parameters then Completely
    Invalid is output.
    """
    weight = input("Enter weight(less than 10): ")
    cost = input("Enter cost(less than or equal to 20): ")
    num1 = float(weight)
    num2 = float(cost)
    if num1 < 10 and num2 <= 20:
        boo_op = "Valid. Both inputs fit the criteria."
    elif num1 < 10 or num2 <= 20:
        boo_op = "Partially Valid. One of the inputs fit the criteria."
    else:  # not(num1 < 10 and/or num2 <= 20)
        boo_op = "Completely Invalid. Both inputs did not fit the criteria."
    output = boo_op
    return output


def main():
    """This is the starting point of the program. It first prints a menu
    with four options to choose from. Depending on the option chosen the
    program goes to that section. Once the section is complete, it goes back
    to the menu page for the user to make another choice. It keeps going
    until the user enters 5.

    """
    # greeting/ introduction to the user
    print("Hello, my name is Jose Nodarse\n")
    user_first_name = input("What is your first name? ")
    user_last_name = input("What is your last name? ")
    print("Nice to meet you,", user_first_name, user_last_name)
    print("This will be a simple program.\nHopefully it does not bore you to "
          "death.\n")

    # Menu
    menu_options = True
    while menu_options:
        print("Enter the choice for what you would like to see")
        print("1.")
        print("2.")
        print("3.")
        print("4.")
        print("5. Quit")
        menu_options = False
        while menu_options == False:
            try:
                pick_option = int(input())
                menu_options = True
            except ValueError:
                print("That was not an acceptable number. Please input a "
                      "whole number between 1 and 5.")
        # noinspection PyUnboundLocalVariable
        if pick_option == 1:
            first_favorite_word = input("What word do you like enough to see "
                                        "it repeated 20 times: ")
            second_favorite_word = input("What other word do you like enough "
                                         "to see it repeated 20 times: ")

            # *: This string operator repeats the same word the indicated
            # number of times.
            print(first_favorite_word * 20)
            print(second_favorite_word * 20)
            print(" ")
            # +: This string operator concatenates or combines words.
            print("Lets see how they look together:", first_favorite_word +
                  second_favorite_word)
            print("It probably looks off right?\nSome words are not meant to "
                  "go together.\n")

        elif pick_option == 2:
            print("Lets do some basic math operations")
            basic_math = False
            while basic_math == False:
                try:
                    first_number = int(input("Enter first number: "))
                    second_number = int(input("Enter second number: "))
                    third_number = int(input("Enter third number: "))
                    fourth_number = int(input("Enter fourth number: "))
                    fifth_number = int(input("Enter fifth number: "))
                    sixth_number = int(input("Enter sixth number: "))
                    seventh_number = int(input("Enter seventh number: "))
                    basic_math = True
                except ValueError:
                    print("That was not an acceptable number. Please input a "
                          "whole number.")
            # noinspection PyUnboundLocalVariable
            num1 = first_number
            # noinspection PyUnboundLocalVariable
            num2 = second_number
            # noinspection PyUnboundLocalVariable
            num3 = third_number
            # noinspection PyUnboundLocalVariable
            num4 = fourth_number
            # noinspection PyUnboundLocalVariable
            num5 = fifth_number
            # noinspection PyUnboundLocalVariable
            num6 = sixth_number
            # noinspection PyUnboundLocalVariable
            num7 = seventh_number

            # basic calculations(**, *, /, %, //, +, -)

            # **: This numeric operator raises numbers to a power.
            print("num1 ** num3 =", num1 ** num3)

            # *: This numeric operator multiplies numbers together.
            print("num2 * num5 =", num2 * num5)

            # /: This numeric operator divides numbers.
            print("num4 / num1 =", num4 / num1)

            # %: This numeric operator is called modulus and it gives the
            # remainder after dividing two numbers.
            print("num3 % num2 =", num3 % num2)

            # //: This numeric operator divides numbers but only gives the
            # integer as the output(does not round).
            print("num1 // num5 =", num1 // num5)

            # +: This numeric operator adds numbers together.
            print("num4 + num6 =", num4 + num6)

            # -: This numeric operator subtracts numbers.
            print("num6 - num7 =", num6 - num7)

            print(" ")
            print("Now to mix it up a little.\n")

            # Combined operations
            print("num2 + num6 * num3 - num4 =", (num2 + num6) * (num3 - num4))
            print("num1 + num2 / num3 - num4 =", (num1 + num2) / (num3 - num4))
            print("num6 % num5 ** num4 + num1 =", (num6 % num5) **
                  (num4 + num1))
            print("num1 / num6 % num7 * num2 =", format((num1 / num6) %
                                                        (num7 * num2), "0.2f"))

            print(" ")

        elif pick_option == 3:
            print("Now lets do something slightly harder, at least for me "
                  "since I am the one coding it\n")

            # Calculating and displaying the the total cost for chosen
            # transport
            print("Imagine you are going traveling, but before you go some "
                  "thinking needs to be done.\n")
            transport_type = input("Enter your favorite mode of "
                                   "transport(ex. airplane, train, etc.): ")
            ticket_cost = False
            while ticket_cost == False:
                try:
                    number_tickets = int(input("Enter the number of tickets "
                                               "needed: "))
                    transport_cost = float(input("Enter the cost of one "
                                                 "ticket: "))
                    ticket_cost = True
                except ValueError:
                    print("That was not an acceptable number. Please input a "
                          "whole number.")
            # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
            total_cost = number_tickets * transport_cost
            print("Transport type:", transport_type)
            print("Cost of one ticket: $", format(transport_cost, ".2f"),
                  sep='')
            print("Number of tickets bought:", number_tickets)
            print("Total cost: $", format(total_cost, ".2f"), sep='')

            print("Lets see if you can follow directions(PS: Don't follow "
                  "directions)")
            print("The operation will repeat, the second will not")
            print(get_good_input())
            print(try_boo_op())

            print("Lets find the average of a set of numbers")
            print("Enter any number you want, except 0. When you want to end, "
                  "enter 0")
            print(format(find_average(), ".2f"))

            print("Finding the Sum of Five Numbers")
            print("The total is:", find_sum())

        elif pick_option == 4:
            # Finding the smaller number
            user_input = False
            while user_input == False:
                try:
                    user_input1 = float(input("Enter a number: "))
                    user_input2 = float(input("Enter a second number: "))
                    user_input = True
                except ValueError:
                    print("That was not a number. Please input a number.")
            # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
            smaller_number = get_smaller(user_input1, user_input2)
            print("The smaller number is:", smaller_number)

            # Get the square root of the cubes of 2 and 3 plus 1
            print("Now lets do some slightly more complicated math")
            print("Lets cube 2 and 3 then add one and take the square root")
            print("The square root of the cubes of 2 and 3 plus 1 is:",
                  format(get_square_root(2, 3), ".2f"))

            # Getting the diameter and Area of a circle
            print("Now for some circle math")
            radius1 = False
            while radius1 == False:
                try:
                    radius = int(input("Enter the radius: "))
                    radius1 = True
                except ValueError:
                    print("That was not a valid number. Please input a whole "
                          "number.")
            # noinspection PyUnboundLocalVariable
            area1 = get_area(radius)
            diameter1 = get_diameter(radius)
            print("The area of the circle is:", format(area1, ".2f"))
            print("The diameter of the circle is:", format(diameter1, ".2f"))

        elif pick_option == 5:
            menu_options = False
        else:
            print("Invalid selection. Try again.")

    print(" ")
    # Using end=
    print("Well that is pretty much it.", end=" ")
    print("Hopefully it was somewhat interesting.")
    print("GOOD BYE :)")


main()
