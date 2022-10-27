import random
import os
import math
from unittest import result

def generate_lists(list_limit=20):
    random_lists = []

    while len(random_lists) < list_limit:
        random_int = random.randint(1, (list_limit*2))
        if(random_int in random_lists):
            continue
        
        random_lists.append(random_int)

    return random_lists

def binary_search(list, search, start_idx, end_idx):
    if start_idx > end_idx:
        return False

    list_len = len(list)
    middle_idx = math.ceil((start_idx + end_idx)/2)

    if search == list[middle_idx]:
        return middle_idx

    if search > list[middle_idx]:
        return binary_search(list, search, middle_idx+1, list_len)
    else:
        return binary_search(list, search, start_idx, middle_idx-1)

def main():
    
    os.system('cls')
    lists = generate_lists()
    lists.sort()

    print("List: {} \n".format(lists))

    search_value = int(input("Search Value: "))

    lists_len = len(lists)
    result = binary_search(lists, search_value, 0, lists_len)

    if result:
        print("Element {} is present at index {}".format(search_value, result))
    else:
        print("Element {} is not in the list".format(search_value))

if __name__ == '__main__':
	main()