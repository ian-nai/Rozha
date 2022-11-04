
# Rozha
A package to simplify and streamline a number of natural language processing processes and methods for a wide variety of languages, empowering users to use NLP on both non-English and English texts.
<p align="center">
<img src="rozha_logo.png">
</p>


## Installation
To install, download the GitHub repo and the install the requirements:
```
pip3 install -r requirements.txt
```
Then begin using the package by importing the modules you plan to use. Rozha is structured into three classes: process, analyze, and visualize.
```
from process import process
from analyze import analyze
from visualize import visualize
```
##  Full Documentation
A full list of the package's functions can be viewed at this link.

## Example Pipelines
Some example pipelines for working with the package are as follows:
Open a file, perform word tokenization and remove stopwords, make the text lowercase, and then get part-of-speech tags for the text:
```
word_tokenized = process.lowerFile(your_file.txt)
pos_tags = analyze.posList(word_tokenized)
print(pos_tags)
```
Open a file, perform sentence tokenization without removing stopwords, and then perform named entity recognition on each sentence using spaCy:
```
sent_tokenized = process.sentTokenizeFile(your_file.txt)
ner_tags = spacyNer(sent_tokenized, 'en')
print(ner_tags)
```

Perform word tokenization and remove stopwords from a string, make the text lowercase, and graph the 10 most common words as a bar graph:
```
word_tokenized = lowerVar(text)
# pass the var, number of words to graph, the height and width of the graph, and your preferred filename
barFreq(word_tokenized, 10, 400, 400, 'my_graph')
```

## Contributing
Contributions are welcome! The following features are of particular interest:
* Increasing the number of methods in the analyze class
* Increasing the number of methods in the visualization class
