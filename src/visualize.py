from src.process import process
import nltk

class visualize:
    '''The visualize class contains methods for creating a variety of visualizations for your text.'''

    def wordcloud(var, filename, w, h):
        if type(var) is list:
            import matplotlib.pyplot as plt
            from wordcloud import WordCloud

            unique_string = (" ").join(var)
            wordcloud = WordCloud(width = w, height = h).generate(unique_string)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.savefig(filename +".png", bbox_inches='tight')
            plt.close()
        elif type(var) is str:
            import matplotlib.pyplot as plt
            from wordcloud import WordCloud

            unique_string = var
            wordcloud = WordCloud(width = w, height = h).generate(unique_string)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.savefig(filename +".png", bbox_inches='tight')
            plt.close()
        else:
            print("Please pass a list or string.")


    def spacyTree(var, lang, save=None):
        import spacy
        from spacy import displacy
        tree_list = []
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)

        if save == 'save':
            from pathlib import Path
            if type(var) is list:
                for s in var:
                    doc = nlp(s)
                    sentence_spans = list(doc.sents)
                    tree_list.append(sentence_spans)
                    svg = displacy.render(sentence_spans, style="dep")
                    file_name = '_'.join([w.text for w in doc if not w.is_punct]) + '.svg'
                    with open(file_name, "w", encoding="utf-8") as f:
                        f.write(svg)
                        f.close()

            elif type(var) is str:
                doc = nlp(var)
                sentence_spans = list(doc.sents)
                tree_list.append(sentence_spans)
                svg = displacy.render(sentence_spans, style="dep")
                file_name = '_'.join([w.text for w in doc if not w.is_punct]) + '.svg'
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(svg)
                    f.close()



        elif save is None:
            if type(var) is list:
                for s in var:
                    doc = nlp(s)
                    sentence_spans = list(doc.sents)
                    tree_list.append(sentence_spans)
                    displacy.serve(sentence_spans, style="dep")

            elif type(var) is str:
                doc = nlp(var)
                sentence_spans = list(doc.sents)
                tree_list.append(sentence_spans)
                displacy.serve(sentence_spans, style="dep")


    def spacyNer(var, lang, save=None):
        import spacy
        from spacy import displacy
        from pathlib import Path
        lang = process.spacyCheckLang(lang)
        nlp = spacy.load(process.spacy_lang_package + process.depth_of_package)

        if save == 'save':
            if type(var) == list:
                for s in var:
                    doc = nlp(s)
                    svg = displacy.render(doc, style="ent")
                    file_name = '_'.join([w.text for w in doc if not w.is_punct]) + '_.svg'

                    with open(file_name, "w", encoding="utf-8") as f:
                        f.write(svg)
                        f.close()

            elif type(var) == str:
                doc = nlp(var)
                svg = displacy.render(doc, style="ent")
                file_name = '_'.join([w.text for w in doc if not w.is_punct]) + '_.svg'

                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(svg)
                    f.close()

        elif save is None:
            if type(var) == list:
                for s in var:
                    doc = nlp(s)
                    displacy.serve(doc, style="ent")

            elif type(var) == str:
                doc = nlp(var)
                displacy.serve(doc, style="ent")


    def posGraph(var, num_words, h, w, filename):
        from collections import Counter
        import matplotlib
        import matplotlib.pyplot as plt
        matplotlib.use('Agg')
        if type(var) == list:
            tags = nltk.pos_tag(var)

            counts = Counter(tag for word, tag in tags)

            graphtags = [tag for word, tag in tags]
            graphfreqs = nltk.FreqDist(graphtags)
            graphfreqs.tabulate(num_words)
            fig = plt.figure(figsize = (h,w))
            graphfreqs.plot(num_words, cumulative=False)
            fig.savefig(filename + '.png', bbox_inches = "tight")


        elif type(var) == str:
            tokenizer = nltk.word_tokenize
            tokens = tokenizer(var)
            text =  nltk.Text(tokens)
            tags = nltk.pos_tag(text)

            counts = Counter(tag for word, tag in tags)

            graphtags = [tag for word, tag in tags]
            graphfreqs = nltk.FreqDist(graphtags)
            graphfreqs.tabulate(num_words)
            fig = plt.figure(figsize = (h,w))
            graphfreqs.plot(num_words, cumulative=False)
            fig.savefig(filename + '.png', bbox_inches = "tight")

    def lexicalDispersion(var, ents, h, w, filename):
        import matplotlib
        import matplotlib.pyplot as plt
        from nltk.draw.dispersion import dispersion_plot
        matplotlib.use('Agg')

        if type(var) == str:
            words = nltk.word_tokenize(var)
        elif type(var) == list:
            words = [w for w in var]
            print(words)
        else:
            print("Please pass a list or string.")


        targets = []
        for ent in ents:
            targets.append(ent)

        fig = plt.figure(figsize = (h,w))
        d_plot = dispersion_plot(words, targets, ignore_case=True, title='Lexical Dispersion Plot')
        fig.savefig(filename + '.png', bbox_inches = "tight")

    def wordFreq(var, num, h, w, filename):
        import matplotlib
        import matplotlib.pyplot as plt
        from nltk.probability import FreqDist
        matplotlib.use('Agg')

        fig = plt.figure(figsize = (h,w))

        if type(var) == list:
            fdist = FreqDist(var)
        elif type(var) == str:
            words = nltk.word_tokenize(var)
            fdist = FreqDist(words)
        else:
            print("Please pass a list or string.")


        fdist.plot(num, cumulative=False)
        fig.savefig(filename + '.png', bbox_inches = "tight")

    def barFreq(var, num_words, h, w, filename):
        from collections import Counter
        import matplotlib
        import matplotlib.pyplot as plt
        from nltk.probability import FreqDist
        matplotlib.use('Agg')
        if type(var) == list:
            word_frequency = Counter(" ".join(var).split()).most_common(num_words)

            words = [word for word, _ in word_frequency]
            counts = [counts for _, counts in word_frequency]


            plt.title("Word Frequencies")
            plt.ylabel("Frequency")
            plt.xlabel("Words")
            plt.bar(words, counts)
            plt.savefig(filename + '.png', bbox_inches = "tight")

        elif type(var) == str:
            word_frequency = Counter(var.split()).most_common(num_words)
            words = [word for word, _ in word_frequency]
            counts = [counts for _, counts in word_frequency]


            plt.title("Word Frequencies")
            plt.ylabel("Frequency")
            plt.xlabel("Words")
            plt.bar(words, counts)
            plt.savefig(filename + '.png', bbox_inches = "tight")
