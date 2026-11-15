chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({ id: "save-snippet", title: "내 문장 모음에 저장", contexts: ["selection"] });
});
chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId !== "save-snippet" || !info.selectionText) return;
  const { snippets = [] } = await chrome.storage.local.get("snippets");
  snippets.unshift({ text: info.selectionText.trim(), from: tab ? tab.title : "", at: Date.now() });
  await chrome.storage.local.set({ snippets: snippets.slice(0, 30) });
});
