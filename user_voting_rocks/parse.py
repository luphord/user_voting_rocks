# -*- coding: utf-8 -*-

'''Parsing (screen scraping) of talk voting HTML page.'''

from bs4 import BeautifulSoup


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
