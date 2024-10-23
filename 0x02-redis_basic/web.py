#!/usr/bin/env python3
"""
Web caching module using Redis.
"""

import redis
import requests
import time

class WebCache:
    """
    A class to represent a web cache using Redis.
    """

    def __init__(self):
        """
        Initializes the WebCache class with a Redis client.
        """
        self._redis = redis.Redis()

    def get_page(self, url: str) -> str:
        """
        Retrieves the HTML content of a URL, caching the result for 10 seconds.

        Args:
            url: The URL to fetch the HTML content from.

        Returns:
            str: The HTML content of the page.
        """
        # Check if the content is already cached
        cached_content = self._redis.get(url)
        if cached_content:
            # Increment the count for the accessed URL
            self._redis.incr(f'count:{url}')
            return cached_content.decode('utf-8')

        # Fetch the content if not cached
        response = requests.get(url)
        if response.status_code == 200:
            # Cache the content with an expiration time of 10 seconds
            self._redis.setex(url, 10, response.text)
            self._redis.incr(f'count:{url}')
            return response.text
        else:
            return ""

# Optional: Decorator for caching
def cache_page(func):
    """
    Decorator to cache the result of the get_page function.
    """
    def wrapper(url: str) -> str:
        web_cache = WebCache()
        cached_content = web_cache._redis.get(url)
        if cached_content:
            web_cache._redis.incr(f'count:{url}')
            return cached_content.decode('utf-8')
        
        content = func(url)
        web_cache._redis.setex(url, 10, content)
        web_cache._redis.incr(f'count:{url}')
        return content
    return wrapper

# Example usage
@cache_page
def fetch_page(url: str) -> str:
    """
    Fetches the HTML content of a URL.

    Args:
        url: The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
