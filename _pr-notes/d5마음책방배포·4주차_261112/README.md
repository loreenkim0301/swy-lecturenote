# DAY 4 보충 + DAY 5 마음책방 자동 배포로 재구성 + 4주차 홈·월요일 교안 (2026-11-12)

## 결과물 링크(병합 후)
- DAY 5: https://loreenkim0301.github.io/swy-lecturenote/261109-ai-pm-week3/d5-chatbot-api.html
- DAY 4 4-10: https://loreenkim0301.github.io/swy-lecturenote/261109-ai-pm-week3/d4-claude-code-chatbot.html#s4-10
- 4주차 홈: https://loreenkim0301.github.io/swy-lecturenote/261116-ai-pm-week4/
- 4주차 월요일: https://loreenkim0301.github.io/swy-lecturenote/261116-ai-pm-week4/d1-claude-code-chatbot.html

## 바뀐 것
| 파일 | 바뀐 내용 |
| --- | --- |
| DAY 4 | 4-10에 오른쪽 클릭 > [검사], 눈으로 보이는 부분·안 되는 부분 보기, STEP 4 콘솔 오류 전체 캡처 → 클로드에게 묻기(16:37~16:38 강사 진행). 키 없을 때 샘플 방식·글꼴 기본값 설명. 편집 그림 대신 강사 실제 화면(제한 없음) 캡처로 교체 |
| DAY 5 | 버셀 함수·API 키·챗봇 시험 세션 삭제. S1 클로드 코드 개념(1-3을 오늘 작업 기준으로) → S2 클로드 코드로 깃헙 올리기(기획자: 올릴 것/안 올릴 것, 구현: .gitignore·커밋·푸시) → S3 깃헙 페이지스(공개 저장소 조건, 자동 반영, 자동이 아니면 나쁜 점) → S4 CI/CD 맛보기(빵집 비유, Actions 기록, 없으면 불편한 점, 선택: 키 검사 CI) → S5 페이지스 내리기·비공개 전환·파이어베이스+깃헙 액션 자동 배포 → S6 3주차 회고. 단어·준비·목표·정리 새로 씀 |
| 4주차 | 새 폴더 261116-ai-pm-week4: 홈(목표·날짜별 초안·흐름·수업 방식·준비물), 월요일 교안(클로드 코드 개념 + 챗봇 4세션, 시간 초안) |
| 3주차 홈·저장소 첫 페이지 | DAY 5 이름·결과물·흐름·준비물 수정, 4주차 링크 추가 |

## 근거(2026-11-12 확인)
- GitHub Pages 공개·비공개 조건: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- Pages는 늘 Actions로 배포: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Unpublish: https://docs.github.com/en/pages/getting-started-with-github-pages/unpublishing-a-github-pages-site
- Firebase GitHub 연동(firebase init hosting:github, 공개·비공개, 2026-11-10 갱신): https://firebase.google.com/docs/hosting/github-integration

## 확인 못 한 것
- 강사 파이어베이스 프로젝트에 수강생 계정을 어떤 권한으로 넣어야 firebase init hosting:github이 되는지(서비스 계정 생성 권한)
- 수강생 PC에서 git push 인증 방식(브라우저 로그인/토큰), 윈도우 깃·노드 설치 여부
- 마음책방 코드가 빌드가 필요한 앱인지(필요하면 깃헙 페이지스에 빌드 워크플로 필요)

## 화면
[DAY 5 목차 전](01_DAY5_목차_전.png) · [후](01_DAY5_목차_후.png) · [S2](02_DAY5_S2_깃헙올리기.png) · [S3](03_DAY5_S3_깃헙페이지스.png) · [S4](04_DAY5_S4_CICD.png) · [S5](05_DAY5_S5_파이어베이스.png) · [DAY 4 4-10](06_DAY4_4-10_콘솔보충.png) · [4주차 홈](07_4주차홈.png) · [4주차 월 목차](08_4주차월_목차.png)
