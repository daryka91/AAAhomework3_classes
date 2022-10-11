class CountVectorizer:

    def __init__(self):
        self._vocabulary = []
        self._matrix = []

    def fit_transform(self, corpus: list[str]) -> list:
        assert isinstance(corpus, list), 'corpus is not list'
        split_corpus = []
        for line in corpus:
            split_line = line.lower().split()
            split_corpus.append(split_line)
            for el in split_line:
                if el not in self._vocabulary:
                    self._vocabulary.append(el)

        for i in range(len(split_corpus)):
            self._matrix.append([])
            for el in self._vocabulary:
                word_counter = 0
                for word in split_corpus[i]:
                    if word == el:
                        word_counter += 1
                self._matrix[i].append(word_counter)

        return self._matrix

    def get_feature_names(
            self) -> list:

        return self._vocabulary


SOURCE_FILE_NAME = 'Pasta.txt'
vec = CountVectorizer()
corpus = []
with open(SOURCE_FILE_NAME, encoding="utf8") as file:
    for line in file.readlines():
        corpus.append(line)

print(vec.fit_transform(corpus))
print(vec.get_feature_names())
