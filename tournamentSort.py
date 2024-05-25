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

# Tournament sort function
def tournamentSort(array):
    def buildTournament(array):
        tournament = []
        while len(array) > 1:
            next_round = []
            for i in range(0, len(array), 2):
                if i + 1 < len(array):
                    if array[i] < array[i + 1]:
                        next_round.append(array[i])
                    else:
                        next_round.append(array[i + 1])
                else:
                    next_round.append(array[i])
            tournament.append(next_round)
            array = next_round
        return tournament

    def extractMin(tournament):
        min_val = tournament[-1][0]
        for level in reversed(tournament):
            idx = level.index(min_val)
            if idx % 2 == 0 and idx + 1 < len(level):
                level[idx // 2] = level[idx + 1]
            else:
                level.pop(idx // 2)
        return min_val

    sorted_array = []
    tournament = buildTournament(array)
    while tournament[-1]:
        sorted_array.append(extractMin(tournament))
    return sorted_array

# Define file paths
name_file_path = 'names.txt'
data_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\pidata.txt'
output_file_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment\Tournament_sort01.txt'

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

    # Call the tournament sort function
    sorted_data = tournamentSort(data)

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

    # Print the sorted array and time taken to a text file
    with open(output_file_path, 'w') as output_file:
        output_file.write("David Abiodun\n")
        output_file.write("31/05/1970\n")
        output_file.write("da24359\n")
        output_file.write(sorted_output)
        output_file.write(time_output)

    print("Sorting completed. Check Tournament_sort01.txt for the result.")

except FileNotFoundError:
    print(f"The file '{data_file_path}' does not exist. Please create the file first.")
except ValueError:
    print(f"The file '{data_file_path}' contains non-integer values. Please ensure all values are integers.")
except Exception as e:
    print(f"An error occurred: {e}")
