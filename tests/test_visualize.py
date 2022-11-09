import unittest
from rozha.visualize import visualize


class TestClient(unittest.TestCase):
    file = 'tests/file.txt'
    var = 'This is a test sentence. This is the second test.'
    var_ner = 'John is here.'
    dir = 'tests'
    var_list = ['This is a test sentence', ' This is the second test.']
    var_list2 = ['This', 'is', 'a', 'test.']

    def test_wordcloud(self):
        visualize.wordcloud(TestClient.var_list2, 'test_wcloud', 100, 100)
        import os.path
        assert os.path.isfile('test_wcloud.png')

    def test_spacyTree(self):
        visualize.spacyTree(TestClient.var, 'en', 'save')
        import os.path
        assert os.path.isfile('This_is_a_test_sentence_This_is_the_second_test.svg')

    def test_spacyNer(self):
        visualize.spacyNer(TestClient.var_ner, 'en', 'save')
        import os.path
        assert os.path.isfile('John_is_here_.svg')

    def test_posGraph(self):
        visualize.posGraph(TestClient.var, 20, 10, 4, 'test_pos')
        import os.path
        assert os.path.isfile('test_pos.png')

    def test_lexicalDispersion(self):
        visualize.lexicalDispersion(TestClient.var_list2, ['John'], 10, 4, 'test_lex')
        import os.path
        assert os.path.isfile('test_lex.png')

    def test_wordFreq(self):
        visualize.wordFreq(TestClient.var, 20, 10, 4, 'test_freq')
        import os.path
        assert os.path.isfile('test_freq.png')

    def test_barFreq(self):
        visualize.barFreq(TestClient.var, 20, 10, 4, 'test_bar_freq')
        import os.path
        assert os.path.isfile('test_bar_freq.png')


if __name__ == '__main__':
    unittest.main()
