#!/usr/bin/env python3
"""
Cache class for Redis operations.
"""

import redis
import uuid

class Cache:
    """
    A class to represent a Cache using Redis.
    """

    def __init__(self):
        """
        Initializes the Cache class with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        Stores data in Redis and returns the generated key.

        Args:
            data: The data to be stored, can be a string, bytes, int, or float.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key
