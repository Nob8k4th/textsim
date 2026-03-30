from collections import Counter
import math

def jaccard(t1, t2):
    inter = [t for t in t1 if t in t2]
    union = t1 + [t for t in t2 if t not in t1]
    return len(inter)/len(union) if union else 1.0

def cosine_similarity(t1, t2):
    c1, c2 = Counter(t1), Counter(t2)
    keys = set(c1)|set(c2)
    dot = sum(c1[k]*c2[k] for k in keys)
    n1 = math.sqrt(sum(v*v for v in c1.values()))
    n2 = math.sqrt(sum(v*v for v in c2.values()))
    return dot/(n1*n2) if n1 and n2 else 0.0
