from app.parsing.helpers import plural


class parser:

    @classmethod
    def parse_dollar_rate(cls, rate: int):
        if not rate:
            raise ValueError
        rate = str(rate)
        if "." in rate:
            rub, kop = rate.split(".")
            kop = kop[0:2]
            return plural(num=rub, ruble=True), plural(num=kop, ruble=False)
        return f"{rate}р"
