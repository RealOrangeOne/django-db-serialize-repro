from django.db import transaction

class ReadReplicaRouter:
    def db_for_read(self, model, **hints):
        if not transaction.get_autocommit(using="default"):
            # In a transaction, use the write database
            return "default"

        return "replica"
