

from calendar import c


list = [6, 5, 7, 4, 9]

def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(0, len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubble_sort(list))




"""

# INTRODUCTION 

Bubble sort is a type of sorting algorithm which iterates through a list of N size, 
comparing the size of two values at a time. Based on which of the two values is
larger, the algorithm will reposition the smaller of the two values to the left and
the larger to the right. The algorithm will continue to iterate through the list until
the data is fully sorted.

To visually conceptualise how the bubble sort algorithm works, I've created a short animation
of the process. After the animation, I'll show you some pseudocode so you can write your own
bubble sorting algorithm.

-

# ANIMATION

As you can see, we are given a list that isn't sorted in any meaningful way.
What we want is for the list to be sorted from lowest to highest values.

In order to do that, let's use the bubble sort algorithm.

The first thing the algorithm would do would be to look at the first two numbers.
As we can see, 6 is greater than 5, so we swap their positions and continue.
Next, we see that 6 is less than 7, so we ignore swapping them.
7 is then compared to 4. Since 7 is greater, we swap their positions.
Lastly, 7 and 9 are compared. Since 9 is greater, we leave them be.

The algorithm will then continue this process until all of the values are properly sorted!


# PSEUDOCODE

comparing two values 

A bubble sort algorithm goes through a list of data a number of times,
comparing two items that are side by side to see which is out of order. 
It will keep going through the list of data until all the data is sorted 
into order. Each time the algorithm goes through the list it is called a ‘pass’.

"""