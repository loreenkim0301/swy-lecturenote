#!/usr/bin/env python3
"""교안 오른쪽 아래 FAB를 '빠른 메뉴'로 바꿔요.

FAB(＋)를 누르면 하위 버튼 2개가 펼쳐져요.
  ▶ 슬라이드로 보기  (기존 #slideBtn을 그대로 옮겨서, 슬라이드 스크립트는 고치지 않아요)
  ↑ 최상단으로       (페이지 맨 위로 이동)

사용법: python3 common/tools/apply_fab_menu.py 파일.html [파일.html ...]
같은 파일에 여러 번 돌려도 한 번만 적용돼요.
"""
import sys

OLD_BTN = '<button id="slideBtn" type="button">▶ 슬라이드로 보기</button>'
MARK = '<!-- fab-menu v1 -->'

NEW_BTN = MARK + '''
<nav id="fabMenu" aria-label="빠른 메뉴">
<div id="fabItems" hidden>
<button id="slideBtn" class="fab-item" type="button">▶ 슬라이드로 보기</button>
<button id="toTopBtn" class="fab-item" type="button">↑ 최상단으로</button>
</div>
<button id="fabMain" type="button" aria-expanded="false" aria-controls="fabItems" aria-label="빠른 메뉴 열기"><span aria-hidden="true">＋</span></button>
</nav>'''

CSS = '''<style>/* fab-menu v1 */
#fabMenu{position:fixed;right:16px;bottom:16px;z-index:30;display:flex;flex-direction:column;align-items:flex-end;gap:10px}
#fabItems{display:flex;flex-direction:column;align-items:flex-end;gap:8px}
#fabItems[hidden]{display:none}
#fabMenu #slideBtn,#fabMenu .fab-item{position:static;right:auto;bottom:auto;background:#fff;color:var(--blue);border:1px solid var(--blue);border-radius:999px;padding:10px 16px;font:700 14px var(--font-sans);cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.18);white-space:nowrap}
#fabMenu .fab-item:hover,#fabMenu .fab-item:focus-visible{background:var(--blue);color:#fff}
#fabMain{width:52px;height:52px;border-radius:50%;border:0;background:var(--blue);color:#fff;font:700 26px/1 var(--font-sans);cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center}
#fabMain span{display:inline-block;transition:transform .2s}
#fabMain[aria-expanded="true"] span{transform:rotate(45deg)}
@media print{#fabMenu{display:none!important}}
</style>
'''

JS = '''<script>/* fab-menu v1 */
(function(){
  var main=document.getElementById('fabMain'),items=document.getElementById('fabItems'),top=document.getElementById('toTopBtn');
  if(!main||!items)return;
  function set(open){items.hidden=!open;main.setAttribute('aria-expanded',open?'true':'false');main.setAttribute('aria-label',open?'빠른 메뉴 닫기':'빠른 메뉴 열기');}
  main.addEventListener('click',function(){set(items.hidden);});
  if(top)top.addEventListener('click',function(){set(false);window.scrollTo({top:0,behavior:'smooth'});});
  var sb=document.getElementById('slideBtn');
  if(sb)sb.addEventListener('click',function(){set(false);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!items.hidden){set(false);main.focus();}});
  document.addEventListener('click',function(e){if(!items.hidden&&!document.getElementById('fabMenu').contains(e.target))set(false);});
})();
</script>
'''


def apply(path):
    s = open(path, encoding='utf-8').read()
    if MARK in s:
        return 'skip(이미 적용)'
    if s.count(OLD_BTN) != 1:
        return 'skip(기존 버튼 없음)'
    s = s.replace(OLD_BTN, NEW_BTN)
    i = s.rfind('</head>')
    s = s[:i] + CSS + s[i:]
    j = s.rfind('</body>')
    s = s[:j] + JS + s[j:]
    open(path, 'w', encoding='utf-8').write(s)
    return 'ok'


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(p, apply(p))
