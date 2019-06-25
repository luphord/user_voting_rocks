# -*- coding: utf-8 -*-

'''Console script for user_voting_rocks.'''
import sys
import click


@click.group(name='user_voting_rocks')
def main(args=None):
    '''Commandline interface for user_voting_rocks.'''
    return 0


@click.command(name='train')
def cli_train():
    '''Train a model user your talk voting.'''
    raise NotImplementedError()


@click.command(name='predict')
def cli_predict():
    '''Predict your interest in a single or multiple talks.'''
    raise NotImplementedError()


main.add_command(cli_train)
main.add_command(cli_predict)


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
