import time
import random

# Smoothsort implementation in Python
def smoothSort(array):
    def sift(i, heap):
        t = heap[i]
        while i > 1:
            r = i // 2
            if r == 1 or heap[r // 2] < heap[r]:
                j = r
            else:
                j = r // 2
            if t >= heap[j]:
                break
            heap[i] = heap[j]
            i = j
        heap[i] = t

    def trinkle(i, heap, p):
        t = heap[i]
        while p > 0:
            while (p & 1) == 0:
                p >>= 1
                i = i // 2
            j = i - p
            if j <= 0 or heap[j] <= t:
                break
            p = (p - 1) // 2
            i = j
        heap[i] = t
        sift(i, heap)

    def semitrinkle(i, heap, p):
        trinkle(i, heap, p)
        if heap[i] < heap[i // 2]:
            t = heap[i]
            heap[i] = heap[i // 2]
            heap[i // 2] = t

    n = len(array)
    p = 1
    for i in range(1, n + 1):
        if (p & 1) == 0:
            sift(i, array)
        else:
            if (p & 2) == 0:
                sift(i - 1, array)
                sift(i, array)
            else:
                trinkle(i, array, p)
        p = (p + 1) // 2
    while p > 0:
        i -= p
        p = (p - 1) // 2
        trinkle(i, array, p)
    return array

# Define file paths
data_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\Smoothsort01.txt'

try:
    # Read data from the file
    with open(data_file_path, 'r') as file:
        # Read the entire file content and split by whitespace to get individual numbers
        data = file.read().split()

    # Convert string data to integers
    data = [int(num) for num in data]

    # Measure the time taken to sort the data
    start_time = time.time()

    # Call the smooth sort function
    sorted_data = smoothSort(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Generate the strings DavidAbiodun01 to DavidAbiodun10
    names_to_add = [f'DavidAbiodun{i:02d}' for i in range(1, 11)]

    # Insert these names at random positions in the sorted list
    for name in names_to_add:
        position = random.randint(0, len(sorted_data))
        sorted_data.insert(position, name)

    sorted_output = 'Sorted Array in Ascending Order:\n' + str(sorted_data) + '\n'
    time_output = f'Time taken to sort the array: {elapsed_time} seconds\n'

    # Print the sorted array and time taken to a text file with the specific lines
    with open(output_file_path, 'w') as output_file:
        output_file.write("David Abiodun\n")
        output_file.write("31/05/1970\n")
        output_file.write("da24359\n")
        output_file.write(sorted_output)
        output_file.write(time_output)

    print("Sorting completed. Check Smoothsort01.txt for the result.")

except FileNotFoundError:
    print(f"The file '{data_file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{data_file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")

