import unittest
from rozha.analyze import analyze


class TestClient(unittest.TestCase):
    file = 'tests/file.txt'
    training_file = 'tests/training_test.csv'
    var = 'This is a test sentence. This is the second test.'
    dir = 'tests'
    var_list = ['This is a test sentence', ' This is the second test.']
    var_list2 = ['This', 'is', 'a', 'test.']

    def test_posString(self):
        analyze.posString(TestClient.var_list2)
        assert analyze.pos_tags[0] == [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('test.', 'NN')]

    def test_posList(self):
        analyze.posList(TestClient.var_list2)
        assert analyze.pos_tags[0] == ('This', 'DT')

    def test_posListSents(self):
        analyze.posListSents(TestClient.var_list)
        assert analyze.pos_tags[0] == [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('test', 'NN'), ('sentence', 'NN')]

    def test_spacyPos(self):
        analyze.spacyPos(TestClient.var_list, 'eng')
        assert analyze.spacy_pos_tags[0] == ['This', 'PRON']

    def test_nerTree(self):
        analyze.nerTree(TestClient.var_list2)
        assert str(analyze.ner_tree) == "[Tree('S', [('This', 'DT')]), Tree('S', [('is', 'VBZ')]), Tree('S', [('a', 'DT')]), Tree('S', [('test', 'NN'), ('.', '.')])]"

    def test_spacyNer(self):
        analyze.spacyNer(['John ran up the hill.'], 'eng')
        assert analyze.spacy_ner_tags[0] == ['John', 'PERSON']

    def test_sentimentBlob(self):
        analyze.sentimentBlob(["The test was good.", "The test was bad."])
        assert str(analyze.blob_sentiment[0]) == "('The test was good.', Sentiment(polarity=0.7, subjectivity=0.6000000000000001))"

    def test_sentimentBlobFile(self):
        analyze.sentimentBlobFile(TestClient.file)
        assert str(analyze.blob_sentiment[0]) == "('This is a test sentence.', Sentiment(polarity=0.0, subjectivity=0.0))"

    def test_sentimentBlobTrain(self):
        analyze.sentimentBlobTrain(TestClient.var_list, TestClient.training_file, 'csv')
        assert analyze.blob_sentiment[0] == ('This is a test sentence', 'pos')

    def test_sentimentBlobTrainFile(self):
        analyze.sentimentBlobTrainFile(TestClient.file, TestClient.training_file, 'csv')
        assert analyze.blob_sentiment[0] == ('This is a test sentence.', 'pos')

    def test_sentimentVaderFile(self):
        analyze.sentimentVaderFile(TestClient.file)
        assert str(analyze.vader_sentiment[0]) == "This is a test sentence.---------------- {'neg': 0.0, 'neu': 0.698, 'pos': 0.302, 'compound': 0.0772}"

    def test_sentimentVader(self):
        analyze.sentimentVader(["The test was good.", "The test was bad."])
        assert str(analyze.vader_sentiment[0]) == "The test was good.---------------------- {'neg': 0.0, 'neu': 0.508, 'pos': 0.492, 'compound': 0.4404}"

    def test_stanzaPosFile(self):
        analyze.stanzaPosFile(TestClient.file, 'en')
        assert analyze.stanza_pos_tags[0] == ['This', 'PRON', 'is', 'AUX', 'a', 'DET', 'test', 'NOUN', 'sentence.', 'NOUN', 'This', 'PRON', 'is', 'AUX', 'the', 'DET', 'second', 'ADJ', 'test.', 'NOUN']

    def test_stanzaPosVar(self):
        analyze.stanzaPosVar(TestClient.var_list, 'en')
        assert analyze.stanza_pos_tags[0] == ['This', 'PRON', 'is', 'AUX', 'a', 'DET', 'test', 'NOUN', 'sentence', 'NOUN']

    def test_stanzaNer(self):
        analyze.stanzaNer(TestClient.var_list, 'en')
        assert analyze.stanza_ner_tags[0] == ['second', 'ORDINAL']

    def test_stanzaSentimentVar(self):
        analyze.stanzaSentimentVar(TestClient.var_list, 'en')
        assert analyze.stanza_sentiment[0] == ('This is a test sentence', 1)

    def test_stanzaSentimentFile(self):
        analyze.stanzaSentimentFile(TestClient.file, 'en')
        assert analyze.stanza_sentiment[0] == ('This is a test sentence.', 1)

    def test_stanzaDependency(self):
        analyze.stanzaDependency(TestClient.var_list, 'en')
        assert str(analyze.stanza_dependency[0]) == "['id: 1, word: This, head id: 5, head: sentence, deprel: nsubj', 'id: 2, word: is, head id: 5, head: sentence, deprel: cop', 'id: 3, word: a, head id: 5, head: sentence, deprel: det', 'id: 4, word: test, head id: 5, head: sentence, deprel: compound', 'id: 5, word: sentence, head id: 0, head: root, deprel: root']"

    def test_stanzaDependencyFile(self):
        analyze.stanzaDependencyFile(TestClient.file, 'en')
        assert str(analyze.stanza_dependency[0]) == "['id: 1, word: This, head id: 5, head: sentence, deprel: nsubj', 'id: 2, word: is, head id: 5, head: sentence, deprel: cop', 'id: 3, word: a, head id: 5, head: sentence, deprel: det', 'id: 4, word: test, head id: 5, head: sentence, deprel: compound', 'id: 5, word: sentence, head id: 0, head: root, deprel: root', 'id: 6, word: ., head id: 5, head: sentence, deprel: punct']"

if __name__ == '__main__':
    unittest.main()
