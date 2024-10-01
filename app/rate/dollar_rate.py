from app.rate.rate import Rate


class Dollar_Rate:

    def __init__(self, url: str = 'https://www.cbr-xml-daily.ru/daily_json.js'):
        self.url = url
        self.rate = Rate
        self.rate.url = self.url

    async def get_dollar_rate(self):
        data = await self.rate.get_rate()
        return data['Valute']['USD']['Value']
