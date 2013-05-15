=========================================================
 kurrency - Currency data and FOREX Utilities for Python
=========================================================

*kurrency* is a Python library which provides currency data and forex
utilities to applications. The data used in the library is obtained
from various resources including `Wikipedia
<http://www.wikipedia.org>`_, `Trading with Clancy
<http://tradingwithclancy.blogspot.sg/2012/04/currency-pairs.html>`_.

Installation
============

You can install the latest version of *kurrency* from the GitHub
repository::

    $ pip install git+https://github.com/telosoft/kurrency.git

Example Usage
=============

Import the canonical *Currency* class::

    >>> from kurrency import Currency

Retrieve a *Currency* object for a given identifier::

    >>> turkish_lira = Currency.get("TRY")

The identifier can be any of ``code``, ``enum`` or ``name`` attributes
of a *Currency* object::

TRY,'949,Turkish lira,2,2,TR

    >>> Currency.get("TRY") == Currency.get("949")
    True
    >>> Currency.get("949") == Currency.get("Turkish Lira")
    True

Quick API Reference
===================

.. todo:: Provide the FULL API reference.
