const line = document.getElementById("line");
const msg = document.getElementById("msg");
chrome.tabs.query({ active: true, currentWindow: true }, async ([tab]) => {
  if (!tab || !tab.url) { line.textContent = "이 페이지의 주소를 읽을 수 없어요."; return; }
  const md = "- [" + tab.title + "](" + tab.url + ")";
  line.textContent = md;
  try {
    await navigator.clipboard.writeText(md);
    msg.textContent = "복사했어요. 회의록에 붙여 넣으세요.";
  } catch (e) {
    msg.textContent = "복사하지 못했어요. 위 글을 직접 드래그해 복사하세요.";
  }
});
