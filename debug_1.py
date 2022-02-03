
# =================================================================================================================================== #
# Program:	debug_1.py
# Version:	1.1
# Created by: Fernando Figueroa
# Date created:	2022-01-23
#
# Main proc.: Debug cape and transfered code
# Purpose: Debug visualization on real time and library Transference to Python from PHP
#
# Receives:
# Realize:
# Returns:
# =================================================================================================================================== #



# ========================================= [ HEADERS & LIBRARIES ] ================================================================= #

import requests				# lib for handling requests like post, get, cookies
import re as preg			# lib for regular expression operations
from datetime import date	# lib for the date and time optimized
import os 					# lib for handle operating system variables 
import sys  				# lib to use things of the system
import math  				# lib for mathematical expression


# ========================================= [ INIT ] ================================================================================ #

# Initialization of the lowest cape, the main purpose of this cape is the
# visualization of a debug procedure where a flag (bool_DEBUG) will indicate
# if it is turned on and every function will display what is doing and what 
# is happening at real time


def init_script_debug(bool_DEBUG, url_from):							# Init function, in the ideal code, this won't appear
																		# it would handle the DEBUG flag inmediatly
    
    r_server_get = requests.get(url_from)								# Get method for a given URL 
    file_path = os.path.realpath(__file__)								# Get the canonical path of the specified filename by 
    																	# eliminating any symbolic links encountered in the path.

    # Block direct access if the file path has "debug" in it's name

    pattern = "/debug/"

    match_pattern_1 = preg.search(pattern, str(r_server_get.headers))	# preg.search will find the pattern ("debug") in the headers of the URL
    match_pattern_2 = preg.search(pattern, str(file_path))				# and on the name of the file path. This method returns a string indicating 
    																	# the position of the matched pattern, how many times it found it (if it's the case)
 																		# and the matched pattern, otherwise, it returns an empty string (None)
 
    if(match_pattern_2 != None) | (match_pattern_1 != None):			# Will check in the both names (path and headers) one or another
        print("= direct access disabled =")								# If the pattern matched, the direct acces is blocked and the system exits
        sys.exit()

    if(bool_DEBUG == 1):												# If the debug flag is on, it shouts the 'p' case and prints it in a html format
        shout('p', 'debug')


# ========================================= [ FUNCTIONS ] ============================================================================== #

# The shout method will print in html format each case in which the debug is working on, this methods needs
# the case variable and the object that has at that time  

def shout(char_class, obj_this):
    match(char_class):
        case 'p': # case SECTION
            print(
                "<br><br><strong style=\"color:#F93;\">SECTION:</strong>", obj_this, "\n")

        case 'i': # case INFO STATUS 
            print(
                "<br><strong style=\"color:#9CF;\">INFO STATUS:</strong>", obj_this, "\n")
            
        case 'e': # case ERROR
            print(
            	"<br><strong style=\"color:#600;\">ERROR:</strong>", obj_this, "\n")
            
        case 'q': # case QUERY
            print(
            	"<br><strong style=\"color:#33C;\">QUERY:</strong>", obj_this, "\n")
            
        case 'r': # case RESULT
            print(
            	"<br><strong style=\"color:#669;\">RESULT:</strong>", obj_this, "\n")
           
        case 's': # case SYSTEM
            print(
            	"<br><strong style=\"color:#06F;\">SYSTEM:</strong>", obj_this, "\n")
           
        case '@': # case ARRAY															# In this particular case, it takes the keys of the dict
            print("<br><strong style=\"color:#C90;\">ARRAY:</strong> <ol><li>")			# and prints it beetween <li> tags on different rows through 
            print('</li>\n<li>'.join(obj_this))											# a for loop
            print("</li></ol> \n")
         
        case '%': # case HASH
            print("<br><strong style=\"color:#093;\">HASH:</strong> <ul> \n")			# In this case, it prints the keys and the values
            for str_thiskey in obj_this:												# beetween <li> tags each one on different rows
                print(" <li>", str_thiskey, ": ",
                      obj_this[str_thiskey], "</li> \n")
            print("</ul>")
        
        case '?': # case STRUCTURE 														# This case informs the type of the object and prints the entire
            print("<br><strong style=\"color:#90F;\">STRUCTURE:</strong> <ul> \n")		# object on a single row
            print("<br><strong style=\"color:palegreen4;\"> ", type(obj_this),
                  "</strong>", repr(obj_this), "\n")
        
        case '_': # case EMPTY
            print("<br><strong style=\"color:#699;\">-:</strong>", obj_this, "\n")


# Ideally, this method starts the debugging, it gets from the URL given data, cookies and path.
# For each key of the info received, it prints them with its values. This method will show everything
# important at the start related to the server and URL.

## *** VERSION 1 - check the request part, the keys that gets and how it works 

def beginDebug(url_from):
    i = date.today()
    r_server_get = requests.get(url_from)
    r_server_put = requests.put(url_from, data={'key': 'value'})				# Request part for the URL *** check
    r_server_cookies = r_server_get.cookies
    file_path = os.path.realpath(__file__)
    above_request = [r_server_get.headers, r_server_put, r_server_cookies]		# In one array, put together all the info gotten above

    print("<h1>", file_path, " DEBUG ", i, " - Python version ",				# prints it in a html format, Python version, and the file path
          sys.version_info[0], "</h1> \n")

    index = 0
    for str_thiskey in above_request:  											# *** check -> what keys has $_REQUEST because the result gives 1, 2 ,3 ...
        print(" ", index, ": ", str_thiskey)									# for each key in the complete array, it prints each value of the object
        index += 1
        if(r_server_get.cookies == True):										# plus, if it has cookies, print them too
            print(" <span style=\"color:darkpink\">[COOKIE]</span> ")
        print("<br> \n")

    print("</small> \n<hr>\n")


# This method will end the debugging procedure, it gives one last time thte file path
# and it prints it in a html format

def endDebug():
    file_path = os.path.realpath(__file__)
    shout('p', "<blockquote><h3><a href=\"" +
          file_path + "\"> NEXT </a></h3></blockquote>")


# This method will obscure a given string, with the puropose of cover a password or an user
# so that, when it's returned, it won't be shown to the screen, replaced by several ---

def obscure(str_value):															# Gets the lenght of the string, then it's divided by 4 and then rounded down
    int_quarter = math.floor((len(str_value))/4) - 1							# finally, 1 is substracted. This will acomplish as how it follows:
    int_length = len(str_value)													# e.g. password -> will get p[asswor]d and replace the middle section with p[-----]d

    repeat_value = int_length - (2 * int_quarter)
    obscure = str_value[0:int_quarter] + repeat_str("-", repeat_value) + str_value[(int_length - int_quarter)]
    return obscure

# To acomplish the last method, we need a function that repeats a given string
# different to php, there is no default function for this

def repeat_str(a_string, target_length):
    number_of_repeats = target_length // len(a_string) + 1
    a_string_repeated = a_string * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:target_length]
    return a_string_repeated_to_target
