# 교안 HTML의 의미 단위(예: 고칠 수 있게, 써 보고)를 줄바꿈 금지 공백으로 묶어요.
# 사용: python3 common/tools/keep_phrase_linebreak.py 폴더/파일.html [...]
# pre·code·script·style·textarea와 태그 속성은 바꾸지 않아요. 여러 번 돌려도 결과가 같아요.
import re,sys
NB=' '
# 의미 단위로 묶을 패턴 (앞말+뒷말 사이 공백을 줄바꿈 금지 공백으로)
pats=[
 # 의존명사 '수' + 있다/없다
 (r'(\S+) 수 (있|없)', lambda m:m.group(1)+NB+'수'+NB+m.group(2)),
 # 보조용언: ~아/어 보다·주다·두다·놓다·버리다·가다·오다
 (r'(\S+[아어여워와줘봐해둬]) (보|봐|봤|봅|줘|주|줬|드려|드리|둬|두|놓|버리|버려|가|와|오)(?=[가-힣\s.,!?)])', lambda m:m.group(1)+NB+m.group(2)),
 # ~고 있다/싶다/나서
 (r'(\S+고) (있|싶|나서|나면)', lambda m:m.group(1)+NB+m.group(2)),
 # ~게 되다/하다/만들다
 (r'(\S+게) (되|돼|됐|하|해|만들)', lambda m:m.group(1)+NB+m.group(2)),
 # 관형형 + 의존명사(것·때·줄·대로·만큼·뿐·중·후·전·뒤·적)
 (r'(\S+[은는을ㄹ던]) (것|거|때|줄|대로|만큼|뿐|적|듯)(?=[가-힣\s.,!?)]|$)', lambda m:m.group(1)+NB+m.group(2)),
 # 숫자 + 단위
 (r'(\d+) (개|분|시간|명|장|번|원|초|일|주|가지|단계|줄)(?=[가-힣\s.,!?)]|$)', lambda m:m.group(1)+NB+m.group(2)),
 # 부정 '안/못' + 동사
 (r'(?<=\s)(안|못|잘) (\S)', lambda m:m.group(1)+NB+m.group(2)),
]
def fix(text):
  n=0
  for p,f in pats:
    text,k=re.subn(p,f,text); n+=k
  return text,n
def run(path):
  s=open(path,encoding='utf-8').read()
  # 보호 구간: script, style, pre, code, textarea, 그리고 태그 자체
  parts=re.split(r'(<script.*?</script>|<style.*?</style>|<pre.*?</pre>|<code.*?</code>|<textarea.*?</textarea>|<[^>]+>)',s,flags=re.S|re.I)
  tot=0;out=[]
  for i,pt in enumerate(parts):
    if i%2==1 or not re.search('[가-힣]',pt): out.append(pt); continue
    nt,n=fix(pt); tot+=n; out.append(nt)
  open(path,'w',encoding='utf-8').write(''.join(out)); print(path,tot)
for p in sys.argv[1:]: run(p)
