# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################
#Body
def capitalize_nested(list_of_words):
    for each_list_item in list_of_words:
        if(str(type(each_list_item)) != "<class 'NoneType'>"):
            if(str(type(each_list_item)) == "<class 'list'>"):
                capitalize_nested(each_list_item)
            else:
                list_of_words[list_of_words.index(each_list_item)] = each_list_item.capitalize()

##############################################################

def main():
    list_1 = ['apple', ['bear'], 'cat', 'doggy', ['elbow', 'fin', 'garage']]
    list_2 = [[[['apple']], 'bear', 'cat', 'doggy',['elbow','fin','garage','house','indigo']], 'jump']
    list_3 = []
    list_4 = ["doggy"]
    list_4 = [[[[[[["this"]]]]]]]
    capitalize_nested(list_1)
    capitalize_nested(list_2)
    capitalize_nested(list_3)
    capitalize_nested(list_4)
    print (list_1)
    print (list_2)
    print (list_3)
    print (list_4)

    pass
if __name__ == '__main__':
    main()
