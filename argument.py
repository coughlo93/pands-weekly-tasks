# The program should take the filename from an argument on the command line. 
# The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
# Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

filename = 'C:\\Users\\owenc\\Desktop\\pands\\pands-weekly-tasks\\moby-dick.txt' 
try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        e_count = text.count('e')
        print("The letter 'e' appears", e_count, "times in the file.")
except ValueError as e:
    print(e)
except PermissionError:
    print("Error: Permission denied to access the file.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

