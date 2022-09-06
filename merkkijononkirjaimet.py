"""
  Vowels and Consonants

: Write a program that asks from a user an English word and tells how many vowels 
  and consonants the word contains.
"""

def main():
    """
    :userinput - taking userinput.    
    :userinput_vlist- split a word into a list of letters    
    : vowel- counting and adding all the vowels from user input
    
    : consonent: calcluating the lenght of the list and substracting the vowel to find out the number of consosnent letters.
    """
    
    userinput= input("Enter a word: ")

    userinput_vlist= list(userinput)

    vowel = userinput_vlist.count('a')+userinput_vlist.count('e')+userinput_vlist.count('i')+userinput_vlist.count('o')+userinput_vlist.count('u')+userinput_vlist.count('y')
    
    consonent =len(userinput_vlist) - vowel

    print("The word \"{}\" contains {} vowels and {} consonants.".format(userinput, vowel,consonent))
    
    
if __name__ == "__main__":
    main()
