import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    """
    Connect to MongoDB and return the connection in the variable conn
    """
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errorsConnectionFailure as e:
        print("could not connect to MongoDB: %s") % e


def show_menu():
    """
    Prints out the user optons to the terminal
    """
    print("========================")
    print("Please select an option")
    print("========================")
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def get_record():
    """
    Helper class: Uses the user input to search the collection and retrieve the details 
    """
    print("")
    first = input("Enter first name >")
    last = input("Enter last name >")
    
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")  
    if not doc:
        print("")
        print("Error, No results found")

    return doc


def add_record():
    """
    Terminal prompts to gather user input for adding to record
    """
    print("")
    first = input("Enter first name >")
    last = input("Enter last name >")
    dob = input("Enter date of birth dd/mm/yyyy >")
    gender = input("Enter gender >")
    hair_color = input("Enter a hair colour >")
    occupation = input("Enter occupation >")
    nationality = input("Enter nationality >")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_color": hair_color.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower()
    }

    try:
        coll.insert_one(new_doc)
        print("")
        print("New document inserted")
    except:
        print("Error accessing the database")


def find_record():
    """
    Retrieve and display a collection record to the user based on first/last name
    """
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ":" + v.capitalize())


def edit_record():
    """
    Retrives a record using first/last name and displays each record one at a time for amending
    """
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                # displays in terminal Last [pratchett] > 
                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("record updated")
        except:
            print("Error accessing the database")


def delete_record():
    """
    Retrieves a record based on first/last name and then requests confirmation before deletion
    """
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": ", v.capitalize())

        print("")
        confirmation = input("Is this the document you wish to delete\n Y or N > ")
        print("")
        
        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("document entry deleted")
            except:
                print("Error accessing the database")
        else:
            print("No records were dleted, please choose an option below")


def main_loop():
    """
    Continues to run so when a action is completed the user is returned to an options menu
    """
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
