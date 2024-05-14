Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 1
2
>>> print('Hello, World!')
Hello, World!
>>> hello_"hello world"
SyntaxError: invalid syntax
>>> hello="hello world"
>>> print hello
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(hello)
hello world
>>> 2++2
4
>>> -2+2
0
>>> # Define the minutes and seconds
... minutes = 42
... additional_seconds = 42
... 
... # Convert minutes to seconds
... seconds_in_minutes = minutes * 60
... 
... # Calculate total seconds
... total_seconds = seconds_in_minutes + additional_seconds
... 
... # Print the result
... print("Total seconds in 42 minutes 42 seconds:", total_seconds)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> SyntaxError: multiple statements found while compiling a single statementminutes = 42
SyntaxError: invalid syntax
>>> minutes = 42
>>> additional_seconds = 42
>>> seconds_in_minutes = minutes * 60
>>> total_seconds = seconds_in_minutes + additional_seconds
>>> print("Total seconds in 42 minutes 42 seconds:", total_seconds)
Total seconds in 42 minutes 42 seconds: 2562
>>> kilometers = 10
>>> km_to_miles = 1 / 1.61
>>> miles = kilometers * km_to_miles
>>> print("There are", miles, "miles in", kilometers, "kilometers.")
There are 6.211180124223602 miles in 10 kilometers.
>>> kilometers = 10
>>> total_minutes = 42
>>> total_seconds = 42
>>> total_time_seconds = total_minutes * 60 + total_seconds
>>> miles = kilometers / 1.61
>>> average_pace_seconds_per_mile = total_time_seconds / miles
>>> average_pace_minutes = int(average_pace_seconds_per_mile // 60)
>>> average_pace_seconds = int(average_pace_seconds_per_mile % 60)
>>> average_speed_mph = (miles / total_time_seconds) * 3600
>>> print(f"Average pace: {average_pace_minutes} minutes {average_pace_seconds} seconds per mile")
Average pace: 6 minutes 52 seconds per mile
>>> print(f"Average speed: {average_speed_mph:.2f} miles per hour")
Average speed: 8.73 miles per hour
>>> 'Spam * 3'
'Spam * 3'
