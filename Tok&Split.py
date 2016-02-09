# -*- coding: utf-8 -*-

import codecs
import re

f = codecs.open('test-big.txt', 'r', 'utf-8')
text = f.read()

arr = []

d = codecs.open('abbr.txt', 'r', 'utf-8')
for line in d:
    line = line.strip()
    arr.append(line)

# normalization

text = re.sub(u' +', ' ', text) #больше одного пробела
text = re.sub(u'([?!])([A-ZА-ЯЁ])', '\\1 \\2', text) # отсутствие пробела перед новым предложением
text = re.sub(u'([“„«\(]) (.+?)', '\\1\\2', text)  #пробел после кавычки
text = re.sub(u'(.+?) ([.,?!;:”„»\)])', '\\1\\2', text)  #пробел перед кавычки
text = re.sub(u'(.+?)-\r\n(.+?)', '\\1\\2', text) #ереносы с дефисом
text = re.sub(u'([.!?]){3,}', '\\1\\1\\1', text)
text = re.sub(u' *— *', u' — ', text) #тире
text = re.sub(u' *- *', '-', text) #дефис
text = re.sub(u'\ufeff', '', text)
text = re.sub(u'(\.){2,}', u' … ', text)
text = re.sub(u' +', ' ', text) #больше одного пробела


# tokenizer

email = re.compile(u'(?:[a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(?:\.[a-z0-9_-]+)*\.[a-z]{2,6}') #email
url = re.compile(u'(?:(?:https?|ftp)\:\/\/)?(?:[a-z0-9]{1})(?:(?:\.[a-z0-9-])|(?:[a-z0-9-]))*\.(?:[a-z]{2,6})(?:\/?)') #url
phone = re.compile(u'\+\d{2}\(?:\d{3}\)\d{3}-\d{2}-\d{2}') #phone
date = re.compile(u'(?:[1-9]|0[1-9]|[1-2]\d|3[01])[\.\/](?:[1-9]|0[1-9]|1[0-2])[\.\/](?:[1-2]\d{3})') #date
time = re.compile(u'[0-9]?[0-9]:[0-9][0-9]') #time
abbr = re.compile(u'(?:[A-ZА-ЯЁ]\.){3,10}') #abbreviation
numb = re.compile(u'[0-9]+[-., ][0-9]+') #float&intervals
hyph = re.compile(u'[A-Za-zА-ЯЁа-яё]+?(?:-[A-Za-zА-ЯЁа-яё]+)+') #hyphen
brack = re.compile(u'[„\"\'“«][A-Za-zА-ЯЁа-яё]+?[“\"\'”»]') #brackets
name = re.compile(u'(?:[A-ZА-ЯЁ]\. *)?[A-ZА-ЯЁ]\. *[A-ZА-ЯЁ][a-zа-яё]+') #name
value = re.compile(u'\$[0-9]+[,.]?[0-9]*') #dollars
percent = re.compile(u'[0-9]+?[-,.]?[0-9]+%') #percentage
month = re.compile(u'[0123]?[0-9] ?(?:янв|февр|мар|июн|июл|авг|сент|окт|нояб|дек)[а-яё]+') #month

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

abbrs = abbr.findall(text) #abbreviation
text = abbr.sub('$$$ABBREV$$$', text) #abbreviation

names = name.findall(text) #name
text = name.sub('$$$NAME$$$', text) #name

values = value.findall(text) #dollars
text = value.sub('$$$VALUE$$$', text)

percents = percent.findall(text) #percentage
text = percent.sub('$$$PERCENTAGE$$$', text)

numbs = numb.findall(text) #float
text = numb.sub('$$$FLOATNUMBER$$$', text) #float

hyphs = hyph.findall(text) #hyphen
text = hyph.sub('$$$HYPHENWORDS$$$', text) #hyphen

bracks = brack.findall(text) #brackets
text = brack.sub('$$$BRACKETS$$$', text) #brackets

months = month.findall(text)
text = month.sub('$$$MONTH$$$', text)


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


text_for_tok = re.sub(u'([^ ]+?)([-,.!?;:\'»>\"@#%&\*\)=\+\\\/`}\]])', '\\1 \\2', text_short_new) # уязвим для $
text_for_tok = re.sub(u'([-,.!?;:\'<«\"@#%&\*\(=\+\\\/`{\[])([^ ]+?)', '\\1 \\2', text_for_tok)
text_for_tok = re.sub(u'([>\"\)}\]])([-,.!?;:\'<\"@#%&\*\(=\+\\\/`{\[])', '\\1 \\2', text_for_tok)


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
val = 0
per = 0
mon = 0

freqs = {}

def freq(x):
    global freqs
    if x in freqs:
        freqs[x] += 1
    else:
        freqs[x] = 1

text_tokenized = text_for_tok.split(' ')
for token in text_tokenized:
    if token == '$$$EMAIL$$$':
        print emails[em]
        freq(emails[em])
        em += 1
    elif token == '$$$URL$$$':
        print urls[ur]
        freq(urls[ur])
        ur += 1
    elif token == '$$$PHONENUMBER$$$':
        print phones[ph]
        freq(phones[ph])
        ph += 1
    elif token == '$$$DATE$$$':
        print dates[dat]
        freq(dates[dat])
        dat += 1
    elif token == '$$$TIME$$$':
        print times[tim]
        freq(times[tim])
        tim += 1
    elif token == '$$$ABBREV$$$':
        print abbrs[ab]
        freq(abbrs[ab])
        ab += 1
    elif token == '$$$FLOATNUMBER$$$':
        print numbs[num]
        freq(numbs[num])
        num += 1
    elif token == '$$$HYPHENWORDS$$$':
        print hyphs[hyp]
        freq(hyphs[hyp])
        hyp += 1
    elif token == '$$$BRACKETS$$$':
        print bracks[br]
        freq(bracks[br])
        br += 1
    elif token == '$$$NAME$$$':
        print names[nam]
        freq(names[nam])
        nam += 1
    elif token == '$$$SHORTENING$$$':
        print shorts[sh]
        freq(shorts[sh])
        sh += 1
    elif token == '$$$VALUE$$$':
        print values[val]
        freq(values[val])
        val += 1
    elif token == '$$$PERCENTAGE$$$':
        print percents[per]
        freq(percents[per])
        per += 1
    elif token == '$$$MONTH$$$':
        print months[mon]
        freq(months[mon])
        mon += 1
    else:
        freq(token.lower())
        print token


# splitter



text_for_split = re.sub(u'([^ .]+?)([-,.…!?;:\'»>\"@#%&\*\)=\+\\\/`}\]])', '\\1 \\2', text_short_new) # уязвим для $
text_for_split = re.sub(u'([-,.…!?;:\'<«\"@#%&\*\(=\+\\\/`{\[])([^ .]+?)', '\\1 \\2', text_for_split)
text_for_split = re.sub(u'([>\"\)}\]])([-,.…!?;:\'<\"@#%&\*\(=\+\\\/`{\[])', '\\1 \\2', text_for_split)

text_split = re.sub(u'((?:\.|[?!])+) ([-A-ZА-ЯЁ])', '\\1 <%%%> \\2', text_for_split) #несколько идущих подряд терминальных знаков
text_split = re.sub(u'(…) ([-A-ZА-ЯЁ])', '\\1 <%%%> \\2', text_split) #многоточие и большая буква
text_split = re.sub(u'([!?])\s?([a-zа-яё])', '\\1 <%%%> \\2', text_split) #новое предложение не с заглавной буквы
text_split = re.sub(u'\r\n', '<%%%>', text_split)
text_split = re.sub(u'(\$\$\$ABBREV\$\$\$) ([А-ЯЁA-Z])', '\\1 <%%%> \\2', text_split)
text_split = re.sub(u'(\$\$\$SHORTENING\$\$\$) ([А-ЯЁA-Z])', '\\1 <%%%> \\2', text_split)

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
val = 0
per = 0
mon = 0

new_text = ''

text_tokenized = text_split.split(' ')
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
    elif token == '$$$VALUE$$$':
        new_text += values[val]
        val += 1
    elif token == '$$$PERCENTAGE$$$':
        new_text += percents[per]
        per += 1
    elif token == '$$$MONTH$$$':
        new_text += months[mon]
        mon += 1
    else:
        new_text += token
    new_text += ' '



new_text = re.sub(u' +', ' ', new_text) #больше одного пробела
new_text = re.sub(u'([?!…])([A-ZА-ЯЁ])', '\\1 \\2', new_text) # отсутствие пробела перед новым предложением
new_text = re.sub(u'([“„«\(]) ([A-Za-zА-ЯЁа-яё]+?)', '\\1\\2', new_text)  #пробел после кавычки
new_text = re.sub(u'(.+?) ([.,…?!;:”„»\)])', '\\1\\2', new_text)  #пробел перед кавычки
new_text = re.sub(u' *— *', u' — ', new_text) #тире
new_text = re.sub(u' *- *', '-', new_text) #дефис

# double
new_text = re.sub(u'([“„«\(]) ([A-Za-zА-ЯЁа-яё]+?)', '\\1\\2', new_text)  #пробел после кавычки
new_text = re.sub(u'(.+?) ([.,…?!;:”„»\)])', '\\1\\2', new_text)  #пробел перед кавычки


text_splitted = new_text.split('<%%%>')
for el in text_splitted:
    print el

for i in freqs:
    print i, freqs[i]
