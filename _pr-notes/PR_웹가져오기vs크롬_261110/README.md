## 산출물 링크
- 교안(브랜치): https://github.com/loreenkim0301/swy-lecturenote/blob/claude/week3-d2-webfetch-vs-chrome/261109-ai-pm-week3/d2-web-crawling.html#s6-1
- 병합 후 공개 주소: https://loreenkim0301.github.io/swy-lecturenote/261109-ai-pm-week3/d2-web-crawling.html#s6-1

## 바꾼 것
| 위치 | 전 | 후 |
|---|---|---|
| 6-1 웹 가져오기란? | "[웹 검색]이 켜져 있으면… 답에는 출처 링크가 함께 붙어요." | 웹 검색 단추가 없는 새 화면 반영. 출처 표시는 기본 꺼짐(API 문서 기준) → 출처를 따로 요청하라고 안내 |
| 6-1 (새로 씀) | 없음 | '클로드인크롬과 무엇이 다른가요?': 한 줄 요약, 서점 비유, 못 읽는 페이지(로그인·자바스크립트) |
| 6-1 (새로 씀) | 없음 | '차이점과 근거' 토글: 7개 항목 비교표 + 'API 문서 기준' 한계 안내 + 출처 4개 |
| 6-2 프롬프트 5 | 페이지 읽었는지·권수 | '읽은 주소' 추가 (출처 확인용) |
| 6-2 STEP 1, 막히면 | 웹 검색 단추 전제 | 단추가 없는 화면 안내, 로그인·자바스크립트 페이지 안내 추가 |
| 6-3 참고 박스 | 로그인 화면·여러 탭 | 자바스크립트로 그리는 화면 추가, 웹 가져오기로 못 읽을 때 쓰는 것으로 연결 |

## 출처 확인 (2026.11.10)
- Claude API 문서 Web fetch tool: 서버에서 가져옴 / "does not support websites dynamically rendered with JavaScript" / 대화에 나온 주소만 / citations "disabled by default"
- Claude 도움말 10684626: 웹 검색 켜면 URL 직접 가져옴, 새 화면에는 토글 없음
- Claude Code 문서 Chrome: 브라우저 로그인 상태 공유, 로그인·CAPTCHA에서 멈춤
- Claude 도움말 12902428: 화면 캡처로 봄, 프롬프트 인젝션이 가장 큰 위험, 별도 프로필 권장

## 확인하지 못한 것
- claude.ai 앱의 웹 가져오기가 API 문서와 똑같이 동작하는지(자바스크립트·주소 제한·출처 표시). 교안에 'Claude API 문서 기준'으로 표시함.
- 클로드인크롬이 자바스크립트 페이지를 그리는 것은 문서에 없음. 실제 크롬을 쓰는 동작 방식으로 본 것이라고 교안에 적음.

## 변경 후 캡처 (토글 펼친 상태)
- 데스크톱: docs/pr-captures/PR_webfetch_261110/s6-1_desktop.png
- 모바일 390px: docs/pr-captures/PR_webfetch_261110/s6-1_mobile.png

## 점검
- 페이지 오류 0, id 중복 0, 390px 가로 스크롤 없음
