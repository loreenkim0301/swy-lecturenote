# -*- coding: utf-8 -*-
"""
스크래핑연습_books_toscrape_다중페이지_v1_20261110
- 대상: https://books.toscrape.com (웹 스크래핑 연습용 데모 사이트)
- 하는 일: 시작 페이지부터 '다음(next)' 버튼을 따라가며 모든 페이지의 책을 모아 CSV로 저장
- 선택: 상세 페이지까지 들어가 재고 '수량'을 가져올 수 있음 (FETCH_DETAIL = True)

[준비] 터미널에서 한 번만 실행:
    pip install requests beautifulsoup4
[실행]
    python 스크래핑연습_books_toscrape_다중페이지_v1_20261110.py
"""

import csv
import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# ─── 설정 (여기만 바꾸면 됨) ─────────────────────────────
# 카테고리 하나: .../category/books/travel_2/index.html
# 사이트 전체(1,000권, 50페이지): https://books.toscrape.com/catalogue/page-1.html
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
OUTPUT_FILE = "books_all.csv"
FETCH_DETAIL = False   # True면 책마다 상세 페이지를 열어 재고 수량까지 수집 (요청 수가 크게 늘어남)
DELAY_SEC = 1.0        # 요청 사이 쉬는 시간(초). 사이트에 부담을 주지 않기 위한 예의
MAX_PAGES = 100        # 혹시 모를 무한 반복 방지용 안전장치
NEED_CHECK = "[확인 필요]"
# ───────────────────────────────────────────────────────

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (scraping practice)"


def get_soup(url):
    """주소 하나를 받아와서 HTML을 분석 가능한 형태로 돌려준다."""
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    resp.encoding = "utf-8"  # 이 줄이 없으면 £ 기호가 'Â£'로 깨질 수 있음
    return BeautifulSoup(resp.text, "html.parser")


def text_or_check(tag):
    return tag.get_text(strip=True) if tag else NEED_CHECK


def get_stock_count(detail_url):
    """상세 페이지의 'In stock (19 available)'에서 숫자만 꺼낸다."""
    soup = get_soup(detail_url)
    raw = text_or_check(soup.select_one("p.instock.availability"))
    m = re.search(r"\((\d+) available\)", raw)
    return m.group(1) if m else NEED_CHECK


def crawl(start_url):
    books, url, page_no = [], start_url, 0

    while url and page_no < MAX_PAGES:
        page_no += 1
        print(f"[{page_no}페이지] {url}")
        soup = get_soup(url)

        for card in soup.select("article.product_pod"):
            link = card.select_one("h3 a")
            # 화면 글자는 잘려 있으므로 title 속성의 전체 제목을 사용
            title = link.get("title") if link and link.get("title") else NEED_CHECK
            price = text_or_check(card.select_one("p.price_color"))
            stock = text_or_check(card.select_one("p.instock.availability"))
            row = {"제목": title, "가격": price, "재고": stock}

            if FETCH_DETAIL and link:
                detail_url = urljoin(url, link["href"])  # 상대 주소 → 전체 주소
                row["재고수량"] = get_stock_count(detail_url)
                time.sleep(DELAY_SEC)

            books.append(row)

        # 핵심: '다음' 버튼이 있으면 그 주소로 이동, 없으면 반복 종료
        next_link = soup.select_one("li.next a")
        url = urljoin(url, next_link["href"]) if next_link else None
        time.sleep(DELAY_SEC)

    return books, page_no


def save_csv(books, pages, path):
    fields = ["제목", "가격", "재고"] + (["재고수량"] if FETCH_DETAIL else [])
    # utf-8-sig: 엑셀에서 더블클릭해도 한글·£가 깨지지 않게 하는 저장 방식
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        f.write(f"페이지를 읽었는지: {'예' if books else '아니요'}, "
                f"모은 책 {len(books)}권 (읽은 페이지 {pages}개)\n")
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    try:
        result, pages = crawl(START_URL)
    except requests.RequestException as e:
        print("접속 실패:", e)
        result, pages = [], 0
    save_csv(result, pages, OUTPUT_FILE)
    print(f"완료: {len(result)}권 → {OUTPUT_FILE}")
