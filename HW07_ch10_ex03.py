# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################
#Body
def cumulative_sum(list_of_numbers):
    iterator = 0
    while (iterator < len(list_of_numbers)-1):
        list_of_numbers[iterator+1] = list_of_numbers[iterator] + list_of_numbers[iterator+1];
        iterator += 1
    return list_of_numbers

##############################################################

def main():
    lst1 = [1,2,3]
    lst2 = [2,5,10]
    print(cumulative_sum(lst1))
    print(cumulative_sum(lst2))
    pass
if __name__ == '__main__':
    main()
