# -*- coding: utf-8 -*-

'''Console script for user_voting_rocks.'''
import sys
import json
import click

from .user_voting_rocks import parse_talk_voting


@click.group(name='user_voting_rocks')
def main(args=None):
    '''Commandline interface for user_voting_rocks.'''
    return 0


@click.command(name='parse')
@click.option('-i', '--input_file',
              type=click.Path(exists=True),
              required=True, help='HTML talk voting file to parse')
def cli_parse(input_file):
    '''Parse talk voting html file.'''
    click.echo(json.dumps(parse_talk_voting(input_file), indent=2))


@click.command(name='predict')
def cli_predict():
    '''Predict your interest in a single or multiple talks.'''
    raise NotImplementedError()


@click.command(name='train')
def cli_train():
    '''Train a model user your talk voting.'''
    raise NotImplementedError()


main.add_command(cli_parse)
main.add_command(cli_predict)
main.add_command(cli_train)


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
