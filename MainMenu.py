
from consolemenu.console_menu import ConsoleMenu
import consolemenu.items as Items

from CandyFactoryMenu import CandyFactoryMenu

class MainMenu(ConsoleMenu):
    
    def __init__(self):
        super().__init__("Main Menu")
        

        self.candy_factory_menu = CandyFactoryMenu()
        self.candy_factory_submenu = Items.SubmenuItem("COOKIE FACTORY!", submenu=self.candy_factory_menu)
        self.clear_candy_button = Items.FunctionItem("Clear candy <Are you sure>?", self.clear_candy)
        
        self.append_item(self.candy_factory_submenu)
        self.append_item(self.clear_candy_button)
        
        
    def clear_candy(self):
        self.candy_factory_menu.candy = 0