#!/usr/bin/env python3
"""
8-all
"""


def list_all(mongo_collection):
    """List all documents in a collection

    Args:
         mongo_collection: The pymongo collection object.

    Returns:
         A list of documents in the collection, or an empty list if no documents.
    """
    return mongo_collection.find()
