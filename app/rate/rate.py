import aiohttp
from pprint import pprint
import asyncio


class Rate:

    _url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str):
        if not value:
            raise ValueError
        self._url = value


    @classmethod
    async def get_rate(cls):
        async with aiohttp.ClientSession() as session:
            async with session.get(url = cls._url) as response:
                rate = await response.json(content_type="application/javascript")
                return rate
