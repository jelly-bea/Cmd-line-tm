import pytest
import csv
from project import create,delete,modify,show,complete,download,loadFile,Exit

tasks=[{"Description":"saying hi","Deadline":"now","Status":"Incomplete"}]
def test_create():
    global tasks
    assert create(tasks,"saying bye","tomorrow") == "\033[94mTask successfully created! 📝\033[0m"
    assert tasks[1]["Description"] == "saying bye"
    assert tasks[1]["Deadline"] == "tomorrow"
    assert tasks[1]["Status"] == "Incomplete"

def test_delete():
    global tasks
    assert len(tasks) == 2
    assert delete(tasks,0) == "\033[94mDeleted successfully! 😌\033[0m"
    assert len(tasks) == 1
    assert delete(tasks,1) == "\033[91mDelete operation cancelled.\033[0m"
    assert delete(tasks,50) == "\033[91mDelete operation cancelled.\033[0m"

def test_modify():
    global tasks
    assert modify(tasks,0,"saying hi-edit","not now") == "\033[94mThe task is modified! \033[0m"
    assert tasks[0] == {"Description":"saying hi-edit","Deadline":"not now","Status":"Incomplete"}
    assert modify(tasks,1,"saying hi-edit","not now") == "\033[91mModify operation cancelled. \033[0m"

def test_show():
    global tasks
    assert show(tasks) == "1. {'Description': 'saying hi-edit', 'Deadline': 'not now', 'Status': 'Incomplete'}\n"

def test_complete():
    global tasks
    assert complete(tasks,0) == "\033[94mTask complete! 🥳\033[0m"
    assert tasks[0] == {"Description":"saying hi-edit","Deadline":"not now","Status":"Complete"}
    assert complete(tasks,2) == "\033[91mComplete operation cancelled. \033[0m"

def test_download():
    global tasks
    download(tasks)
    with open("tasks.csv") as f:
        r = csv.DictReader(f)
        result=list(r)
    expected=[{"Description":"saying hi-edit","Deadline":"not now","Status":"Complete"}]
    assert result == expected

def test_loadFile():
    global tasks
    assert loadFile("tasks.csv") == "\033[94mSuccessfully loaded the file! 😋\033[0m"
    assert loadFile("invalid.csv") == "\033[91mFile not found\033[0m"

def test_Exit():
    assert Exit() == "\033[91mbye...👋\033[0m"


