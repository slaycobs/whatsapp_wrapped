from collections import Counter, defaultdict
from typing import Dict, List

class ChatStats:
    def __init__(self) -> None:
        self.names = set()
        self.words = Counter()
        self.sender_word_count = defaultdict(int)
        self.sender_message_count = defaultdict(int)
        self.sender_media_count = defaultdict(int)
        self.wordsender_count = defaultdict(int)

    def add(self, entry: Dict) -> None: 
        d, t, sender, message = entry["date"], entry["time"], entry["sender"], entry["message"]
        words = message.split()
        self.words.update(words)
        self.sender_word_count[sender] += len(words)
        self.sender_message_count[sender] += 1
        if message == "media omitted":
            self.sender_media_count[sender] += 1
        for word in words:
            self.wordsender_count[sender + word] += 1

    def clean(self):
        self.sender_message_count["flower"] += self.sender_message_count["+61 424 993 883"] 
        del self.sender_message_count["+61 424 993 883"]
        del self.sender_message_count["childless alana started a cal"]
        del self.sender_message_count["flower started a cal"]
        del self.sender_message_count["flower started a video cal"]
        self.sender_word_count["flower"] += self.sender_word_count["+61 424 993 883"] 
        del self.sender_word_count["+61 424 993 883"]
        del self.sender_word_count["childless alana started a cal"]
        del self.sender_word_count["flower started a cal"]
        del self.sender_word_count["flower started a video cal"]
        self.sender_media_count["flower"] += self.sender_media_count["+61 424 993 883"] 
        del self.sender_media_count["+61 424 993 883"]
        
