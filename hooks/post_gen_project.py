#!/usr/bin/env python
# -*- coding: utf-8 -*-

# example: https://github.com/pydanny/cookiecutter-django/blob/master/hooks/post_gen_project.py

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    pass
    #if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
    #    remove_file('travis_pypi_setup.py')
