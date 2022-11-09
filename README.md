
# Rozha
A package to simplify and streamline a number of natural language processing processes and methods for a wide variety of languages, empowering users to use NLP on both non-English and English texts.
<p align="center">
<img src="https://raw.githubusercontent.com/ian-nai/Rozha/main/rozha_logo.png">
</p>
Rozha is named after Rozhanitsa, a goddess from Slavic mythology.


## Installation
Install using pip:
```
pip3 install rozha
```
Or download the GitHub repo and the install the requirements:
```
pip3 install -r requirements.txt
```
Then begin using the package by importing the modules you plan to use. Rozha is structured into three classes: process, analyze, and visualize. If running from a local copy of the files, use the following:
```
from process import process
from analyze import analyze
from visualize import visualize
```
If you installed using pip, use this syntax:
```
import rozha.process as process (or whatever name you choose)
import rozha.analyze as analyze (or whatever name you choose)
import rozha.visualize as visualize (or whatever name you choose)
```
##  Full Documentation
A full list of the package's functions can be viewed [at this link](https://github.com/ian-nai/Rozha/blob/main/Functions.md).

## Example Pipelines
Some example pipelines for working with the package are as follows:
Open a file, perform word tokenization and remove stopwords, make the text lowercase, and then get part-of-speech tags for the text:
```
import rozha.process as process
import rozha.analyze as analyze

word_tokenized = process.lowerFile("your_file.txt")
pos_tags = analyze.posList(word_tokenized)
print(pos_tags)
```
Open a file, perform sentence tokenization without removing stopwords, and then perform named entity recognition on each sentence using spaCy:
```
import rozha.process as process
import rozha.analyze as analyze

sent_tokenized = process.sentTokenizeFile(your_file.txt)
ner_tags = analyze.spacyNer(sent_tokenized, 'en')
print(ner_tags)
```

Perform word tokenization and remove stopwords from a string, make the text lowercase, and graph the 10 most common words as a bar graph:
```
import rozha.process as process
import rozha.visualize as visualize

word_tokenized = process.lowerVar(text)
# pass the var, number of words to graph, the height and width of the graph, and your preferred filename
visualize.barFreq(word_tokenized, 10, 400, 400, 'my_graph')
```

## Contributing
Contributions are welcome! The following features are of particular interest:
* Increasing the number of methods in the analyze class
* Increasing the number of methods in the visualization class
