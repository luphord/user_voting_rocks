# -*- coding: utf-8 -*-

'''Main module.'''

from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from.stop_words import STOP_WORDS


def parse_talk_voting(file_path):
    proposals = list(parse_talk_voting_iter(file_path))
    return dict(proposals=proposals)


def parse_talk_voting_iter(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        for proposal in soup.find_all('div', class_='proposal'):
            title = proposal.h2.text
            paragraphs = proposal.find_all('p')
            tags = [span.text.strip()
                    for span in paragraphs[0].find_all('span')]
            talk_type_level = paragraphs[-3].code.text
            talk_type, python_level, domain_level = \
                [s.split(':')[1].strip() for s in talk_type_level.split(';')]
            description = '\n'.join(p.text.replace('\n', '')
                                    for p in paragraphs[2:-4])
            votes = proposal.find_all('button', 'btn-primary')
            vote = votes[0].text if votes else None
            yield dict(title=title,
                       tags=tags,
                       talk_type=talk_type,
                       python_level=python_level,
                       domain_level=domain_level,
                       description=description,
                       vote=vote)


def vote_to_binary(vote):
    return {
        'No vote': 0,
        'Not Interested': 0,
        'Maybe': 0,
        'Want to see': 1,
        'Must see': 1
    }[vote]


def train_model(voted_proposals):
    data = [p['description'] for p in voted_proposals]
    target = [vote_to_binary(p['vote']) for p in voted_proposals]
    model = Pipeline([
        ('counter', CountVectorizer(min_df=0.05, max_df=0.5,
                                    stop_words=STOP_WORDS)),
        ('tfidf', TfidfTransformer()),
        ('naive_bayes', MultinomialNB(fit_prior=False))
    ])
    model.fit(data, target)
    return model
