import csv

def add_todo(file_name):
    print("Add to do")
    # Ask the title of the to do
    todo_name = input("Enter a to do: ")
    # todo_file = open(file_name, "r")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # Insert values   - title = user entered
                        # - completed = False
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove to do")
    todo_name = input("Enter a to do that you want to remove: ")
    # copy all the contents on the csv into a new csv
    # while doing this, we constantly check for the condition
    # when we encounter the to do to be removed, we don't copy that one
    # then the final new to do will be written in the csv file
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if todo_name != row[0]:
                todo_lists.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo(file_name):
    print("Mark to do")
    todo_name = input("Enter the to do name that you want to mark as completed: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if todo_name != row[0]:
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def view_todo(file_name):
    print("View to do")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # row = ["To do 1", "False"]
            if row[1] == "True":
                print(f"To do {row[0]} is completed")
            else:
                print(f"To do {row[0]} is not completed")