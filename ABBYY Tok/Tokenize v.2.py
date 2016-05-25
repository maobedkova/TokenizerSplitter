# -*- coding: utf-8 -*-

import codecs
import re

# ask for file name

file = raw_input('File name, please ').decode('utf-8')

# dictionaries

# create the arr with abbreviations

abbrevs = []
abbrev = codecs.open('abbrev.ru.txt', 'r', 'utf-8')
for line in abbrev:
    line = line.strip()
    abbrevs.append(line)
abbrev.close()

# create the arr with words from closed class

closed_class = []
cl_class = codecs.open('new_closed_class.txt', 'r', 'utf-8')
for line in cl_class:
    line = line.strip()
    closed_class.append(line)
cl_class.close()

# add defis abbreviations to arr with words from closed class

defis_abbr = codecs.open('defis_abbreviations.ru.txt', 'r', 'utf-8')
for line in defis_abbr:
    line = line.strip()
    closed_class.append(line)
defis_abbr.close()

# create the arr with toponim parts

topon_parts = []
t_parts = codecs.open('topon_parts.txt', 'r', 'utf-8')
for line in t_parts:
    line = line.strip()
    topon_parts.append(line)
t_parts.close()

# open a file

text = ''
f = codecs.open(file, 'r', 'utf-8-sig')
text = f.read()
f.close()

# reg exp compilation

url_1 = re.compile(u'(?:https?|ftp|www\\.)[a-z0-9/\\._:]+') ### here go urls of common type: file, https, etc
url_2 = re.compile(u'((?:[a-zа-я]+\\.)+(?:biz|com|edu|gov|info|int|mil|name|net|org|pro|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|sv|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|sv|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|za|zm|zw|рф|ру))') # tokens that resemble to url
email = re.compile(u'([_a-z0-9-]+(?:\\.[_a-z0-9-]+)*@(?:[a-zа-я]+\\.)+(?:biz|com|edu|gov|info|int|mil|name|net|org|pro|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|sv|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|sv|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|za|zm|zw|рф|ру))') # tokens that resemble to e-mail
smile_1 = re.compile(u'([:=]\-?[)(]+)') ### tokens that resemble to smile
smile_2 = re.compile(u'[ツ‿♡ノヽ・∀*ω)(_/¯^OoОо0\\\]{3,}') ###
number = re.compile(u'(?:^| )((?:[+-]?\d+(?:[.,]\d+(?:e-?\d+)?)?)|(?:\\\[0-3]{1,2})|(?:0x[0-9a-fA-F]{1,16}))') # natural & floating point numbers | octets | hex digits
acronym = re.compile(u'(?:[A-ZА-ЯЁ]\\. ?){1,10}[A-ZА-ЯЁ]\\.') ### tokens that resemble to acronym
rep_punct = re.compile(u'(?:[?!]{2,}|\\.{3})') ### repeated punctuation
hashtag = re.compile(u'\#[^-“”«»,.?!:;)(\\]\\[`\"„†‡‹}{\'%…‰‘’•–—›\\\|\r\n ]*') ### comments
sgml = re.compile(u'^<.*>$') ### sgml tags
defis = re.compile(u'[^-“”«»,.?!:;)(\\]\\[`\"„†‡‹}{\'%…‰‘’•–—›\\\|\r\n ]+?(?:-[^-“”«»,.?!:;)(\\]\\[`\"„†‡‹}{\'%…‰‘’•–—›\\\|\r\n ]+)+') #hyphen
short = re.compile(u'[^-“”«»,.?!:;)(\\]\\[`\"„†‡‹}{\'%…‰‘’•–—›\\\|\r\n ]+?\\.')
date = re.compile(u'(?:[1-9][0-9]{3}|(?:0[1-9]|[12][0-9]|3[01]))[\./](?:[01][0-9])[\\./](?:(?:0[1-9]|[12][0-9]|3[01])|[1-9][0-9]{3})[\.\/]?')

# change

smiles_type1 = smile_1.findall(text)
text = smile_1.sub(' SMILETOKEN_TYPE_109484712 ', text)

smiles_type2 = smile_2.findall(text)
text = smile_2.sub(' SMILETOKEN_TYPE_209484712 ', text)

urls_type1 = url_1.findall(text)
text = url_1.sub(' URLTOKEN_TYPE_109484712 ', text)

urls_type2 = url_2.findall(text)
text = url_2.sub(' URLTOKEN_TYPE_209484712 ', text)

emails = email.findall(text)
text = email.sub(' EMAILTOKEN_TYPE_109484712 ', text)

defises = defis.findall(text)
text = defis.sub(' DEFISTOKEN_TYPE_109484712 ', text)

dates = date.findall(text)
text = date.sub(' DATETOKEN_TYPE_109484712 ', text)

numbers = number.findall(text)
text = number.sub(' NUMBERTOKEN_TYPE_109484712 ', text)

acronyms = acronym.findall(text)
text = acronym.sub(' ACRONYMTOKEN_TYPE_109484712 ', text)

rep_puncts = rep_punct.findall(text)
text = rep_punct.sub(' REPPUNCTTOKEN_TYPE_109484712 ', text)

hashtags = hashtag.findall(text)
text = hashtag.sub(' HASHTAGTOKEN_TYPE_109484712 ', text)

sgmls = sgml.findall(text)
text = sgml.sub(' SGMLTAGTOKEN_TYPE_109484712 ', text)

shorts = short.findall(text)
text = short.sub(' SHORTENINGTOKEN_TYPE_109484712 ', text)

# normalization

text = re.sub('^[\t\r\n]+', '', text) # delete tabulation and endings in the beginning of the string
text = re.sub('[\t\r\n]+$', '', text) # delete tabulation and endings in the end of the string
text = re.sub(u' ', ' ', text) #replace non-break spaces
text = re.sub('[\n\t]', ' ', text) # replace newlines and tab characters with blanks
text = re.sub(' ', ' ', text)
text = re.sub(u'([-“”«»,.?!:;)(\\]\\[`"„†‡‹}{\'%…‰‘’•–—›\\\|])', ' \\1 ', text)
text = re.sub(u'…', ' ... ', text)
text = re.sub(' +', ' ', text)

# return

em = 0
url1 = 0
url2 = 0
sm1 = 0
sm2 = 0
num = 0
acr = 0
rp = 0
hsh = 0
sgm = 0
df = 0
sh = 0
dt = 0

w = codecs.open('output.txt', 'w', 'utf-8')

text_tokenized = text.split()
for token in text_tokenized:
    rest = ''
    if token == 'EMAILTOKEN_TYPE_109484712':
        print emails[em]
        w.write(emails[em] + '\n')
        em += 1
    elif token == 'URLTOKEN_TYPE_109484712':
        print urls_type1[url1]
        w.write(urls_type1[url1] + '\n')
        url1 += 1
    elif token == 'URLTOKEN_TYPE_209484712':
        print urls_type2[url2]
        w.write(urls_type2[url2] + '\n')
        url2 += 1
    elif token == 'SMILETOKEN_TYPE_109484712':
        print smiles_type1[sm1]
        w.write(smiles_type1[sm1] + '\n')
        sm1 += 1
    elif token == 'SMILETOKEN_TYPE_209484712':
        print smiles_type2[sm2]
        w.write(smiles_type2[sm2] + '\n')
        sm2 += 1
    elif token == 'NUMBERTOKEN_TYPE_109484712':
        print numbers[num]
        w.write(numbers[num] + '\n')
        num += 1
    elif token == 'ACRONYMTOKEN_TYPE_109484712':
        print acronyms[acr]
        w.write(acronyms[acr] + '\n')
        acr += 1
    elif token == 'REPPUNCTTOKEN_TYPE_109484712':
        print rep_puncts[rp]
        w.write(rep_puncts[rp] + '\n')
        rp += 1
    elif token == 'HASHTAGTOKEN_TYPE_109484712':
        print hashtags[hsh]
        w.write(hashtags[hsh] + '\n')
        hsh += 1
    elif token == 'SGMLTAGTOKEN_TYPE_109484712':
        print sgmls[sgm]
        w.write(sgmls[sgm] + '\n')
        sgm += 1
    elif token == 'DATETOKEN_TYPE_109484712':
        print dates[dt]
        w.write(dates[dt] + '\n')
        dt += 1
    elif token == 'SHORTENINGTOKEN_TYPE_109484712':
        if shorts[sh] in abbrevs:
            print shorts[sh]
            w.write(shorts[sh] + '\n')
        else:
            print shorts[sh][:-1], '\n.'
            w.write(shorts[sh][:-1] + '\n.\n')
        sh += 1
    elif token == 'DEFISTOKEN_TYPE_109484712':
        def_parts = defises[df].split('-')
        if re.search(u'^(то|де|ка|таки)$', def_parts[-1].lower()):
            if defises[df] not in closed_class:
                defises[df] = '-'.join(def_parts[:-1]) # token
                rest = '-\n' + def_parts[-1] # cut particle
        def_parts = defises[df].split('-')
        def check_func(word, closed_class = closed_class, topon_parts = topon_parts):
            spl_word = word.split('-')
            if len(spl_word) == 1:
                return word, 0
            elif word.lower() in closed_class:
                return word, 0 # found in file (whole)
            elif spl_word[0].lower() + '-' in closed_class:
                return word, 0 # found in file (part)
            elif '-' + spl_word[1].lower() in closed_class:
                return word, 0 # found in file (part)
            elif '-' + spl_word[1].lower() + '-' in topon_parts:
                return word, 0 # found in toponim parts
            elif re.search(u'[А-ЯЁ][а-яё]+', spl_word[0]) and re.search(u'[А-ЯЁ][а-яё]+', spl_word[-1]): # last\first part has the first letter capital and other lower
                return word, 0
            return ['<o composite="true">\n', '\n-\n'.join(spl_word), '\n</o>'], 1

        if len(def_parts) <= 3:
            check, comp = check_func(defises[df])
            print ''.join(check)
            w.write(''.join(check) + '\n')
        elif len(def_parts) > 3:
            part_1 = def_parts[:len(def_parts)/2]
            part_2 = def_parts[len(def_parts)/2:]
            check_1, comp_1 = check_func('-'.join(part_1))
            check_2, comp_2 = check_func('-'.join(part_2))
            if comp_1 == 1:
                check_1.pop(0)
                check_1.pop(-1)
                check_1 = ''.join(check_1)
            if comp_2 == 1:
                check_2.pop(0)
                check_2.pop(-1)
                check_2 = ''.join(check_2)
            print '<o composite="true">\n', check_1, '\n-\n', check_2, '\n</o>'
            w.write('<o composite="true">\n' + check_1 + '\n-\n' + check_2 + '\n</o>\n')
        if rest:
            print rest
            w.write(rest + '\n')
        df += 1
    else:
        print token
        w.write(token + '\n')
w.close()