import re


class SimpleTokenizer:
    """A simple tokenizer that encodes text into a list of integers and decodes a list of integers back into text."""
    
    def __init__(self, file_name):
        self.vocab = self.vocab(file_name)
        self.str_to_int = self.vocab
        self.int_to_str = {integer:token for token, integer in self.vocab.items()}

    def vocab(self, file_name):

        # read the file
        with open(file_name, "r", encoding="utf-8") as f:
            raw_text = f.read()
        #splitting the text into tokens
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        # get all word without repetition
        all_words = sorted(set(preprocessed))
        # vocabulary
        vocab = {token: integer for integer, token in enumerate(all_words)}
        return vocab

    def encode(self, text):
        # split the text into tokens
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        # remove empty tokens and strip whitespace
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        # get the id for each token
        ids = [self.str_to_int[token] for token in preprocessed]
        return ids

    def decode(self, ids):
        # get the tokens
        tokens = [self.int_to_str[id] for id in ids]
        # get the text 
        text = " ".join(tokens)
        return text
    

tokenizer = SimpleTokenizer("./the-verdict.txt")

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print("Encoded IDs:", ids)
print("Decoded text:", tokenizer.decode(ids))