# Ask the user a series of questions
import os

compatibility = (
    ("Marmite", "Hate it", "Love it"),
    ("Rockers with long hair", "Get a haircut!", "Let me at 'um"),
    ("Cigarettes", "Cough, splutter", "Inhale deeply"),
    ("Great Yarmouth", "Hate it", "Love it"),
    ("6Music", "Six What?", "Weekend Joy"),
    ("Strictly", "Lord help us", "Thank the Lord"),
    ("Food", "Meat is murder", "Mmmm Bacon"),
    ("Ice skating", "Heaven", "Hell")    
)

def ask_questions(questions: list) -> list:
    '''
    Give a list of questions, present each one to the user and record
    the result.
    '''
    question_num = 1
    answers = []
    
    for question in questions:
        print("%d) %s?      [1]%s      [5]%s" % (question_num, question[0], question[1], question[2]));
        
        # add their input to the list of answers
        # could do some error checking here - what if they enter '6'?
        answer = input()
        answers.append(int(answer))
        
        # Output a new line
        print("")
        
        question_num = question_num + 1
    
    return answers


def ask_questions_pretty(questions: list) -> list:
    '''
    Give a list of questions, present each one to the user. 
    Format the output nicely.
    @return - all answers as a list
    '''
    QUESTION_PAD = 35
    ANSWER_PAD = 20
    
    answers = []
    nof_questions = len(questions)
    
    # using enumerate also returns the index number
    for index_num, question in enumerate(questions):
        #  copy the question into the string
        prompt = "%d/%d) %s?" % (index_num+1, nof_questions, question[0])
        
        # Pad it out to be the correct length
        while len(prompt) < QUESTION_PAD:
            prompt = prompt + " "
            
        # Now add in the first answer
        prompt = prompt + question[1]
        
        # and adjust the padding again
        while len(prompt) < QUESTION_PAD + ANSWER_PAD:
            prompt = prompt + " "
        
        prompt = prompt + question[2]
        print(prompt)
        
        # now print a scale to guide the user what to enter
        line = " " * QUESTION_PAD + "1"
        while len(line)+1 < len(prompt):
            line = line + "_"
        
        line += "5: "
        answer = input(line)
        answers.append(int(answer))
        print("")
        
    return answers
    

def welcome()->str:
    """
    Say hello and ask for a name.
    @returns: user's name
    """
    
    # clear the screen
    os.system('cls||clear')

    # Say hello and give some instructions
    print("COMPATIBILITY TEST")
    print("==================")

    name = input("What is your name? ")

    print("**** Welcome %s! ****\n" % name)
    return name


def get_answers() -> (str, list):
    """
    Ask each question in turn.
    @return - answers
    """
    
    print("Please answer the following %d questions on a scale of 1...5\n" % len(compatibility))

    answers = ask_questions_pretty(questions=compatibility)
    
    print("Your answers: %s" % answers)
    print("Thanks - you're all done!")
    
    return answers

    
# ==== Program Start
if __name__ == "__main__":
    welcome()
    get_answers()



    
