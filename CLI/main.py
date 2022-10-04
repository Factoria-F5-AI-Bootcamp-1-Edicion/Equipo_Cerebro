import curses
import time
from curses import textpad
import subprocess
import sys
from predictor import predictor
import os
from subprocess import call


import curses

PREDICTOR = 'Use predictor'
STREAMLIT ='Go to Dashboard --> Performance report'
DATA ='View data'
EXIT='Exit'

INTRODUCTION ="SP.22"
                
# TODO : HACER DESCRIPCION DE LA APP
class MenuDisplay:

    def __init__(self, menu):
        # set menu parameter as class property
        self.menu = menu
        
        # run curses application
        curses.wrapper(self.mainloop)

    ## stdscr : objeto ventana
    def mainloop(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)
        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        
        # set screen object as class property
        self.stdscr = stdscr

        # get screen height and width
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        box = [[3,3], [self.screen_height-3, self.screen_width-3]]
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        # specify the current selected row
        current_row = 0
        
        # print the menu
        self.print_menu(current_row)
        stdscr.getch()
        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if menu[current_row] == PREDICTOR:   
                    os.system('cls')   
                    subprocess.run([sys.executable, "-c","from predictor import predictor;  predictor()"],shell=True)
                elif menu[current_row] == STREAMLIT:
                    os.system("start python ../DASHBOARD/brain_dash.py")
                    #subprocess.run(["bash", "streamlit run ../DASHBOARD/brain.py"],shell = True)
                    #subprocess.run([sys.executable,'-c',"from dash_script import main;main()"],shell=True)
                    #subprocess.Popen("streamlit run ../DASHBOARD/brain.py", shell=True, stdout=subprocess.PIPE).stdout.read()
                   # subprocess.call("echo Hello World", shell=True)  
                elif menu[current_row] == DATA:
                    os.system('cls')
                    subprocess.run([sys.executable, "-c","from processing_data import show_table; show_table();"],shell=True)
                    self.stdscr.getch()
                self.stdscr.getch()
                # if user selected last row (Exit), confirm before exit the program
                if current_row == len(self.menu) - 1:
                    if self.confirm("Are you sure you want to exit?"):
                        break

            self.print_menu(current_row)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        self.stdscr.addstr(8, 57,INTRODUCTION, curses.color_pair(1))
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_confirm(self, selected="yes"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "yes"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "no"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "yes"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "yes":
                current_option = "no"
            elif key == curses.KEY_LEFT and current_option == "no":
                current_option = "yes"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "yes" else False

            self.print_confirm(current_option)

    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()


if __name__ == "__main__":
    menu = [PREDICTOR, STREAMLIT, DATA,EXIT]
    MenuDisplay(menu)
