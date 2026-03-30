# textsim

`textsim` 用于文本相似度计算，覆盖字符级、词级以及矩阵批量计算。

## 模块一览

- `levenshtein_distance`、`jaro_winkler`：字符级相似度/距离
- `Tokenizer`：空格分词、标点分词、停用词过滤
- `jaccard`、`cosine_similarity`：词级相似度
- `SimilarityMatrix`：批量文本两两相似度矩阵

## 快速使用

```bash
pip install -e .
```

```python
from textsim import Tokenizer, jaccard, cosine_similarity, levenshtein_distance, SimilarityMatrix

t = Tokenizer()
a = t.split_punct("NLP is fun!")
b = t.split_punct("NLP is very fun")

print(levenshtein_distance("kitten", "sitting"))
print(jaccard(a, b))
print(cosine_similarity(a, b))
print(SimilarityMatrix().build(["a b", "a c"], lambda x, y: 1.0 if x == y else 0.0))
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
