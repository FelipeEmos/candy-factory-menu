from LayoutHelper import LayoutHelper
from consolemenu import *
from consolemenu.format import *
import consolemenu.items as Items

class CandyFactoryMenu(ConsoleMenu):

    # An example of different layout for the menu.
    # There are plenty of examples in the "examples" folder in the 
    # source code of the "consolemenu" package we are using
    # https://github.com/aegirhall/console-menu
    layout_formater = MenuFormatBuilder() \
        .set_title_align('center')\
        .set_subtitle_align('center')\
        .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER)\
        .show_prologue_top_border(True)\
        .show_prologue_bottom_border(True) \
        .set_left_margin(4) \
        .set_right_margin(4) 
   
   
    # Constructor
    def __init__(self):
        super().__init__("Candy Factory")
        self.formatter = CandyFactoryMenu.layout_formater
        self.candy = 0
        self.speed = 1
        
        self.addCandyButton = Items.FunctionItem("", self.add_candy)
        self.setSpeedButton = Items.FunctionItem("", self.set_speed)
        
        self.append_item(self.addCandyButton)
        self.append_item(self.setSpeedButton)

        self.easter_egg_menu_visit_count = 0
        
    # We need to overide this function because the value of candy
    # needs an update before we display our menu. 
    def draw(self):
        self.render()
        return super().draw()
        
    def start(self):
        self.easter_egg_menu_visit_count += 1
        super().start()
        
    def render(self):
        self.addCandyButton.text = LayoutHelper.getLine_TwoColums(
            leftStr="Candy : ",
            rightStr=str(self.candy),
            marginLeft=3,
            marginRight=5)
        self.setSpeedButton.text = LayoutHelper.getLine_TwoColums(
            leftStr="Speed : ",
            rightStr=str(self.speed),
            marginLeft=3,
            marginRight=5)

        self.rendet_easter_egg()


    def add_candy(self):
        self.candy += self.speed
        # we need to update our candy text
        self.render()
    
    def set_speed(self):
        print("What is the speed you want to create candy?")
        is_ans_valid = False
        while(not is_ans_valid):
            answer = input("New speed : ")
            
            if(answer.isnumeric and int(answer) > 0):
                self.speed = int(answer)
                is_ans_valid = True
            else:
                print("\nInvalid value. Try again...")
        
    def rendet_easter_egg(self):

        # Enter in the candy enough times and you get to see it ;)
        if(self.easter_egg_menu_visit_count > 2):
            self.prologue_text = "You have been here in this menu {} times".format(self.easter_egg_menu_visit_count)
        if(self.easter_egg_menu_visit_count > 4):
            self.prologue_text = "You have been here in this menu {} times, let me tell you a story...".format(self.easter_egg_menu_visit_count)
            
            # Observe that the character "\n" doesn't work
            self.prologue_text += "\n"
            self.prologue_text += "There is a monkey trap that is quite simple"

            # The funciton I created in LayoutHelper kinda "solves" this problem, but there are bugs
            # To do this properly, the best would  be to study their implementation.
            # For me: "Try and error", that's the lemma. My LayoutHelper works for what I want
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "A hunter makes it by slicing a small hole on a coconut"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "It needs to be big enough so a monkey can easily pass his OPEN hand through it, but, at the same time, smaller than a monkey's CLOSED fist"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "After the hole is done, the hunter locks the coconut on a fixed place (like a tree) and puts a bait inside: a piece of CANDY"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "The trap is ready.."
            self.prologue_text += LayoutHelper.fillLine(".")
            # I can't jump a blank line. Two LayoutHelper.fillLine("") in a rowdoesn't work
            self.prologue_text += LayoutHelper.fillLine("...")
            self.prologue_text += "When a monkey sees the trap, it observes it carefully and when it finds out there's CANDY inside, it decides to grab it!"
            self.prologue_text += LayoutHelper.fillLine("")
            self.prologue_text += "Easy, right? The monkey puts his open hand through the small hole and grabs the CANDY"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "But now his fist is closed... he can't take his hand out anymore and hold the CANDY at the same time"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine("...")
            self.prologue_text += "Well, if you think about it, the monkey just has to let go of the CANDY to be free. He will open his hand and he will be able to take it out in the same way he got it in."
            self.prologue_text += LayoutHelper.fillLine("")
            self.prologue_text += "Simple in theory, but not in practice.."
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "He feels the CANDY touching his skin! He can't let go"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "A monkey doesn't let go of the CANDY"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine("...")
            self.prologue_text += "He screams! He fights! He gets desperate!"
            self.prologue_text += LayoutHelper.fillLine("")
            self.prologue_text += "But a monkey doesn't let go of the CANDY"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine("...")
            self.prologue_text += "Even with the hunter getting closer and closer..."
            self.prologue_text += LayoutHelper.fillLine("")
            self.prologue_text += "(the monkey sees the hunter coming!)"
            self.prologue_text += LayoutHelper.fillLine("")
            self.prologue_text += "But a monkey doesn't let go of the CANDY"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "That's why the trap works"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "Suffering less is seeing things as they really are... not as you would like them to be"
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += LayoutHelper.fillLine(".")
            self.prologue_text += "The CANDY never belonged to the monkey."
            self.prologue_text += LayoutHelper.fillLine("")
            