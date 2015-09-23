# backend-phonenumber-field

A Django library which interfaces with [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) to validate, pretty print and convert phone numbers. [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) is a port of Google's [libphonenumber](https://code.google.com/p/libphonenumber/) library, which powers Android's phone number handling.

Included are:

* ``PhoneNumber``, a pythonic wrapper around ``python-phonenumbers`` ``PhoneNumber`` class
* ``PhoneNumberField``, a model field
* ``PhoneNumberField``, a form field

## Basic usage

Use it like any regular model field

    from phonenumber_field.modelfields import PhoneNumberField

    class MyModel(models.Model):
        name = models.CharField(max_length=255)
        phone_number = PhoneNumberField()
        fax_number = PhoneNumberField(blank=True)

Internally, PhoneNumberField is based upon ``CharField`` and by default
represents the number as a string of an international phonenumber in the database (e.g
``'+557198765432'``).

Representation can be set by ``PHONENUMBER_DB_FORMAT`` variable in django settings module.
This variable must be one of  ``'E164'``, ``'INTERNATIONAL'``, ``'NATIONAL'`` or ``'RFC3966'``.
Recommended is one of the globally meaningful formats  ``'E164'``, ``'INTERNATIONAL'`` or
``'RFC3966'``. ``'NATIONAL'`` format require to set up ``PHONENUMBER_DEFAULT_REGION`` variable.

As with ``CharField``'s, it is discouraged to use ``null=True``.

The object returned is a PhoneNumber instance, not a string. If strings are used to initialize it,
e.g. via ``MyModel(phone_number='+557198765432')`` or form handling, it has to be a phone number
with country code.

because the object returned is a PhoneNumber instance, you can do interesting stuff like

    instance = MyModel(phone_number='+557198765432')
    print instance.phone_number.as_national
    (71) 9876-5432
