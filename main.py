from pyscript import display, document

class Classmate:
    def __init__(self, name, section, favsubject):
        self.name = name
        self.section = section
        self.favsubject = favsubject

classmates = [ #list of classmates with info
    Classmate('Jazmar', 'Sapphire', 'SS'),
    Classmate('Khen', 'Sapphire', 'PE'),
    Classmate('Fil', 'Topaz', 'SS'),
    Classmate('Lance', 'Ruby', 'Math'),
    Classmate('Fiona', 'Sapphire', 'Math')
]

def process(e):
    introhere = "" #string that will hold the introductions of all classmates

    for cm in classmates: #for loop that goes through each classmate in the list and creates an introduction for them
        intro = f"Hello! My name is {cm.name}. I am in {cm.section} and my favorite subject is {cm.favsubject}.\n"
        
        introhere += intro + "<br>"

    document.getElementById("intro").innerHTML = introhere

def add(e): #function that adds a new classmate to the list using the input fields
    name = document.getElementById("user").value
    section = document.getElementById("pass").value
    favsubject = document.getElementById("fav").value

    if name == "" or section == "" or favsubject == "": #checks if any of the input fields are empty
        document.getElementById("intro").innerHTML = "<span style='color: red;'>Please fill out all fields before adding a classmate.</span>"
        return

    new_classmate = Classmate(name, section, favsubject) #creates a new classmate object using the input values
    classmates.append(new_classmate)

    document.getElementById("user").value = "" #clears the input fields after adding the classmate
    document.getElementById("pass").value = ""
    document.getElementById("fav").value = ""

    process(e) #calls the process function to update the introductions with the new classmate included