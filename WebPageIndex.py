'''
    File name: WebPageIndex.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 3/14/2022
    Program: This code contains a class that contains the index representation
    of a web page and stores it in an AVL tree.
'''

import re
import AVL as AVL 

# Question 1.1 - Web Page Index
class WebPageIndex:
    # Initializes an instance of class from txt file
    def __init__(self, file):
        self.file = file

    # Method to read the file, and create a striped list of words
    def get_word_list(self):
        file_in = open(self.file,"r")
        words = file_in.read().lower()
        word_list = re.findall(r"[\w']+", words)
        return word_list
    
    # Method to count the number of occurences of a given word
    def get_count(self, s):
        word_list = self.get_word_list()
        count = 0
        for i in word_list:
            if i == s:
                count +=1
        return count

    # Method to put all of the words in the file into an AVL tree
    # Keys = words (no duplicates)
    # Value = List of occurences (all indexs key occurs)
    def put_in_tree(self):
        word_list = self.get_word_list()
        base_list = word_list
        # List to hold keys and values before putting into tree
        temp_list = []

        # AVL assumes no duplicates, so remove all duplicates:
        no_dupes = []
        for i in word_list:
            if i not in no_dupes:
                no_dupes.append(i)

        # Find positions of each word existing in the txt file
        for key in no_dupes:
            indexs = []    
            count = self.get_count(key)
            while len(indexs) < count:
                for i in word_list:
                    if i == key:
                        indexs.append(word_list.index(i))
                        # Need to remove word to not double count, while mainting original positons
                        word_list[word_list.index(i)]='space_filler'
            # Add keys and values to temp list as a tuple            
            temp_list.append((key,indexs))

        #print("\nWORD, INDEXS:", temp_list,'\n')

        k,v=temp_list[0]
        tree = AVL.AVLtree(k,v)
        for i in temp_list[1:]:
            k,v= i
            tree.put(k,v)
            
        word_list = base_list
        return tree

def main():
    file = WebPageIndex("doc5-queue.txt")
    print("FILE CONTENTS:", file.get_word_list())
    tree = file.put_in_tree()
    tree.printTree()

main()


        
