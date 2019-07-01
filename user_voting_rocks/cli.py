# -*- coding: utf-8 -*-

'''Console script for user_voting_rocks.'''
import sys
import json
import click

import joblib

from .user_voting_rocks import parse_talk_voting, train_model, predict, \
                               evaluate_model


@click.group(name='user_voting_rocks')
def main(args=None):
    '''Commandline interface for user_voting_rocks.'''
    return 0


@click.command(name='evaluate')
@click.option('-i', '--input-file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='HTML talk voting file to parse')
def cli_evaluate(input_file):
    '''Evaluate the talk voting classifier.'''
    talks = parse_talk_voting(input_file)
    voted_proposals = [p for p in talks['proposals'] if p['vote']]
    scores = evaluate_model(voted_proposals)
    click.echo(f'Accuracy (cross-validation): {scores.mean():.2f}')


@click.command(name='parse')
@click.option('-i', '--input-file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='HTML talk voting file to parse')
@click.option('-o', '--output-file',
              type=click.Path(file_okay=True, dir_okay=False),
              required=True, help='JSON output file for parsed content')
def cli_parse(input_file, output_file):
    '''Parse talk voting html file.'''
    with open(output_file, 'w') as f:
        json.dump(parse_talk_voting(input_file), f, indent=2)


@click.command(name='predict')
@click.option('-m', '--model-file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='Model file to load')
@click.option('-i', '--input-file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='JSON file containing parsed talk votes')
@click.option('-s', '--skip-voted/--no-skip-voted', default=True,
              show_default=True,
              help='Skips all voted talks.')
def cli_predict(model_file, input_file, skip_voted):
    '''Predict your interest in a single or multiple talks.'''
    with open(input_file, 'r') as f:
        talks = json.load(f)
        unvoted_proposals = [p for p in talks['proposals']
                             if not skip_voted or not p['vote']]
        with open(model_file, 'rb') as f:
            model = joblib.load(f)
        res = predict(model, unvoted_proposals)
        click.echo(json.dumps(res, indent=2))


@click.command(name='recommend')
@click.option('-i', '--input-file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='HTML talk voting file to parse')
@click.option('-s', '--skip-voted/--no-skip-voted', default=True,
              show_default=True,
              help='Skips all voted talks.')
def cli_recommend(input_file, skip_voted):
    '''Parse html, train model and predict unvoted talks.'''
    talks = parse_talk_voting(input_file)
    voted_proposals = [p for p in talks['proposals'] if p['vote']]
    proposals_to_predict = [p for p in talks['proposals']
                            if not skip_voted or not p['vote']]
    model = train_model(voted_proposals)
    for pred in predict(model, proposals_to_predict):
        click.echo(f'{pred["interest"]:.2f} {pred["title"]}')


@click.command(name='train')
@click.option('-i', '--input-file',
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              required=True, help='JSON file containing parsed talk votes')
@click.option('-m', '--model-file',
              type=click.Path(file_okay=True, dir_okay=False),
              required=True, help='Model file to save')
def cli_train(input_file, model_file):
    '''Train a model user your talk voting.'''
    with open(input_file, 'r') as f:
        talks = json.load(f)
        voted_proposals = [p for p in talks['proposals'] if p['vote']]
        model = train_model(voted_proposals)
        with open(model_file, 'wb') as f:
            joblib.dump(model, f)


main.add_command(cli_evaluate)
main.add_command(cli_parse)
main.add_command(cli_predict)
main.add_command(cli_recommend)
main.add_command(cli_train)


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
