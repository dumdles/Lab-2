print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(numbers):
    avg_temp = sum(numbers) / len(numbers)
    return avg_temp

def get_user_input():
    user_input = input('Enter your numbers: ')
    split_text = user_input.split(',')
    numbers = [float(num) for num in split_text]  # convert list of strings to list of floats
    print(numbers)  # print the list of floats
    return numbers

def find_min_max(number):
    min_num = min(number)
    max_num = max(number)
    return min_num, max_num

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature(numbers):
    sorted_temps = sorted(numbers)   # The sorted() function is used to sort the numbers in ascending order.
    n = len(sorted_temps)   # The length of the sorted list is calculated 2and stored in n.
    mid = n // 2    #The middle index of the list is calculated using integer division (//) and stored in mid.
    if n % 2 == 0:
        median = (sorted_temps[mid - 1] + sorted_temps[mid]) / 2
    else:
        median = sorted_temps[mid]
    return median

#numbers = get_user_input()
#avg_temp = calc_average(numbers)
#min_max = find_min_max(numbers)
#median = calc_median_temperature(numbers)

#print('Average: ', avg_temp)
#print('Median: ', median)
#print('Minimum: ', min_max[0])
#print('Maximum: ', min_max[1])
