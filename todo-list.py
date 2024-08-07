import os, sys

FILENAME = "todo_list.txt"

def todo_Options():
    appRead = input("Would you like to append (add to), read the file, mark as complete or delete a task? (A, R, M, D or (E) to exit): ")
    # Will exit the program if user enters (e)
    if appRead.upper() == "E":
        sys.exit()
    # Will open and read file if appRead is == "R"
    if appRead.upper() == "R":
        f = open(FILENAME, "r")
        # Prints all of the file contents to the user so they can read
        print(f.read())
        f.close()
        # Recursive function to re-loop until the user exits
        todo_Options()
    # Section for appending to the file
    elif appRead.upper() == "A":
        f = open(FILENAME, "a")
        todoContent = input("Enter what task you would like to add to your TODO List: ")
        # Write the content that the user wants to add but also add \n to the end to create a new line for new appendations
        f.write(todoContent + "\n")
        print("Content has been added to file.")
        f.close()
        # Recursive function number 2
        todo_Options()
    # Section for marking any tasks as complete
    elif appRead.upper() == "M":
        # Linecounter is here to keep track of if a task is in the file or not
        lineCounter = 0
        f = open(FILENAME, "r")
        # Store the data of f into the lines variable
        lines = f.readlines()
        # Print all of the lines of the file to the CLI so the user can see what they need to enter in taskToMark
        for line in lines:
            print(line.strip())
        taskToMark = input("Enter the task you want to mark as complete: ")
        # Loop through all of the lines in the file i = line number and line = the contents of that line, we enumerate through lines, lines is a list
        for (i, line) in enumerate(lines, 1):
            if taskToMark.lower() in line.strip().lower():
                taskComplete = i
                # If the task has (TASK COMPLETED) anywhere in the line then it won't do anything
                if ("(TASK COMPLETED)".lower() in lines[taskComplete - 1].strip().lower()):
                    print("Task has been completed already...")
                    # Recursive function number 3
                    todo_Options()
                # If the user tries to edit the title then again it won't work and just recall the function
                if ("TODO List 'Application'".lower() in lines[taskComplete - 1].strip().lower()):
                    print("Cannot complete a title of a file 😂")
                    # Recursive function number 4
                    todo_Options()
                # Modifies the content at the index where the task is in the lines list and then sets that equal to itself + (TASK COMPLETED)
                lines[taskComplete - 1] = lines[taskComplete - 1].strip() + " (TASK COMPLETED)\n" # Modify the text in line[index]
                f = open(FILENAME, "w")
                # Write the new modified line to the file
                f.writelines(lines)
                print("Task has been updated to complete status...")
                f.close()
                # Recursive function number 5
                todo_Options()
            else:
                lineCounter += 1
                # If lineCounter is equal to the length of lines then the task does not exist so recall function
                if lineCounter == len(lines):
                    print("Task does not exist...")
                    f.close()
                    # Recursive function number 6
                    todo_Options()
    # Section for deleting any tasks available in the file
    elif appRead.upper() == "D":
        f = open(FILENAME, "r")
        lines = f.readlines()
        # Linecounter is here to keep track of if a task is in the file or not
        lineCounter = 0
        # Print all of the lines of the file to the CLI so the user can see what they need to enter in taskToDelete
        for line in lines:
            print(line.strip())
        taskToDelete = input("Enter the name of the task you would like to delete: ")
        # If there is a (TASK COMPLETED) in the user's input then we remove that and replace it with empty space
        if ("(TASK COMPLETED)" in taskToDelete):
            taskToDelete.replace("(TASK COMPLETED)", "")
        # Loop through all of the lines in the file i = line number and line = the contents of that line, we enumerate through lines, lines is a list
        for (i, line) in enumerate(lines, 1):
            if "(TASK COMPLETED)" not in taskToDelete.lower() or "(task completed)" not in taskToDelete.lower():
                if taskToDelete.lower().strip() in line.lower().strip():
                    taskDeleted = i
                    # Again cannot delete the title of the file
                    if ("TODO List 'Application'".lower() in lines[taskDeleted - 1].strip().lower()):
                        print("Cannot delete a title of a file 😂")
                        # Recursive function number 7
                        todo_Options()
                else:
                    lineCounter += 1
                    # If lineCounter is directly equal to the length of lines then the task isn't available
                    if lineCounter == len(lines):
                        print("Invalid task, please try again...")
                        # Recursive function number 8
                        todo_Options()
            else:
                print("Invalid task...")
                # Recursive function number 9
                todo_Options()
        # Delete the contents in the lines array and the file
        del lines[taskDeleted - 1]
        f = open(FILENAME, "w")
        # Rewrite the modified lines, removing the requested text
        f.writelines(lines)
        print("Task has been removed")
        # Recursive function number 10
        todo_Options()

# Initialize the file where data will be kept and check if it exists or not, if not create the file
def startFun():
    if os.path.exists(FILENAME):
        todo_Options()
    else:
        f = open(FILENAME, "w")
        f.write("TODO List 'Application'\n")
        f.close()
        todo_Options()

if __name__ == "__main__":
    startFun()