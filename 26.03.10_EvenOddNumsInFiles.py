
"""
import threading



# FUNCTIONS

def load_numbers_from_file(path):
    with open(path, 'r') as file:
        numbers = file.read().split() 
        return numbers


def create_even_nums_file(path, numbers):
    with open(path, 'w') as file:
        for num in numbers:
            if int(num) % 2 == 0:
                file.write(num + "\n")


def create_even_nums_file_2(path, numbers):
    with open(path, 'w') as file:
        even_numbers = []
        for num in numbers:
            if int(num) % 2 == 0:
                even_numbers.append(num)
        even_numbers_string = ", ".join(even_numbers)
        file.write(even_numbers_string)


def create_odd_nums_file(path, numbers):
    with open(path, 'w') as file:
        for num in numbers:
            if int(num) % 2 != 0:
                file.write(num + "\n")




# MAIN

# read numbers from file into list
numbers = load_numbers_from_file("numbers.txt")
print(numbers)


# start two threads to process even and odd numbers
thread_even = threading.Thread(targer=create_even_nums_file, args=numbers)
thread_odd = threading.Thread(target=create_odd_nums_file, args=numbers)

thread_even.start()
thread_odd.start()
"""



# from Patrik
import threading
import time
 

file_lock = threading.Lock()
 
def load_numbers(path):
    cisla = []
    with open(path, 'r') as file:
        for line in file:
            cisla_string = line.strip().split(sep=",")
            for cislo in cisla_string:
                cisla.append(int(cislo))
    return cisla
 

def write_numbers(path, numbers, is_even):
    with open(path, 'a') as file:
        cisla = []
        time.sleep(5)

        for number in numbers:
            if number % 2 == 0 and is_even:
                cisla.append(str(number))
            elif number % 2 != 0 and not is_even:
                cisla.append(str(number))
        parne_cisla_string = ", ".join(cisla) + ", "

        file_lock.acquire()
        file.write(parne_cisla_string)
        file_lock.release()
 

 
cisla_zo_suboru = load_numbers("cisla.txt")
 
#write_numbers("cisla_nove.txt", cisla_zo_suboru, False)
 
start_time = time.time()
parne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru,True,))
neparne = threading.Thread(target=write_numbers, args=("cisla_nove.txt", cisla_zo_suboru,False))
 
parne.start()
neparne.start()
 
parne.join()
neparne.join()
 
print(f"Dokoncene za {time.time() - start_time}")