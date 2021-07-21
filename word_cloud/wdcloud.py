#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import Counter
from wordcloud import WordCloud
from konlpy.tag import Okt
import nltk

def wordcloud_from_text(input_file, output_file='wordcloud.png'):
    # get text from file
    try:
        with open(input_file, "rb") as f:
            text=f.read().decode('utf8')
    except Exception as e:
        print ('wordcloud_from_text() - %s' %(e))
        return        

    # 예외 처리
    if text == None:
        print ('wordcloud_from_text() text is None')
        return

    # get noun list
    noun_list = get_noun_list(text)

    # 예외 처리 2
    if len(noun_list) < 10:
        print ('wordcloud_from_text() - Too small noun list')
        return

    # Generate a word cloud image
    wc = WordCloud(font_path = './gulim.ttf',
                        background_color = 'white',
                        width=512, height=512,
                        max_font_size=500,
                        max_words=1000)
    wc.generate_from_frequencies(dict(noun_list))
    # Save to png
    wc.to_file(output_file)
    print ('Create WordCloud:', output_file)

#-------------------------------------------------------------------------------------------------------------------
def get_noun_list(text, method=0):    
    # Sentence to token
    if method == 0:
        # 한국어
        noun = tokenizer_konlpy(text)
    else:
        # 영어
        noun = tokenizer_nltk(text)

    # count word
    count = Counter(noun)

    # get most frequent words
    noun_list = count.most_common(3000)
    return noun_list

#-------------------------------------------------------------------------------------------------------------------
def tokenizer_nltk(text):
    # NNP: 단수 고유명사, VB: 동사, VBP: 동사 현재형, TO: to 전치사, NN: 명사(단수형 혹은 집합형), DT: 관형사
    is_noun = lambda pos : (pos[:2] == 'NN' or pos[:2] == 'NNP')
    tokenized = nltk.word_tokenize(text)
    return [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

#-------------------------------------------------------------------------------------------------------------------
def tokenizer_konlpy(text):
    okt = Okt()
    return [word for word in okt.nouns(text) if len(word) >1]

#-------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    wordcloud_from_text (input_file='test.txt')


