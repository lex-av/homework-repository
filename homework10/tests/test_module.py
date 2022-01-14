# -*- coding: utf-8 -*-

from unittest.mock import patch

from ..pack_task1.module_task1 import MarketsInsiderRawData
from ..pack_task1.parse_utils import CorpDataParser


def test_pos_build_data_table(html_3m_details_text_data, growth_table, fake_get_rate):
    """Checks if computing and building is alive"""
    data_table = CorpDataParser([html_3m_details_text_data], growth_table)
    with patch("homework10.pack_task1.parse_utils.CorpDataParser._get_rate", fake_get_rate):
        data_table.compute_data()
    data_table.build_data_table()


def test_pos_generate_top(html_3m_details_text_data, growth_table, data_table_fixture, fake_get_rate):
    """Checks if report is being build and not empty"""
    data_table = CorpDataParser([html_3m_details_text_data], growth_table)
    with patch("homework10.pack_task1.parse_utils.CorpDataParser._get_rate", fake_get_rate):
        data_table.compute_data()
    data_table.build_data_table()
    lst = data_table.generate_top("price", length=1)

    assert lst == data_table_fixture


def test_pos_complete_execution(html_3m_details_text_data, growth_table, data_table_fixture, fake_get_rate):
    def fake_collect_info(self):
        self.growth_values = growth_table
        self.details_text_data = html_3m_details_text_data

    with patch("homework10.pack_task1.parse_utils.CorpDataParser._get_rate", fake_get_rate):
        raw_data = MarketsInsiderRawData()

    with patch("homework10.pack_task1.module_task1.MarketsInsiderRawData.collect_info", fake_collect_info):
        raw_data.collect_info()

    details = raw_data.details_text_data
    growth = raw_data.growth_values
    data_table = CorpDataParser([details], growth)
    data_table.compute_data()
    data_table.build_data_table()
    lst = data_table.generate_top("price", length=1)
    assert lst == data_table_fixture
