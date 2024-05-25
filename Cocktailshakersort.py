import time
import random

# Function to add a name to the start of a file
def add_name_to_file(file_path, name):
    try:
        # Open the file in read mode and read its contents
        with open(file_path, 'r') as file:
            contents = file.read()

        # Prepend the name to the contents
        new_contents = name + '\n' + contents

        # Open the file in write mode and write the updated contents back to the file
        with open(file_path, 'w') as file:
            file.write(new_contents)

        print("Name added to the start of the file successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist. Please create the file first.")

# Cocktail Shaker Sort function
def cocktailShakerSort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start += 1

# Define file paths
data_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\Cocktailshakersort01.txt'

try:
    # Read data from the file
    with open(data_file_path, 'r') as file:
        # Read the entire file content and split by whitespace to get individual numbers
        data = file.read().split()

    # Convert string data to integers
    data = [int(num) for num in data]

    # Measure the time taken to sort the data
    start_time = time.time()

    # Call the cocktail shaker sort function
    cocktailShakerSort(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Generate the strings DavidAbiodun01 to DavidAbiodun10
    names_to_add = [f'DavidAbiodun{i:02d}' for i in range(1, 11)]

    # Insert these names at random positions in the sorted list
    for name in names_to_add:
        position = random.randint(0, len(data))
        data.insert(position, name)

    sorted_output = 'Sorted Array in Ascending Order:\n' + str(data) + '\n'
    time_output = f'Time taken to sort the array: {elapsed_time} seconds\n'

    # Print the sorted array and time taken to a text file
    with open(output_file_path, 'w') as output_file:
        # Insert specified lines at the beginning of the file
        output_file.write("David Abiodun\n")
        output_file.write("31/05/1970\n")
        output_file.write("da24359\n")
        output_file.write(sorted_output)
        output_file.write(time_output)

    print("Sorting completed. Check Cocktailshakersort01.txt for the result.")

except FileNotFoundError:
    print(f"The file '{data_file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{data_file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")
