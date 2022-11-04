import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
import stanza
import re
import glob
import csv
import spacy
import codecs


class process:
    '''The process class contains methods for cleaning and processing text using the NLTK, spaCy, and Stanza NLP packages.'''

    depth_of_package = 'md'
    spacy_lang_package = 'en_core_web_'

    sentences = []
    spacy_sentences = []
    stanza_sentences = []
    words = []
    spacy_words = []
    stanza_words = []
    lines = []
    spacy_lines = []
    stanza_lines = []
    lowercase = []
    cleaned = []
    spacy_cleaned = []
    lemmas = []
    spacy_lemmas = []
    stanza_lemmas = []

    def changeDepth(depth):
        if depth == 'sm':
            process.depth_of_package = 'sm'
        elif depth == 'md':
            process.depth_of_package = 'md'
        elif depth == 'lg':
            process.depth_of_package = 'lg'
        elif depth == 'trf':
            process.depth_of_package = 'trf'
        else:
            print('No such package exists.')

        print('Your current depth is set to ' + process.depth_of_package + '.')

    def NLTKlanguages():
        print('''arabic,
 azerbaijani,
 danish,
 dutch,
 english,
 finnish,
 french,
 german,
 greek,
 hungarian,
 indonesian,
 italian,
 kazakh,
 nepali,
 norwegian,
 portuguese,
 romanian,
 russian,
 slovene,
 spanish,
 swedish,
 tajik,
 turkish''')

    def spacyLanguages():
        print('''Catalan ca \n
        Chinese (simplified) zh \n
        Danish da \n
        Dutch nl \n
        English en \n
        Finnish fi \n
        French fr \n
        German de \n
        Greek el \n
        Italian it \n
        Japanese ja \n
        Korean ko \n
        Lithuanian lt \n
        Macedonian mk \n
        Norwegian Bokmål nb \n
        Polish pl \n
        Portuguese pt \n
        Romanian ro \n
        Russian ru \n
        Spanish es \n
        Swedish sv \n
        ''')

    def stanzaLanguages():
        print('''Afrikaans  af \n
Ancient Greek  grc \n
Arabic	ar \n
Armenian  hy \n
Basque  eu \n
Belarusian  be \n
Bulgarian  bg \n
Buryat  bxr \n
Catalan  ca \n
Chinese (simplified)  zh / zh-hans \n
Chinese (traditional)  zh-hant \n
Classical Chinese  lzh \n
Coptic  cop \n
Croatian  hr \n
Czech  cs \n
Danish	da \n
Dutch	nl \n
English  en \n
Estonian  et \n
Finnish  fi \n
French  fr \n
Galician  gl \n
German  de \n
Gothic  got \n
Greek  el \n
Hebrew  he \n
Hindi	hi \n
Hungarian  hu \n
Indonesian  id \n
Irish  ga \n
Italian  it \n
Japanese  ja \n
Kazakh  kk \n
Korean  ko \n
Kurmanji  kmr \n
Latin  la \n
Latvian  lv \n
Lithuanian  lt \n
Livvi  olo \n
Maltese  mt \n
Marathi  mr \n
North Sami  sme \n
Norwegian (Bokmaal)  no / nb \n
Norwegian (Nynorsk)  nn \n
Old Church Slavonic  cu \n
Old French  fro \n
Old Russian  orv \n
Persian  fa \n
Polish	pl \n
Portuguese  pt \n
Romanian  ro \n
Russian	 ru \n
Scottish Gaelic	 gd \n
Serbian	 sr \n
Slovak	sk \n
Slovenian  sl \n
Spanish  es \n
Swedish  sv \n
Swedish Sign Language  swl \n
Tamil  ta \n
Telugu	te \n
Turkish  tr \n
Ukrainian  uk \n
Upper Sorbian  hsb \n
Urdu  ur \n
Uyghur  ug \n
Vietnamese  vi \n
Wolof  wo''')

    def lowerFile(file):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()
        lowered = nltk.word_tokenize(text)
        lowered = [word.lower() for word in lowered]

        # Remove single character words/punctuation
        lowered = [word for word in lowered if len(word) > 1]

        # Remove numbers
        process.lowercase = [word for word in lowered if not word.isnumeric()]

        for word in process.lowercase:
            word = [item.replace("_", "") for item in word]
            word = [item.replace("|", "") for item in word]
            pattern = '[0-9]'
            word = [re.sub(pattern, '', i) for i in word]

        return process.lowercase


    def lowerVar(text):
        lowered = nltk.word_tokenize(text)
        lowered = [word.lower() for word in lowered]

        lowered = [word for word in lowered if len(word) > 1]

        # Remove numbers
        process.lowercase = [word for word in lowered if not word.isnumeric()]

        for word in process.lowercase:
            word = [item.replace("_", "") for item in word]
            word = [item.replace("|", "") for item in word]
            pattern = '[0-9]'
            word = [re.sub(pattern, '', i) for i in word]


        return process.lowercase


    def wordTokenizeFile(file):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()
        process.words = nltk.word_tokenize(text)
        return process.words

    def sentTokenizeFile(file):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()
        process.sentences = nltk.sent_tokenize(text)
        return process.sentences

    def stopwordsFile(file, lang):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()

        default_stopwords = set(nltk.corpus.stopwords.words(lang))

        lines_cleaned = []

        tokenizer = nltk.data.load('tokenizers/punkt/PY3/' + lang + '.pickle')

        lines_split = tokenizer.tokenize(text)

        for f in lines_split:
        # Tokenize the text into words
            words = nltk.word_tokenize(f)

        # Remove single-character tokens (mostly punctuation)
            words = [word for word in words if len(word) > 1]

        # Remove numbers
            words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
            words = [word.lower() for word in words]

        # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            str_words = " ".join(words)
            lines_cleaned.append(str_words)

        for line in lines_cleaned:
            if not line:
                lines_cleaned.remove(line)

        process.cleaned = lines_cleaned

        return process.cleaned


    def stopwordsVar(text, lang):

        default_stopwords = set(stopwords.words(lang))

        lines_cleaned = []

        tokenizer = nltk.data.load('tokenizers/punkt/PY3/' + lang + '.pickle')

        lines_split = tokenizer.tokenize(text)

        for f in lines_split:
        # Tokenize the text into words
            words = nltk.word_tokenize(f)

        # Remove single-character tokens (mostly punctuation)
            words = [word for word in words if len(word) > 1]

        # Remove numbers
            words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
            words = [word.lower() for word in words]

        # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            str_words = " ".join(words)
            lines_cleaned.append(str_words)

        for line in lines_cleaned:
            if not line:
                lines_cleaned.remove(line)
        process.cleaned = lines_cleaned
        return process.cleaned

    def allSentsFile(file, lang):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()

        default_stopwords = set(nltk.corpus.stopwords.words(lang))

        lines_cleaned = []

        tokenizer = nltk.data.load('tokenizers/punkt/PY3/' + lang + '.pickle')

        lines_split = tokenizer.tokenize(text)

        for f in lines_split:
        # Tokenize the text into words
            words = nltk.word_tokenize(f)

        # Remove single-character tokens (mostly punctuation)
            words = [word for word in words if len(word) > 1]

        # Remove numbers
            words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
            words = [word.lower() for word in words]

        # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            str_words = " ".join(words)
            lines_cleaned.append(str_words)

        for line in lines_cleaned:
            if not line:
                lines_cleaned.remove(line)

        process.cleaned = lines_cleaned
        return process.cleaned

    def allSentsVar(text, lang):
        default_stopwords = set(nltk.corpus.stopwords.words(lang))

        lines_cleaned = []

        tokenizer = nltk.data.load('tokenizers/punkt/PY3/' + lang + '.pickle')

        lines_split = tokenizer.tokenize(text)

        for f in lines_split:
        # Tokenize the text into words
            words = nltk.word_tokenize(f)

        # Remove single-character tokens (mostly punctuation)
            words = [word for word in words if len(word) > 1]

        # Remove numbers
            words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
            words = [word.lower() for word in words]

        # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            str_words = " ".join(words)
            lines_cleaned.append(str_words)

        for line in lines_cleaned:
            if not line:
                lines_cleaned.remove(line)
        process.cleaned = lines_cleaned
        return process.cleaned


    def allLinesFile(file, lang):

        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()


        default_stopwords = set(nltk.corpus.stopwords.words(lang))

        new_lines = []

        lines_split = LineTokenizer(blanklines='discard').tokenize(text)

        for line in lines_split:
            words = nltk.word_tokenize(line)

            # Remove single character words/punctuation
            words = [word for word in words if len(word) > 1]

            # Remove numbers
            words = [word for word in words if not word.isnumeric()]

            # Lowercase all words (default_stopwords are lowercase, too)
            words = [word.lower() for word in words]

            # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            for word in words:
                word = [item.replace("_", "") for item in word]
                word = [item.replace("|", "") for item in word]
                pattern = '[0-9]'
                word = [re.sub(pattern, '', i) for i in word]

            str_words = " ".join(words)
            new_lines.append(str_words)


        for line in new_lines:
            if not line:
                new_lines.remove(line)


        process.cleaned = new_lines
        return process.cleaned


    def allLinesVar(text, lang):
       default_stopwords = set(nltk.corpus.stopwords.words(lang))

       new_lines = []

       lines_split = LineTokenizer(blanklines='discard').tokenize(text)

       for line in lines_split:
           words = nltk.word_tokenize(line)

           # Remove single character words/punctuation
           words = [word for word in words if len(word) > 1]

           # Remove numbers
           words = [word for word in words if not word.isnumeric()]

           # Lowercase all words (default_stopwords are lowercase, too)
           words = [word.lower() for word in words]

           # Remove stopwords
           words = [word for word in words if word not in default_stopwords]

           for word in words:
               word = [item.replace("_", "") for item in word]
               word = [item.replace("|", "") for item in word]
               pattern = '[0-9]'
               word = [re.sub(pattern, '', i) for i in word]

           str_words = " ".join(words)
           new_lines.append(str_words)

       for line in new_lines:
           if not line:
               new_lines.remove(line)

       process.cleaned = new_lines
       return process.cleaned

    def allWordsFile(file, lang):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()

        default_stopwords = set(nltk.corpus.stopwords.words(lang))

        cleaned_words = []

        words = nltk.word_tokenize(text)

        # Remove single character words/punctuation
        words = [word for word in words if len(word) > 1]

        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase, too)
        words = [word.lower() for word in words]

        # Remove stopwords
        words = [word for word in words if word not in default_stopwords]

        for word in words:
           word = [item.replace("_", "") for item in word]
           word = [item.replace("|", "") for item in word]
           pattern = '[0-9]'
           word = [re.sub(pattern, '', i) for i in word]

        str_words = " ".join(words)
        cleaned_words.append(str_words)

        for word in cleaned_words:
           if not word:
               cleaned_words.remove(word)

        process.cleaned = cleaned_words
        return process.cleaned

    def allWordsVar(var, lang):
       default_stopwords = set(nltk.corpus.stopwords.words(lang))

       cleaned_words = []

       words = nltk.word_tokenize(var)

       # Remove single character words/punctuation
       words = [word for word in words if len(word) > 1]

       # Remove numbers
       words = [word for word in words if not word.isnumeric()]

       # Lowercase all words (default_stopwords are lowercase, too)
       words = [word.lower() for word in words]

       # Remove stopwords
       words = [word for word in words if word not in default_stopwords]

       for word in words:
           word = [item.replace("_", "") for item in word]
           word = [item.replace("|", "") for item in word]
           pattern = '[0-9]'
           word = [re.sub(pattern, '', i) for i in word]

       str_words = " ".join(words)
       cleaned_words.append(str_words)

       for word in cleaned_words:
           if not word:
               cleaned_words.remove(word)

       process.cleaned = cleaned_words
       return process.cleaned




    def allSentsDir(dir, lang):
        files_to_convert = []
        type = dir + '**/*.txt'

        master_lines = []
        for file in glob.glob(type, recursive=True):
            files_to_convert.append(file)

        for file in files_to_convert:
          with codecs.open(file, 'r', 'utf-8') as f:
              text = f.read()

          default_stopwords = set(nltk.corpus.stopwords.words(lang))

          lines_cleaned = []

          tokenizer = nltk.data.load('tokenizers/punkt/PY3/' + lang + '.pickle')

          lines_split = tokenizer.tokenize(text)

          for f in lines_split:
          # Tokenize the text into words
              words = nltk.word_tokenize(f)

          # Remove single-character tokens (mostly punctuation)
              words = [word for word in words if len(word) > 1]

          # Remove numbers
              words = [word for word in words if not word.isnumeric()]

          # Lowercase all words (default_stopwords are lowercase too)
              words = [word.lower() for word in words]

          # Remove stopwords
              words = [word for word in words if word not in default_stopwords]

              str_words = " ".join(words)
              lines_cleaned.append(str_words)

              for line in lines_cleaned:
                  if not line:
                      lines_cleaned.remove(line)

              master_lines.append(lines_cleaned)

        process.cleaned = master_lines
        return process.cleaned


    def allLinesDir(dir, lang):

        files_to_convert = []
        type = dir + '**/*.txt'

        master_lines = []

        for file in glob.glob(type, recursive=True):
            files_to_convert.append(file)

        for file in files_to_convert:
            with codecs.open(file, 'r', 'utf-8') as f:
                text = f.read()

            default_stopwords = set(nltk.corpus.stopwords.words(lang))

            new_lines = []

            lines_split = LineTokenizer(blanklines='discard').tokenize(text)

            for line in lines_split:
                words = nltk.word_tokenize(line)

            # Remove single character words/punctuation
            words = [word for word in words if len(word) > 1]

            # Remove numbers
            words = [word for word in words if not word.isnumeric()]

            # Lowercase all words (default_stopwords are lowercase, too)
            words = [word.lower() for word in words]

            # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            for word in words:
               word = [item.replace("_", "") for item in word]
               word = [item.replace("|", "") for item in word]
               pattern = '[0-9]'
               word = [re.sub(pattern, '', i) for i in word]

            str_words = " ".join(words)
            new_lines.append(str_words)

            for line in new_lines:
               if not line:
                   new_lines.remove(line)

            master_lines.append(new_lines)

        process.cleaned = master_lines
        return process.cleaned


    def allWordsDir(dir, lang):
        files_to_convert = []
        type = dir + '**/*.txt'

        master_words = []

        for file in glob.glob(type, recursive=True):
             files_to_convert.append(file)

        for file in files_to_convert:
            with codecs.open(file, 'r', 'utf-8') as f:
                text = f.read()

            default_stopwords = set(nltk.corpus.stopwords.words(lang))

            cleaned_words = []

            words = nltk.word_tokenize(text)

            # Remove single character words/punctuation
            words = [word for word in words if len(word) > 1]

            # Remove numbers
            words = [word for word in words if not word.isnumeric()]

            # Lowercase all words (default_stopwords are lowercase, too)
            words = [word.lower() for word in words]

            # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            for word in words:
              word = [item.replace("_", "") for item in word]
              word = [item.replace("|", "") for item in word]
              pattern = '[0-9]'
              word = [re.sub(pattern, '', i) for i in word]

            str_words = " ".join(words)
            cleaned_words.append(str_words)

            for word in cleaned_words:
              if not word:
                  cleaned_words.remove(word)

            master_words.append(cleaned_words)

        process.cleaned = master_words
        return process.cleaned

    def spacyCheckLang(lang):
        trf_langs = ['ca', 'zh', 'da', 'en', 'fr', 'de', 'ja', 'es']

        if lang == 'ca':
            process.spacy_lang_package = "ca_core_news_"
        elif lang == 'zh':
            process.spacy_lang_package = "zh_core_web_"
        elif lang == 'da':
            process.spacy_lang_package = "da_core_news_"
        elif lang == 'nl':
            process.spacy_lang_package = "nl_core_news_"
        elif lang == 'en':
            process.spacy_lang_package = "en_core_web_"
        elif lang == 'fi':
            process.spacy_lang_package = "fi_core_news_"
        elif lang == 'fr':
            process.spacy_lang_package = "fr_core_news_"
        elif lang == 'de':
            process.spacy_lang_package = "de_core_news_"
        elif lang == 'el':
            process.spacy_lang_package = "el_core_news_"
        elif lang == 'it':
            process.spacy_lang_package = "it_core_news_"
        elif lang == 'ja':
            process.spacy_lang_package = "ja_core_news_"
        elif lang == 'ko':
            process.spacy_lang_package = "ko_core_news_"
        elif lang == 'lt':
            process.spacy_lang_package = "lt_core_news_"
        elif lang == 'mk':
            process.spacy_lang_package = "mk_core_news_"
        elif lang == 'nb':
            process.spacy_lang_package = "nb_core_news_"
        elif lang == 'pl':
            process.spacy_lang_package = "pl_core_news_"
        elif lang == 'pt':
            process.spacy_lang_package = "pt_core_news_"
        elif lang == 'ro':
            process.spacy_lang_package = "ro_core_news_"
        elif lang == 'ru':
            process.spacy_lang_package = "ru_core_news_"
        elif lang == 'es':
            process.spacy_lang_package = "es_core_news_"
        elif lang == 'sv':
            process.spacy_lang_package = "sv_core_news_"

        try:
            if lang not in trf_langs:
                if process.depth_of_package == 'trf':
                    process.depth_of_package = 'lg'
                    print(
                        'No trf package available for your language; depth has been changed to lg.')

            if lang == 'ca':
                nlp = spacy.load("ca_core_news_" + process.depth_of_package)
            elif lang == 'zh':
                nlp = spacy.load("zh_core_web_" + process.depth_of_package)
            elif lang == 'da':
                nlp = spacy.load("da_core_news_" + process.depth_of_package)
            elif lang == 'nl':
                nlp = spacy.load("nl_core_news_" + process.depth_of_package)
            elif lang == 'en':
                nlp = spacy.load("en_core_web_" + process.depth_of_package)
            elif lang == 'fi':
                nlp = spacy.load("fi_core_news_" + process.depth_of_package)
            elif lang == 'fr':
                nlp = spacy.load("fr_core_news_" + process.depth_of_package)
            elif lang == 'de':
                nlp = spacy.load("de_core_news_" + process.depth_of_package)
            elif lang == 'el':
                nlp = spacy.load("el_core_news_" + process.depth_of_package)
            elif lang == 'it':
                nlp = spacy.load("it_core_news_" + process.depth_of_package)
            elif lang == 'ja':
                nlp = spacy.load("ja_core_news_" + process.depth_of_package)
            elif lang == 'ko':
                nlp = spacy.load("ko_core_news_" + process.depth_of_package)
            elif lang == 'lt':
                nlp = spacy.load("lt_core_news_" + process.depth_of_package)
            elif lang == 'mk':
                nlp = spacy.load("mk_core_news_" + process.depth_of_package)
            elif lang == 'nb':
                nlp = spacy.load("nb_core_news_" + process.depth_of_package)
            elif lang == 'pl':
                nlp = spacy.load("pl_core_news_" + process.depth_of_package)
            elif lang == 'pt':
                nlp = spacy.load("pt_core_news_" + process.depth_of_package)
            elif lang == 'ro':
                nlp = spacy.load("ro_core_news_" + process.depth_of_package)
            elif lang == 'ru':
                nlp = spacy.load("ru_core_news_" + process.depth_of_package)
            elif lang == 'es':
                nlp = spacy.load("es_core_news_" + process.depth_of_package)
            elif lang == 'sv':
                nlp = spacy.load("sv_core_news_" + process.depth_of_package)

        except OSError as e:
            while True:
                try:
                    if 'E050' in str(e):
                        print(
    'You need to download that spaCy package. Try running python -m spacy download ' +
    process.spacy_lang_package +
    process.depth_of_package +
     ' from the command line.')
                        break
                    elif 'E050' not in str(e):
                        print(e)
                        break
                except:
                    pass

    def spacyStopwordsFile(file, lang):
        with codecs.open(file, 'r', 'utf-8') as f:
            var = f.read()

        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)

        all_stopwords = nlp.Defaults.stop_words

        doc = nlp(str(var))
        text_tokens = [token.text for token in doc]
        tokens_without_sw = [
        word for word in text_tokens if not word in all_stopwords]

        process.spacy_cleaned = tokens_without_sw
        return(process.spacy_cleaned)

    def spacyStopwordsVar(var, lang):
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)

        all_stopwords = nlp.Defaults.stop_words

        doc = nlp(str(var))
        text_tokens = [token.text for token in doc]
        tokens_without_sw = [
        word for word in text_tokens if not word in all_stopwords]

        process.spacy_cleaned = tokens_without_sw
        return(process.spacy_cleaned)


    def spacyLinesFile(file, lang):
        lang = process.spacyCheckLang(lang)

        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()

        lines_list = text.splitlines()

        nlp_lines = []

        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)

        for x in lines_list:
            doc = nlp(x)
            nlp_lines.append(doc)

        process.spacy_lines = nlp_lines
        return(process.spacy_lines)

    def spacyLinesVar(var, lang):
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        nlp_lines = []
        for x in var:
            doc = nlp(x)
            nlp_lines.append(doc)

        process.spacy_lines = nlp_lines
        return(process.spacy_lines)

    def spacySentsFile(file, lang):

        lang = process.spacyCheckLang(lang)

        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)

        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()

        process.spacy_sentences = [i for i in nlp(text).sents]

        return process.spacy_sentences

    def spacySentsVar(var, lang):
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        process.spacy_sentences = [i for i in nlp(var).sents]

        return process.spacy_sentences

    def spacyWordsFile(file, lang):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        doc = nlp(text)
        for token in doc:
            process.spacy_words.append(str(token))

        return process.spacy_words


    def spacyWordsVar(var, lang):
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        doc = nlp(var)
        words = []
        for token in doc:
            words.append(token)

        process.spacy_words = words
        return process.spacy_words



    def stanzaSentsFile(file, lang):
        nlp = stanza.Pipeline(lang)

        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()

        doc = nlp(text)
        sentences = []

        for sent in doc.sentences:
            sentences.append(sent)


        process.stanza_sentences = sentences
        return process.stanza_sentences

    def stanzaSentsVar(var, lang):
        nlp = stanza.Pipeline(lang)

        doc = nlp(var)
        sentences = []

        for sent in doc.sentences:
            sentences.append(sent)

        process.stanza_sentences = sentences
        return process.stanza_sentences


    def stanzaWordsFile(file, lang):
            nlp = stanza.Pipeline(lang)

            with codecs.open(file, 'r', 'utf-8') as f:
                text = f.read()

            doc = nlp(text)

            words = []

            for sent in doc.sentences:
                for word in sent.words:
                    words.append(word)

            process.stanza_words = words
            return process.stanza_words


    def stanzaWordsVar(var, lang):
            nlp = stanza.Pipeline(lang)

            doc = nlp(var)
            words = []

            for sent in doc.sentences:
                for word in sent.words:
                    words.append(word)

            process.stanza_words = words
            return process.stanza_words

    def stanzaLinesFile(file, lang):
                nlp = stanza.Pipeline(lang)

                with codecs.open(file, 'r', 'utf-8') as f:
                    text = f.read()

                line_list = LineTokenizer(blanklines='discard').tokenize(text)

                lines = []

                for x in line_list:
                    doc = nlp(x)
                    lines.append(doc)

                process.stanza_lines = lines
                return process.stanza_lines

    def stanzaLinesVar(var, lang):
            nlp = stanza.Pipeline(lang)

            line_list = LineTokenizer(blanklines='discard').tokenize(var)

            lines = []

            for x in line_list:
                doc = nlp(x)
                lines.append(doc)

            process.stanza_lines = lines
            return process.stanza_lines

    def spacyLemmaFile(file, lang):
        with codecs.open(file, 'r', 'utf-8') as f:
            text = f.read()
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
        lemmatized = []
        lemmatized_sentence = []
        doc = nlp(text)
        for token in doc:
             lemmatized_sentence.append(token.lemma_)
        lemmatized.append(lemmatized_sentence)

        process.spacy_lemmas = lemmatized
        return(process.spacy_lemmas)

    def spacyLemmaVar(var, lang):
       lang = process.spacyCheckLang(lang)
       nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)
       lemmatized = []
       for s in var:
           lemmatized_sentence = []
           doc = nlp(s)
           for token in doc:
               lemmatized_sentence.append(token.lemma_)
           lemmatized.append(lemmatized_sentence)

       process.spacy_lemmas = lemmatized
       return(process.spacy_lemmas)


    def stanzaLemmaVar(var, lang):
       lemmatized_text = []
       nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos,lemma')
       for line in var:
           doc = nlp(line)
           print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
           for sent in doc.sentences:
               lemmas = []
               for word in sent.words:
                   lemma_tuple = (str(word.text), str(word.lemma))
                   lemmas.append(lemma_tuple)
           lemmatized_text.append(lemmas)


       process.spacy_lemmas = lemmatized_text
       return(process.spacy_lemmas)


    def stanzaLemmaFile(file, lang):
       lemmatized_text = []
       with codecs.open(file, 'r', 'utf-8') as f:
           text = f.read()
       sents = nltk.sent_tokenize(text)
       nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos,lemma')
       for line in sents:
           doc = nlp(line)
           print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
           for sent in doc.sentences:
               lemmas = []
               for word in sent.words:
                   lemma_tuple = (str(word.text), str(word.lemma))
                   lemmas.append(lemma_tuple)
           lemmatized_text.append(lemmas)

       process.stanza_lemmas = lemmatized_text
       return(process.stanza_lemmas)

    def stanzaLemmaVar(var, lang):
        lemmatized_text = []
        sents = nltk.sent_tokenize(var)
        nlp = stanza.Pipeline(lang=lang, processors='tokenize,mwt,pos,lemma')
        for line in sents:
            doc = nlp(line)
            print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
            for sent in doc.sentences:
                lemmas = []
                for word in sent.words:
                    lemma_tuple = (str(word.text), str(word.lemma))
                    lemmas.append(lemma_tuple)
            lemmatized_text.append(lemmas)

        process.stanza_lemmas = lemmatized_text
        return(process.stanza_lemmas)

    def saveTxt(results, filename):
        if type(results) is list:
            with open(filename + '.txt', 'w') as f:
                for line in results:
                    f.write("\n" + (str(line)))
        else:
            with open(filename + '.txt', 'w') as f:
                f.write(str(results))

    def zip_lists(**kwargs):
        from itertools import zip_longest
        list_of_lists = []
        for list in kwargs:
            list_of_lists.append(list)
        zipped_lists = zip_longest(*list_of_lists, fillvalue = '')

        process.zipped_lists = zipped_lists
        return process.zipped_lists

    def saveCsv(results, filename):
        if type(results) == str:
            print('Please pass a list.')
        elif type(results) == list:
            with open(filename + '.csv', 'w') as csvfile:
                fieldname = ['text']
                writer = csv.DictWriter(csvfile, fieldnames=fieldname)
                writer.writeheader()
                for entry in results:
                        writer.writerow({'text': entry})


    def saveCsvMulti(filename, *args):
            from itertools import zip_longest
            list_of_lists = []
            for list in args:
                list_of_lists.append(list)
            zipped_lists = zip_longest(*list_of_lists, fillvalue = '')
            with open(filename + '.csv', 'w', encoding="utf-8", newline='') as myfile:
                  wr = csv.writer(myfile)
                  wr.writerow(("List1", "List2"))
                  wr.writerows(zipped_lists)
            myfile.close()
