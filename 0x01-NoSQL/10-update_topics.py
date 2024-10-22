#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (list): A list of topics to set.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
