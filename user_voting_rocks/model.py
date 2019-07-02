# -*- coding: utf-8 -*-

'''Training and prediction of Naive Bayes classifier.'''

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

from .stop_words import STOP_WORDS


def vote_to_binary(vote):
    return {
        'No vote': 0,
        'Not Interested': 0,
        'Maybe': 0,
        'Want to see': 1,
        'Must see': 1
    }[vote]


def prepare_model():
    return Pipeline([
               ('counter', CountVectorizer(min_df=0.05, max_df=0.5,
                                           stop_words=STOP_WORDS)),
               ('tfidf', TfidfTransformer()),
               ('naive_bayes', MultinomialNB(fit_prior=False))
           ])


def train_model(voted_proposals):
    data = [p['description'] for p in voted_proposals]
    target = [vote_to_binary(p['vote']) for p in voted_proposals]
    model = prepare_model()
    model.fit(data, target)
    return model


def predict(model, unvoted_proposals):
    pred = model.predict_proba([p['description']
                                for p in unvoted_proposals])
    res = sorted([dict(title=proposal['title'], interest=interest)
                  for proposal, interest
                  in zip(unvoted_proposals, pred[:, 1].tolist())],
                 key=lambda d: d['interest'],
                 reverse=True)
    return res


def evaluate_model(voted_proposals):
    data = [p['description'] for p in voted_proposals]
    target = [vote_to_binary(p['vote']) for p in voted_proposals]
    model = prepare_model()
    return cross_val_score(model, data, target, cv=5)
