# Data Structure: Lists
# The items in a list can be data types such as integers, floating-point decimals, strings, and Boolean values, as well as other data structures like lists, tuples, and dictionarie
# 1. We can use indexing and slicing to retrieve specific items from the list
# 2. We can add or remove items from a list, which makes lists a dynamic data structure
# 3. We can change the contents in a list. For example, we can change "Jefferson" to "El Paso." This means lists are mutable: we can change one or more items in a list to something else
# syntax: my_list = []


school_supplies = ["pencils","pens","notebooks","markers","backpack"]
print(school_supplies)

# An index of a variable is its position in the array. Here are some general rules for indexing:
# 1. Each item in a list has an index that specifies its position in the list
# 2. Indexing starts at 0. Therefore, the index of the first item is 0, the index of the second number is 1, and so on
# 3. Because indexing begins at 0, the index of the last item in a list is 1 less than the number of items in the list
# To get the 2nd item, pens, from a list:
print(school_supplies[1])

# Negative indexes are used to identify a list item's position relative to the end of the list. This is to identify the last item on the list:
print(school_supplies[-1])
# To get the second-to-last item in a list (markers), we would type list[-2], and so forth.
print(school_supplies[-2])

# Find the Length of a List
print(len(school_supplies))

# Slice Lists
# Sometimes we'll need to retrieve certain items from the list. To do this, we can use the index values to slice a list 
# Slicing is used to get specific items from a list. The format for slicing a list is as follows: list[start : end]
# The expression list[start : end] returns a list containing a copy of the items in the list from the starting index value up to, but not including, the ending index value
# To pull a list of the first 4 items:
print(school_supplies[0:4])
print(school_supplies)

# Add Items to a List
# list.append()
# items added without assigning an index will always be added to the end of the list. adding laptop to the list
print(school_supplies.append("Laptop"))
print(school_supplies)

# To specify where in a list to add a new item, select the location with an index by using the following syntax, list.insert(index, obj)
# add Post-it Notes as the 3rd item on the list
school_supplies.insert(2, "Post-it Notes")
print(school_supplies)

# To remove - list.remove()
# remove Post-it Notes
school_supplies.remove("Post-it Notes")
print(school_supplies)

# Another method list.pop() > remove pencils
school_supplies.pop(0)
print(school_supplies)

# Change an Element in a List
# syntax list[index] on the left side of the equals sign; on the right side, you assign the index a new data value
# The new value can be an integer, floating-point decimal number, string, Boolean value, another list, tuple, or dictionary
# change markers (3rd on the list) calendar
school_supplies[2] = "Calendar"
print(school_supplies)

# Data Structures: Tuples
# Tuples are lists, but are immutable: we can't add or remove items from them
# my_tuple = ()
grocery_list = ("Peanut Butter","Jelly","Almond Milk","Veggies")
print(grocery_list)

# to find the length of the list, it's the same syntax
len(grocery_list)
print(len(grocery_list))

# Get item from tuple list, apply index position and slicing using square brackets
print(grocery_list[2])

# Data Structures: Dictionaries. A dictionary is an object that stores a collection of data.
# A Python dictionary has a key and a value, or key-value pairs
# Key-value pairs are enclosed in a set of curly braces, {} followed by a colon :
# {key:value}
# Keys must be immutable objects, like integers, floating-point decimals, or strings. Keys cannot be lists or any other type of mutable object.
# Values in a dictionary can be objects of any type: integers, floating-point decimals, strings, Boolean values, datetime values, and lists.
# Create a Dictionary
# my_dictionary = {}

dog_descriptions = {}
dog_descriptions["Beans"] = "White Lab Husky Eskimo"
dog_descriptions["Roshi"] = "Chocolate Lab"
dog_descriptions["Jeter"] = "Yellow Golden Retriever"
dog_descriptions["Georgie"] = "Tri Colored English Shepard"
print(dog_descriptions)

# get lenghth of items in dictionary
print(len(dog_descriptions))

# get list of both keys and values in dictionary
print(dog_descriptions.items())

# Get All the Keys
# .keys()
# dictionary_list.keys()
dog_descriptions.keys()
print(dog_descriptions.keys())

# Get All the Values
# .values()
# dictionary_list.values()
dog_descriptions.values()
print(dog_descriptions.values())

# Get a Specific Value
# 2 ways to get a specific value of a key
# first is
# .get("key")
dog_descriptions.get("Beans")
print(dog_descriptions.get("Beans"))
# second is wrapping the key in square brackets
# dictionary_name["Beans"]
dog_descriptions["Beans"]
print(dog_descriptions["Beans"])

# Lists of Dictionaries
# Sometimes Python dictionaries have the same keys associated with different values, which are written in this format
# [{key1:value1, key2:value2}, {key1:value3, key2:value4}]
# first, create an empty dictionary list
# list_name = []
# to start a new dictionary list, we have to add the name with square brackets
voting_data = []
# to write out the code/list of dictionary, we have to use parenthesis and curly brackets
voting_data.append({"county":"Araphaoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered voters":463353})
voting_data.append({"county":"Jefferson","registered voters":432438})
print(voting_data)

# Decision Statements
# The 'input' function asks a user for text input. Once the user inputs text and presses Enter, the program will resume.

# If Statements: If a condition is met (ie: is true) then an action is performed. If the condition is not met (ie: false), then the action is not performed
# In Python, the general format for the 'if' statement is to write a single alternative decision as follows:

# if condition:
   # statement 1
   # statement 2

# Remember, if statements tell the computer that certain lines of code should only run under certain conditions. 
# The if statement checks if a condition is true. If it's true, then a block of code below it will run.
# If the statement is not met (i.e., is false), then the statements in the block are skipped.

# Membership Operators
# Membership operators are used to test if an object, like a string, integer, or other data type is present in an expression, list, tuple, or dictionary. 
# The following table describes these operators and provides an example of each one.
# operator 'in' means it will return "true" if a sequence with the specified value is present in the object.
# operator 'not in' it will return "true" if a sequence with the specified value is NOT present in the object.

# Logical Operators
# Logical operators allow us to connect multiple comparison expressions to create a compound expression. There are three logical operators: 'and', 'or' and 'not'
    # 'and' Evaluates two Boolean expressions into one compound expression. The compound expression is True if both Boolean expressions are True.
    # If one of the expressions is False, then the compound expression is False.

    # 'or' Evaluates two Boolean expressions into one compound expression. The compound expression is True if either Boolean expression is True.
    # If one of the expressions is false, then the compound expression is True. If both expressions are False, then the compound expression is False.

    # 'not' Evaluates a Boolean expression. The expression is true if the conditional is false.

# Repetition Statements
# There are two categories of repetition structures: condition-controlled loops and count-controlled loops
    # a 'condition-controlled loop' uses a true/false condition to control the # of times it will repeat - this is called  a 'while' loop
    # Needs two parts to run:
        # A condition that is tested for a true or false value.
        # A statement or statements that are repeated as long as the condition is true.

        # x = 0
        # while x <= 5:
        #   print(x)
        #   x = x + 1

    # a 'count-controlled' loop repeats a specified # of times depending on the conditions - this is called a 'for' loop
        # 'for' loops iterate, or run through, a program a specidfic # of times before it stops. A 'for' loop can be written like 'if' and 'if-else'.

        # for item in [item]:
        #   statement 1
        #   statement 2  

        # cities = ["San Diego","Nashville","Boston"]
        # for test in cities:
        #    print(test)

# Iterate Through a Dictionary
# We can use a for loop to iterate over a dictionary and get all the keys, all the values, or all the keys and values.
# Get the Keys of a Dictionary
    # To get only the keys from a dictionary using a 'for' loop, the loop can be written like we are iterating over a list or tuple
        # for 'county' in 'counties_dict':
            # print('county')

# Get the Values from a List of Dictionaries
# To retrieve only the values from each dictionary in the list of dictionaries, we need to use a nested 'for' loop
    # First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. 
    # Then, in the second for loop, use the values() method on the variable county_dict to reference the data in the second for loop in order to get each value

        # for county_dict in voting_data:
            # for value in county_dict.values():
                # print(value)

# The print() Function
# 1. print("Hello World")
    # Hello World
# 2. print("Your interest for the year is $" + str(interest))
# interest = 3
# print("Your interest for the year is " + str(interest))
    # Your interest for the year is 3

# F-strings: Formatted String Literals
    # With Python 3.7, printing has become much easier with the use of f-string literals, which can be used in place of concatenation. 
    # The general format for f-strings is as follows
        # 1. the f-string begins with the letter 'f' following by a string contained within quotes
        # 2. in the f-string, curly braces are used to add variables or expressions to the f-string
                    # my_votes = int(input("How many votes did you get in the election? "))
                    # total_votes = int(input("What is the total votes in the election? "))
                        # print(f"I received {my_votes / total_votes * 100}% of the total votes")
# How many votes did you get in the election? 2500
# What is the total votes in the election? 4000
 # I received 62.5% of the total votes

# Using F-Strings with Dictionaries
    # F-strings can be used to print out the keys or values of a dictionary. This will make our code easier to write and read.
    # If we use f-stings, we can rewrite the print statement to be more intuitive and clear.
                    # for county, voters in counties_dict():
                        # print(f"{county} has {voters} registered voters.")
# Araphahoe has 369237 registered voters.
# Denver has 413229 registered voters.
# Jefferson has 390222 registered voters.

# Multiline F-Strings
    # Another use for f-strings is to print multiple strings or lines to the screen. 
    # Let's say you need to tell a candidate how many votes they won, the total number of votes, and the percentage of votes they received. 
    # You can use the code you wrote to calculate the percentage of votes and create a message to be printed to a screen, like this:
                # candidate_votes = int(input("How many votes did the candidate get in the election? "))
                # total_votes = int(input("What is the total number of votes in the election? "))
                # message_to_candidate = (
                #   f"You received {candidate_votes} number of votes. "
                #   f"The total number of votes in the election was {total_votes}. "
                #   f"You received {candidate_votes / total_votes * 100}% of the total votes.")
                # print(message_to_candidate)
# How many votes did the candidate get in the election? 1234
# What is the total of votes in the election? 4321
# You received 1234 number of votes. The total number of votes in the election was 4321. You received 28.558204119416803% of the total votes. 

# Format Floating-Point Decimals
    # In Python, we can format numbers with a thousands separator and specify a decimal precision.
    # The general format for a number to format it in an f-string is as follows:
    # f'{value:width}.{precision}}'
    # width specifies the number of characters used to display the value, however if a value needs more space than the width spcifies, the additonal space is used
    # precision indicates the number of decimal places to format the value. ie: to format interest to two decimal places, we use .2f, where f means floating-decimal format
    # when formatting numbers, we use the thousands separator comma and it's placed after the {width}
        # f'{value:{width},.{precision}}'

# Pseudocoding
    # Pseudocode will make the audit easier to present to nontechnical colleagues and stakeholders.