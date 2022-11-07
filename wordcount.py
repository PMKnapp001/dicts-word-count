"""Count words in file."""

# count_words_in_file
# open file
# read lines in file

# word.split ("")

#open file, set it to file name variable , so we can refer to it
#declare empty dict
#compare....dict to filename
#for loop, for line in file
#create new list with words from lines seperated by space 
#print to screen for debugging purposes

#each line from list...if its a duplicate add to it, count! initialize it first <- dict.get(key) which returns value if its there, if not set it to return 0
#return the actual words and the count <----dict.items() 

def word_count(input_file):
    """return word and word count as a dictionary of key:val pairs"""
    file = open(input_file)
    word_count = {} #final dict we'll return
    #counter = 0
    for line in file:
        line = line.rstrip()
        seperated_words_list = line.split(" ")
        #^each line is a sentence
        for word in seperated_words_list:
            word_count[word] = word_count.get(word, 0)+1
            #first get word(aka the key) from dict(which is word_count), .get() checks dictionary for specific key(aka the word).
            #returns literal value associated with key if already in dictionary, creates key if not with default value(0) as value
    for word, count in word_count.items():
        print(f"{word} {count}")