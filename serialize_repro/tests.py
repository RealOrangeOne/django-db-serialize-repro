from django.test import TransactionTestCase


class TestTestCase(TransactionTestCase):
    databases = "__all__"

    serialized_rollback = True

    def test_empty(self):
        pass
