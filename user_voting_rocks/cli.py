# -*- coding: utf-8 -*-

'''Console script for user_voting_rocks.'''
import sys
import json
import click
import pickle

from .user_voting_rocks import parse_talk_voting, train_model


@click.group(name='user_voting_rocks')
def main(args=None):
    '''Commandline interface for user_voting_rocks.'''
    return 0


@click.command(name='parse')
@click.option('-i', '--input_file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='HTML talk voting file to parse')
@click.option('-o', '--output_file',
              type=click.Path(file_okay=True, dir_okay=False),
              required=True, help='JSON output file for parsed content')
def cli_parse(input_file, output_file):
    '''Parse talk voting html file.'''
    with open(output_file, 'w') as f:
        json.dump(parse_talk_voting(input_file), f, indent=2)


@click.command(name='predict')
def cli_predict():
    '''Predict your interest in a single or multiple talks.'''
    raise NotImplementedError()


@click.command(name='train')
@click.option('-i', '--input_file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='JSON file containing parsed talk votes')
@click.option('-m', '--model_file',
              type=click.Path(file_okay=True, dir_okay=False),
              required=True, help='Model file to save')
def cli_train(input_file, model_file):
    '''Train a model user your talk voting.'''
    with open(input_file, 'r') as f:
        talks = json.load(f)
        voted_proposals = [p for p in talks['proposals'] if p['vote']]
        model = train_model(voted_proposals)
        with open(model_file, 'wb') as f:
            pickle.dump(model, f)


main.add_command(cli_parse)
main.add_command(cli_predict)
main.add_command(cli_train)


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
