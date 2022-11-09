# Rozha's Functions
The full list of Rozha's functions is below. To jump to a specific class, use these links:

* [process](#process)
* [analyze](#analyze)
* [visualize](#visualize)
 
## Process
```
Process.changeDepth(depth)
```
Changes the depth of your spaCy models. 

```
NLTKlanguages()
```
Prints a list of languages passable to NLTK functions.

```
spacyLanguages()
```
Prints a list of languages and their two letter codes passage to spaCy functions.

```
stanzaLanguages()
```
Prints a list of languages and their two letter codes passable to Stanza functions.

```
lowerFile(file)
```
Converts all text in a file to lowercase, removes punctuation, and tokenizes the text into words. Returns a list of the words named ```process.lowercase```.

```
lowerVar(text)
```
Converts all text in a string to lowercase, removes punctuation, and tokenizes the text into words. Returns a list of the words named ```process.lowercase```.

```
wordTokenizeFile(file)
```
Tokenizes a file into words, leaving any punctuation or other characters intact. Returns a list named ```process.words```.

```
sentTokenizeFile(file)
```
Tokenizes a file into sentences, leaving any punctuation or other characters intact. Returns a list named ```process.sentences```.

```
stopwordsFile(file, lang)
```
Removes stopwords from a file using NLTK. Returns a list named ```process.cleaned```.

```
stopwordsVar(text, lang)
```
Removes stopwords from a string using NLTK. Returns a list named ```process.cleaned```.

```
allSentsFile(file, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from a file and tokenizes it into sentences using NLTK. Returns a list of the cleaned sentences called ```process.cleaned```.

```
allSentsVar(text, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from a string and tokenizes it into sentences using NLTK. Returns a list of the cleaned sentences called ```process.cleaned```.

```
allLinesFile(file, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from a file and splits it on newlines using NLTK. Returns a list of the cleaned lines called ```process.cleaned```.

```
allLinesVar(text, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from a string and splits it on newlines using NLTK. Returns a list of the cleaned lines called ```process.cleaned```.

```
allWordsFile(file, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from a file and tokenizes it into words using NLTK. Returns a list of the cleaned words called ```process.cleaned```.

```
allWordsVar(var, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from a string and tokenizes it into words using NLTK. Returns a list of the cleaned words called ```process.cleaned```.

```
allSentsDir(dir, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from all files in a directory and tokenizes them into sentences using NLTK. Returns a list of lists of the cleaned sentences from the files called ```process.cleaned```.

```
allLinesDir(dir, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from all files in a directory and splits them on newlines using NLTK. Returns a list of lists of the cleaned sentences from the files called ```process.cleaned```.

```
allWordsDir(dir, lang)
```
Removes stopwords, alphanumeric characters, and punctuation from all files in a directory and tokenizes them into words using NLTK. Returns a list of lists of the cleaned words from the files called ```process.cleaned```.

```
spacyStopwordsFile(var, lang)
```
Use spaCy to remove stopwords from a file. Returns a list of the words called ```process.spacy_cleaned```.

```
spacyStopwordsVar(var, lang)
```
Use spaCy to remove stopwords from a string. Returns a list of the words called ```process.spacy_cleaned```.
```
spacyLinesFile(file, lang)
```
Use spaCy to split a file on newlines and return the spacy NLP output for each line. Returns a list of the lines called ```process.spacy_lines```.

```

spacyLinesVar(var, lang)
```
Use spaCy to split a string on newlines and return the spacy NLP output for each line. Returns a list of the lines called ```process.spacy_lines```.

```
spacySentsFile(file, lang)
```
Use spaCy to tokenize a file into sentences. Returns a list of the sentences called ```process.spacy_sents```.

```
spacySentsVar(file, lang)
```
Use spaCy to tokenize a file into sentences. Returns a list of the sentences called ```process.spacy_sents```.

```
spacyWordsFile(file, lang)
```
Use spaCy to tokenize a file into words. Returns a list of the words called ```process.spacy_words```.


```
spacyWordsVar(var, lang)
```
Use spaCy to tokenize a string into words. Returns a list of the words called ```process.spacy_words```.

```
stanzaSentsFile(file, lang)
```
Use Stanza to tokenize a file into sentences. Returns a list of the sentences called ```process.stanza_sents```.

```
stanzaSentsVar(var, lang)
```
Use Stanza to tokenize a string into sentences. Returns a list of the sentences called ```process.stanza_sents```.

```
stanzaWordsFile(file, lang)
```
Use Stanza to tokenize a file into words. Returns a list of the words called ```process.stanza_words```.

```
stanzaWordsVar(var, lang)
```
Use Stanza to tokenize a string into words. Returns a list of the words called ```process.stanza_words```.

```
stanzaLinesFile(file, lang)
```
Use Stanza to split a file on newlines and return the Stanza NLP output for each line. Returns a list of the lines called ```process.stanza_lines```.
```
stanzaLinesVar(var, lang)
```
Use Stanza to split a string on newlines and return the Stanza NLP output for each line. Returns a list of the lines called ```process.stanza_lines```.

```
spacyLemmaFile(file, lang)
```
Use spaCy to tokenize a file into sentences and lemmatize them. Returns a list of the lemmatized text called ```process.spacy_lemmas```.

```
spacyLemmaVar(var, lang)
```
Use spaCy to tokenize a string into sentences and lemmatize them. Returns a list of the lemmatized text called ```process.spacy_lemmas```.

```
stanzaLemmaFile(file, lang)
```
Use Stanza to tokenize a file into sentences and lemmatize them. Returns a list of the lemmatized text called ```process.stanza_lemmas```.

```
stanzaLemmaVar(var, lang)
```
Use Stanza to tokenize a string into sentences and lemmatize them. Returns a list of the lemmatized text called ```process.stanza_lemmas```.

```
saveTxt(results, filename)
```
Saves the passed variable "results" to a .txt file with the passed filename. Accepts lists and strings.

```
saveCsv(results, filename)
```
Saved the passed variable "results" to a .csv file with the passed filename. Only accepts a list.

```
saveCsv_multi(filename, *args)
```
Saved the passed variables to a .csv file with the passed filename. Accepts multiple lists.


## Analyze
```
posString(var)
```
Use NLTK to tag the parts of speech in a string. Returns a list of the words and their tags. Returns a list called ```analyze.pos_tags```.

```
posList(var)
```
Use NLTK to tag the parts of speech in the elements of a list. Returns tuples containing the words and POS tags for each list element in a list called ```analyze.pos_tags```.

```
posListSents(var)
```
Use NLTK to word tokenize and tag the parts of speech in the elements of a list. Returns a list of lists, with each list containing the POS tags for its respective words, called ```analyze.pos_tags```.


```
spacyPos(var, lang)
```
Use spaCy to tag the parts of speech in the elements of a list. Returns a list of lists, with each list containing the POS tags for its respective element. Returns a list called ```analyze.spacy_pos_tags```.

```
stanzaPos(var, lang)
```
Use Stanza to tag the parts of speech in the elements of a list. Returns a list of lists, with each list containing the POS tags for its respective element. Returns a list called ```analyze.stanza_pos_tags```.

```
nerTree(var)
```
Use NLTK to create a named entity recognition tree for each element in a passed list. Returns a list called ```analyze.ner_tree```.

```
spacyNer(var, lang)
```
Use spaCy to perform named entity recognition for each element in a passed list. Returns a list of named entities called ```analyze.spacy_ner_tags```.

```
stanzaNer(var, lang)
```
Use spaCy to perform named entity recognition for each element in a passed list. Returns a list of named entities called ```analyze.spacy_ner_tags```.

```
sentimentBlob(var)
```
Perform sentiment analysis on either a list or a string using TextBlob. Returns a list of tuples (the text and its sentiment score) called ```analyze.blob_sentiment```.

```
sentimentBlobFile(file)
```
Perform sentiment analysis on a file using TextBlob. Returns a list of tuples (sentences and their sentiment score) called ```analyze.blob_sentiment```.

```
sentimentBlobTrain(var, training_file, file_format)
```
Train a Naive Bayes sentiment classifier and then apply it to a string or list. The var supplied is the string or list to analyze, the training file is the list of pre-tagged sentences, and the file format specifies the extension of the file. JSON, CSV, and TSV files are accepted for the training data. Outputs a list of tuples with the original text and its sentiment score called ```analyze.blob_sentiment```.

```
sentimentBlobTrainFile(var, training_file, file_format)
```
Train a Naive Bayes sentiment classifier and then apply it to a file. The var supplied is the file to analyze, the training file is the list of pre-tagged sentences, and the file format specifies the extension of the file. Text files are accepted for the file to analyze, and JSON, CSV, and TSV files are accepted for the training data. Outputs a list of tuples with the original text and its sentiment score called ```analyze.blob_sentiment```.

```
sentimentVader(var)
```
Perform sentiment analysis on either a list or a string using Vader. Returns a list of tuples (the text and its sentiment score) called ```analyze.vader_sentiment```.

```
sentimentVaderFile(file)
```
Perform sentiment analysis on a file using Vader. Returns a list of tuples (sentences and their sentiment score) called ```analyze.vader_sentiment```.

```
stanzaSentiment(var, lang)
```
Perform sentiment analysis on either a list or a string using Stanza. Returns a list of tuples (the text and its sentiment score) called ```analyze.stanza_sentiment```.

```
stanzaDependency(var, lang)
```
Create a dependency tree from a list using Stanza. Returns a list of the trees generated called ```analyze.dependency```.

```
stanzaDependencyFile(file, lang)
```
Create a dependency tree from a file using Stanza. Returns a list of the trees generated called ```analyze.dependency```.

## Analyze
```
posString(var)
```
Use NLTK to tag the parts of speech in a string. Returns a list of the words and their tags. Returns a list called ```analyze.pos_tags```.

```
posList(var)
```
Use NLTK to tag the parts of speech in the elements of a list. Returns a list of lists, with each list containing the POS tags for its respective element. Returns a list called ```analyze.pos_tags```.

```
spacyPos(var, lang)
```
Use spaCy to tag the parts of speech in the elements of a list. Returns a list of lists, with each list containing the POS tags for its respective element. Returns a list called ```analyze.spacy_pos_tags```.

```
stanzaPos(var, lang)
```
Use Stanza to tag the parts of speech in the elements of a list. Returns a list of lists, with each list containing the POS tags for its respective element. Returns a list called ```analyze.stanza_pos_tags```.

```
nerTree(var)
```
Use NLTK to create a named entity recognition tree for each element in a passed list. Returns a list called ```analyze.ner_tree```.

```
spacyNer(var, lang)
```
Use spaCy to perform named entity recognition for each element in a passed list. Returns a list of named entities called ```analyze.spacy_ner_tags```.

```
stanzaNer(var, lang)
```
Use spaCy to perform named entity recognition for each element in a passed list. Returns a list of named entities called ```analyze.spacy_ner_tags```.

```
sentimentBlob(var)
```
Perform sentiment analysis on either a list or a string using TextBlob. Returns a list of tuples (the text and its sentiment score) called ```analyze.sentiment```.

```
sentimentBlobFile(file)
```
Perform sentiment analysis on a file using TextBlob. Returns a list of tuples (sentences and their sentiment score) called ```analyze.sentiment```.

```
sentimentVader(var)
```
Perform sentiment analysis on either a list or a string using Vader. Returns a list of tuples (the text and its sentiment score) called ```analyze.vader_sentiment```.

```
sentimentVaderFile(file)
```
Perform sentiment analysis on a file using Vader. Returns a list of tuples (sentences and their sentiment score) called ```analyze.vader_sentiment```.

```
stanzaSentiment(var, lang)
```
Perform sentiment analysis on either a list or a string using Stanza. Returns a list of tuples (the text and its sentiment score) called ```analyze.stanza_sentiment```.

```
stanzaDependency(var, lang)
```
Create a dependency tree from a list using Stanza. Returns a list of the trees generated called ```analyze.dependency```.

```
stanzaDependencyFile(file, lang)
```
Create a dependency tree from a file using Stanza. Returns a list of the trees generated called ```analyze.dependency```.

## Visualize
```
wordcloud(var, filename, w, h)
```
Generates a wordcloud from the passed list with the specified file name (saved as a .png). "W" and "h" designate the width and height of the image.

```
spacyTree(var, lang, save=None)
```
Generates a dependency tree visualization for either a string or the elements in a list. If "save" is passed then the trees are saved as .svg files, and if it isn't then the visualizations are served via displacy.

```
spacyNer(var, lang, save=None)
```
Generates a NER visualization for either a string or the elements in a list. If "save" is passed then the trees are saved as .svg files, and if it isn't then the visualizations are served via displacy.

```
posGraph(var, num_words, h, w, filename)
```
Generates a graph of the parts of speech in a string or list of words. Pass how many words to graph, the height and width of the graph, and your preferred filename. The file is saved as a .png.

```
lexicalDispersion(var, ents, h, w, filename):
```
Create a lexical dispersion plot from a string or list of words. Specify the words to graph ("ents"), the height and width of the graph, and your preferred filename. The file is saved as a .png.

```
wordFreq(var, num_words, h, w, filename)
```
Generates a line graph of word frequencies in a string or list of words. Pass how many words to graph, the height and width of the graph, and your preferred filename. The file is saved as a .png.

```
barFreq(var, num_words, h, w, filename)
```
Generates a bar graph of word frequencies in a string or list of words. Pass how many words to graph, the height and width of the graph, and your preferred filename. The file is saved as a .png.
