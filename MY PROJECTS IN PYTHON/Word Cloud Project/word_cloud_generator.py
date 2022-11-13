"""
A WORD CLOUDS GENERATOR

Date: 13 November 2022
Written by: Ebube Anozie

Purpose: Ecstatic per se.

It generates and displays words in different sizes
according to their number of occurences in a text
"""

import wordcloud
import matplotlib.pyplot as plt
import string







def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words to remove before display
    characters = string.punctuation + string.whitespace
    uninteresting_words = ['hers', 'when', 'my', 'she', 'was', 'each', 'just', 'is', 'he', \
                          'are', 'too', 'i', 'more', 'no', 'to', 'her', 'here', 'but', 'their', \
                          'with', 'a', 'what', 'very', 'we', 'if', 'its', 'can', 'all', 'or', 'him', \
                          'you', 'were', 'at', 'it', 'have', 'where', 'ours', 'as', 'that', 'his', 'they', \
                          'few', 'being', 'has', 'an', 'them', 'am', 'whom', 'of', 'will', 'by', 'how', 'nor', \
                          'the', 'do', 'from', 'some', 'your', 'our', 'any', 'yours', 'be', 'had', 'this', 'did', \
                          'does', 'me', 'been', 'which', 'such', 'both', 'who', 'and']


    word_list = []
    for line in file_contents:
        for word in line.strip().split():
            new_word = word.strip(characters).lower()
            if new_word not in uninteresting_words:
                word_list.append(new_word)

    # store the frequency of each word in a dictionary
    word_count = {}
    for word in word_list:
        word_count.setdefault(word, 0)
        word_count[word] = word_count[word] + 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    return cloud.to_array()
	


# Ask user for a text or display a default
def ask_user():
    not_number = True
    while not_number:
        try:
            _invalid = True
            while _invalid:
                response = int(input("Do you have a text to display?\nEnter 1 for yes or 0 to display a built-in text: "))
                if response == 1:
                    text = input("Enter or paste your text here: ")
                    if text != '':
                        line_list = text.strip().split()
                        return line_list
                    print("You have entered no text")
                    continue
                elif response == 0:
                    with open("wordCloudexample.txt", "r") as my_file:
                        line_list = my_file.readlines()
                    return line_list
                print("You can only choose 1 or 0.")
                continue
        except:
            print("Invalid response")
            continue
        
            


# Display your wordcloud image
line_list = ask_user()
myimage = calculate_frequencies(line_list)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
