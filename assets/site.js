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

(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.sidebar nav a[href^="#"]'));
  var items = links.map(function (link) {
    var id = decodeURIComponent(link.getAttribute('href').slice(1));
    var target = document.getElementById(id);
    return target ? { link: link, target: target } : null;
  }).filter(Boolean);
  if (!items.length) return;

  function setActive(activeLink) {
    links.forEach(function (l) { l.classList.remove('active', 'active-parent'); });
    if (!activeLink) return;
    activeLink.classList.add('active');
    var li = activeLink.closest('li');
    while (li) {
      var parentLi = li.parentElement && li.parentElement.closest('li');
      if (parentLi) {
        var parentLink = parentLi.querySelector(':scope > a');
        if (parentLink) parentLink.classList.add('active-parent');
      }
      li = parentLi;
    }
  }

  function updateActive() {
    var triggerY = window.scrollY + 110;
    var current = items[0];
    for (var i = 0; i < items.length; i++) {
      if (items[i].target.getBoundingClientRect().top + window.scrollY <= triggerY) {
        current = items[i];
      } else {
        break;
      }
    }
    setActive(current.link);
  }

  var ticking = false;
  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(function () { updateActive(); ticking = false; });
      ticking = true;
    }
  }, { passive: true });
  window.addEventListener('resize', updateActive);
  updateActive();
})();
