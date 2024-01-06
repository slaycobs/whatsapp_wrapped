from ChatStats import ChatStats
from typing import Dict, List
from pprint import pprint as pp
from collections import defaultdict, OrderedDict


class StatsPrinter:
    def __init__(self, chat_stats: ChatStats) -> None:
        self.chat_stats = chat_stats
        self.senders = chat_stats.sender_message_count.keys()
        print("initialising stats with senders list: ", self.senders)

    def print_stats(self):
        self.word_counts()
        self.calculate_words_per_message()
        self.write_dict_to_file(self.chat_stats.sender_word_count, "results/sender_word_count.txt")
        self.write_dict_to_file(self.chat_stats.sender_message_count, "results/sender_message_count.txt")
        self.write_dict_to_file(self.chat_stats.sender_media_count, "results/sender_media_count.txt")
        self.write_dict_to_file(self.chat_stats.sender_url_count, "results/sender_url_count.txt")
        self.write_dict_to_file(self.chat_stats.emoji_count, "results/emoji_count.txt")
        self.specific_word_stats()
        self.name_counts()
        self.word_usage_per_sender()

    def output(self, title: str, contents: any): 
        print(title)
        pp(contents)
        print()

    def word_counts(self):
        ordered_words = self.chat_stats.words.most_common()
        with open("results/most_common_words.txt", "w") as fp:
            for word, frequency in ordered_words:
                fp.write(f"{word}: {frequency}\n")

    def sender_message_count(self):
        with open("results/sender_message_count.txt", "w") as fp:
            for sender, count in self.chat_stats.sender_message_count.items():
                fp.write(f"{sender}: {count}\n")

    def calculate_words_per_message(self): 
        with open("results/words_per_message", "w") as fp:
            for sender in self.senders:
                count = self.chat_stats.sender_word_count[sender] / self.chat_stats.sender_message_count[sender]
                fp.write(f"{sender}: {count}\n")

    def write_dict_to_file(self, d, file_name):
        with open(file_name, "w") as fp:
            for sender, count in d.items(): 
                fp.write(f"{sender}: {count}\n")
    
    def specific_word_stats(self):
        with open("specific_words.txt", "r") as fp:
            contents = fp.readlines()

        with open("results/specific_word_stats.txt", "w") as fp:
            for word in contents:
                word = word.strip()
                fp.write(f"{word}:\n")
                fp.write(f"Total uses: {self.chat_stats.words[word]}\n")
                for sender in self.senders:
                    word_sender = f"{sender}:{word}"
                    fp.write(f"{sender}: {self.chat_stats.wordsender_count[word_sender]}\n")
                fp.write("\n")

    def word_usage_per_sender(self):
        od = sorted(self.chat_stats.wordsender_count.items(), key=lambda item: item[1])
        # od = OrderedDict(sorted(self.chat_stats.wordsender_count.items()))
        with open("results/word_usage_per_sender.txt", "w") as fp:
            for word_sender, num in od:
                # sender, word = word_sender.split(":")
                fp.write(f"{word_sender}: {num}\n")

    def name_counts(self):
        with open("results/name_counts.txt", "w") as fp:
            fp.write(f"ben: {self.chat_stats.words['ben']}\n")
            fp.write(f"lani: {self.chat_stats.words['lani']}\n")
            fp.write(f"sam: {self.chat_stats.words['sam']}\n")
            fp.write(f"dad: {self.chat_stats.words['dad']}\n")
            fp.write(f"mum: {self.chat_stats.words['mum']}\n")

