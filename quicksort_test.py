# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:39:50 2021

@author: Jorgen
"""
import numpy as np
# from IPython import get_ipython
import time

# %%
# Python program for implementation of Quicksort Sort
  
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

# TODO: implement error correction
  
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    j = low             # set first index of j
    pivot = arr[high]   # pivot
    
    # save variables for "oops" reset functionality
    prevarr  = arr[:] # save a copy
    prevoops = True
    previ    = i
    
    # for j in range(low, high):
    while j <= high: # include a last buffer step
        
        # catch the buffer case
        if j == high:
            try: # gotta do this, otherwise trying to manually halt execution doesn't work
                # get_ipython().magic('clear')
                time.sleep(0.05)
                antwort  = input( 'Type "oops" if previous answer was in error: ' )
                
                print('your answer was: %s' % antwort)
                time.sleep(0.2)
                
                if antwort == 'exit': # this is really annoying, but the only way I can think to get it to respect keyboard interrupts
                    raise Exception("Please work") # and don't you DARE try to halt execution with ctrl+c while in the middle of an input sequence. that WILL break things.
            
                if antwort == 'oops': # assume this state cannot possibly be entered immediately after an oops
                    j        = j-1
                    arr[:]   = prevarr[:] # deal the elements rather than re-assigning the list, otherwise you get annoying bugs
                    i        = previ
                    prevoops = True
                    continue
                else:
                    j        = j+1
                    prevoops = True
                    continue
                
            except:
                raise Exception("Manual stop")
  
        # If current element is smaller than or
        # equal to pivot
        # if arr[j] <= pivot:
        logval = lgtr(arr[j],pivot)
        if logval == 'oops':
            if j > low and not prevoops:
                j        = j-1
                arr[:]   = prevarr[:]
                i        = previ
                prevoops = True
                print('undo previous!')
            else:
                print('sorry, cannot undo.')
            time.sleep(1)
            continue
        else:
            pass
        
        prevarr  = arr[:] # overwrite prevarr & other such things
        prevoops = False
        previ    = i
        if logval: # if arr[j] is stronger (i.e., SMALLER rank, e.g., #1 vs. #2) than the pivot
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            pass
            
        j = j+1
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    
    if low < high:
        
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
# %%
def lgtr(lel,rel):
    # query the human to determine > or <
    
    # randomize order it's presented in to avoid biasing the poor human
    flipflag = np.random.rand() < 0.5
    
    if flipflag:
        val1 = rel
        val2 = lel
    else:
        val1 = lel
        val2 = rel
    
    isdone = False
    while not isdone:
        try: # gotta do this, otherwise trying to manually halt execution doesn't work
            # get_ipython().magic('clear')
            time.sleep(0.05)
            antwort  = input( 'Which Pokemon is stronger?\n%s(1) | %s(2): ' \
                             % (val1,val2) )
            
            print('your answer was: %s' % antwort)
            time.sleep(0.2)
            print('Type "oops" if previous answer was in error!')
            
            if antwort == 'exit': # this is really annoying, but the only way I can think to get it to respect keyboard interrupts
                raise Exception("Please work") # and don't you DARE try to halt execution with ctrl+c while in the middle of an input sequence. that WILL break things.
            
            if antwort == 'oops':
                return 'oops'
            
            # just hit enter if an error occurs, for example the display has cleared the current question
            if antwort != '1' and antwort != '2':
                isdone = False
                continue
            else:
                isdone = True
                
            aw = int(antwort)
            
            if (aw == 1 and not flipflag) or (aw==2 and flipflag): # i.e., if l is greater than r
                return True
            else:
                return False
                
        except:
            raise Exception("Manual stop")
    
# %% test
#lgtrval = lgtr('Snorlax','Zapdos')
#print(lgtrval)

#pokeslist = ['Cloyster','Snorlax','Raikou','Gengar','Zapdos']
#quickSort(pokeslist,0,len(pokeslist)-1)
            
# %%
## Driver code to test above
#arr = [10, 7, 8, 9, 1, 5]
#n = len(arr)
#quickSort(arr, 0, n-1)
#print("Sorted array is:")
#for i in range(n):
#    print("%d" % arr[i]),
#  
## This code is contributed by Mohit Kumra
##This code in improved by https://github.com/anushkrishnav