# -*- coding: utf-8 -*-

import codecs
import re

f = codecs.open('sentences.txt', 'r', 'utf-8')
text = f.read()

arr = []

d = codecs.open('abbr.txt', 'r', 'utf-8')
for line in d:
    line = line.strip()
    arr.append(line)

# normalization

text = re.sub(' +', ' ', text) #больше одного пробела
text = re.sub('([.?!])([A-ZА-ЯЁ])', '\\1 \\2', text) # отсутствие пробела перед новым предложением
text = re.sub('([“„«\(]) ([A-Za-zА-ЯЁа-яё]+?)', '\\1\\2', text)  #пробел после кавычки
text = re.sub('([A-Za-zА-ЯЁа-яё]+?) ([.,?!;:”„»\)])', '\\1\\2', text)  #пробел перед кавычки
text = re.sub(' *— *', ' — ', text) #тире
text = re.sub(' *- *', '-', text) #дефис


# tokenizer

email = re.compile(u'(?:[a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(?:\.[a-z0-9_-]+)*\.[a-z]{2,6}') #email
url = re.compile(u'(?:(?:https?|ftp)\:\/\/)?(?:[a-z0-9]{1})(?:(?:\.[a-z0-9-])|(?:[a-z0-9-]))*\.(?:[a-z]{2,6})(?:\/?)') #url
phone = re.compile(u'\+\d{2}\(?:\d{3}\)\d{3}-\d{2}-\d{2}') #phone
date = re.compile(u'(?:[1-9]|0[1-9]|[1-2]\d|3[01])[\.\/](?:[1-9]|0[1-9]|1[0-2])[\.\/](?:[1-2]\d{3})') #date
time = re.compile(u'[0-9]?[0-9]:[0-9][0-9]') #time
abbr = re.compile(u'((?:[A-ZА-ЯЁ]\.)+?) ') #abbreviation
numb = re.compile(u'[0-9]+?[-.,][0-9]+?') #float
hyph = re.compile(u'[A-Za-zА-ЯЁа-яё]+?(?:-[A-Za-zА-ЯЁа-яё]+?)+') #hyphen
brack = re.compile(u'[„\"\'“«][A-Za-zА-ЯЁа-яё]+?[“\"\'”»]') #brackets
name = re.compile(u'(?:[A-ZА-ЯЁ]\. *)?[A-ZА-ЯЁ]\. *[A-ZА-ЯЁ][a-zа-яё]+') #name

emails = email.findall(text) #email
text = email.sub('$$$EMAIL$$$', text) #email

urls = url.findall(text) #url
text = url.sub('$$$URL$$$', text) #url

phones = phone.findall(text) #phone
text = phone.sub('$$$PHONENUMBER$$$', text) #phone

dates = date.findall(text) #date
text = date.sub('$$$DATE$$$', text) #date

times = time.findall(text) #time
text = time.sub('$$$TIME$$$', text) #time

names = name.findall(text) #name
text = name.sub('$$$NAME$$$', text) #name

abbrs = abbr.findall(text) #abbreviation
text = abbr.sub('$$$ABBREV$$$', text) #abbreviation

numbs = numb.findall(text) #float
text = numb.sub('$$$FLOATNUMBER$$$', text) #float

hyphs = hyph.findall(text) #hyphen
text = hyph.sub('$$$HYPHENWORDS$$$', text) #hyphen

bracks = brack.findall(text) #brackets
text = brack.sub('$$$BRACKETS$$$', text) #brackets


text_short_new = ''
shorts = []
text_short = text.split()
for el in text_short:
    if el in arr:
        shorts.append(el)
        text_short_new += '$$$SHORTENING$$$'
    else:
        text_short_new += el
    text_short_new += ' '       


text_for_tok = re.sub(u'([A-Za-zА-ЯЁа-яё$])([-,.!?;:\'<>\"@#%&\*\)\(=\+\\\/`}{\]\[])', '\\1 \\2', text_short_new) # уязвим для $


em = 0
ur = 0
ph = 0
dat = 0
tim = 0
ab = 0
num = 0
hyp = 0
br = 0
nam = 0
sh = 0

text_tokenized = text_for_tok.split(' ')
for token in text_tokenized:
    if token == '$$$EMAIL$$$':
        print emails[em]
        em += 1
    elif token == '$$$URL$$$':
        print urls[ur]
        ur += 1
    elif token == '$$$PHONENUMBER$$$':
        print phones[ph]
        ph += 1
    elif token == '$$$DATE$$$':
        print dates[dat]
        dat += 1
    elif token == '$$$TIME$$$':
        print times[tim]
        tim += 1
    elif token == '$$$ABBREV$$$':
        print abbrs[ab]
        ab += 1
    elif token == '$$$FLOATNUMBER$$$':
        print numbs[num]
        num += 1
    elif token == '$$$HYPHENWORDS$$$':
        print hyphens[hyp]
        hyp += 1
    elif token == '$$$BRACKETS$$$':
        print bracks[br]
        br += 1
    elif token == '$$$NAME$$$':
        print names[nam]
        nam += 1
    elif token == '$$$SHORTENING$$$':
        print shorts[sh]
        sh += 1
    else:
        print token


# splitter

text_split = re.sub(u'([a-zа-яё][.?!]+) ([A-ZА-ЯЁ])', '\\1 <%%%> \\2', text_short_new) #несколько идущих подряд терминальных знаков
text_split = re.sub(u'(?:…|\.\.\.) ([A-ZА-ЯЁ])', '\\1 <%%%> \\2', text_split) #многоточие и большая буква
text_split = re.sub(u'([.!?])\s?([a-zа-яё])', '\\1 <%%%> \\2', text_split) #новое предложение не с заглавной буквы

text_for_split = re.sub(u'([A-Za-zА-ЯЁа-яё$])([-,.!?;:\'<>\"@#%&\*\)\(=\+\\\/`}{\]\[])', '\\1 \\2', text_split)

em = 0
ur = 0
ph = 0
dat = 0
tim = 0
ab = 0
num = 0
hyp = 0
br = 0
nam = 0
sh = 0

new_text = ''

text_tokenized = text_for_split.split(' ')
for token in text_tokenized:
    if token == '$$$EMAIL$$$':
        new_text += emails[em]
        em += 1
    elif token == '$$$URL$$$':
        new_text += urls[ur]
        ur += 1
    elif token == '$$$PHONENUMBER$$$':
        new_text += phones[ph]
        ph += 1
    elif token == '$$$DATE$$$':
        new_text += dates[dat]
        dat += 1
    elif token == '$$$TIME$$$':
        new_text += times[tim]
        tim += 1
    elif token == '$$$ABBREV$$$':
        new_text += abbrs[ab]
        ab += 1
    elif token == '$$$FLOATNUMBER$$$':
        new_text += numbs[num]
        num += 1
    elif token == '$$$HYPHENWORDS$$$':
        new_text += hyphs[hyp]
        hyp += 1
    elif token == '$$$BRACKETS$$$':
        new_text += bracks[br]
        br += 1
    elif token == '$$$NAME$$$':
        new_text += names[nam]
        nam += 1
    elif token == '$$$SHORTENING$$$':
        new_text += shorts[sh]
        sh += 1
    else:
        new_text += token
    new_text += ' '


new_text = re.sub(u' +', ' ', new_text) #больше одного пробела
new_text = re.sub(u'([.?!])([A-ZА-ЯЁ])', '\\1 \\2', new_text) # отсутствие пробела перед новым предложением
new_text = re.sub(u'([“„«\(]) ([A-Za-zА-ЯЁа-яё]+?)', '\\1\\2', new_text)  #пробел после кавычки
new_text = re.sub(u'([A-Za-zА-ЯЁа-яё]+?) ([.,?!;:”„»\)])', '\\1\\2', new_text)  #пробел перед кавычки
new_text = re.sub(u' *— *', ' — ', new_text) #тире
new_text = re.sub(u' *- *', '-', new_text) #дефис


text_splitted = new_text.split('<%%%>')
for el in text_splitted:
    print el


