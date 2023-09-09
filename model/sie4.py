import datetime

from pydantic import BaseModel


class Flagga(BaseModel):
    flagga: int


class Fnamn(BaseModel):
    fnamn: str


class Format(BaseModel):
    pass


class Gen(BaseModel):
    date: datetime.date


class Ib(BaseModel):
    year: int
    account: int
    amount: int


class Konto(BaseModel):
    account: int
    description: str


class Kptyp(BaseModel):
    kptyp: str


class Orgnr(BaseModel):
    orgnr: str


class Program(BaseModel):
    name: str
    version: int


class Rar(BaseModel):
    year: int
    start: datetime.date
    stop: datetime.date

class Res(BaseModel):
    year: int
    account: int
    amount: int


class Sietyp(BaseModel):
    version: int


class Sru(BaseModel):
    account: int
    code: int


class Ub(BaseModel):
    year: int
    account: int
    amount: int


class Trans(BaseModel):
    account: int
    amount: int


class Ver(BaseModel):
    serie: str
    number: int
    date: datetime.date
    description: str
    transactions: list[Trans]

