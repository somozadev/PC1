import pandas as pd
from sklearn.datasets import load_breast_cancer


class DecissionTree():
    def __init__(self, parent=None):
        super(DecissionTree, self).__init__(parent)

        data = load_breast_cancer()
        dataset = pd.DataFrame(data=data['data'], columns=data['feature_names'])
        dataset


