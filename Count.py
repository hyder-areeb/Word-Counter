#count.py
#A simple program that counts the number of words in a given sentence

def main():

    #Ask the user for an input sentence
    space =(input("Type a sentence with proper punctuation. "))
    #count the number of spaces in the sentence 
    spc = space.count(' ')
    #add 1 to the number of spaces and print 
    print ("There are",spc + 1, "words in your sentence")


main()
