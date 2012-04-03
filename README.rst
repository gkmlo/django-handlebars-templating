====================
django-handlebars-templating
====================

Renders Handlebars templates in Django templates. For real-time web apps, the client side often needs to re-render certain parts of the HTML page. A popular approach is to store and load Mustache.js templates with ICanHaz.js on the client. Not to mention the nice things about the logic-less templates, it saves time and follows the DRY (Don't repeat yourself) principle when using the same templating engine in Django as well. This project aims to provide a reliable and consistent rendering of Handlebars.js (superset of Mustache.js) templates in Django as in Javascript.

Quickstart
==========

Dependencies
------------
.. _Django: http://www.djangoproject.com/
.. _Python: http://www.python.org/
.. _PyBars:  http://pypi.python.org/pypi/pybars/0.0.1
 
Installation
------------
pip install -e git+git@github.com:gkmlo/django-handlebars-templating.git#egg=django-handlebars-templating

Usage
-----
* Add ``"handlebars-templating"`` to your ``INSTALLED_APPS`` setting.
* By default it searches for handlebars templates in a directory named ``/js/templates`` in ``STATIC_DIR``.
* Add ``{% load handlebars %}`` and use ``{% handlebars "templatename" %}`` in your Django templates.
