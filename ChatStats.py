from collections import Counter, defaultdict
from typing import Dict, List
from emoji import UNICODE_EMOJI

class ChatStats:
    def __init__(self) -> None:
        self.names = set()
        self.words = Counter()
        self.sender_word_count = defaultdict(int)
        self.sender_message_count = defaultdict(int)
        self.sender_media_count = defaultdict(int)
        self.wordsender_count = defaultdict(int)
        self.sender_url_count = defaultdict(int)
        self.emoji_count = defaultdict(int)

    def add(self, entry: Dict) -> None: 
        d, sender, message = entry["date"], entry["sender"], entry["message"]
        words = message.split()
        # replace people tagging phone numbers or nicknames with their names
        for i, word in enumerate(words):
            if word == "61424994881":
                words[i] = "lani"
            elif word == "alana":
                words[i] = "lani"
            elif word == "61426192626":
                words[i] = "sam"
            elif word == "wu":
                words[i] = "sam"
            elif word == "wuness":
                words[i] = "sam"
            elif word == "sambo":
                words[i] = "sam"
            elif word == "61411577990":
                words[i] = "dad"
            elif word == "jj":
                words[i] = "dad"
            elif word == "jeremy":
                words[i] = "dad"
            elif word == "61428567518":
                words[i] = "ben"
            elif word == "benno":
                words[i] = "ben"
            elif word == "bennas":
                words[i] = "ben"
            elif word == "benas":
                words[i] = "ben"
            elif word == "benassy":
                words[i] = "ben"
            elif word == "61416844044":
                words[i] = "mum"
            elif word == "alison":
                words[i] = "mum"
            elif word == "ali":
                words[i] = "mum"

        self.words.update(words)
        self.sender_word_count[sender] += len(words)
        self.sender_message_count[sender] += 1
        if "omitted" in message:
            self.sender_media_count[sender] += 1
        for word in words:
            self.wordsender_count[sender + ":" + word] += 1

        if "www" in message or "http" in message:
            self.sender_url_count[sender] += 1

        for word in words:
            for letter in word:
                if letter in UNICODE_EMOJI:
                    self.emoji_count[sender] += 1


    def clean(self):
        pass
        # self.sender_message_count["flower"] += self.sender_message_count["+61 424 993 883"] 
        # del self.sender_message_count["+61 424 993 883"]
        # # del self.sender_message_count["childless alana started a cal"]
        # # del self.sender_message_count["flower started a cal"]
        # # del self.sender_message_count["flower started a video cal"]
        # self.sender_word_count["flower"] += self.sender_word_count["+61 424 993 883"] 
        # del self.sender_word_count["+61 424 993 883"]
        # # del self.sender_word_count["childless alana started a cal"]
        # # del self.sender_word_count["flower started a cal"]
        # # del self.sender_word_count["flower started a video cal"]
        # self.sender_media_count["flower"] += self.sender_media_count["+61 424 993 883"] 
        # del self.sender_media_count["+61 424 993 883"]
        
