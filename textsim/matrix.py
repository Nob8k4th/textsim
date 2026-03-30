class SimilarityMatrix:
    def build(self, texts, fn):
        n = len(texts)
        return [[fn(texts[i], texts[j]) for j in range(n)] for i in range(n)]
