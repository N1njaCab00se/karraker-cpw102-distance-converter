# Distance Converter
# This program does two conversions:
# 1. miles, feet, and inches -> total inches
# 2. total inches -> miles, feet, and inches

# numbers I need for the math
inches_in_feet = 12
feet_in_mile = 5280
inches_in_mile = inches_in_feet * feet_in_mile


# this function turns miles, feet, and inches into total inches
def convert_to_inches(miles, feet, inches):
    miles_in_inches = miles * inches_in_mile
    feet_in_inches = feet * inches_in_feet
    total = miles_in_inches + feet_in_inches + inches
    return total


print("Distance Converter")
print()

# Part 1: miles, feet, inches -> total inches
print("Part 1: Convert miles, feet, and inches to total inches")
miles_input = int(input("How many miles? "))
feet_input = int(input("How many feet? "))
inches_input = int(input("How many inches? "))

total_inches = convert_to_inches(miles_input, feet_input, inches_input)

print(f"{miles_input} miles, {feet_input} feet, and {inches_input} inches is {total_inches} total inches.")
print()

# Part 2: total inches -> miles, feet, inches
print("Part 2: Convert total inches to miles, feet, and inches")
total_inches_input = int(input("How many total inches? "))

# floor division gives the whole miles, and % gives what is left over
miles_result = total_inches_input // inches_in_mile
inches_left_after_miles = total_inches_input % inches_in_mile

# now do the same thing with the leftover inches to get feet
feet_result = inches_left_after_miles // inches_in_feet
inches_result = inches_left_after_miles % inches_in_feet

print(f"{total_inches_input} inches is {miles_result} miles, {feet_result} feet, and {inches_result} inches.")