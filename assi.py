import nltk
from collections import Counter
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

after_clean = set(stopwords.words('english'))
with open("/pc/data/random_paragraphs.txt", "r") as file:
    dataset = file.read()

tokenize_words = word_tokenize(dataset)

tokenize_words_without_after_cleaning = []

for word in tokenize_words:
    if word not in after_clean:
        tokenize_words_without_after_cleaning.append(word)
print("Stop words :" , set(tokenize_words)-set(tokenize_words_without_after_cleaning))


new = Counter(tokenize_words_without_after_cleaning)
for word , count in new.items():
    print(f"{word} ,{count}")
