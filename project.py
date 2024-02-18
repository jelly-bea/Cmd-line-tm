import csv
import re

tasks=[]

def create(tasks,n,w):
    #storing the task in tasks
    tasks.append({"Description" : n, "Deadline" : w, "Status" : "Incomplete"})
    return "\033[94mTask successfully created! 📝\033[0m"

def delete(tasks,task):
    try:
        if task>=len(tasks):
            raise Exception
        #deleting a task
        else:
            del tasks[task]
            return "\033[94mDeleted successfully! 😌\033[0m"

    except Exception:
        return "\033[91mDelete operation cancelled.\033[0m"

def modify(tasks,task,modifiedName,modifiedDeadline):
    try:
        if task>=len(tasks):
            raise Exception
        tasks[task]["Description"] = modifiedName
        tasks[task]["Deadline"] = modifiedDeadline
        return "\033[94mThe task is modified! \033[0m"
    except Exception:
        return "\033[91mModify operation cancelled. \033[0m"

def show(tasks):
    t=""
    print("\n\033[1mTasks - \033[0m")
    #printing all the tasks
    for i,task in enumerate(tasks, start = 1):
        t += f"{i}. {task}\n"
    return t

def complete(tasks,task):
    try:
        if task>=len(tasks):
            raise Exception
        #marking the task complete
        tasks[task]["Status"] = "Complete"
        return "\033[94mTask complete! 🥳\033[0m"
    except Exception:
        return "\033[91mComplete operation cancelled. \033[0m"

def download(tasks):
    #saving the tasks to a file, overwrites if already exists
    with open("tasks.csv","w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Description","Deadline","Status"])
        w.writeheader()
        for task in tasks:
            w.writerow(task)

def loadFile(fn):
    global tasks
    #loading tasks already saved from a csv file
    try:
        with open(fn) as f:
            r = csv.DictReader(f)
            for task in r:
                tasks.append(task)
        return "\033[94mSuccessfully loaded the file! 😋\033[0m"
    except FileNotFoundError:
        return "\033[91mFile not found\033[0m"

def Exit():
    return "\033[91mbye...👋\033[0m"


def main():
    while True:
        #task manager window
        print("\n\033[1mTask Manager - \033[0m")
        print("1. Create a new task")
        print("2. Modify an existing task")
        print("3. View tasks")
        print("4. Mark task as complete")
        print("5. Delete a task")
        print("6. Save tasks to file")
        print("7. Load tasks from file")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    #getting name of the task
                    name = input("What's the task? ")
                    #getting the deadline of the task to be completed
                    when = input("When is the deadline? ")
                    print(create(tasks,name,when))

                case 2:
                    print(show(tasks))
                    a=int(input("\nWhich task to be modified? "))
                    #getting name of the task
                    mn = input("What's the modified task name? ")
                    #getting the deadline of the task to be completed
                    md = input("When is the deadline? ")
                    print(modify(tasks,a-1,mn,md))

                case 3:
                    print(show(tasks))

                case 4:
                    print(show(tasks))
                    a=int(input("Which task is complete? "))
                    print(complete(tasks,a-1))

                case 5:
                    print(show(tasks))
                    a=int(input("Which task to be deleted? "))
                    print(delete(tasks,a-1))

                case 6:
                    download(tasks)
                    print("\033[94mTasks saved to file! 📁\033[0m")

                case 7:
                    fileName = input("What is the file name? ").strip()
                    if re.search(r"\.csv$",fileName):
                        print(loadFile(fileName))
                    else:
                        print("\033[91mOnly csv files are supported.\033[0m")
                case 8:
                    print(Exit())
                    break

                case _:
                    raise Exception

        except Exception:
            print("\033[91mInvalid input 😕\033[0m")
            break


if __name__ == "__main__":
    main()