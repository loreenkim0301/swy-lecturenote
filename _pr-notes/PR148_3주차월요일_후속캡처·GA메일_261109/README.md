## 산출물 링크
- 월요일 교안(브랜치): https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/d1-sheet-appsscript.html
- 병합 후 공개 주소: https://loreenkim0301.github.io/swy-lecturenote/261109-ai-pm-week3/d1-sheet-appsscript.html
- 앞 PR: #147 (11/9 05:40 병합). 이 PR은 #147 병합 뒤에 올린 커밋 4개를 담아요.

## ① 무엇을 바꿨나
- 2-3: MovieLoop A/B 참고 상자를 지웠어요.
- 4-4 (새로 씀): GA 보고서를 내 메일로 정기적으로 받기
  - 조건 표: 관리자만 예약할 수 있어요. 받는 사람도 속성 권한이 있어야 해요. 최대 50명이에요. 매일·매주·매월·분기마다 보낼 수 있고, 첫 메일은 빨라야 다음 날이에요. 1~12개월 동안 보내요. PDF·CSV로 보내요. 실시간 보고서는 예약할 수 없어요.
  - 출처: support.google.com/analytics/answer/13722168 (2026.11.09 확인)
- 4-2: 실제 GA 화면에 맞춰 버튼 이름과 순서를 고쳤어요([다음], [만들고 계속하기], [태그 안내 보기] → [직접 설치]).

## ② 실제로 해 보고 넣은 캡처 (2026-11-09)
- GA 새 속성 만들기 6장: 계정, 속성, 플랫폼, 스트림, 태그 안내, 태그 복사
- GA 보고서 메일 6장: 데모 계정 공유 메뉴, 관리자 속성 공유 메뉴, 이메일 보내기, 받은 메일(주소 가림), 예약, 예약 목록
- 구글 권한 승인 1장(d1-s3-allow, 주소 가림)
- 3세션 데이터 정리 3장: 메뉴, 알림 창, 정리본 시트
  - 알림 창의 숫자는 원본 124줄 → 정리본 118줄, 확인 필요 18줄이에요. 교안의 기준값과 같아요.
- 4-2 GA 연결 4장: 깃헙 편집 버튼, head 아래 Google 태그, 버셀 배포 Ready, GA 실시간 개요
  - 백엔드 플랫폼 교안 실습 때 만든 저장소 swy-ab-practice, 버셀 프로젝트, GA 속성 swy-ab-practice-vercel에서 찍었어요. 저장소는 편집 화면만 열고 커밋하지 않았어요.
  - 실제 화면에 맞춰 문장을 고쳤어요: [실시간] → [실시간 개요], 커밋 창 설명.
- 해 보고 알게 된 것
  - 데모 계정은 보기 권한만 있어서 공유 메뉴에 '링크 공유'만 나와요. 그래서 예약 이메일은 관리자 권한이 있는 속성에서 했어요.
  - [이메일 보내기]로 테스트 메일을 보냈어요. 메일은 11/9 05:53에 왔어요.

![메뉴](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-s5-menu-hl.png?raw=true)
![알림](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-s5-alert-hl.png?raw=true)
![정리본](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-s5-cleaned-sheet-hl.png?raw=true)
![GA 예약](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-ga-schedule-hl.png?raw=true)
![GA 태그 복사](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-s6-tag-copy-hl.png?raw=true)
![깃헙 태그](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-s6-github-paste-hl.png?raw=true)
![GA 실시간](https://github.com/loreenkim0301/swy-lecturenote/blob/claude/ai-pm-week3-d1-followup/261109-ai-pm-week3/images/d1-s6-realtime-hl.png?raw=true)

## ③ 캡처 없이 글로 바꾼 12곳
- 남은 캡처 자리 12개를 모두 지웠어요. 그 자리에 '화면에서 볼 것' 상자(회색 테두리)를 넣어 무엇이 보여야 하는지 글로 적었어요.
  - 복습 3·4 웹 앱 화면 10곳: 배포 주소, PC·휴대폰 명단, 제목·신청 수, 새 버전 배포, 같은 주소, 입력 화면, 빈칸 안내, 시트 새 줄
  - 확인되지 않은 앱 경고 1곳: 회사 계정에서는 경고 없이 바로 권한 목록이 나올 수 있다고 적었어요.
  - 실행 기록·GA 첫 화면 2곳: 상자 없이 본문 문장만 남겼어요. 예: "[실행]을 눌러요. 상태가 [실패]인 줄을 눌러 열어요."
- 그림이 없어진 곳의 번호 표시 ①②③을 본문에서 지웠어요.
- 캡처를 찍으면 같은 자리에 그림으로 다시 넣을 수 있어요.

## ④ 병합
- 로린 님이 "병합해"라고 하시면 병합할게요.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01C4uqyAL9psqyp3PzBZ6jMH
