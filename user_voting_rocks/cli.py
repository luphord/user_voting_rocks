# -*- coding: utf-8 -*-

'''Console script for user_voting_rocks.'''
import sys
import click


@click.command()
def main(args=None):
    '''Console script for user_voting_rocks.'''
    click.echo('Replace this message by putting your code into '
               'user_voting_rocks.cli.main')
    click.echo('See click documentation at http://click.pocoo.org/')
    return 0


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
