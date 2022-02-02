
# ============================================================
# Program:	debug_1.py
# Version:	1.1
# Created by: Fernando Figueroa
# Date:	2022-01-23
#
# Main proc.: Library convertion
# Purpose: Library Transference to Python from PHP
#
# Receives:
# Realize:
# Returns:
#============================================================

# Headers and libraries 

import requests
import re as preg
from datetime import date
import os
import sys
import math


# Init the lowest cape

def init_script_debug(bool_DEBUG, url_from):

	r_server_get = requests.get(url_from)
	file_path = os.path.realpath(__file__)

	# Block direct access

	pattern = "/debug/"

	match_pattern_1 = preg.search(pattern, str(r_server_get.headers))
	match_pattern_2 = preg.search(pattern, str(file_path))

	if(match_pattern_2 != None) | (match_pattern_1 != None):
		print("= direct access disabled =")
		sys.exit();

	if(bool_DEBUG == 1):
		shout('p', 'debug')


# ========================================= [ FUNCTIONS ]

# Show status

def shout(char_class, obj_this):
	match(char_class):
		case 'p':
			print("<br><br><strong style=\"color:#F93;\">SECTION:</strong>", obj_this, "\n")
			#exit()
		case 'i':
			print("<br><strong style=\"color:#9CF;\">INFO STATUS:</strong>", obj_this, "\n")
			#exit()
		case 'e':
			print("<br><strong style=\"color:#600;\">ERROR:</strong>", obj_this, "\n")
			#exit()
		case 'q':
			print("<br><strong style=\"color:#33C;\">QUERY:</strong>", obj_this, "\n")
			#exit()
		case 'r':
			print("<br><strong style=\"color:#669;\">RESULT:</strong>", obj_this, "\n")
			#exit()
		case 's':
			print("<br><strong style=\"color:#06F;\">SYSTEM:</strong>", obj_this, "\n")
			#exit()
		case '@':
			print("<br><strong style=\"color:#C90;\">ARRAY:</strong> <ol><li>")
			print('</li>\n<li>'.join(obj_this))
			print("</li></ol> \n") 
			#exit()
		case '%':
			print("<br><strong style=\"color:#093;\">HASH:</strong> <ul> \n")
			for str_thiskey in obj_this:
				print(" <li>", str_thiskey, ": ", obj_this[str_thiskey], "</li> \n")
			print("</ul>")
			#exit()
		case '?':
			print("<br><strong style=\"color:#90F;\">STRUCTURE:</strong> <ul> \n")
			print("<br><strong style=\"color:palegreen4;\"> ", type(obj_this), 
					"</strong>", repr(obj_this), "\n")
			#exit()
		case '_':
			print("<br><strong style=\"color:#699;\">-:</strong>", obj_this, "\n")
			#exit()


#Init Debug 

def beginDebug(url_from):
    i = date.today()
    r_server_get = requests.get(url_from)
    r_server_put = requests.put(url_from, data={'key': 'value'})
    r_server_cookies = r_server_get.cookies
    file_path = os.path.realpath(__file__)
    above_request = [r_server_get.headers, r_server_put, r_server_cookies]

    print("<h1>", file_path, " DEBUG ", i, " - Python version ",
          sys.version_info[0], "</h1> \n")

    index = 0
    for str_thiskey in above_request: #check -> what keys has $_REQUEST
        print(" ", index, ": ", str_thiskey)
        index += 1
        if(r_server_get.cookies == True):
            print(" <span style=\"color:darkpink\">[COOKIE]</span> ")
        print("<br> \n")

    print("</small> \n<hr>\n")


# End debug

def endDebug():
	file_path = os.path.realpath(__file__)
	shout('p', "<blockquote><h3><a href=\""+file_path+"\"> NEXT </a></h3></blockquote>")



# Obscure string

def obscure(str_value):
    int_quarter = math.floor(len(str_value)/4)
    int_length = len(str_value)

    repeat_value = int_length-(2*int_quarter);
                                       
    return  str_value[0:int_quarter] + repeat_str("-", repeat_value) + str_value[int_length:(int_length-int_quarter)]


def repeat_str(a_string, target_length):
    number_of_repeats = target_length // len(a_string) + 1
    a_string_repeated = a_string * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:target_length]
    return a_string_repeated_to_target

