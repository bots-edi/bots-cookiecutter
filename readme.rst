=================
bots-cookiecutter
=================

.. toctree::
   :maxdepth: 1
   readme


Introduction
============
``Cookiecutter`` is a tool to create projects from project-templates, e.g. Python package projects.
``bots-cookiecutter`` is a cookiecutter-template to generate
the file- and directory structure for a bots-instance. It will generate config/, botsys, and usersys-directories.


Current Version
===============
The current version of ``bots-cookiecutter`` is

.. include:: version.rst


Installation
============

The installation of ``cookiecutter`` and the templates is done in following steps::

 1. Create a new miniconda-environment.
 2. Install the cookiecutter-package.
 3. Pull in the templates you want to use.
 4. Use the cookie-cutter template to create a new project.


Here is an example session:

.. code-block:: bash

  # create a new miniconda-environment
  > cd /opt/miniconda/
  > bin/conda create --name cookiecutter python=2
  > cd envs/cookiecutter

  # install the cookiecutter pythonpackage
  > bin/pip install cookiecutter

  # get the template you want to use
  > mkdir templates
  > cd templates
  > git clone https://github.com/bots-edi/bots-cookiecutter.git

Now you are ready to use the template:

.. code-block:: bash

    > bin/cookiecutter templates/bots-cookiecutter


Personal config-file
--------------------

.. code-block:: bash

  > cd ~
  > vi .cookiecutterrc

    default_context:
        instance_name: "bots


Usage
=====
Now you are ready to start using the template:

.. code-block:: bash

    > bin/cookiecutter templates/bots-cookiecutter


Fill out the ``readme.rst``.


Rationale
=========

The decisions ``bots-cookiecutter`` makes should all be explained here.

- ``readme.rst``

  - readme.rst should use reStructuredText format
  This is the format used by most Python tools, is expected by [setuptools](http://pythonhosted.org/setuptools/), and can be used by [Sphinx](http://sphinx-doc.org/).


.. include changes.rst
.. include:: changes.rst

.. include contributors.rst
.. include:: contributors.rst

.. include license.rst
.. include:: license.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

.. * :ref:`modindex`
