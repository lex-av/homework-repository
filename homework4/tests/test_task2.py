# -*- coding: utf-8 -*-

import os
from unittest import mock

import pytest

from homework4.pack_task2.module_task2 import count_dots_on_i


def test_pos_count_dots_on_i():
    path_to_hws = os.getcwd()

    with open(path_to_hws + "/homework4/tests/test_data/example_domain.txt") as src:
        html_data = src.read()

    # Implement fake response getter, mock status code and text
    def fake_get(url):
        fake_response = mock.Mock()
        fake_response.read = mock.Mock(return_value=html_data)
        fake_response.getcode = mock.Mock(return_value=200)
        return fake_response

    # Run count_dots with fake resp getter
    with mock.patch("homework4.pack_task2.module_task2.get_url_response", fake_get):
        assert count_dots_on_i("https://example.com/") == 59


def test_neg_network_error():
    # Implement fake response getter, mock status code only
    def fake_get(url):
        fake_response = mock.Mock()
        fake_response.getcode = mock.Mock(return_value=404)
        return fake_response

    # Run count_dots with fake resp getter
    with mock.patch("homework4.pack_task2.module_task2.get_url_response", fake_get):
        with pytest.raises(ValueError):
            assert count_dots_on_i("https://exampleeeee.com/")
