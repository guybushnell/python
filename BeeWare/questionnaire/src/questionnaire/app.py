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

TEXT_SIZE = 15


class Questionnaire(toga.App):
    question_num = 0
    light_bar_size = (0,0)
    choice = -1
    choices = []
    
    def create_questionnaire(self):
        """
        Setup the windows with a question number, question and answer buttons.
        
        [ Username - Q1/5]
        [ Question text  ]
        [ 1  2  3  4  5  ]
        [ -------------  ]
        [ Next           ]
        """
        
        column_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # the question number e.g. Q1/5
        self.question_num_label = toga.Label("Username - Q1/10", style=Pack(color="red", font_size=TEXT_SIZE, padding_bottom=10))
        column_box.add(self.question_num_label)
        
        # The actual question
        self.question_label = toga.Label("Would you rather be a fish or a ferret?",
                                         style=Pack(font_size=TEXT_SIZE*2, font_weight="bold", padding_bottom=10))
        column_box.add(self.question_label)
        
        # Make up an array of choice buttons for the user's answer
        self.buttons = []
        
        for i in range(0, 5):
            choice_button = toga.Button(text=str(i+1), 
                                        style=Pack(flex=1, padding=5, font_size=TEXT_SIZE),
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
                                       style=Pack(background_color="green", color="white", font_size=TEXT_SIZE, padding_top=20),
                                       on_press=self.next_question, enabled=False)
        
        column_box.add(toga.Box(style=Pack(alignment=RIGHT, flex=1), children=[self.next_button]))
        
        self.main_window.content = column_box
        
        
    def create_welcome(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        
        main_box.add(toga.Label(text="Welcome!", style=Pack(text_align=CENTER, font_size=TEXT_SIZE*2, padding_bottom=20)))
        
        # We need to get the user's name
        name_input = toga.TextInput(placeholder="Your name...", on_change=self.on_change_name, style=Pack(font_size=TEXT_SIZE, width=200))

        tidy_box = toga.Box(style=Pack(direction=ROW))
        tidy_box.add(toga.Canvas(style=Pack(flex=1)))
        tidy_box.add(name_input)        
        tidy_box.add(toga.Canvas(style=Pack(flex=1)))

        main_box.add(tidy_box)

        main_box.add(toga.Label(text="Enter your name then press Start.\nYou will then be asked a series of questions \nto help find your perfect match!", 
                                style=Pack(text_align=CENTER, padding=20, font_size=TEXT_SIZE)))
                
        self.start_button = toga.Button(text="Start", 
                                        style=Pack(background_color="green", color="white", font_size=TEXT_SIZE),
                                        on_press=self.start, enabled=False)
        main_box.add(self.start_button)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        
        
    def create_summary(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        
        main_box.add(toga.Label(text="Thank You!", style=Pack(text_align=CENTER, font_size=TEXT_SIZE*3, padding=20)))        
        main_box.add(toga.Label(text="Here is a summary of your answers:", style=Pack(text_align=CENTER, padding=5, font_size=TEXT_SIZE)))
        main_box.add(toga.Label(text=str(self.choices), style=Pack(text_align=CENTER, font_size=TEXT_SIZE)))
                
        row = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding_top=50))
        row.add(toga.Canvas(style=Pack(flex=1)))
        row.add(toga.Button(text="Goodbye", on_press=self.on_exit, style=Pack(font_size=TEXT_SIZE)))
        row.add(toga.Canvas(style=Pack(flex=1)))
        main_box.add(row)
        
        self.main_window.content = main_box
        
        
    def on_change_name(self, widget:toga.TextInput):
        self.username = widget.value
        
        if len(self.username) > 0:
            self.start_button.enabled = True
        else:
            self.start_button.enabled = False
            
    
    def start(self, widget):
        self.create_questionnaire()
        
        self.question_num = 0
        self.answers = []

        self.show_question(compatibility)
        
        
    def next_question(self, widget):
        # store the last choice made
        self.choices.append(self.choice)

        self.question_num = self.question_num + 1
        
        if self.question_num < len(compatibility):
            self.show_question(compatibility)
        
            self.choice = -1
            self.update_button_light()
            self.next_button.enabled = False
        else:
            self.create_summary()
        
        
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
        self.question_num_label.text = "%s - Question %d/%d" % (self.username, self.question_num+1, len(questions))
        
        # label the first and last button
        self.buttons[0].text = "1-%s" % question[1]
        self.buttons[4].text = "5-%s" % question[2]
        
        # show the text of the question
        self.question_label.text = question[0] + "?"
        
        
    def startup(self):
        self.create_welcome()
        # self.create_summary()
        self.main_window.show()



def main():
    return Questionnaire()
