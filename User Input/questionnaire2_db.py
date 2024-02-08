# Ask the user a series of questions
# Store answers on file so we can load them-in later.

import json

# use some functions and data from previous version of the program
from questionnaire1 import welcome, get_answers


def load_database() -> dict:
    """
    Try to load responses from users for previous runs of the program
    @return - dictionary of name:answers
    """
    
    # Try to load existing answers from file
    try:
        file = open("answers.json", "r")
        database = json.loads(file.read())
        file.close()

        # output size of database and names of all those in it (no newline on this print)
        print("Loaded previous answers from: ", end='')
        
        # get each name and the answers for it...
        for name, answers in database.items():
            print("%s, " % name, end='')
            
        # finally, add a newline.
        print("")
    except IOError as e:
        # no existing answers, just make an empty dictionary
        database = {}
        print("Starting with an empty database - you're the first volunteer!")
        
    return database
        
        
def save_database(database: dict):
    """
    Store the database of user-names and answers to file
    """
    try:
        file = open("answers.json", "w")
        json.dump(database, file)
        file.close()
        print(">> Database saved <<")
        
    except IOError as e:
        print("Can't save the database - %s" % str(e))
        
        
# Stop this bit running if we're using importing this as a module
if __name__ == "__main__":
    username = welcome()
    database = load_database()
    answers = get_answers()
    database[username] = answers
    save_database(database)
