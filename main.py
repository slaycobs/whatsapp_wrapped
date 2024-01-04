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
YEAR = 2023

def get_date(line: str) -> date:
    try:
        line = line[1:line.find("]")]
        day_end = line.find("/")
        day = int(line[0:day_end])
        month_end = line.find("/", day_end+1)
        month = int(line[day_end+1:month_end])
        year_end = line.find(",")
        year = int(line[month_end+1:year_end])
        return date(year, month, day)
    except:
        return None


def parse_line(line: str) -> Tuple[str, str]:
    # split message sender, message
    sender_onwards = line[line.find("]") + 2:]
    sender = sender_onwards[:sender_onwards.find(":")].lower()

    message = line[line.find(":", 20) + 2:].lower()
    # strip punctuation
    message = message.translate(str.maketrans('', '', string.punctuation))
    message = message.replace("’", "")
    message = message.replace("‘", "")

    return sender, message

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
    begun_year = False
    with open(filename, "r") as fp:
        contents = fp.readlines()
        for line in contents:
            line = line.strip().replace("‎", "")
            d = get_date(line)
            # if it's a new message it will have a date, add it to the contents list
            if d != None:
                sender, message = parse_line(line)
                # filter by year
                if d.year == YEAR:
                    begun_year = True
                    parsed_contents.append({"date": d, "sender": sender, "message": message})
                # assume chat is chronological and exit as soon as year is over
                else:
                    pass
                    # if not begun_year:
                    #     continue
                    # break
            # otherwise, extend the most recently added message
            else:
                if len(parsed_contents) > 0:
                    parsed_contents[-1]["message"] += line                
    print("total messages: ", len(parsed_contents))
    print(parsed_contents)
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