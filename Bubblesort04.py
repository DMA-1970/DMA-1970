import time
import random

# Bubble sort function
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Define file paths
data_file_path = r'D:\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\BubbleSort01.txt'

try:
    # Read data from the file
    with open(data_file_path, 'r') as file:
        # Read the entire file content and split by whitespace to get individual numbers
        data = file.read().split()

    # Convert string data to integers
    data = [int(num) for num in data]

    # Measure the time taken to sort the data
    start_time = time.time()

    # Call the bubble sort function
    bubbleSort(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Generate the strings DavidAbiodun01 to DavidAbiodun10
    names_to_add = [f'DavidAbiodun{i:02d}' for i in range(1, 11)]

    # Insert these names at random positions in the sorted list
    for name in names_to_add:
        position = random.randint(0, len(data))
        data.insert(position, name)

    # Prepare the output with the required lines at the start
    output_content = (
        "David Abiodun\n"
        "31/05/1970\n"
        "da24359\n"
        'Sorted Array in Ascending Order:\n' + str(data) + '\n'
        f'Time taken to sort the array: {elapsed_time} seconds\n'
    )

    # Write the output content to the file
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_content)

    print("Sorting completed. Check BubbleSort01.txt for the result.")

except FileNotFoundError:
    print(f"The file '{data_file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{data_file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")

