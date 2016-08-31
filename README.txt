.. image:: https://img.shields.io/codeship/a4d04cb0-51e6-0134-0d6b-325cd45b0ee2/default.svg
   :target: https://bitbucket.org/hellwig/django-query-signals
.. image:: https://coveralls.io/repos/bitbucket/hellwig/django-query-signals/badge.svg?branch=default 
   :target: https://coveralls.io/bitbucket/hellwig/django-query-signals?branch=default
.. image:: https://img.shields.io/pypi/v/django-query-signals.svg
   :target: https://pypi.python.org/pypi/Django-Query-Signals/
.. image:: https://img.shields.io/badge/Donate-PayPal-blue.svg
   :target: https://paypal.me/MartinHellwig
.. image:: https://img.shields.io/badge/Donate-Patreon-orange.svg
   :target: https://www.patreon.com/hellwig
   

####################
Django Query Signals
####################

What is it?
===========
A library that will send signals on queryset data manipulation methods. 

What problem does it solve?
===========================
Django sends many signals, including when a model instance is created, deleted
and updated. However when using bulk methods like bulk_create or delete. There
is no signal send, with this library signals are send on the following methods:

- bulk_create
- delete 
- get_or_create
- update_or_create
- update

A signal will be send before and after the method is executed.

How do I install it?
====================
.. sourcecode:: shell

  pip install django-query-signals


Adding to Django (using integrator)
-----------------------------------
.. sourcecode:: shell

  >>> import django_integrator
  >>> django_integrator.add_application('django_query_signals')

If you don't want to use the above, you can just add 'django_query_signals' to
your installed apps.

How do I use it?
================
From the namespace django_query_signals you can import the below signals which
you can connect to via the usual way.

 - pre_bulk_create
 - post_bulk_create,
 - pre_delete
 - post_delete
 - pre_get_or_create
 - post_get_or_create
 - pre_update_or_create
 - post_update_or_create
 - pre_update
 - post_update

For example:

.. sourcecode:: shell

  >>> @receiver(post_bulk_create)
  >>> def callback(signal, sender, args):
  >>>       pass

The argument 'signal' is the signal that is connected, 'sender' is the
underlying model class and 'args' is a dictionary which the method in queryset
is called with, this is supplemented with 'self' which contains the queryset
instance and if the connecting signal is a 'post' type the key 'return' is also
added which contains the value the method has returned. 

If you connect to the 'pre' type signal, changing the 'args' and 'self' will
also change the actual execution of the method.

Caveat
======
This library relies on monkey patching django.db.models.query.QuerySet, thus if
your instance also monkey patches the same thing or you use a custom QuerySet in
your Manager, then there is a good chance that this library will not work at all
for you, however most likely you can work around this issue by examining the
signals.py file in this library.  

What license is this?
=====================
Two-clause BSD


How can I get support?
======================
Please use the repo's bug tracker to leave behind any questions, feedback,
suggestions and comments. I will handle them depending on my time and what looks
interesting. If you require guaranteed support please contact me via
e-mail so we can discuss appropriate compensation.


Signing Off
===========
Is my work helpful or valuable to you? You can repay me by donating via:

https://paypal.me/MartinHellwig

.. image:: https://img.shields.io/badge/PayPal-MartinHellwig-blue.svg
  :target: https://paypal.me/MartinHellwig
  :alt: Donate via PayPal.Me
  :scale: 120 %

-or-

https://www.patreon.com/hellwig

.. image:: https://img.shields.io/badge/Patreon-hellwig-orange.svg
  :target: https://www.patreon.com/hellwig
  :alt: Donate via Patreon
  :scale: 120 %


Thank you!