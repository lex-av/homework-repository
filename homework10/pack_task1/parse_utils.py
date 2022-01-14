# -*- coding: utf-8 -*-

import asyncio
import json
import re
from multiprocessing import Pool

import aiohttp
import xmltodict
from bs4 import BeautifulSoup, SoupStrainer

from .connection_utils import float_normalizer


def urls_growth_parse(text_data):
    base_url = "https://markets.businessinsider.com"
    limiter = SoupStrainer("table")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    url_cells = soup.find("table", class_="table__layout--fixed").find_all("td", "table__td--big")
    table_rows = soup.find("table", class_="table__layout--fixed").find_all("tr")[1:]  # skip table header

    urls = []
    growth_percentages = []

    for cell in url_cells:
        urls.append(base_url + cell.find("a").get("href"))

    for row in table_rows:
        percentage_cell = row.find_all("td")[7]
        cell_value = percentage_cell.find_all("span")[1]
        growth_percentages.append(float_normalizer(cell_value.contents[0]))

    parsed_data = []

    for url, percentage in zip(urls, growth_percentages):
        parsed_data.append({"url": url, "year_growth": percentage})

    return parsed_data


def corp_name_parse(text_data):
    limiter = SoupStrainer("span")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    print("parsed some name")
    return soup.find("span", class_="price-section__label").contents[0]


def corp_code_parse(text_data):
    limiter = SoupStrainer("span")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    print("parsed some code")

    return soup.find("span", class_="price-section__category").find("span").contents[0].strip(",").strip(" ")


def corp_price_parse(text_data, rub_rate):
    limiter = SoupStrainer("div")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)

    try:
        price = float_normalizer(
            soup.find("div", text=re.compile("Prev. Close")).parent.text.strip().strip("Prev. Close").strip()
        )
        price = round(rub_rate * price, 2)
    except AttributeError:
        price = None

    print("parsed some price")
    return price


def corp_pe_parse(text_data):
    limiter = SoupStrainer("div")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)

    try:
        p_e = float_normalizer(
            soup.find("div", text=re.compile("P/E Ratio")).parent.text.strip().strip("P/E Ratio").strip()
        )
    except AttributeError:
        p_e = None

    print("parsed some PE")
    return p_e


def corp_max_profit_parse(text_data):
    limiter = SoupStrainer("div")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    tag_class_name_low = "snapshot__data-item snapshot__data-item--small"
    tag_class_name_high = "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"

    try:
        week_52_low = float_normalizer(soup.find_all("div", class_=tag_class_name_low)[1].contents[0].strip())
        week_52_high = float_normalizer(soup.find_all("div", class_=tag_class_name_high)[1].contents[0].strip())
        week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)
    except IndexError:
        try:
            week_52_low = float_normalizer(soup.find_all("div", class_=tag_class_name_low)[0].contents[0].strip())
            week_52_high = float_normalizer(soup.find_all("div", class_=tag_class_name_high)[0].contents[0].strip())
            week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)
        except IndexError:
            week_profit = None

    print("parsed some profits")
    return week_profit


class CorpDataParser:
    """Class to process and present data from MarketInsider"""

    def __init__(self, details_text_data, growth_table, cpu_count=6):
        self.cpu_count = cpu_count
        self.details_text_data = details_text_data
        self.growth_table = growth_table
        self.rub_rate = self._get_rate()

        self.corp_names = []
        self.corp_codes = []
        self.corp_prices = []
        self.pe_vals = []
        self.corp_max_profit_vals = []

        self.data_table = []

    def _get_rate(self):
        """Return valute rate for current date"""
        data = asyncio.run(self._get_req())
        rate_data = xmltodict.parse(data)
        usd = float(rate_data["ValCurs"]["Valute"][10]["Value"].replace(",", "."))
        return usd

    @staticmethod
    async def _get_req():
        """aiohttp getter for valute rate xml-data from bank api"""
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.cbr.ru/scripts/XML_daily.asp") as resp:
                response = await resp.text()
                return response

    def compute_data(self):
        with Pool(self.cpu_count) as p:
            self.corp_names = p.map(corp_name_parse, self.details_text_data)
            self.corp_codes = p.map(corp_code_parse, self.details_text_data)
            self.corp_prices = p.starmap(
                corp_price_parse, zip(self.details_text_data, [self.rub_rate] * len(self.details_text_data))
            )
            self.pe_vals = p.map(corp_pe_parse, self.details_text_data)
            self.corp_max_profit_vals = p.map(corp_max_profit_parse, self.details_text_data)

    def build_data_table(self):
        for name, code, price, pe, max_profit, growth in zip(
            self.corp_names,
            self.corp_codes,
            self.corp_prices,
            self.pe_vals,
            self.corp_max_profit_vals,
            self.growth_table,
        ):

            self.data_table.append(
                {
                    "code": code,
                    "name": name,
                    "price": price,
                    "growth": growth,
                    "PE": pe,
                    "max_profit": max_profit,
                }
            )

    def generate_top(self, parameter, rev=True, length=10):
        """
        Generates top ten corps from data_table by given parameter
        Cleans table from line with None values
        """
        remove_indexes = []

        for index, corp_data in enumerate(self.data_table):
            if corp_data["price"] is None or corp_data["PE"] is None or corp_data["max_profit"] is None:
                remove_indexes.append(index)
        for index in sorted(remove_indexes, reverse=True):
            self.data_table.pop(index)

        return sorted(self.data_table, key=lambda row: row[parameter], reverse=rev)[:length]

    @staticmethod
    def json_writer(dict_list, report_name):
        """Generates json-file, based on given report"""

        file_name = report_name + ".json"
        with open(file_name, "w") as report:
            json.dump(dict_list, report, indent=2)


if __name__ == "__main__":
    pass
