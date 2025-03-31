from string import whitespace
from string import punctuation

from re import sub

punctuation: str = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
table_punctuation: str = str.maketrans('','',punctuation)

def clean_txt(txt: str):
    # Remove punctuation
    no_punctuation: str = txt.translate(table_punctuation)
    # Remove digits using regex
    no_digits: str = sub(r'\d+', '', no_punctuation)
    return no_digits

if __name__ == "__main__":
    print(clean_txt("ashish12323@#:$"))