=================
User Voting Rocks
=================


.. image:: https://img.shields.io/pypi/v/user_voting_rocks.svg
        :target: https://pypi.python.org/pypi/user_voting_rocks

.. image:: https://img.shields.io/travis/luphord/user_voting_rocks.svg
        :target: https://travis-ci.org/luphord/user_voting_rocks

.. image:: https://readthedocs.org/projects/user-voting-rocks/badge/?version=latest
        :target: https://user-voting-rocks.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Use your personal talk voting for PyConDE 2019 to predict your interest in a talk.


Installation
------------

In order to install the released version, use pip install:

.. code-block:: console

        pip install user_voting_rocks

In order to work with the current master, clone this respository, create + activate a virtual environment and then use pip install like this:

.. code-block:: console

        pip install -e .

Usage
-----

Vote for talks you are interested in using the PyConDE 2019 community voting link you have received.
Then reload the page (using your secret link) and save as `Pycon\ Voting.html` using your browser's *Save As* dialog.

To receive recommendations, please try

.. code-block:: console

        user_voting_rocks recommend -i ./Pycon\ Voting.html

This command will output the list of talks (that you have not yet voted on) by *decreasing* order of your predicted preference.

Full command line interface:

.. code-block:: console

        Usage: user_voting_rocks [OPTIONS] COMMAND [ARGS]...

        Commandline interface for user_voting_rocks.

        Options:
        --help  Show this message and exit.

        Commands:
        evaluate   Evaluate the talk voting classifier.
        parse      Parse talk voting html file.
        predict    Predict your interest in a single or multiple talks.
        recommend  Parse html, train model and predict unvoted talks.
        train      Train a model user your talk voting.


* Free software: MIT license
* Documentation: https://user-voting-rocks.readthedocs.io.


Features
--------

* Parse PyConDE 2019 community voting HTML page to JSON
* Train a Naive Bayes classifier on word frequencies of abstracts
* Custom stop word list
* Predict interest in a talk using the trained Naive Bayes classifier
* CLI for parsing, training and predicting with persistence for parsed content and model

Credits
-------

Main author and project maintainer is luphord_.

This package was prepared with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _luphord: https://github.com/luphord
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
