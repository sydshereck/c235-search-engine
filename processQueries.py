'''
    File name: processQueries.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 3/14/2022
    Program: This code contains a small search engine.
'''
import os
from WebpagePriorityQueue import *

def readFiles(path):
    webpages = []
    folder = os.listdir(path)
    
    # seperate txt files from others in folder
    for file in folder:
        if file.endswith('txt'):
            webpages.append(file)
    webpages.remove('queries (1).txt')

    # create tree with indexs out of every txt file
    web_page_indexs = []
    for i in webpages:
        file_wpi = WebPageIndex(i)
        file_wpi.put_in_tree()
        web_page_indexs.append(file_wpi)

    return web_page_indexs
     
def main():
    print('\n\nSEARCH ENGINE\n\n')
    webpages = readFiles("/Users/tracysherecktracyshereck/Desktop/school/2/cisc 235/A3")
    print("WEBPAGES", webpages)

    # read the queries file line by line
    f = open('queries (1).txt',"r")
    queries = f.readlines()

    # remove \n character from queries
    search_queries = []
    for i in queries:
        search_queries.append(i[:len(i)- 1])

    print(search_queries)

    print("\nQUERY: ", search_queries[0])

    x = WebpagePriorityQueue('tree', webpages)
    priorities = x.find_priorities()
    sorted_priorities = sorted(priorities, key=lambda tup: tup[1], reverse = True)
    search_result = []

    for i in sorted_priorities:
        wpi, pri = i
        if pri != 0:
            search_result.append(wpi.file)

    if len(search_result)>3:
        print("RESULTS (priority order):  ", search_result[0:3])
    else:
        print("RESULTS (priority order):  ", search_result)

    
    # for each query find 3 files with most occurences
    for i in search_queries[1:]:
        print("\nQUERY: ", i)
        x.reheap(i)
        priorities = x.find_priorities()
        sorted_priorities = sorted(priorities, key=lambda tup: tup[1], reverse = True)
        search_result = []

        for i in sorted_priorities:
            wpi, pri = i
            if pri != 0:
                search_result.append(wpi.file)

        if len(search_result)>3:
            print("RESULTS (priority order):  ", search_result[0:3])
        else:
            print("RESULTS (priority order):  ", search_result)

main()
