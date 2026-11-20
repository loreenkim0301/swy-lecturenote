# 4주차 DAY2 선택 과제 6-1: 깃헙 커넥터가 안 될 때 깃헙 CLI로 하기 (261117)

## 바꾼 곳
- 파일: `261116-ai-pm-week4/d2-api.html`
- 위치: SESSION 6 「내 손으로 만드는 자체 개발 블로그」 → 6-1. 전체 공통 지침 → 기존 '깃 CLI·깃헙 CLI·깃헙 커넥터' 비교표(PR #198) 바로 아래. 6-2 단계별 목표의 1차 '깃헙에 코드 올리기' 전에 읽도록 배치

## 추가한 내용
1. 상황 설명: 회사·학교 계정은 관리자가 커넥터를 켜 주지 않아 연결이 안 될 수 있음 → 터미널에서 깃헙 CLI로 내 계정 로그인
2. 비유 상자: 커넥터 = 도서관 열람증(읽기만, 관리자 발급) / 깃헙 CLI = 내 도장(내 계정으로 바로)
3. 비교표: 어디서 써요 / 누구 이름으로 / 할 수 있는 일 / 연결하려면 / 막히면
4. 따라하기 4단계: gh --version → gh auth login(직접 입력) → gh auth status → 클로드 코드에 프롬프트
5. 복사 상자 2개: 터미널 명령 3줄, 「깃헙 CLI로 코드 올리기」 프롬프트(요청·내용·형식)
6. 주의: 로그인 코드·토큰은 API 키처럼 다루기
7. 출처 2건 (2026-11-17 확인)

## 근거 (2026-11-17 확인)
- Claude Docs GitHub integration https://claude.com/docs/connectors/github
  - 파일 이름·내용·브랜치 내용만 가져오고 커밋 기록·PR·이슈·저장소 메타데이터는 가져오지 않음
  - Team·Enterprise는 조직에서 GitHub가 켜져 있을 때만 Customize > Connectors에 보임 → 조직 관리자에게 요청
  - 내가 관리하지 않는 깃헙 조직 저장소는 Request access → 조직 관리자에게 이메일
- GitHub CLI 매뉴얼 https://cli.github.com/manual/gh_auth_login
  - 플래그 없이 실행하면 브라우저 로그인, 토큰은 시스템 자격 증명 저장소에 저장
- GitHub CLI 매뉴얼 https://cli.github.com/manual/ : gh repo clone, gh pr create, gh issue 명령

## 확인하지 않은 것
- 회사 깃헙 조직이 외부 앱(OAuth) 접근을 막아 둔 경우 gh 로그인 뒤에도 조직 저장소가 막히는지는 이번에 확인하지 않아 교안에 넣지 않음
- 프롬프트 번호: 이 교안은 프롬프트 1·3만 있어 번호 대신 이름(「깃헙 CLI로 코드 올리기」)을 붙임

## 변경 후 확인 캡처
- PC(1280px): d2-api_s6-1_커넥터대체_pc.png
- 모바일(390px): d2-api_s6-1_커넥터대체_m.png
- 처음엔 비유 상자에 why-box를 썼더니 본문 안에서 글자가 흐리게 보여 notice 상자로 바꿈
