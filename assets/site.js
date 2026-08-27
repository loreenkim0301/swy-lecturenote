function copyPrompt(btn) {
  var box = btn.nextElementSibling;
  var text = box.innerText || box.textContent;
  var orig = btn.textContent;
  function done(ok) {
    btn.textContent = ok ? '복사됨' : '복사 실패';
    setTimeout(function () { btn.textContent = orig; }, 1500);
  }
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(function () { done(true); }, function () { fallbackCopy(text, done); });
  } else {
    fallbackCopy(text, done);
  }
}
function fallbackCopy(text, cb) {
  var ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.focus();
  ta.select();
  var ok = false;
  try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
  document.body.removeChild(ta);
  cb(ok);
}

document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('sidebar-toggle');
  if (!toggle) return;
  document.querySelectorAll('.sidebar nav a').forEach(function (a) {
    a.addEventListener('click', function () { toggle.checked = false; });
  });
});
