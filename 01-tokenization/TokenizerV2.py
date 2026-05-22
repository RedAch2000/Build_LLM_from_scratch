import re


class SimpleTokenizerV2:
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
        all_words.extend(["<|endoftext|>", "<|unk|>"])
        # vocabulary
        vocab = {token: integer for integer, token in enumerate(all_words)}
        return vocab

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text
    

tokenizer = SimpleTokenizerV2("./the-verdict.txt")

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."

text = " <|endoftext|> ".join((text1, text2))

ids = tokenizer.encode(text)
print("Encoded IDs:", ids)
print("Decoded text:", tokenizer.decode(ids))