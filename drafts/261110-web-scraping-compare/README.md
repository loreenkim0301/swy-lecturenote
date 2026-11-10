# 스크래핑연습_수집환경별대조실습_v1_20261110 (내부용)

- 작성: 김수정(셀렉트웨이) · 실습 실행: Claude · 작성일: 2026-11-10 KST
- 실습 대상: books.toscrape.com Mystery 카테고리 (2페이지, 32권, 웹 스크래핑 연습용 데모 사이트)
- 수집 항목: 제목(잘리지 않은 전체 제목), 가격, 재고

## 0. 결론 요약

| 상태 | 방법 | 실행 결과 | 수집 권수 | 가격 합계 | 기준(2번)과 동일 |
|---|---|---|---|---|---|
| 1. 채팅만 | 클라우드 WebFetch로 페이지마다 읽기 | 성공 | 32 | £1,015.01 | 동일 |
| 2. 채팅 + Claude in Chrome | 로린님 크롬에서 JS로 다음 페이지 따라가기 | 성공 | 32 | £1,015.01 | (기준) |
| 3-A. 데스크톱 앱 | 내장 브라우저에서 같은 JS 실행 | 성공 | 32 | £1,015.01 | 동일 |
| 3-B. 데스크톱 앱 | 컴퓨터 유즈로 터미널에서 파이썬 실행 | 불가 | - | - | 비교 불가 |

- 1, 2, 3-A 세 결과는 32행 전부 제목·가격·재고·순서까지 같았다 (파이썬으로 행별 자동 대조).
- 3-B는 실행하지 못했다. 컴퓨터 유즈에서 터미널은 'click' 등급으로만 허용된다. 화면 보기와 왼쪽 클릭만 되고, 글자 입력·키 누르기·붙여넣기가 막혀 있어 명령을 칠 수 없다. 안전장치이므로 우회하지 않았다.
- 따라서 "4가지 모두 동일"은 아니다. 실행된 3가지가 동일했다.

## 1. 상태 1 — Claude 채팅 기능만 사용

**원리:** Anthropic 서버가 페이지를 받아 AI가 정리해 준다. 다음 페이지는 Claude가 주소를 보고 한 번 더 호출한다.

**실습 프롬프트**

```
아래 주소의 책 목록을 읽고 CSV로 정리해 줘.
주소: https://books.toscrape.com/catalogue/category/books/mystery_3/index.html
열: 제목(잘리지 않은 전체 제목, 링크의 title 속성), 가격, 재고
"next" 링크가 있으면 다음 페이지도 계속 읽고, 없으면 멈춰.
페이지에서 확인할 수 없는 칸은 [확인 필요]로 남기고, 값을 짐작하지 마.
파일 첫 줄에 '페이지를 읽었는지(예/아니요), 모은 책 ○권'을 써 줘.
```

**코드:** 없음 (Claude가 WebFetch 도구를 페이지마다 호출)

**주의:** 결과를 AI가 요약해서 주기 때문에 대량·정밀 수집의 기준값으로 쓰지 않는다. 다른 방법으로 검증할 것.

## 2. 상태 2 — 채팅 + Claude in Chrome 확장 프로그램

**원리:** 로린님 크롬에서 페이지를 연 뒤, 페이지 안에서 자바스크립트를 실행한다. 코드가 HTML 태그에서 값을 그대로 꺼낸다(AI 해석 없음).

**실습 프롬프트**

```
Claude in Chrome으로 아래 주소를 새 탭에서 열어 줘.
https://books.toscrape.com/catalogue/category/books/mystery_3/index.html
페이지 안에서 자바스크립트로 "next" 링크를 따라가며 모든 페이지의 책을 모아 줘.
제목은 링크의 title 속성, 가격은 p.price_color, 재고는 p.instock.availability에서 가져와.
끝나면 CSV로 만들어 주고, 사이트에 표시된 전체 권수와 맞는지 확인해 줘. 다 쓴 탭은 닫아 줘.
```

**코드 (브라우저 콘솔에서도 그대로 실행 가능)**

```javascript
const out = []; let u = location.href; let p = 0;
while (u) {
  p++;
  const d = new DOMParser().parseFromString(await (await fetch(u)).text(), 'text/html');
  d.querySelectorAll('article.product_pod').forEach(c => out.push([
    c.querySelector('h3 a')?.getAttribute('title') ?? '[확인 필요]',
    c.querySelector('p.price_color')?.textContent.trim() ?? '[확인 필요]',
    c.querySelector('p.instock.availability')?.textContent.trim() ?? '[확인 필요]'
  ].join('|')));
  const n = d.querySelector('li.next a');
  u = n ? new URL(n.getAttribute('href'), u).href : null;
}
'PAGES=' + p + ' COUNT=' + out.length + '\n' + out.join('\n');
```

**실습 중 생긴 시행착오 (교안 포인트)**
1. 코드를 `(async () => { ... })()`로 감싸면 도구가 결과를 기다리지 않아 빈 값 `{}`이 돌아왔다 → 감싸지 않고 맨 위에서 await 사용.
2. 결과가 길면 화면에서 잘렸다 → 나눠서 받거나 결과를 짧은 형식(| 구분)으로 출력.

## 3. 상태 3 — Claude 데스크톱 앱 설치

### 3-A. 내장 브라우저로 수집

**원리:** 데스크톱 앱 안의 별도 브라우저 창에서 상태 2와 같은 자바스크립트를 실행한다. 로린님 크롬과 로그인 상태가 분리되어 있다.

**실습 프롬프트**

```
Claude 데스크톱 앱의 내장 브라우저로 아래 주소를 열어 줘. (Claude in Chrome은 쓰지 마)
https://books.toscrape.com/catalogue/category/books/mystery_3/index.html
페이지 안에서 자바스크립트로 "next" 링크를 따라가며 모든 페이지의 책(제목·가격·재고)을 모아 CSV로 만들어 줘.
```

**코드:** 상태 2와 동일

**결과:** 성공, 32권, 상태 2와 완전히 동일.

### 3-B. 컴퓨터 유즈로 터미널에서 파이썬 실행

**원리(계획):** Claude가 맥 화면을 보고 터미널 앱에 명령을 입력해 파이썬 스크립트를 실행한다.

**실습 프롬프트 (시도용)**

```
컴퓨터 유즈로 맥의 터미널 앱을 열고,
python3 스크래핑연습_books_toscrape_다중페이지_v1_20261110.py 를 실행해 줘.
```

**확인 결과: 불가**
- 터미널은 컴퓨터 유즈에서 'click' 등급으로만 허용된다 (보기·왼쪽 클릭만 가능, 입력·키·붙여넣기 차단).
- 터미널이나 코드 편집기(VS Code 등)에 Claude가 화면 조작으로 명령을 치는 것은 의도적으로 막혀 있다.
- 대안: ① 로린님이 터미널에서 직접 실행, ② Claude Code처럼 셸 명령 도구가 있는 환경을 쓴다.

**코드 (로린님 직접 실행용, `pip install requests beautifulsoup4` 필요)** — 별도 파일: 스크래핑연습_books_toscrape_다중페이지_v1_20261110.py

## 4. 교안에 넣을 메시지

1. 같은 결과를 얻는 길이 여러 개다. 어떤 도구가 설치되어 있는지가 선택지를 정한다.
2. AI가 읽은 값(상태 1)은 코드가 꺼낸 값(상태 2·3-A)으로 검증한다.
3. 화면 조작(컴퓨터 유즈)은 만능이 아니다. 터미널처럼 위험한 앱은 안전 등급으로 막혀 있다.

## 5. 이 폴더의 파일

| 파일 | 내용 |
|---|---|
| `data/스크래핑연습_mystery_books_클라우드다중페이지_v1_20261110.csv` | 상태 1 결과 (32권) |
| `data/스크래핑연습_mystery_books_크롬다중페이지_v1_20261110.csv` | 상태 2 결과 (32권, 대조 기준) |
| `data/스크래핑연습_mystery_books_내장브라우저다중페이지_v1_20261110.csv` | 상태 3-A 결과 (32권) |
| `data/스크래핑연습_travel_books_WebFetch단일페이지_v1_20261110.csv` | 첫 실습: Travel 1페이지 11권 (상태 1, 원래 파일명 travel_books.csv) |
| `code/스크래핑연습_브라우저수집_다중페이지_v1_20261110.js` | 상태 2·3-A에서 실제로 실행한 자바스크립트 |
| `code/스크래핑연습_books_toscrape_다중페이지_v1_20261110.py` | 3-B 대안. 내 컴퓨터 터미널에서 직접 실행하는 파이썬 (아직 실제 사이트로 실행 검증 안 됨) |
| `code/스크래핑연습_결과대조_v1_20261110.py` | 세 CSV를 한 행씩 대조하는 스크립트 |

## 6. Claude Code에서 이어서 할 일

이 브랜치(`drafts-web-scraping-compare-261110`)를 Claude Code에서 이어받아 아래를 진행한다.

1. **파이썬 스크립트 실제 실행 검증 (3-B 대안):** Claude Code는 셸 명령을 직접 실행할 수 있으므로, `code/스크래핑연습_books_toscrape_다중페이지_v1_20261110.py`의 `START_URL`을 Mystery 주소로 바꿔 실행하고 결과 CSV를 `data/`에 `스크래핑연습_mystery_books_파이썬다중페이지_v1_20261110.csv`로 저장한다.
2. **4번째 결과 대조:** `code/스크래핑연습_결과대조_v1_20261110.py`의 `FILES`에 파이썬 결과를 추가해 실행하고, 이 문서 0번 표의 3-B 행을 실제 결과로 고친다.
3. **(선택) HTML 교안화:** 저장소 규칙에 맞춰 이 폴더에 `index.html` 교안을 만들고, `drafts/index.html` 목록에 연결한다.

**검증 명령 예시 (Claude Code 터미널)**

```bash
cd drafts/261110-web-scraping-compare
pip install requests beautifulsoup4
python3 code/스크래핑연습_결과대조_v1_20261110.py
```
