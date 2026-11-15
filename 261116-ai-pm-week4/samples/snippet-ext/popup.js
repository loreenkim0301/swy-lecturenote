const list = document.getElementById("list");
const toast = document.getElementById("toast");
async function render() {
  const { snippets = [] } = await chrome.storage.local.get("snippets");
  document.getElementById("count").textContent = snippets.length + " / 30";
  list.innerHTML = "";
  if (!snippets.length) { list.innerHTML = '<p class="empty">문장을 드래그하고 우클릭 → [내 문장 모음에 저장]을 눌러 보세요.</p>'; return; }
  for (const s of snippets) {
    const li = document.createElement("li");
    li.textContent = s.text;
    const from = document.createElement("span"); from.className = "from"; from.textContent = s.from;
    li.appendChild(from);
    li.addEventListener("click", async () => {
      await navigator.clipboard.writeText(s.text);
      toast.classList.add("on"); setTimeout(() => toast.classList.remove("on"), 1200);
    });
    list.appendChild(li);
  }
}
render();
