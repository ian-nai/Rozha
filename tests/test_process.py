import unittest
from rozha.process import process
from pathlib import Path


class TestClient(unittest.TestCase):
    file = 'tests/file.txt'
    dir = 'tests'
    var = 'This is a test sentence. This is the second test.'
    stanza_var = 'Test.'
    var_list = ['This is a test sentence.', 'This is the second test.']

    def test_changeDepth(self):
        process.changeDepth('md')
        assert process.depth_of_package == 'md'

    def test_lowerFile(self):
        process.lowerFile(TestClient.file)
        res = any(ele.isupper() for ele in process.lowercase)
        assert res == False

    def test_lowerVar(self):
        process.lowerVar(TestClient.var)
        res = any(ele.isupper() for ele in process.lowercase)
        assert res == False

    def test_wordTokenizeFile(self):
        process.wordTokenizeFile(TestClient.file)
        assert type(process.words) is list
        assert process.words[0] == 'This'

    def test_sentTokenizeFile(self):
        process.sentTokenizeFile(TestClient.file)
        assert type(process.sentences) is list
        assert process.sentences[0] == 'This is a test sentence.'

    def test_stopwordsFile(self):
        process.stopwordsFile(TestClient.file, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence'

    def test_stopwordsVar(self):
        process.stopwordsVar(TestClient.var, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence'

    def test_allSentsFile(self):
        process.allSentsFile(TestClient.file, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence'

    def test_allSentsVar(self):
        process.allSentsVar(TestClient.var, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence'

    def test_allLinesFile(self):
        process.allLinesFile(TestClient.file, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence second test'

    def test_allLinesVar(self):
        process.allLinesVar(TestClient.var, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence second test'

    def test_allWordsFile(self):
        process.allWordsFile(TestClient.file, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence second test'

    def test_allWordsVar(self):
        process.allWordsVar(TestClient.var, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == 'test sentence second test'

    def test_allSentsDir(self):
        process.allSentsDir(TestClient.dir, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == ['test sentence', 'second test']

    def test_allLinesDir(self):
        process.allLinesDir(TestClient.dir, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == ['test sentence second test']

    def test_allWordsDir(self):
        process.allLinesDir(TestClient.dir, 'english')
        assert type(process.cleaned) is list
        assert process.cleaned[0] == ['test sentence second test']

    def test_spacyCheckLang(self):
        process.spacyCheckLang('en')
        assert process.spacy_lang_package == "en_core_web_"

    def test_spacyStopwordsFile(self):
        process.spacyStopwordsFile(TestClient.file, 'eng')
        assert type(process.spacy_cleaned) is list
        assert process.spacy_cleaned[0] == 'This'

    def test_spacyStopwordsVar(self):
        process.spacyStopwordsVar(TestClient.var, 'eng')
        assert type(process.spacy_cleaned) is list
        assert process.spacy_cleaned[0] == 'This'

    def test_spacyLinesFile(self):
        process.spacyLinesFile(TestClient.file, 'eng')
        assert type(process.spacy_lines) is list
        assert str(process.spacy_lines[0]) == 'This is a test sentence. This is the second test.'

    def test_spacySentsFile(self):
        process.spacySentsFile(TestClient.file, 'eng')
        assert type(process.spacy_sentences) is list
        assert str(process.spacy_sentences[0]) == 'This is a test sentence.'

    def test_spacyWordsFile(self):
        process.spacyWordsFile(TestClient.file, 'eng')
        assert type(process.spacy_words) is list
        assert str(process.spacy_words[0]) == 'This'

    def test_spacyLinesVar(self):
        process.spacyLinesVar(TestClient.var_list, 'eng')
        assert type(process.spacy_lines) is list
        assert str(process.spacy_lines[0]) == 'This is a test sentence.'

    def test_spacySentsVar(self):
        process.spacySentsVar(TestClient.var, 'eng')
        assert type(process.spacy_sentences) is list
        assert str(process.spacy_sentences[0]) == 'This is a test sentence.'

    def test_spacyWordsVar(self):
        process.spacyWordsVar(TestClient.var, 'eng')
        assert type(process.spacy_words) is list
        assert str(process.spacy_words[0]) == 'This'
    #
    def test_stanzaSentsVar(self):
        process.stanzaSentsVar(TestClient.stanza_var, 'en')
        assert str(process.stanza_sentences[0]) == '''[
  {
    "id": 1,
    "text": "Test",
    "lemma": "test",
    "upos": "NOUN",
    "xpos": "NN",
    "feats": "Number=Sing",
    "head": 0,
    "deprel": "root",
    "start_char": 0,
    "end_char": 4,
    "ner": "O",
    "multi_ner": [
      "O"
    ]
  },
  {
    "id": 2,
    "text": ".",
    "lemma": ".",
    "upos": "PUNCT",
    "xpos": ".",
    "head": 1,
    "deprel": "punct",
    "start_char": 4,
    "end_char": 5,
    "ner": "O",
    "multi_ner": [
      "O"
    ]
  }
]'''

        def test_stanzaSentsFile(self):
            process.stanzaSentsFile('stanza_file.txt', 'en')
            assert str(process.stanza_sentences[0]) == '''[
      {
        "id": 1,
        "text": "Test",
        "lemma": "test",
        "upos": "NOUN",
        "xpos": "NN",
        "feats": "Number=Sing",
        "head": 0,
        "deprel": "root",
        "start_char": 0,
        "end_char": 4,
        "ner": "O",
        "multi_ner": [
          "O"
        ]
      },
      {
        "id": 2,
        "text": ".",
        "lemma": ".",
        "upos": "PUNCT",
        "xpos": ".",
        "head": 1,
        "deprel": "punct",
        "start_char": 4,
        "end_char": 5,
        "ner": "O",
        "multi_ner": [
          "O"
        ]
      }
    ]'''

        def test_stanzaWordsFile(self):
            process.stanzaWordsFile('stanza_file.txt', 'en')
            assert str(process.stanza_words[0]) == '''{
      "id": 1,
      "text": "Test",
      "lemma": "test",
      "upos": "NOUN",
      "xpos": "NN",
      "feats": "Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 4
    }'''

        def test_stanzaWordsVar(self):
            process.stanzaWordsVar(TestClient.stanza_var, 'en')
            assert str(process.stanza_words[0]) == '''{
      "id": 1,
      "text": "Test",
      "lemma": "test",
      "upos": "NOUN",
      "xpos": "NN",
      "feats": "Number=Sing",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 4
    }'''


        def test_stanzaLinesVar(self):
            process.stanzaLinesVar(TestClient.stanza_var, 'en')
            assert str(process.stanza_lines[0]) == '''[
      [
        {
          "id": 1,
          "text": "Test",
          "lemma": "test",
          "upos": "NOUN",
          "xpos": "NN",
          "feats": "Number=Sing",
          "head": 0,
          "deprel": "root",
          "start_char": 0,
          "end_char": 4,
          "ner": "O",
          "multi_ner": [
            "O"
          ]
        },
        {
          "id": 2,
          "text": ".",
          "lemma": ".",
          "upos": "PUNCT",
          "xpos": ".",
          "head": 1,
          "deprel": "punct",
          "start_char": 4,
          "end_char": 5,
          "ner": "O",
          "multi_ner": [
            "O"
          ]
        }
      ]
    ]'''


        def test_stanzaLinesFile(self):
            process.stanzaLinesFile('stanza_file.txt', 'en')
            assert str(process.stanza_lines[0]) == '''[
      [
        {
          "id": 1,
          "text": "Test",
          "lemma": "test",
          "upos": "NOUN",
          "xpos": "NN",
          "feats": "Number=Sing",
          "head": 0,
          "deprel": "root",
          "start_char": 0,
          "end_char": 4,
          "ner": "O",
          "multi_ner": [
            "O"
          ]
        },
        {
          "id": 2,
          "text": ".",
          "lemma": ".",
          "upos": "PUNCT",
          "xpos": ".",
          "head": 1,
          "deprel": "punct",
          "start_char": 4,
          "end_char": 5,
          "ner": "O",
          "multi_ner": [
            "O"
          ]
        }
      ]
    ]'''


        def test_stanzaLemmaFile(self):
            process.stanzaLemmaFile(TestClient.file, 'en')
            #assert type(process.stanza_lemmas) is list
            print('STANZALEMMAFILE:' + str(process.stanza_lemmas[0]) + '\n\n')

        def test_stanzaLemmaVar(self):
            process.stanzaLemmaVar(TestClient.var, 'en')
            assert type(process.stanza_lemmas) is list
            print('STANZALEMMAVAR:' + str(process.stanza_lemmas[0]) + '\n\n')

    def test_spacyLemmaVar(self):
        process.spacyLemmaVar(TestClient.var_list, 'eng')
        assert type(process.spacy_lemmas) is list
        assert process.spacy_lemmas[0] == ['this', 'be', 'a', 'test', 'sentence', '.']

    def test_spacyLemmaFile(self):
        process.spacyLemmaFile(TestClient.file, 'eng')
        assert type(process.spacy_lemmas) is list
        assert process.spacy_lemmas[0] == ['this', 'be', 'a', 'test', 'sentence', '.', 'this', 'be', 'the', 'second', 'test', '.', '\n']

    def test_saveTxt(self):
        process.saveTxt(TestClient.var_list, 'test_saveTxt')
        import os.path
        assert os.path.isfile('test_saveTxt.txt')
        with open("test_saveTxt.txt") as f:
            line_list = f.readlines()
            test_line = line_list[1].rstrip()
            assert test_line == 'This is a test sentence.'

    def test_saveCsv(self):
        process.saveCsv(TestClient.var_list, 'test_saveCsv')
        import os.path
        assert os.path.isfile('test_saveCsv.csv')
        with open("test_saveCsv.csv") as f:
            list_test = [row.split()[0] for row in f]
            assert list_test[1] == 'This'

    def test_saveCsvMulti(self):
        process.saveCsvMulti('test_saveCsv_lists', TestClient.var_list)
        import os.path
        assert os.path.isfile('test_saveCsv_lists.csv')
        with open("test_saveCsv_lists.csv") as f:
            list_test = [row.split()[0] for row in f]
            assert list_test[1] == 'This'


if __name__ == '__main__':
    unittest.main()
