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

def mark_todo(file_name):
    print("Mark to do")

def view_todo(file_name):
    print("View to do")