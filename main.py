#-----------------------------#
#          6/16/2024          #
#-----------------------------#
from flask import * 
from bs4 import *

# Flask Server Configuration
SERVER = Flask(__name__)
# List Of Tasks (Needed for saving them and looping through them)
tasks: list = []

@SERVER.route("/", methods= ["GET", "POST"])
def HOME():
    # Getting Html From The file And Turning it into a BeautifulSoup object so we can add Elements to it
    a: str = render_template("index.html")
    soup: BeautifulSoup = BeautifulSoup(a, features= "lxml")
    # Adding Div Elements to the BeautifulSoup Object for every item in tasks list
    for i in range(len(tasks)):
        LIST: Tag = soup.new_tag("div") 
        LIST.string = f"{i + 1} : {tasks[i]}"
        LIST["class"] = "container g-5 border border-white text-white mt-1 rounded-2"
        LIST["id"] = "TASKS"
        # Adding the new element
        soup.html.body.append(LIST) 
    # Returning the BeautifulSoup object instead of html because we have Added Elements
    return str(soup)


@SERVER.route("/add_Item", methods= ["GET", "POST"])
def Add_element():
    # Getting The task from the form and adding it to task list 
    Task: str = str(request.form.get("Task"))
    tasks.append(Task)
    # Redirecting to home
    return redirect("/")


@SERVER.route("/delete_Item", methods= ["GET", "POST"])
def Remove_Element():
    try :
        # Getting The Task id from the form and removing it from the task list
        Task_Id: int = int(request.form.get("TaskId")) - 1
        tasks.remove(tasks[Task_Id])
        # Redirecting to home
        return redirect("/")
    # If the user inserted an index that the list didn't contain it would warn the user
    except IndexError:
        return "Couldn't Find any item with that id please try another one"

# Running Flask Server
if __name__ == "__main__":
    SERVER.run(debug= True)