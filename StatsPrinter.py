from ChatStats import ChatStats
from typing import Dict, List
from pprint import pprint as pp
from collections import defaultdict


class StatsPrinter:
    def __init__(self, chat_stats: ChatStats) -> None:
        self.chat_stats = chat_stats

    def print_stats(self):
        self.word_counts()
        self.sender_word_count()
        self.sender_message_count()
        self.calculate_words_per_message()

    def output(self, title: str, contents: any): 
        print(title)
        pp(contents)
        print()

    def word_counts(self):
        ordered_words = self.chat_stats.words.most_common()
        with open("results/most_common_words.txt", "w") as fp:
            for word, frequency in ordered_words:
                fp.write(f"{word}: {frequency}\n")

    def sender_word_count(self) -> None:
        with open("results/sender_word_count.txt", "w") as fp:
            for sender, count in self.chat_stats.sender_word_count.items():
                fp.write(f"{sender}: {count}\n")

    def sender_message_count(self):
        with open("results/sender_message_count.txt", "w") as fp:
            for sender, count in self.chat_stats.sender_message_count.items():
                fp.write(f"{sender}: {count}\n")

    def calculate_words_per_message(self): 
        with open("results/words_per_message", "w") as fp:
            senders = self.chat_stats.sender_message_count.keys()
            for sender in senders:
                count = self.chat_stats.sender_word_count[sender] / self.chat_stats.sender_message_count[sender]
                fp.write(f"{sender}: {count}\n")
