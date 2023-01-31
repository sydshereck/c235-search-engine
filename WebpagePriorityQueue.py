'''
    File name: WebpagePriorityQueue.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 3/14/2022
    Program: This code contains a heap-based implementation of a PriorityQueue
    used to find the most relevant web page given a specific query.
'''
from WebPageIndex import *

# Question 1.2 - Webpage Priority Queue
class WebpagePriorityQueue:
    def __init__(self, query, web_page_indexs):
        self.query = query
        self.web_page_indexs = web_page_indexs
        self.priority_queue = []

    # Creates a new heap with a new query
    def reheap(self, new_query):
        self.query = new_query
        self.priority_queue = []
        self.find_priorities()
        self.build_max_heap()
        
    # Creates array of tuples contianing (webPageIndexs, priorities) 
    def find_priorities(self):
        for web_page in self.web_page_indexs:
            appearances = 0
            query_words = self.query.split(' ')
            for word in query_words:
                appearances += web_page.get_count(word)
            self.priority_queue.append((web_page, appearances))
            
        return self.priority_queue

    # Return the WebpageIndex with the highest priority in the WebpagePriorityQueue
    # Since max heap, the first element = highest priority
    def peek(self):
        x,y = self.priority_queue[0]
        print(x.file)

    def poll(self):
        return self.priority_queue.pop(0)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def is_leaf(self, i):
        if i >= (len(self.priority_queue)//2) and i <= len(self.priority_queue):
            return True
        else:
            return False
        
    def max_heapify(self, i):
        # if the node is a non-leaf
        if not self.is_leaf(i):
            left_index = self.left(i)
            right_index = self.right(i)
            
            # break up the tuples (data, priority)
            webPage_curr, priority_curr = self.priority_queue[i]
            webPage_left, priority_left = self.priority_queue[left_index]
            webPage_right, priority_right = self.priority_queue[right_index]

            # compare priorities, if root of subtree is lowesr then either left or right swap
            if (priority_curr < priority_left or priority_curr < priority_right):
                # if left is higher make left root
                if (priority_left > priority_right):
                    self.priority_queue[i], self.priority_queue[left_index] = self.priority_queue[left_index], self.priority_queue[i]
                    self.max_heapify(left_index)
                # if right is higher make right root
                else:
                    self.priority_queue[i], self.priority_queue[right_index] = self.priority_queue[right_index], self.priority_queue[i]
                    self.max_heapify(right_index)
            return self.priority_queue
        
            
    def build_max_heap(self):        
        # Get largest non leaf node
        n = int((len(self.priority_queue)//2)-1)
        for i in range (n, -1, -1):
            self.max_heapify(i)
        print ("HEAP:",  self.priority_queue)
    

def main():
    wpi = WebPageIndex("doc1-arraylist.txt")
    wpi.put_in_tree()

    wpi2 = WebPageIndex("doc2-graph.txt")
    wpi2.put_in_tree()

    wpi3 = WebPageIndex("doc3-binarysearchtree.txt")
    wpi3.put_in_tree()

    wpi4 = WebPageIndex("doc4-stack.txt")
    wpi4.put_in_tree()

    wpi5 = WebPageIndex("doc5-queue.txt")
    wpi5.put_in_tree()

    wpi6 = WebPageIndex("doc6-AVLtree.txt")
    wpi6.put_in_tree()

    wpi7 = WebPageIndex("doc7-redblacktree.txt")
    wpi7.put_in_tree()

    wpi8 = WebPageIndex("doc8-heap.txt")
    wpi8.put_in_tree()

    wpi9 = WebPageIndex("doc9-hashtable.txt")
    wpi9.put_in_tree()


    web_page_indexs = [wpi, wpi2, wpi3, wpi4, wpi5, wpi6, wpi7, wpi8, wpi9]
    

    x = WebpagePriorityQueue("tree".lower(), web_page_indexs)
    x.find_priorities()
    x.build_max_heap()
    x.peek()


main()
