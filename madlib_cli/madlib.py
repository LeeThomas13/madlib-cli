print('''
Hey There User!

Welcome to my madlib game!

When prompted, follow the instructions and add whatever you want into the text box!

''')

import re

open_file = open('assets/game.txt')

mad_lib_language = {}



def read_template(path):
    #should read a file and return its content as a stripped string
    content = open(path).read()
    return content.strip()

string_template = read_template('assets/game.txt')

def parse(string_template):
    #should take in a template string and push contents within {} into a dictionary, then clear the space.
    parse_template = re.findall(r"\{(.*?)\}", string_template)
    print(re.sub(r"\{(.*?)\}", "{}", string_template))
    return(re.sub(r"\{(.*?)\}", "{}", string_template))

def merge():
    #should take in a bare template and fill it with user inputted variables.
    pass

