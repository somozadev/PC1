from sklearn.feature_extraction.text import TfidfVectorizer


class TfIdf():
    def __init__(self, parent=None):
        super(TfIdf, self).__init__(parent)

    def GetTfIdf(self, df):
        df["tf-idf"] = None
        if len(df.axes[0]) <= 210:
            tfidf = TfidfVectorizer(min_df=0.02, max_df=100, ngram_range=(1, 2))
        elif len(df.axes[0]) > 210 & len(df.axes[0]) < 310:
            tfidf = TfidfVectorizer(min_df=0.002, max_df=250, ngram_range=(1, 2))

        for i in range(len(df)):
            features = tfidf.fit_transform(df["textoPLN"][i])
            df["tf-idf"][i] = features

        return df
