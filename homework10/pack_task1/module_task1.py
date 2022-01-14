"""
    Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
    https://markets.businessinsider.com/index/components/s&p_500

    Подробно про задание:
    https://github.com/lex-av/epam_python_autumn_2020/blob/main/lecture_10_parallelization/hw/stonks.md
"""


import asyncio

import aiohttp

from homework10.pack_task1.connection_utils import (
    get_base_response_text,
    get_page_count,
    get_page_links,
)
from homework10.pack_task1.parse_utils import urls_growth_parse


class MarketsInsiderRawData:
    """Class for getting all the data as responses.text"""

    def __init__(self, fixed_page_count=None):
        self.fixed_page_count = fixed_page_count

    def collect_info(self):
        self.base_resp_text = get_base_response_text()
        self.page_count = get_page_count(self.base_resp_text, self.fixed_page_count)
        self.page_links = get_page_links(self.page_count)
        self.pages_text_data = self._build_response_list(self.page_links)

        self.links_growth_data = []
        for text_data in self.pages_text_data:
            self.links_growth_data += urls_growth_parse(text_data)

        self.details_links = [corp["url"] for corp in self.links_growth_data]
        self.growth_values = [corp["year_growth"] for corp in self.links_growth_data]
        self.details_text_data = self._build_response_list(self.details_links)

    @staticmethod
    async def _get_request_text(session, url):
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.text()

    async def _get_multiple_requests_text(self, url_list):
        async with aiohttp.ClientSession() as session:
            task_list = []
            for url in url_list:
                task = asyncio.create_task(self._get_request_text(session, url))
                task_list.append(task)
            return await asyncio.gather(*task_list)

    def _build_response_list(self, url_list):
        return asyncio.run(self._get_multiple_requests_text(url_list))


if __name__ == "__main__":
    pass
