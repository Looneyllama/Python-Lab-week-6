# Python-Lab-week-6
Python assignments I had to do in my coding lab: 




fibonacci_iterative.py instructions:
Write a function fibonacci_iterative(n) that calculates the nth Fibonacci number using an iterative approach.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. That is, the sequence starts 0, 1, 1, 2, 3, 5, 8, 13,...

In mathematical terms, the nth Fibonacci number is defined recursively as: F(n) = F(n-1) + F(n-2)

with initial conditions:
F(0) = 0, F(1) = 1




hexagonal.py instructions: 

Functions can accept 0 or more arguments and can return exactly 1 item, which may
be None, a single variable, or a container that holds several items. To show how this
works and get you some practice, you will write a complete Python 3 program that
calculates the surface area of a hexagonal prism using a few different types of
functions.

First, the surface area of a hexagonal prism can be described as follows:
This means that the total surface area of the prism is the sum of the area of the
hexagonal faces (at the top and bottom) and the area of the six rectangular sides.
Write a small, but complete Python3 program called Lab6A.py that computes and
prints out the surface area of a hexagonal prism as follows:

A = 6ah + 3 * sqrt(3) * a^2 

a. Create a user-defined function called calc_hex_area() that accepts one
argument, the length of the base edge of the hexagonal prism in feet. This function
will simply have one line that returns the surface area of the 2 hexagonal faces
using the formula above.

b. Create a user-defined function called calc_side_area() that accepts two
arguments, the length of the base edge and the height of the hexagonal prism in
feet. This function will simply have one line that returns the surface area of the 6
rectangular faces using the formula above.

c. Create a user-defined function called display_surface_area() that
accepts two arguments, the surface area of the hexagonal faces and the surface
area of the rectangular sides returned in calc_hex_area() and
calc_side_area() functions, respectively. This function will simply have one
line that prints the sum of the two area arguments passed to the function with no
return statement. Be sure to format the result to 3 decimal places.

d. Prompt the user for and read in the length of the base edge, a, and height, h, of a
hexagonal prism as floating-point numbers in feet.

e. Call the calc_hex_area() function, passing in the length of the base edge
entered by the user, and assigning its return value to the variable called
hex_area. Then, print the surface area of the hexagonal faces, formatting the
result to 3 decimal places.

f. Call the calc_side_area() function, passing in the length of the base edge
and the height of the hexagonal prism entered by the user, and assigning its return
value to a variable called side_area. Then, print the surface area of the
rectangular sides, formatting the result to 3 decimal places

g. Call the display_surface_area() function, passing in the surface areas of
the hexagonal faces and rectangular sides. Note that no assignment is needed
since this function does not return any item.

For example, the output might look like this (input shown in bold):
$ python3 Lab6A.py
Enter height of hexagonal prism in feet: 6.5
Enter length of the base edge in feet : 4.2
Surface area of hexagonal faces is 91.660 square feet
Surface area of rectangular sides is 163.800 square feet
The total surface area is 255.460 square feet




list.py instructions:

In this lab component, you will explore working with functions and lists.
a. Create a user-defined function that accepts no arguments and returns a list.
  • Create an empty list.
  • Prompt for and read in the number of integer values in the list.
  • Use a loop and the range() function to iterate through the number of values
    in the list. Inside the loop:
    o Prompt for and read in each integral value and then append the item to
    the end of the list.
  • Return the list.

b. Create another user-defined function that accepts one argument, the list of
integers, and returns the second highest number in a list of integers without
modifying the original list.

There are several ways to do this. The first is the more complicated way of
manually stepping through each element in the list, keeping track of the both the
highest and second highest integers in the list. However, we want to take
advantage of some Python 3 capabilities and let Python do the work! Other ways
would be to sort the list or remove the largest integer, but since lists are mutable,
this modifies the list, which is not acceptable. Let’s explore a couple different ways
to copy a list.

  • Make a copy of the list using the assignment operator =, such as new_list
    = old_list.
  • Use the list sort() method to sort the list. Remember the difference
    between a method and a function – a method is associated with an object and
    accessed using the dot operator.
  • Print the original list (i.e., the list that was passed to the function to see if it
    was updated by the sort() method.
  • Return the second largest element in the now sorted copy of the list.
    Remember that you can access the largest item at the end of the list using -1.
    Before we go on to the next part of this lab component, was the original list
    modified when you sorted your new list? What happened is that the assignment
    operator = made a shallow copy of the original list, meaning that the objects were
    the same so that if one was modified, so was the other. Instead, we want a deep
    copy that can be accomplished using the copy() method that creates a separate
    instance of the list.
  • Now, instead of making a copy using the assignment operator =, use the
    copy() method to make a deep copy of the original list.

c. Create another user-defined function that accepts one argument, the list of
integers, and modifies the list so that all the integers in the list are zero or positive
(i.e., not negative) without returning any item.
  • Loop through the list, but instead since we want to access and modify
    individual elements in the list, we should iterate from 0 to the length of the list
    (using the range() function). Inside the loop:
    o If the element in the list is less than 0, modify that element in the list to
    make it positive using the abs() function in the math module.
    o Note that there is no return statement in this function.
  
d. Once the three functions are defined, you will call your function to create your list,
without passing any arguments, assigning the result to a list.

e. Print your list.

f. In a print() statement, call your function that returns the second highest
integer, passing in your list as an argument, with an appropriate message.

g. Call your function to make all elements in the list zero or positive, passing in your
list as an argument.

h. Finally, print your now positive list.

For example, the output might look like this (input shown in bold):
$ python3 Lab6B.py
Enter number of integers in list: 5
Enter item #1: 4
Enter item #2: -3
Enter item #3: 8
Enter item #4: 7
Enter item #5: -1
My original list: [4, -3, 8, 7, -1]
[4, -3, 8, 7, -1]
Second largest integer in list is 7
My now positive list is [4, 3, 8, 7, 1]

