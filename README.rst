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

.. code-block:: console

        Usage: user_voting_rocks [OPTIONS] COMMAND [ARGS]...

        Commandline interface for user_voting_rocks.

        Options:
        --help  Show this message and exit.

        Commands:
        parse    Parse talk voting html file.
        predict  Predict your interest in a single or multiple talks.
        train    Train a model user your talk voting.


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
