# Django DB serialization bug reproduction

A repository to reproduce a bug with serializing many to many through table models when using a database router and TransactionTestCase.

Confirmed on Django 4.2, 5.0, 5.1 and `main`.

---

Steps to recreate:

1. `django-admin startproject`
2. Create second database connection, pointing to the same database, but using `MIRROR` in tests
3. Create a database router to use the secondary connection for reads (outside of a transaction).
4. Create a model with a `ManyToManyField`, and create an instance in a migration
5. Create a test case which uses `TransactionTestCase`, `serialize_rollback = True`, and connects to both databases
6. Do not run migrations (the actual database shouldn't exist)

When running tests, you'll receive an error:

```
django.db.utils.OperationalError: no such table: auth_user
```

This seems to be because the serializer is attempting to connect to the actual database rather than the test instance. This can be confirmed by running `manage.py migrate` and re-running tests, which now work.
