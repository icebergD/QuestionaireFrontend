#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Mar 05, 2022 07:55:28 PM +03  platform: Windows NT
#    Mar 05, 2022 08:21:29 PM +03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import questionnaire_main

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = questionnaire_main.login(_top1)
    # Creates a toplevel widget.
    global _top4, _w4
    _top4 = tk.Toplevel(root)
    _w4 = questionnaire_main.menu(_top4)
    # Creates a toplevel widget.
    global _top7, _w7
    _top7 = tk.Toplevel(root)
    _w7 = questionnaire_main.Questionnaire(_top7)
    # Creates a toplevel widget.
    global _top8, _w8
    _top8 = tk.Toplevel(root)
    _w8 = questionnaire_main.Statistics(_top8)
    root.mainloop()

def login_func(*args):
    print('questionnaire_main_  cccc')

def logout_func(*args):
    print('questionnaire_main_support.logout_func')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()

def to_menu_func(*args):
    print('questionnaire_main_support.to_menu_func')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()

def to_questionnaire_func(*args):
    print('questionnaire_main_support vvvv')
    

def to_statistics_func(*args):
    print('questionnaire_main_s ffff')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()

if __name__ == '__main__':
    questionnaire_main.start_up()





