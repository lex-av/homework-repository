# -*- coding: utf-8 -*-

from unittest import mock

import pytest

from ..pack_task2.module_task2 import count_dots_on_i


@mock.patch("homework4.pack_task2.module_task2.get_info_from_url")
def test_positive_count_dots_on_i(mock_get_info_from_url):
    get_url_str = ""
    with open("test_data/example_domain.txt") as src:
        for line in src:
            get_url_str += line

    mock_get_info_from_url.return_value = get_url_str
    assert count_dots_on_i("https://example.com/") == 59


def test_network_error():
    with pytest.raises(ValueError):
        assert count_dots_on_i("https://exampleeeee.com/")
