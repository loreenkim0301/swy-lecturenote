# -*- coding: utf-8 -*-
"""
스크래핑연습_파이썬수집_v2_20261110
- 실행 환경: Claude 데스크톱 앱의 <Claude Code> 탭 (Claude Code가 내 컴퓨터에서 명령을 실행)
- 하는 일: Travel·Mystery 카테고리를 '다음(next)' 버튼을 따라가며 수집해 data/ 폴더에 CSV로 저장
- 저장 파일: data/스크래핑연습_travel_books_파이썬_v2_20261110.csv
            data/스크래핑연습_mystery_books_파이썬_v2_20261110.csv
  → 대조 스크립트(스크래핑연습_결과대조_v2_20261110.py)가 이 파일들을 자동으로 함께 비교함

[준비] pip install requests beautifulsoup4
[실행] 폴더 261110-web-scraping-compare 에서  python3 code/스크래핑연습_파이썬수집_v2_20261110.py
"""
import csv, os, time
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

CATEGORIES = {
    "travel": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "mystery": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
}
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
DELAY_SEC = 1.0
NEED_CHECK = "[확인 필요]"
KST = timezone(timedelta(hours=9))

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (scraping practice)"


def get_soup(url):
    r = session.get(url, timeout=15)
    r.raise_for_status()
    r.encoding = "utf-8"
    return BeautifulSoup(r.text, "html.parser")


def text_or_check(tag):
    return tag.get_text(strip=True) if tag else NEED_CHECK


def crawl(start):
    rows, url, pages, total = [], start, 0, NEED_CHECK
    while url:
        pages += 1
        soup = get_soup(url)
        if pages == 1:
            strong = soup.select_one("form.form-horizontal strong")
            total = strong.get_text(strip=True) if strong else NEED_CHECK
        for card in soup.select("article.product_pod"):
            a = card.select_one("h3 a")
            rows.append([
                a.get("title") if a and a.get("title") else NEED_CHECK,
                text_or_check(card.select_one("p.price_color")),
                text_or_check(card.select_one("p.instock.availability")),
            ])
        nxt = soup.select_one("li.next a")
        url = urljoin(url, nxt["href"]) if nxt else None
        time.sleep(DELAY_SEC)
    return rows, pages, total


def main():
    started = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")
    for cat, start in CATEGORIES.items():
        try:
            rows, pages, total = crawl(start)
            read = "예"
        except requests.RequestException as e:
            print(f"[{cat}] 접속 실패: {e}")
            rows, pages, total, read = [], 0, NEED_CHECK, "아니요"
        match = "일치" if str(len(rows)) == str(total) else "불일치"
        path = os.path.join(DATA, f"스크래핑연습_{cat}_books_파이썬_v2_20261110.csv")
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            f.write(f"페이지를 읽었는지: {read}, 모은 책 {len(rows)}권 "
                    f"(읽은 페이지 {pages}개 / 사이트 표기 {total}권과 {match}) · 실행 {started}\n")
            w = csv.writer(f)
            w.writerow(["제목", "가격", "재고"])
            w.writerows(rows)
        print(f"[{cat}] {len(rows)}권 → {path}")


if __name__ == "__main__":
    main()
