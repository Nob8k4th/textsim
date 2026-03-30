from textsim.tokenizer import Tokenizer

def test_space_pass():
    assert Tokenizer().split_space('a b  c') == ['a','b','c']

def test_punct_pass():
    assert Tokenizer().split_punct('a,b.c') == ['a','b','c']

def test_stopwords_fail_case_sensitive():
    assert Tokenizer().remove_stopwords(['The','cat']) == ['cat']

def test_stopwords_pass():
    assert Tokenizer().remove_stopwords(['the','cat']) == ['cat']

def test_empty_pass():
    assert Tokenizer().split_space('') == []
