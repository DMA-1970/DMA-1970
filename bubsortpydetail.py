import time

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        # Recursively sort the halves
        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Define the file path
file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\sorted_output.txt'

try:
    # Read data from the file
    with open(file_path, 'r') as file:
        # Read the entire file content and split by whitespace to get individual numbers
        data = file.read().split()

    # Convert string data to integers
    data = [int(num) for num in data]

    # Measure the time taken to sort the data
    start_time = time.time()

    # Call the merge sort function
    mergeSort(data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    sorted_output = 'Sorted Array in Ascending Order:\n' + str(data) + '\n'
    time_output = f'Time taken to sort the array: {elapsed_time} seconds\n'

    # Print the sorted array and time taken to a text file
    with open(output_path, 'w') as output_file:
        output_file.write(sorted_output)
        output_file.write(time_output)

    print("Sorting completed. Check sorted_output.txt for the result.")

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")
