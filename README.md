# Tokenizer and Splitter for Russian

In this repository you can find tokenizer and splitter that was made as a HSE course project and tokenizer that is used for Geekrya project by ABBYY. The project consists of tokenizer and splitter programs for Russian. It has built-in normalization of a text.

## How to use

We advise to use HSE Tok&Split for splitting a text into sentences and ABBYY Tok for tokenization of a text.

### Splitting

Use **Tok&Split.py** from HSE Tok&Split. Change the name 'test.txt' in 'f = codecs.open('test.txt', 'r', 'utf-8-sig')' in the fifth line to the name of your file and put the file in the same directory where Tok&Split.py is.

### Tokenization

Use **tokenize_v2.py** from ABBYY Tok.

```
python2 tokenize_v2.py <text name.txt>
```

