# Ask the user a series of questions
# Store answers on file so we can load them-in later.
# Give a recommended best match for a romantic date!

# use some functions and data from previous version of the program
from questionnaire1 import welcome, get_answers
from questionnaire2_db import load_database, save_database


def get_score(a: list, b: list) -> int:
    """
    Add up the difference between each number in the two lists
    @return - total difference - 0 means perfect match
    """
    total = 0
    
    for index in range(0, len(a)):
        difference = a[index] - b[index]
        difference = abs(difference)
        
        total = total + difference
        
    return total
        
        
def get_best_match(target_user: str, database: dict) -> str:
    """
    Search the database, scoring each set of answers against target_user's
    @returns - the name of the best match
    """
    best_score = 100000
    best_match = "Nobody!"
    
    # look at each name and their answers...
    for (name, answers) in database.items():
        
        # ignore the answers of the target_user
        if name == target_user:
            continue
        
        # lower score is better...
        score = get_score(answers, database[target_user])
        if score < best_score:
            best_score = score
            best_match = name
            
    return best_match
                
    
# ==== Program Start
if __name__ == "__main__":
    username = welcome()
    database = load_database()
    
    # have they already done the quiz?
    if username in database:
        print("It looks like have already answered the questionnaire %s" % username)
        answers = database[username]
    else:
        # no. Do the quiz now and store their answers
        answers = get_answers()
        database[username] = answers
        save_database(database)

    # Now find the best match
    match_name = get_best_match(username, database)
    print("Your best match is: %s" % match_name)
