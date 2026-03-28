---
layout: page
title: 3. Course Schedule
description: Weekly course schedule, including readings, quizzes, and assignments.
---

# Schedule

<div style="margin-bottom:1em;">
  <button id="toggle-su-tue-thu" class="btn">Su/Tue/Thu</button>
  <button id="toggle-mo-we" class="btn">Mo/We</button>
</div>

<div id="schedule-su-tue-thu">
  {% for module in site.modules_su_tue_thu %}
    {% if module.note %}
      <div class="schedule-note">
      {{ module.note }}
      </div>
    {% endif %}
    {% include module-su-tue-thu.html module=module %}
  {% endfor %}
</div>

<div id="schedule-mo-we" style="display:none;">
  {% for module in site.modules_mo_we %}
    {% if module.note %}
      <div class="schedule-note">
      {{ module.note }}
      </div>
    {% endif %}
    {% include module-mo-we.html module=module %}
  {% endfor %}
</div>

{% raw %}
<script>
(function() {
  function init() {
    var su = document.getElementById("schedule-su-tue-thu");
    var mo = document.getElementById("schedule-mo-we");
    var btnSu = document.getElementById("toggle-su-tue-thu");
    var btnMo = document.getElementById("toggle-mo-we");
    
    if (!su || !mo || !btnSu || !btnMo) return;
    
    btnSu.style.backgroundColor = "#007cba";
    btnSu.style.color = "white";
    btnMo.style.padding = "2px 16px";
    btnSu.style.padding = "2px 16px";

    btnSu.onclick = function() {
      su.style.display = "block";
      mo.style.display = "none";
      btnSu.style.backgroundColor = "#007cba";
      btnSu.style.color = "white";
      btnMo.style.backgroundColor = "#f0f0f0";
      btnMo.style.color = "#333";
    };
    
    btnMo.onclick = function() {
      su.style.display = "none";
      mo.style.display = "block";
      btnMo.style.backgroundColor = "#007cba";
      btnMo.style.color = "white";
      btnSu.style.backgroundColor = "#f0f0f0";
      btnSu.style.color = "#333";
    };
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
{% endraw %}




<!-- ---
layout: page
title: 3. Course Schedule
description: Weekly course schedule, including readings, quizzes, and assignments.
---

# Schedule

{% for module in site.modules %}
{{ module }}
{% endfor %} -->