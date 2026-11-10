// 상태 2(Claude in Chrome)·3-A(내장 브라우저)에서 실제로 실행한 코드
// 대상 페이지를 연 뒤 페이지 안(또는 브라우저 콘솔)에서 실행. 맨 위에서 await를 쓰므로 함수로 감싸지 말 것.
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
