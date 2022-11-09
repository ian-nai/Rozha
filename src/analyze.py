import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
import stanza
import re
import glob
import csv
import spacy
import codecs

from rozha.process import process

class analyze:
    '''The analyze class contains methods for performing various analysis methodologies using the NLTK, spaCy, and Stanza NLP packages.'''

    pos_tags = []
    spacy_pos_tags = []
    stanza_pos_tags = []
    spacy_ner_tags = []
    stanza_ner_tags = []
    lemmas = []
    stanza_dependency = []
    vader_sentiment = []
    blob_sentiment = []

    def posString(var):
        pos_tags = []
        pos_tags.append(nltk.pos_tag(var))

        analyze.pos_tags = pos_tags
        return(analyze.pos_tags)

    def posList(var):
        pos_tags = nltk.pos_tag(var)
        analyze.pos_tags = pos_tags
        return(analyze.pos_tags)

    def posListSents(var):
        pos_tags = []
        for s in var:
            tokens = nltk.word_tokenize(s)
            pos_tags.append(nltk.pos_tag(tokens))

        analyze.pos_tags = pos_tags
        return(analyze.pos_tags)

    def spacyPos(var, lang):
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        pos_processed = []
        for x in var:
            doc = nlp(x)
            for token in doc:
                token_list = []
                token_list.append(token.text)
                token_list.append(token.pos_)
                pos_processed.append(token_list)

        analyze.spacy_pos_tags = pos_processed
        return(analyze.spacy_pos_tags)

    def stanzaPosFile(file, lang):
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos', tokenize_pretokenized=True)
        pos_processed = []
        with codecs.open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            doc = nlp(text)
            for sent in doc.sentences:
                pos_temp = []
                for word in sent.words:
                    pos_temp.append(word.text)
                    pos_temp.append(word.upos)

            pos_processed.append(pos_temp)
            f.close()

        analyze.stanza_pos_tags = pos_processed
        return(analyze.stanza_pos_tags)

    def stanzaPosVar(var, lang):
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos', tokenize_pretokenized=True)
        pos_processed = []
        for x in var:
            doc = nlp(x)
            for sent in doc.sentences:
                pos_temp = []
                for word in sent.words:
                    pos_temp.append(word.text)
                    pos_temp.append(word.upos)

            pos_processed.append(pos_temp)

        analyze.stanza_pos_tags = pos_processed
        return(analyze.stanza_pos_tags)

    def nerTree(var):
        ner_processed = []
        for x in var:
            tokens = nltk.word_tokenize(x)
            tag = nltk.pos_tag(tokens)

            ner_tree = nltk.ne_chunk(tag, binary=True)
            ner_processed.append(ner_tree)


        analyze.ner_tree = ner_processed
        return(analyze.ner_tree)

    def spacyNer(var, lang):
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        ner_processed = []
        for x in var:
            doc = nlp(x)
            for ent in doc.ents:
                token_list = []
                token_list.append(ent.text)
                token_list.append(ent.label_)
                ner_processed.append(token_list)

        analyze.spacy_ner_tags = ner_processed
        return(analyze.spacy_ner_tags)

    def stanzaNer(var, lang):
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,ner', tokenize_pretokenized=True)
        ner_processed = []
        for x in var:
            doc = nlp(x)
            for sent in doc.sentences:
                for ent in sent.ents:
                    token_list = []
                    token_list.append(ent.text)
                    token_list.append(ent.type)
                    ner_processed.append(token_list)

        analyze.stanza_ner_tags = ner_processed
        return(analyze.stanza_ner_tags)

    def sentimentBlob(var):
        from textblob import TextBlob
        sentiment_list = []
        if type(var) is list:
            for s in var:
                q = TextBlob(s)
                sen_tup = (s, q.sentiment)
                sentiment_list.append(sen_tup)
        elif type(var) is str:
            sents = nltk.sent_tokenize(s)
            for sen in sents:
                q = TextBlob(sen)
                sen_tup = (sen, q.sentiment)
                sentiment_list.append(sen_tup)

        analyze.blob_sentiment = sentiment_list
        return(analyze.blob_sentiment)

    def sentimentBlobFile(file):
        from textblob import TextBlob
        sentiment_list = []
        with codecs.open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            sents = nltk.sent_tokenize(text)
            for sen in sents:
                q = TextBlob(sen)
                sen_tup = (sen, q.sentiment)
                sentiment_list.append(sen_tup)
            f.close()

        analyze.blob_sentiment = sentiment_list
        return(analyze.blob_sentiment)

    def sentimentBlobTrain(var, training_file, file_format):
        from textblob import TextBlob
        from textblob.classifiers import NaiveBayesClassifier

        sentiment_list = []
        train = []

        with open(training_file, 'r') as fp:
            cl = NaiveBayesClassifier(fp, format=file_format)

        if type(var) is list:
            for s in var:
                classified = cl.classify(s)
                sen_tup = (s, classified)
                sentiment_list.append(sen_tup)
        elif type(var) is str:
            sents = nltk.sent_tokenize(s)
            for sen in sents:
                classified = cl.classify(s)
                sen_tup = (sen, classified)
                sentiment_list.append(sen_tup)

        analyze.blob_sentiment = sentiment_list
        return(analyze.blob_sentiment)

    def sentimentBlobTrainFile(file, training_file, file_format):
        from textblob import TextBlob
        from textblob.classifiers import NaiveBayesClassifier
        sentiment_list = []

        with open(training_file, 'r') as fp:
            cl = NaiveBayesClassifier(fp, format=file_format)

        with codecs.open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            sents = nltk.sent_tokenize(text)
            for sen in sents:
                classified = cl.classify(sen)
                sen_tup = (sen, classified)
                sentiment_list.append(sen_tup)

            f.close()

        analyze.blob_sentiment = sentiment_list
        return(analyze.blob_sentiment)


    def sentimentVaderFile(file):
        from nltk.sentiment.vader import SentimentIntensityAnalyzer

        analyzer = SentimentIntensityAnalyzer()

        sentiment_list = []
        with codecs.open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            sents = nltk.sent_tokenize(text)
            sentiment_list = []
            for s in sents:
                snt = analyzer.polarity_scores(s)
                print("{:-<40} {}".format(s, str(snt)))
                sentiment_list.append("{:-<40} {}".format(s, str(snt)))
            f.close()

        analyze.vader_sentiment = sentiment_list
        return(analyze.vader_sentiment)

    def sentimentVader(var):
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        sentiment_list = []
        if type(var) is list:
            for s in var:
                snt = analyzer.polarity_scores(s)
                print("{:-<40} {}".format(s, str(snt)))
                sentiment_list.append("{:-<40} {}".format(s, str(snt)))
        elif type(var) is str:
            sents = nltk.sent_tokenize(var)
            for s in sents:
                snt = analyzer.polarity_scores(s)
                print("{:-<40} {}".format(s, str(snt)))
                sentiment_list.append("{:-<40} {}".format(s, str(snt)))

        analyze.vader_sentiment = sentiment_list
        return(analyze.vader_sentiment)

    def stanzaSentimentVar(var, lang):
        import stanza
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,sentiment')
        sentiment_list = []
        if type(var) is list:
            for x in var:
                doc = nlp(x)
                for i, sentence in enumerate(doc.sentences):
                    sentiment_temp = tuple((sentence.text, sentence.sentiment))
                    sentiment_list.append(sentiment_temp)
        else:
            doc = nlp(var)
            for i, sentence in enumerate(doc.sentences):
                sentiment_temp = tuple((sentence.text, sentence.sentiment))
                sentiment_list.append(sentiment_temp)

        analyze.stanza_sentiment = sentiment_list
        return(analyze.stanza_sentiment)

    def stanzaSentimentFile(file, lang):
        import stanza
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,sentiment')
        sentiment_list = []
        with codecs.open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            doc = nlp(text)
            for i, sentence in enumerate(doc.sentences):
                sentiment_temp = tuple((sentence.text, sentence.sentiment))
                sentiment_list.append(sentiment_temp)
            f.close()

        analyze.stanza_sentiment = sentiment_list
        return(analyze.stanza_sentiment)

    def stanzaDependency(var, lang):
        import stanza
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos,lemma,depparse')
        dependency_list = []
        for x in var:
            doc = nlp(x)
            print(*[f'id: {word.id} word: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
            dependency_list.append([f'id: {word.id}, word: {word.text}, head id: {word.head}, head: {sent.words[word.head-1].text if word.head > 0 else "root"}, deprel: {word.deprel}' for sent in doc.sentences for word in sent.words])

        analyze.stanza_dependency = dependency_list
        return(analyze.stanza_dependency)

    def stanzaDependencyFile(file, lang):
        import stanza
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos,lemma,depparse')
        dependency_list = []
        with codecs.open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            sents = nltk.sent_tokenize(text)
            for sent in sents:
                doc = nlp(sent)
                print(*[f'id: {word.id} word: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
                dependency_list.append([f'id: {word.id}, word: {word.text}, head id: {word.head}, head: {sent.words[word.head-1].text if word.head > 0 else "root"}, deprel: {word.deprel}' for sent in doc.sentences for word in sent.words])
            f.close()

        analyze.stanza_dependency = dependency_list
        return(analyze.stanza_dependency)
