import random
import time

def selection_sort(list):
    comps = 0
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
            comps += 1
        list[i], list[min] = list[min], list[i]
    return comps


def insertion_sort(list):
    comps = 0
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if value < list[j]:
                list[j + 1] = list[j]
                list[j] = value
                j = j - 1
            else:
                break
    return comps
   

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 100000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

