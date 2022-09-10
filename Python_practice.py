counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == 'Denver':
     print(counties[1])

temperature = int(input("What is the temperature outside?"))

if temperature > 80:
     print("Turn on the AC.")
else:
     print("Open the windows.")

counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
     print("El Paso is in the list of counties.")
else:
     print("El Paso is not in the list of counties.")

if "Araphahoe" in counties and "El Paso" in counties:
    print("Araphahoe and El Paso in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso in list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

# practicing making my own 'while' loop
# a = 10
# while a >= 5:
#   print(a)
#   a = a -1
#
# practicing making my own 'for' loop
# cities = ["San Diego","Nashville","Boston"]
# for test_list in cities:
#    print(test_list)

# numbers = [0,1,2,3,4,5]
# for num in numbers:
#     print(num)

# for num in range(6):
#     print(num)

counties = ["Arapahoe","Denver","Jefferson"]
for L in range(len(counties)):
    print(counties[L])

# to get keys of dictionary
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

# we can also use the syntax .keys(): to get only the keys from a dictionary
for county in counties_dict.keys():
    print(county)

# to get only the values of a dictionary, use the .values(): syntax
for county in counties_dict.values():
    print(county)

# Get both the Key-Value Pairs of a Dictionary
# use the syntax .items(): in the 'for' loop
for county, voters in counties_dict.items():
    print(county,voters)

voting_data =[{"county":"Arapahoe","registered_voters": 422829},{"county":"Denver","registered_voters": 463353},{"county":"Jefferson","registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
{'county': 'Arapahoe', 'registered_voters': 422829}
{'county': 'Denver', 'registered_voters': 463353}
{'county': 'Jefferson', 'registered_voters': 432438}

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# #Arapahoe
# #422829
# #Denver
# #463353
# #Jefferson
# #432438

for county_dict in voting_data:
    print(county_dict['county'])
# Arapahoe
# Dever
# Jefferson

# F-strings: Formatted String Literals

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of total votes.")

# And here's how you would edit the code to use f-strings

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes")

# Skill Drill to print each county and registered voters from counties dictionary list
counties_dict = {"Araphahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters. ")
        # Araphahoe county has 369237 registered voters. 
        # Denver county has 413229 registered voters. 
        # Jefferson county has 390222 registered voters.

# Using F-Strings with Dictionaries
    # F-strings can be used to print out the keys or values of a dictionary. This will make our code easier to write and read.
        # If we use f-stings, we can rewrite the print statement to be more intuitive and clear.
for county, voters in counties_dict():
      print(f"{county} has {voters} registered voters.")
for county, voters in counties_dict.items():
      print(f"{county} has {voters} registered voters.")
# Araphahoe has 369237 registered voters.
# Denver has 413229 registered voters.
# Jefferson has 390222 registered voters.

# Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
     f"You received {candidate_votes} number of votes. "
     f"The total number of votes in the election was {total_votes}. "
     f"You received {candidate_votes / total_votes * 100}% of the total votes. ")
print(message_to_candidate)

# Format Floating-Point Decimals
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("what is the total number of votes in the election? "))
message_to_candidate = (
     f"You received {candidate_votes:,} number of votes. "
     f"The total number of votes in the election was {total_votes:,}. "
     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")
print(message_to_candidate)