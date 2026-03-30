import pytest
from textsim.char_sim import levenshtein_distance, jaro_winkler

@pytest.mark.parametrize('a,b,e', [('abc','abc',0),('a','b',1)])
def test_lev(a,b,e):
    assert levenshtein_distance(a,b)==e

def test_lev_same_fail():
    assert levenshtein_distance('same','same')==0

def test_jw_pass():
    assert jaro_winkler('x','x')==1.0

def test_lev_empty_pass():
    assert levenshtein_distance('', 'ab')==2
