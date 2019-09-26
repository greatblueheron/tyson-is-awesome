""" this is code for summing the digits of a number """

my_number = 1408                            # this is my number
my_split = str(my_number)                   # this converts my number to a string

my_list = [int(s) for s in my_split]        # this splits the string into its individual numbers in a list

result = sum(my_list)                       # this sums the numbers in the list

print('My result is ', result)              # this prints the result
