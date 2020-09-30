import os
import pickle
from sklearn.externals import joblib

config = {
    'webpage': {
        'cluster': 'production/cluster.pkl',
        'centroid': 'production/centroid.pkl',
        'datax': 'production/datax.pkl',
    }}

dir = os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

# def GetPickleFile(filepath):
#     if os.path.isfile(os.path.join(dir, filepath)):
#         return pickle.load( open(os.path.join(dir, filepath), "rb" ) )
#     return None

def GetCluster():
    return GetJobLibFile(config['webpage']['cluster'])


def GetCentroid():
    return GetJobLibFile(config['webpage']['centroid'])

def Getdatax():
    return GetJobLibFile(config['webpage']['datax'])


def GetAll():
    return (GetCluster(),GetCentroid(),Getdatax())

# def GetAllClassifiersForHeart():
#     return (GetSVCClassifierForHeart(),GetLogisticRegressionClassifierForHeart(),GetNaiveBayesClassifierForHeart(),GetDecisionTreeClassifierForHeart(),GetDeepLearningClassifierForHeart(),GetKNNClassifierForHeart())

# def GetSVCClassifierForHeart():
#     return GetJobLibFile(config['heart']['SVC'])

# def GetLogisticRegressionClassifierForHeart():
#     return GetJobLibFile(config['heart']['LogisticRegression'])

# def GetNaiveBayesClassifierForHeart():
#     return GetJobLibFile(config['heart']['NaiveBayes'])

# def GetDecisionTreeClassifierForHeart():
#     return GetJobLibFile(config['heart']['DecisionTree'])

# def GetKNNClassifierForHeart():
#     return GetJobLibFile(config['heart']['KNN'])

# def GetDeepLearningClassifierForHeart():
#     return GetJobLibFile(config['heart']['deep_learning'])


