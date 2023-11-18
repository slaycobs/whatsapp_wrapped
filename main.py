import sys
import os
import pandas as pd
from typing import List, Dict, Tuple
from datetime import date, time
from ChatStats import ChatStats
from StatsPrinter import StatsPrinter
import string

# make sure to remove the first three default messages from the exported file
FILE_NAME = "chat.txt"

def parse_line(line: str) -> Tuple[date, time, str, str]:
    # split message into date, time, sender, message
    # year, month, day
    d = date(int(line[6:10]), int(line[3:5]), int(line[0:2]))
    # hour, minute
    t = time(int(line[12:14]), int(line[15:17]))

    sender_onwards = line[20:]
    sender = sender_onwards[:sender_onwards.find(":")].lower()

    message = line[line.find(":", 20) + 2:].lower()
    # strip punctuation
    message = message.translate(str.maketrans('', '', string.punctuation))

    return d, t , sender, message

def is_new_message(line: str) -> bool:
    # if the message starts with a date, then its a new message
    # assumes no organic message starts with a date
    try:
        d = date(int(line[6:10]), int(line[3:5]), int(line[0:2]))
        return True
    except:
        return False 

def read_file(filename: str) -> List[Dict]:
    # read through the file and add parsed contents to a list
    parsed_contents = []
    with open(filename, "r") as fp:
        contents = fp.readlines()
        for line in contents:
            line = line.strip()
            # if it's a new message, then add it to the contents list
            if is_new_message(line): 
                d, t, sender, message = parse_line(line)
                parsed_contents.append({"date": d, "time": t, "sender": sender, "message": message})
            # otherwise, extend the most recently added message
            else:
                parsed_contents[-1]["message"] += line
    return parsed_contents

def form_word_bank(contents: List[Dict]) -> ChatStats:
    chat_stats = ChatStats()
    for entry in contents:
        chat_stats.add(entry)
    return chat_stats

def main() -> None:
    contents = read_file(FILE_NAME)
    chat_stats = form_word_bank(contents)
    chat_stats.clean()
    stats_printer = StatsPrinter(chat_stats)
    stats_printer.print_stats()

if __name__=="__main__":
    sys.exit(main())