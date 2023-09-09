#!/usr/bin/env python

import argparse
import datetime
import os

from collections import defaultdict
from lark import Lark

from sie4_transformer import Sie4Transformer

from model.sie4 import Flagga, Fnamn, Format, Gen, Ib, Konto, Kptyp, Orgnr, Program, Rar, Res, Sietyp, Sru, Ub, Ver, Trans


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "sie4.lark"), "r") as f:
    sie4_grammar = f.read()


def validate_ib_ub(rows):
    balances = defaultdict(lambda: 0)
    for row in rows:
        match row:
            case ib if type(ib) == Ib and ib.year == 0 and ib.account < 3000:
                balances[ib.account] = balances[ib.account] + ib.amount
            case ub if type(ub) == Ub and ub.year == 0 and ib.account < 3000:
                balances[ub.account] = balances[ub.account] - ub.amount
            case ver if type(ver) == Ver:
                for t in ver.transactions:
                    if t.account < 3000:
                        balances[t.account] = balances[t.account] + t.amount
    for account, amount in balances.items():
        assert amount == 0, f"Weird balance for {account}"


def generate_hledger_output(rows):
    vers = list([row for row in rows if type(row) == Ver])
    vers.sort(key=lambda ver: ver.number)

    for ver in vers:
        print(f"{ver.date.isoformat()} \"{ver.description}\"")
        for trans in ver.transactions:
            print(f"\t{trans.account}\t\tSEK {str(trans.amount)[0:-2]}.{str(trans.amount)[-2:]}")

        print("")


parser = argparse.ArgumentParser(description="SIE4 to ledger converter")
parser.add_argument("input")

args = parser.parse_args()

with open(args.input, "r", encoding="cp437") as f:
    sie4_parser = Lark(sie4_grammar)
    rows = Sie4Transformer().transform(sie4_parser.parse(f.read()))
    validate_ib_ub(rows)
    generate_hledger_output(rows)





