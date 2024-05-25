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

# Quick sort function
def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quickSort(left) + middle + quickSort(right)

# Define file paths
name_file_path = 'names.txt'
data_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\Quicksort01.txt'

# Add name to file
add_name_to_file(name_file_path, "John Doe")

try:
    # Read data from the file
    with open(data_file_path, 'r') as file:
        # Read the entire file content and split by whitespace to get individual numbers
        data = file.read().split()

    # Convert string data to integers
    data = [int(num) for num in data]

    # Measure the time taken to sort the data
    start_time = time.time()

    # Call the quick sort function
    sorted_data = quickSort(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Generate the strings DavidAbiodun01 to DavidAbiodun10
    names_to_add = [f'DavidAbiodun{i:02d}' for i in range(1, 11)]

    # Insert these names at random positions in the sorted list
    for name in names_to_add:
        position = random.randint(0, len(sorted_data))
        sorted_data.insert(position, name)

    # Prepare the output content
    sorted_output = 'David Abiodun\n31/05/1970\nda24359\n' + 'Sorted Array in Ascending Order:\n' + str(sorted_data) + '\n'
    time_output = f'Time taken to sort the array: {elapsed_time} seconds\n'

    # Print the sorted array and time taken to a text file
    with open(output_file_path, 'w') as output_file:
        output_file.write(sorted_output)
        output_file.write(time_output)

    print("Sorting completed. Check Quicksort01.txt for the result.")

except FileNotFoundError:
    print(f"The file '{data_file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{data_file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")
