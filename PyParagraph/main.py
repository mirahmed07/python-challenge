import csv
import os
import re
from pathlib import Path
# file_name_input = input("What is the file name? (include file extension as well) ")
# file_path = os.path.join("..","Resources", file_name_input)
para1_path = os.path.join("Resources", 'paragraph_1.txt')
para2_path = os.path.join("Resources", 'paragraph_2.txt')
#  A fucntion to analyze the file calculate all the counts 
def analyze_file(filepath):
    filename = Path(filepath).stem 
    file_to_output = os.path.join('analysis',str(filename)+'_analysis.txt')  
    paragraph = ""
    with open(filepath) as txt_data:
    # Store the contents as a string (with no new lines)
        paragraph = txt_data.read().replace("\n", " ")
    # Split the paragraph based on spaces to calculate word count
    word_split = paragraph.split(" ")
    word_count = len(word_split)
    # Create a list for holding all the letter counts
    letter_counts = []
    # Loop through the word array and calculate the length of each word
    for word in word_split:
        # Add each letter count into the letter_counts list
        letter_counts.append(len(word))
    # Calculate the avg letter count
    avg_letter_count = sum(letter_counts) / float(len(letter_counts))
    # Re-split the original paragraph based on punctuation (. ? !)
    sentence_split = re.split("(?<=[.!?]) +", paragraph)
    sentence_count = len(sentence_split)
    words_per_sentence = []
    # Loop through the sentence array and calculate the number of words in each
    for sentence in sentence_split:
        # Calculate the number of words in each sentence and add to the list
        words_per_sentence.append(len(sentence.split(" ")))
    # Calculate the avg word count (per sentence)
    avg_sentence_len = sum(words_per_sentence) / float(len(words_per_sentence))
    # Generate Paragraph Analysis Output
    output = (
        f"\n{filename.title().split('_')[0]} {filename.title().split('_')[1]} Analysis\n"
        f"---------------------\n"
        f"Approximate Word Count: {word_count}\n"
        f"Approximate Sentence Count: {sentence_count}\n"
        f"Average Letter Count: {avg_letter_count}\n"
        f"Average Sentence Length: {avg_sentence_len}\n")
    # Print all of the results (to terminal)
    print(output)
    # Save the results to analysis text file
    with open(file_to_output, "a") as txt_file:
        txt_file.write(output)
# Invoke the function for each file
# analyze_file(file_path)
analyze_file(para1_path)
analyze_file(para2_path)
# Below portion is enabling uer interaction with the function (not necessary)
# retry = 'y'
# while retry == 'y':
#     user_choice = input("Do you want to analyze another file? (y/n) ")
#     if user_choice == 'y':
#         file_name_input = input("What is the file name? (include file extension as well) ")
#         file_path = os.path.join("..","Resources", file_name_input)
#         analyze_file(file_path)
#     else:
#         retry = 'n'