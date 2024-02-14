"""
My first application
"""
import toga
from toga.colors import WHITE, rgb
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, CENTER, Pack

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

class Questionnaire(toga.App):
    question_num = 0
    light_bar_size = (0,0)
    choice = 2
    choices = []
    
    def create_questionnaire(self):
        """
        Setup the windows with a question number, question and answer buttons.
        
        [ Q1/5 | Question text ]
        [      | 1  2  3  4  5 ]
        [      | ------------- ]
        [      | Next          ]
        """
        
        row_box = toga.Box(style=Pack(direction=ROW, padding=10))

        # the question number e.g. Q1/5
        self.question_num_label = toga.Label("Q1/10", style=Pack(font_size=20, color="blue", padding_right=10))
        row_box.add(self.question_num_label)

        # The question text, the button choice, choice indicator and Next button are all in this column
        column_box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        row_box.add(column_box)
        
        # The actual question
        self.question_label = toga.Label("Would you rather be a fish or a ferret?",
                                         style=Pack(font_size=20, font_weight="bold", padding_bottom=20))
        column_box.add(self.question_label)
        
        # Make up an array of choice buttons for the user's answer
        self.buttons = []
        
        for i in range(0, 5):
            choice_button = toga.Button(text=str(i+1), 
                                        style=Pack(flex=1, padding_left=2, padding_right=2),
                                        on_press=self.on_make_choice)
            
            self.buttons.append(choice_button)
        
        # Put all the buttons in a box and place it after the question text
        button_box = toga.Box(children=self.buttons, style=Pack(padding_bottom=5))
        column_box.add(button_box)

        # Create the canvas we draw on to indicate the user's choice
        self.light_bar = toga.Canvas(style=Pack(flex=1, height=10), on_resize=self.on_resize)
        column_box.add(self.light_bar)
        
        # Finally, add a "Next" button to move to the next question
        self.next_button = toga.Button(text="Next", 
                                       style=Pack(background_color="green", color="white", font_size=20, padding_top=20),
                                       on_press=self.next_question, enabled=False)
        
        column_box.add(toga.Box(style=Pack(alignment=RIGHT, flex=1), children=[self.next_button]))
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = row_box
        self.main_window.show()
        
        
    def next_question(self, widget):
        # store the last choice made
        self.choices.append(self.choice)

        self.question_num = self.question_num + 1
        
        if self.question_num < len(compatibility):
            self.show_question(compatibility)
        
            self.choice = 2
            self.update_button_light()
        else:
            self.main_window.info_dialog("Finished", "You're all clear kid!")

        self.next_button.enabled = False
        
        
    def on_resize(self, widget, width, height, **kwargs):
        self.light_bar_size = (width, height)
        self.update_button_light()
            
    
    def show_button_light(self, index: int, lit: bool):    
        canvas = self.light_bar
        
        if lit:
            col = rgb(0, 255, 0)
        else:
            col = rgb(255, 255, 255)
                
        width = self.light_bar_size[0] / 5
        
        with canvas.context.Fill(color=col) as f:
            f.rect(index*width, 0, width, 10)
          
  
    def update_button_light(self):
        self.light_bar.context.clear()

        for i in range(0, 5):
            if i is self.choice:
                self.show_button_light(i, lit=True)
            else:
                self.show_button_light(i, lit=False)
        
                
    def on_make_choice(self, pressed_button: toga.Button):
        for i, button in enumerate(self.buttons):
            if button is pressed_button:
                print("Button %d pressed" % (i+1))
                self.choice = i
        
        self.update_button_light()
        self.next_button.enabled = True
                
        
    def show_question(self, questions: list) -> list:
        '''
        Give a list of questions, present each one to the user and record
        the result.
        '''        
        question = questions[self.question_num]
        
        # Show the question number
        self.question_num_label.text = "Q %d/%d" % (self.question_num+1, len(questions))
        
        # label the first and last button
        self.buttons[0].text = "1-%s" % question[1]
        self.buttons[4].text = "5-%s" % question[2]
        
        # show the text of the question
        self.question_label.text = question[0] + "?"
        
        
    def startup(self):
        self.create_questionnaire()
        
        self.question_num = 0
        self.answers = []
        self.show_question(compatibility)
         
        print("Hello wold")


def main():
    return Questionnaire()
