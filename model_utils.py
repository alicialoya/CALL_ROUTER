import numpy as np
import os
from hmmlearn import hmm
from audio_utils import load_audio, extract_mfcc

def train_hmm(features):
    model = hmm.GaussianHMM(n_components=5, covariance_type='diag', n_iter=1000)
    model.fit(features)
    return model

def prepare_training_data(dataset_path):
    models = {}
    for keyword in os.listdir(dataset_path):
        keyword_path = os.path.join(dataset_path, keyword)
        if not os.path.isdir(keyword_path):
            continue
        features = []
        for file in os.listdir(keyword_path):
            if not file.endswith('.wav'):
                continue
            filepath = os.path.join(keyword_path, file)
            y, sr = load_audio(filepath)
            mfcc = extract_mfcc(y, sr)
            features.append(mfcc)
        features = np.vstack(features)
        model = train_hmm(features)
        models[keyword] = model
    return models

def predict(models, filepath):
    y, sr = load_audio(filepath)
    mfcc = extract_mfcc(y, sr)
    scores = {}
    for keyword, model in models.items():
        try:
            score = model.score(mfcc)
            scores[keyword] = score
        except:
            scores[keyword] = float('-inf')
    predicted_keyword = max(scores, key=scores.get)
    return predicted_keyword
