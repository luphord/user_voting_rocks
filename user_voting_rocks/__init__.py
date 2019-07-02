# -*- coding: utf-8 -*-

'''Use your personal talk voting for PyConDE 2019 to predict
   your interest in a talk. Main methods are `parse_talk_voting`
   for scraping data from the talk voting HTML file and
   `train_model` as well as `predict` for training and predicting
   with a Naive Bayes classifier.
'''

__author__ = '''luphord'''
__email__ = 'luphord@protonmail.com'
__version__ = '0.3.0'

from .parse import parse_talk_voting
from .model import train_model, predict

__all__ = ['parse_talk_voting', 'train_model', 'predict']
