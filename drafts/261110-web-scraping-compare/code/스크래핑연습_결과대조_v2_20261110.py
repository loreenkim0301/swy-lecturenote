# -*- coding: utf-8 -*-
"""수집 결과 CSV를 한 행씩 대조한다 (v2: Travel·Mystery, 1차·2차 실행, 파이썬 결과 자동 포함).
실행: 폴더 261110-web-scraping-compare 에서  python3 code/스크래핑연습_결과대조_v2_20261110.py
"""
import csv, glob, os

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def load(path):
    lines = open(path, encoding="utf-8-sig").read().splitlines()[1:]   # 첫 줄 요약 제외
    return [tuple(r) for r in list(csv.reader(lines))[1:]]             # 머리글 제외

for cat in ["travel", "mystery"]:
    files = sorted(glob.glob(os.path.join(DATA, f"스크래핑연습_{cat}_books_*.csv")))
    if not files:
        continue
    results = {os.path.basename(p): load(p) for p in files}
    # 기준: 2차 실행 Claude in Chrome 결과 (코드가 HTML에서 직접 꺼낸 값)
    base_name = f"스크래핑연습_{cat}_books_크롬_v2_20261110.csv"
    base = results[base_name]
    print(f"\n[{cat}] 기준 = {base_name} ({len(base)}권)")
    for name, rows in results.items():
        total = sum(float(r[1].lstrip("£")) for r in rows)
        same = "동일" if rows == base else "다름"
        print(f"  {name}: {len(rows)}권, £{total:.2f} → {same}")
        if rows != base:
            for i, (x, y) in enumerate(zip(rows, base), 1):
                if x != y:
                    print(f"    {i}행 차이: {x} ≠ {y}")
