# -*- coding: utf-8 -*-
"""세 수집 결과 CSV를 한 행씩 대조한다. 실행: python3 code/스크래핑연습_결과대조_v1_20261110.py (폴더 261110-web-scraping-compare 에서)"""
import csv, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
FILES = {
    "1 클라우드 WebFetch": "스크래핑연습_mystery_books_클라우드다중페이지_v1_20261110.csv",
    "2 Claude in Chrome": "스크래핑연습_mystery_books_크롬다중페이지_v1_20261110.csv",
    "3-A 내장 브라우저": "스크래핑연습_mystery_books_내장브라우저다중페이지_v1_20261110.csv",
}
def load(name):
    lines = open(os.path.join(BASE, name), encoding="utf-8-sig").read().splitlines()[1:]  # 첫 줄 요약 제외
    return [tuple(r) for r in list(csv.reader(lines))[1:]]                            # 머리글 제외
data = {k: load(v) for k, v in FILES.items()}
for k, rows in data.items():
    print(f"{k}: {len(rows)}권, 가격 합계 £{sum(float(r[1][1:]) for r in rows):.2f}")
base = data["2 Claude in Chrome"]
for k, rows in data.items():
    print(f"{k} == 기준(2번): {rows == base}")
