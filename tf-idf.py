import math
from collections import Counter


class CountVectorizer():
    """Преобразует список текстовых документов
    в матрицу подсчета вхождений слов в каждый документ."""
    def __init__(self):
        self.feature_names = []

    def fit(self, corpus) -> list:
        splitted_sentences = []
        for sentence in corpus:
            splitted_sentence = sentence.lower().split()
            for word in splitted_sentence:
                if word not in self.feature_names:
                    self.feature_names.append(word)
            splitted_sentences.append(splitted_sentence)
        return splitted_sentences

    def transform(self, corpus) -> list:
        matrix = []
        for sentence in self.fit(corpus):
            count_words_in_sentence = []
            counter = Counter(sentence)
            for word in self.feature_names:
                count_words_in_sentence.append(counter.get(word, 0))
            matrix.append(count_words_in_sentence)
        return matrix

    def fit_transform(self, corpus):
        return self.transform(corpus)

    def get_feature_names(self) -> set:
        return self.feature_names


class TfidfTransformer:
    @staticmethod
    def _tf_transform(matrix):
        matrix_tf = []
        for vec in matrix:
            num_of_words = sum(vec)
            tf_matrix_row = [round(n / num_of_words, 3) for n in vec]
            matrix_tf.append(tf_matrix_row)
        return matrix_tf

    @staticmethod
    def _idf_transform(matrix):
        def count_idf(n_doc, word_id_docs):
            return round(math.log((n_doc + 1) / (word_id_docs + 1)) + 1, 3)
        cnt_doc = len(matrix)
        idf = []
        for i in range(len(matrix[0])):
            count = 0
            for j in range(len(matrix)):
                if matrix[j][i] != 0:
                    count += 1
            idf.append(count_idf(cnt_doc, count))
        return idf

    def fit_transform(self, matrix):
        tf = self._tf_transform(matrix)
        idf = self._idf_transform(matrix)
        tf_idf_matrix = []
        for row in tf:
            tf_idf_matrix.append([round(x * y, 3) for x, y in zip(row, idf)])
        return tf_idf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super(TfidfVectorizer, self).__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super(TfidfVectorizer, self).fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
