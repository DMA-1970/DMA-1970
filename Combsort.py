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

# Comb sort function
def combSort(array):
    gap = len(array)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(array):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False
            i += 1

# Define file paths
name_file_path = 'names.txt'
data_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\Combsort01.txt'

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

    # Call the comb sort function
    combSort(data)

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

    # Prepare the final output content
    final_output = f"David Abiodun\n31/05/1970\nda24359\n{sorted_output}{time_output}"

    # Print the sorted array and time taken to a text file
    with open(output_file_path, 'w') as output_file:
        output_file.write(final_output)

    print("Sorting completed. Check Combsort01.txt for the result.")

except FileNotFoundError:
    print(f"The file '{data_file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{data_file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")
