# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
##############################################################
#Body
def is_sorted(word1, word2):
    converted_list_word_1 = list(word1)
    converted_list_word_2 = list(word2)
    sorted_list_word_1 = sorted(converted_list_word_1, reverse = False)
    sorted_list_word_2 = sorted(converted_list_word_2, reverse = False)
    if(sorted_list_word_1 == sorted_list_word_2):
        return True
    else:
        return False

##############################################################

def main():
    lst1 = "rat"
    lst2 = "tar"
    print(is_sorted(lst1,lst2))
    pass
if __name__ == '__main__':
    main()
