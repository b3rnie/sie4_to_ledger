import datetime

from lark import Transformer, v_args
from model.sie4 import Flagga, Fnamn, Format, Gen, Ib, Konto, Kptyp, Orgnr, Program, Rar, Res, Sietyp, Sru, Ub, Ver, Trans


class Sie4Transformer(Transformer):
    start = list
    INT = int
    POSITIVE_INT = int

    def ESCAPED_STRING(self, s):
        return s[1:-1]

    def AMOUNT(self, n):
        return int(n.replace(".", ""))

    def DATE(self, date):
        return datetime.datetime.strptime(date, "%Y%m%d").date()

    @v_args(inline=True)
    def flagga(self, flagga):
        return Flagga(flagga=flagga)

    @v_args(inline=True)
    def fnamn(self, fnamn):
        return Fnamn(fnamn=fnamn)

    @v_args(inline=True)
    def format(self):
        return Format()

    @v_args(inline=True)
    def gen(self, date):
        return Gen(date=date)

    @v_args(inline=True)
    def ib(self, year, account, amount):
        return Ib(year=year, account=account, amount=amount)

    @v_args(inline=True)
    def konto(self, account, description):
        return Konto(account=account, description=description)

    @v_args(inline=True)
    def kptyp(self, kptyp):
        return Kptyp(kptyp=kptyp)

    @v_args(inline=True)
    def orgnr(self, orgnr):
        return Orgnr(orgnr=orgnr)

    @v_args(inline=True)
    def program(self, name, version):
        return Program(name=name, version=version)

    @v_args(inline=True)
    def rar(self, year, start, stop):
        return Rar(year=year, start=start, stop=stop)

    @v_args(inline=True)
    def res(self, year, account, amount):
        return Res(year=year, account=account, amount=amount)

    @v_args(inline=True)
    def sietyp(self, version):
        return Sietyp(version=version)

    @v_args(inline=True)
    def sru(self, account, code):
        return Sru(account=account, code=code)

    @v_args(inline=True)
    def ub(self, year, account, amount):
        return Ub(year=year, account=account, amount=amount)

    @v_args(inline=True)
    def ver(self, serie, number, date, description, added_date, *transactions):
        return Ver(serie=serie, number=number, date=date, description=description, transactions=list(transactions))

    @v_args(inline=True)
    def trans(self, account, amount):
        return Trans(account=account, amount=amount)
