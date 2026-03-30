from textsim.word_sim import jaccard, cosine_similarity
from textsim.matrix import SimilarityMatrix

def test_jaccard_fail_duplicates():
    assert jaccard(['a','a','b'], ['a']) == 0.5

def test_jaccard_pass():
    assert round(jaccard(['a','b'], ['b','c']),4) == round(1/3,4)

def test_cosine_pass():
    assert round(cosine_similarity(['a','b'], ['a','b']),5) == 1.0

def test_cosine_zero_pass():
    assert cosine_similarity([],[]) == 0.0

def test_matrix_symmetry_pass():
    m = SimilarityMatrix().build(['x','x'], lambda a,b: 1.0 if a==b else 0.0)
    assert m[0][1] == m[1][0]

def test_matrix_diag_pass():
    m = SimilarityMatrix().build(['x'], lambda a,b: 1.0)
    assert m[0][0] == 1.0
