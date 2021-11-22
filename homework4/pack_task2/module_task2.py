# -*- coding: utf-8 -*-
"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
 count_dots_on_i("https://example.com/")
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""


import urllib.request
from collections import Counter


def get_info_from_url(_url: str) -> str:
    try:
        file_html = urllib.request.urlopen(_url)
    except Exception:
        raise ValueError(f"Unreachable {_url}")

    file_html = str(file_html.read())

    return file_html


def count_dots_on_i(url: str) -> int:
    """
    Returns count of i symbols in html document. Will raise ValueError
    on any network error
    """

    file_html = get_info_from_url(url)
    count_i = Counter(file_html)['i']

    return count_i


if __name__ == '__main__':
    print(count_dots_on_i("https://example.com/"))
