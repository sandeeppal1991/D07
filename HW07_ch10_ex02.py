# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################
#Body
def capitalized_nested(list_of_words):
    for each_list_item in list_of_words:
        if(str(type(each_list_item)) != "<class 'NoneType'>"):
            if(str(type(each_list_item)) == "<class 'list'>"):
                capitalized_nested(each_list_item)
            else:
                list_of_words[list_of_words.index(each_list_item)] = each_list_item.upper()

##############################################################

def main():
    # lst1 = ['apple', ['bear'], 'cat']
    lst2 = ['apple',['bear','cat'],'dog']
    capitalized_nested(lst2)
    print(lst2)

    pass
if __name__ == '__main__':
    main()
