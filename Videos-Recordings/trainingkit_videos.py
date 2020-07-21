'''
Training Kit Videos 

'''
# runtime complexity 

def print_100th_element(array):
    print(array[99])

def loop_50_times(array):
    for i in range(50):
        print(array[i])

#logarithimic Time definiton 
'''
the algorithm in question increase the number of operations it performs as a logarithmic function of the input size n. 

the function log n grows very slowly, so as n gets larger, the number of operations the algorithm needs to perform does not increase by very much. 

logarithmic time examples: dictionary, books on shelf alphabetized  
        Binary Search 
code example: (psuedo code)
'''
def binary_search(sorted_arr, target):
    low = 0, high = len(sorted_arr) -1 
    midpoint == (high - low) // 2
    if target == sorted_arr[midpoint]:
        return midpoint
    elif target < sorted_arr[midpoint]:
        return binary_search(sorted_arr[:midpoint])
    else:
        return binary_search(sorted_arr[midpoint:])


# Linear Time Definiton 
'''
increases the number of operations it performs as a linear function of the input size n. 
The number of additional operations the algorithm needs to perform grows in direct proportion to the increase in input size n. 

Examples: counting(have to look at each item counting)
, washing 11 dogs one at a time 
code example:
'''
def search(array, target):
    for el in array:
        if target == el:
            return True
        return False 

def print_all_elements_twice(array):
    for el in array:
        print(el)
    for el in array:
        print(el)

def print_up_to_n(n):
    for i in range(n):
        print(i)

#Log Liner Time Definiton
'''
increases the number of operations it performs as a log-linear function of the input size n. 

Intuitively you can think of this runtime classification as "looking over every single element and doing some additional work on each one".
examples: sorting(items in numerical order) quicksort mergesort hepsort timsort
'''

# quadratic Time Definition 
'''
increases the number of operations it performs as a quadratic function of the input size n. 
n = 100 -> n^2 = 100
n = 100 -> n^2 = 1,000,000

examples: numerate possible options within a string of choices, Bubble Sorting, 
code examples:
'''
def print_all_pairs(array):
    for first_item in array:
        for second_item in arra:
            print(first_item, second_item)

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


# exponential time definition
'''
increases the number of operations it performs as an exponential function of the input size n. 

for exponential problems, the number of nested loops increases as a function of the input size n. 
examples: cracking an unknown password, decision problem form of kanpsack problem, minesweeper, prime factorization of large integers, longest common subsequence of strings problem

code examples:
'''
'''
O(5n) ~ O(n)

O(1/2n) ~ O(n)

O(n^3 + 1/2n + 101) ~ O(n^3)
'''

#linked lists 
'''
in order to reallly understand how linked lists work, we'll need to build up a conceptual mental model in our heads and then translate that model into code.

stored lists of values, like an array but each item is a single node. 

(head)     (tail)
12 -> 39-> 5 -> N (none or null) (last of the linked list)
    (value)

[12, 39, 5, , , , ] (array - continues block of memory) 

code example: 
'''
class Node:
    self.value = value
    self.next = next_node

class LinkedList:
    self.head = head_node
    self.tail = tail_node

'''
inserting into a linked list

list.insert(15)
(head)     (tail) 15 -> N (new node)
12 -> 39-> 5 -> N (none or null) (last of the linked list)
    (value)

    then move five pointer. then call next to make new linked list 
    12 -> 39 -> 5 -> 15-> N 

How would you insert an element into an empty linked list? What about a linked list with only one element?

How would you iterate along a linked list to reach an element that isn't the head or tail of the list?
How would you delete an element from a linked list?
    We can keep adding elements to linked lists as much as we want, unlike arrays with a static amount of allocated memory. 
'''
#queue Data Structure 
'''
in order to reallly understand how queues work, we'll need to build up a conceptual mental model in our heads and then translate that model into code.

example: line at the store 
(FIFO) - first in first out

code example:
'''
class Queue:
    self.size = 0
    self.storage = storage_data_structure
'''
pro: easier to insert inot and delete from middle of a linked list compared to an array  
pro: we can keep adding elements to linked lists as much as we want, unlike arrays with a static amount of allocated memory. 
cons: linked lists are not cache friendly since caches are typically optimized from contiguous memory access.
'''

'''
What's the opposite of fifo ordering? what data structures exhibit this ordering?
What data strucutres would yo use to implement a queue?
When is FIFO ordering useful? When is not?

Pros: simple, intutive to use and implement. Can be used to serialize data coming in from multiple sources. 
Cons: Are not general purpose at all in and of themselves. 
'''

