#!/usr/bin/env python3
"""
insert with mongodb in python
"""


def insert_school(mongo_collection, **kwargs):
    """
     Insert a new document in a collectio

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The fields and values to insert as a document.

    Returns:
        The new document's _id.
    
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
