---
layout: page
title: "7. Deployment"
description: Interactive guide to Recreate, Rolling, Blue-Green, and Canary deployment strategies.
permalink: /deployment-strategies/
nav_order: 7
---

<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
  :root {
    --bg: #f4f6fb;
    --surface: #ffffff;
    --border: #e2e8f0;
    --accent: #0077cc;
    --accent2: #7c3aed;
    --accent3: #f59e0b;
    --text: #1a202c;
    --muted: #64748b;
    --recreate: #dc2626;
    --rolling: #2563eb;
    --bluegreen: #059669;
    --canary: #d97706;
  }

  .deployment-strategies-page * { margin: 0; padding: 0; box-sizing: border-box; }

  .deployment-strategies-page {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
    border: 1px solid var(--border);
    border-radius: 14px;
  }

  /* Animated grid background */
  .deployment-strategies-page::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,119,204,0.06) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,119,204,0.06) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .deployment-strategies-page .container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 48px 24px;
    position: relative;
    z-index: 1;
  }

  /* Header */
  .deployment-strategies-page .header {
    text-align: center;
    margin-bottom: 60px;
    animation: fadeDown 0.6s ease both;
  }

  .deployment-strategies-page .header .tag {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    border: 1px solid rgba(0,229,255,0.3);
    padding: 4px 14px;
    border-radius: 2px;
    margin-bottom: 20px;
  }

  .deployment-strategies-page .header h1 {
    font-family: 'Space Mono', monospace;
    font-size: clamp(28px, 5vw, 52px);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -1px;
    color: #1a202c;
  }

  .deployment-strategies-page .header h1 span { color: var(--accent); }

  .deployment-strategies-page .header p {
    margin-top: 16px;
    color: var(--muted);
    font-size: 15px;
    max-width: 480px;
    margin-inline: auto;
    line-height: 1.7;
  }

  /* Nav tabs */
  .deployment-strategies-page .nav {
    display: flex;
    gap: 4px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 4px;
    margin-bottom: 40px;
    overflow-x: auto;
    animation: fadeUp 0.6s 0.1s ease both;
  }

  .deployment-strategies-page .nav-btn {
    flex: 1;
    min-width: 120px;
    padding: 10px 16px;
    background: transparent;
    border: none;
    border-radius: 6px;
    color: var(--muted);
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
  }

  .deployment-strategies-page .nav-btn:hover { color: var(--text); background: rgba(0,0,0,0.04); }

  .deployment-strategies-page .nav-btn.active {
    background: rgba(0,119,204,0.1);
    color: var(--accent);
    border: 1px solid rgba(0,119,204,0.25);
  }

  /* Sections */
  .deployment-strategies-page .section { display: none; animation: fadeUp 0.4s ease both; }
  .deployment-strategies-page .section.active { display: block; }

  /* Why matters cards */
  .deployment-strategies-page .why-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 32px;
  }

  .deployment-strategies-page .why-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 24px 20px;
    transition: border-color 0.2s, transform 0.2s;
  }

  .deployment-strategies-page .why-card:hover { border-color: rgba(0,119,204,0.35); transform: translateY(-2px); }
  .deployment-strategies-page .why-card .why-icon {
    display: block;
    width: auto;
    height: auto;
    font-size: 24px;
    margin-bottom: 12px;
    color: var(--text);
  }
  .deployment-strategies-page .why-card h3 { font-size: 13px; font-weight: 600; color: var(--accent); margin-bottom: 6px; font-family: 'Space Mono', monospace; }
  .deployment-strategies-page .why-card p { font-size: 12px; color: var(--muted); line-height: 1.6; }

  /* Strategy cards */
  .deployment-strategies-page .strategy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 20px;
  }

  .deployment-strategies-page .strategy-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 28px 24px;
    cursor: pointer;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
  }

  .deployment-strategies-page .strategy-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    border-radius: 12px 12px 0 0;
  }

  .deployment-strategies-page .strategy-card.recreate::before { background: var(--recreate); }
  .deployment-strategies-page .strategy-card.rolling::before { background: var(--rolling); }
  .deployment-strategies-page .strategy-card.bluegreen::before { background: var(--bluegreen); }
  .deployment-strategies-page .strategy-card.canary::before { background: var(--canary); }

  .deployment-strategies-page .strategy-card:hover { transform: translateY(-4px); border-color: rgba(0,0,0,0.12); }
  .deployment-strategies-page .strategy-card.recreate:hover { box-shadow: 0 12px 40px rgba(239,68,68,0.12); }
  .deployment-strategies-page .strategy-card.rolling:hover { box-shadow: 0 12px 40px rgba(59,130,246,0.12); }
  .deployment-strategies-page .strategy-card.bluegreen:hover { box-shadow: 0 12px 40px rgba(16,185,129,0.12); }
  .deployment-strategies-page .strategy-card.canary:hover { box-shadow: 0 12px 40px rgba(245,158,11,0.12); }

  .deployment-strategies-page .strategy-card .s-name {
    font-family: 'Space Mono', monospace;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 8px;
  }

  .deployment-strategies-page .strategy-card.recreate .s-name { color: var(--recreate); }
  .deployment-strategies-page .strategy-card.rolling .s-name { color: var(--rolling); }
  .deployment-strategies-page .strategy-card.bluegreen .s-name { color: var(--bluegreen); }
  .deployment-strategies-page .strategy-card.canary .s-name { color: var(--canary); }

  .deployment-strategies-page .strategy-card .s-desc { font-size: 13px; color: var(--muted); line-height: 1.6; margin-bottom: 18px; }
  .deployment-strategies-page .pro-con { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; }

  .deployment-strategies-page .badge {
    font-size: 11px;
    font-family: 'Space Mono', monospace;
    padding: 3px 8px;
    border-radius: 3px;
    font-weight: 700;
  }

  .deployment-strategies-page .badge.pro { background: rgba(16,185,129,0.1); color: #10b981; border: 1px solid rgba(16,185,129,0.2); }
  .deployment-strategies-page .badge.con { background: rgba(239,68,68,0.1); color: #ef4444; border: 1px solid rgba(239,68,68,0.2); }

  .deployment-strategies-page .s-meta {
    font-size: 11px;
    color: var(--muted);
    font-family: 'Space Mono', monospace;
    border-top: 1px solid var(--border);
    padding-top: 14px;
    margin-top: 4px;
  }

  .deployment-strategies-page .s-meta span { color: var(--accent); }

  /* Comparison table */
  .deployment-strategies-page .table-wrap {
    overflow-x: auto;
    border: 1px solid var(--border);
    border-radius: 12px;
    background: var(--surface);
  }

  .deployment-strategies-page table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
  }

  .deployment-strategies-page thead tr {
    border-bottom: 1px solid var(--border);
  }

  .deployment-strategies-page th {
    padding: 16px 20px;
    text-align: left;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .deployment-strategies-page td {
    padding: 16px 20px;
    border-bottom: 1px solid rgba(0,0,0,0.06);
  }

  .deployment-strategies-page tr:last-child td { border-bottom: none; }
  .deployment-strategies-page tr:hover td { background: rgba(0,0,0,0.02); }

  .deployment-strategies-page .pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    font-family: 'Space Mono', monospace;
  }

  .deployment-strategies-page .pill.yes { background: rgba(239,68,68,0.1); color: #ef4444; }
  .deployment-strategies-page .pill.no { background: rgba(16,185,129,0.1); color: #10b981; }
  .deployment-strategies-page .pill.high { background: rgba(239,68,68,0.1); color: #ef4444; }
  .deployment-strategies-page .pill.medium { background: rgba(245,158,11,0.1); color: #f59e0b; }
  .deployment-strategies-page .pill.low { background: rgba(16,185,129,0.1); color: #10b981; }
  .deployment-strategies-page .pill.very-low { background: rgba(16,185,129,0.15); color: #34d399; }

  .deployment-strategies-page .strat-name { font-weight: 600; font-size: 14px; }
  .deployment-strategies-page .strat-name.recreate { color: var(--recreate); }
  .deployment-strategies-page .strat-name.rolling { color: var(--rolling); }
  .deployment-strategies-page .strat-name.bluegreen { color: var(--bluegreen); }
  .deployment-strategies-page .strat-name.canary { color: var(--canary); }

  /* When to use */
  .deployment-strategies-page .when-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
  }

  .deployment-strategies-page .when-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 28px 24px;
    position: relative;
  }

  .deployment-strategies-page .when-card .badge-use {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 10px;
    display: block;
  }

  .deployment-strategies-page .when-card h3 { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
  .deployment-strategies-page .when-card p { font-size: 13px; color: var(--muted); line-height: 1.6; }

  /* Tools */
  .deployment-strategies-page .tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 14px;
    margin-bottom: 40px;
  }

  .deployment-strategies-page .tool-chip {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    transition: all 0.2s;
  }

  .deployment-strategies-page .tool-chip:hover { border-color: rgba(0,119,204,0.35); }
  .deployment-strategies-page .tool-chip .t-icon { font-size: 22px; margin-bottom: 8px; }
  .deployment-strategies-page .tool-chip .t-name { font-family: 'Space Mono', monospace; font-size: 12px; color: var(--accent); font-weight: 700; }
  .deployment-strategies-page .tool-chip .t-use { font-size: 11px; color: var(--muted); margin-top: 4px; }

  /* Best practices */
  .deployment-strategies-page .practices-list { display: flex; flex-direction: column; gap: 14px; }

  .deployment-strategies-page .practice-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px 22px;
    transition: border-color 0.2s;
  }

  .deployment-strategies-page .practice-item:hover { border-color: rgba(0,119,204,0.25); }

  .deployment-strategies-page .practice-num {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    font-weight: 700;
    min-width: 28px;
    padding-top: 2px;
  }

  .deployment-strategies-page .practice-item h3 { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
  .deployment-strategies-page .practice-item p { font-size: 13px; color: var(--muted); line-height: 1.5; }

  /* Quiz */
  .deployment-strategies-page .quiz-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 32px;
  }

  .deployment-strategies-page .quiz-progress {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 28px;
  }

  .deployment-strategies-page .progress-bar {
    flex: 1;
    height: 4px;
    background: var(--border);
    border-radius: 2px;
    overflow: hidden;
  }

  .deployment-strategies-page .progress-fill {
    height: 100%;
    background: var(--accent);
    border-radius: 2px;
    transition: width 0.4s ease;
  }

  .deployment-strategies-page .quiz-count { font-family: 'Space Mono', monospace; font-size: 12px; color: var(--muted); white-space: nowrap; }
  .deployment-strategies-page .quiz-q { font-size: 17px; font-weight: 500; margin-bottom: 24px; line-height: 1.5; }
  .deployment-strategies-page .quiz-options { display: flex; flex-direction: column; gap: 10px; }

  .deployment-strategies-page .quiz-opt {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 18px;
    font-size: 14px;
    cursor: pointer;
    text-align: left;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    transition: all 0.15s;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .deployment-strategies-page .quiz-opt:hover:not(:disabled) { border-color: rgba(0,119,204,0.4); background: rgba(0,119,204,0.04); }

  .deployment-strategies-page .quiz-opt .opt-letter {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
    min-width: 20px;
  }

  .deployment-strategies-page .quiz-opt.correct { border-color: #10b981; background: rgba(16,185,129,0.08); }
  .deployment-strategies-page .quiz-opt.correct .opt-letter { color: #10b981; }
  .deployment-strategies-page .quiz-opt.wrong { border-color: #ef4444; background: rgba(239,68,68,0.08); }
  .deployment-strategies-page .quiz-opt.wrong .opt-letter { color: #ef4444; }
  .deployment-strategies-page .quiz-opt:disabled { cursor: default; opacity: 0.7; }

  .deployment-strategies-page .quiz-feedback {
    margin-top: 20px;
    padding: 14px 18px;
    border-radius: 8px;
    font-size: 13px;
    line-height: 1.6;
    display: none;
  }

  .deployment-strategies-page .quiz-feedback.show { display: block; }
  .deployment-strategies-page .quiz-feedback.correct { background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #059669; }
  .deployment-strategies-page .quiz-feedback.wrong { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.2); color: #dc2626; }

  .deployment-strategies-page .quiz-next {
    margin-top: 20px;
    padding: 12px 24px;
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: 6px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    display: none;
    letter-spacing: 1px;
    transition: opacity 0.2s;
  }

  .deployment-strategies-page .quiz-next:hover { opacity: 0.85; }
  .deployment-strategies-page .quiz-next.show { display: inline-block; }

  .deployment-strategies-page .quiz-result {
    text-align: center;
    padding: 20px 0;
    display: none;
  }

  .deployment-strategies-page .quiz-result.show { display: block; }
  .deployment-strategies-page .quiz-result .score { font-family: 'Space Mono', monospace; font-size: 48px; font-weight: 700; color: var(--accent); }
  .deployment-strategies-page .quiz-result p { color: var(--muted); font-size: 14px; margin-top: 8px; margin-bottom: 24px; }

  .deployment-strategies-page .quiz-restart {
    padding: 12px 28px;
    background: transparent;
    border: 1px solid var(--accent);
    color: var(--accent);
    border-radius: 6px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 1px;
    transition: all 0.2s;
  }

  .deployment-strategies-page .quiz-restart:hover { background: rgba(0,229,255,0.08); }

  /* Section heading */
  .deployment-strategies-page .s-heading {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .deployment-strategies-page .s-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-16px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .deployment-strategies-page ::-webkit-scrollbar { width: 6px; height: 6px; }
  .deployment-strategies-page ::-webkit-scrollbar-track { background: var(--bg); }
  .deployment-strategies-page ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }

  @media (max-width: 768px) {
    .deployment-strategies-page .container { padding: 32px 14px; }
    .deployment-strategies-page .quiz-card { padding: 20px; }
  }
</style>

<div class="deployment-strategies-page">
  <div class="container">
    <div class="header">
      <div class="tag">Interactive Study Session</div>
      <h1>Deployment<br><span>Strategies</span></h1>
      <p>Reliable application delivery in modern systems - from Recreate to Canary.</p>
    </div>

    <nav class="nav">
      <button class="nav-btn active" onclick="switchTab('why', this)">Why It Matters</button>
      <button class="nav-btn" onclick="switchTab('strategies', this)">Strategies</button>
      <button class="nav-btn" onclick="switchTab('compare', this)">Comparison</button>
      <button class="nav-btn" onclick="switchTab('when', this)">When to Use</button>
      <button class="nav-btn" onclick="switchTab('tools', this)">Tools</button>
      <button class="nav-btn" onclick="switchTab('practices', this)">Best Practices</button>
      <button class="nav-btn" onclick="switchTab('quiz', this)">Quiz</button>
    </nav>

    <div class="section active" id="tab-why">
      <div class="s-heading">Why Deployment Strategy Matters</div>
      <div class="why-grid">
        <div class="why-card"><div class="why-icon">Time</div><h3>Reduce Downtime</h3><p>Keep services available during releases, maintaining SLAs and user trust.</p></div>
        <div class="why-card"><div class="why-icon">Shield</div><h3>Minimize Risk</h3><p>Controlled rollouts reduce the blast radius if a release contains bugs.</p></div>
        <div class="why-card"><div class="why-icon">Spark</div><h3>User Experience</h3><p>Seamless updates mean users never notice deployments happening.</p></div>
        <div class="why-card"><div class="why-icon">Boost</div><h3>Faster Delivery</h3><p>CI/CD pipelines with solid strategies ship features more frequently.</p></div>
        <div class="why-card"><div class="why-icon">Rollback</div><h3>Rollback & Recovery</h3><p>A clear strategy always includes a path back when things go wrong.</p></div>
        <div class="why-card"><div class="why-icon">Alert</div><h3>Avoid Incidents</h3><p>No strategy means production incidents waiting to happen.</p></div>
      </div>
    </div>

    <div class="section" id="tab-strategies">
      <div class="s-heading">The Four Core Strategies</div>
      <div class="strategy-grid">
        <div class="strategy-card recreate">
          <div class="s-name">Recreate</div>
          <div class="s-desc">Stop the old version completely, then deploy the new one. Simple but causes downtime.</div>
          <div class="pro-con">
            <span class="badge pro">Simple</span>
            <span class="badge pro">Easy</span>
            <span class="badge con">Downtime</span>
            <span class="badge con">Risky</span>
          </div>
          <div class="s-meta">Used for: <span>Non-critical systems</span></div>
        </div>
        <div class="strategy-card rolling">
          <div class="s-name">Rolling</div>
          <div class="s-desc">Gradually replace instances one by one. Old and new versions coexist temporarily.</div>
          <div class="pro-con">
            <span class="badge pro">No Downtime</span>
            <span class="badge pro">Controlled</span>
            <span class="badge con">Mixed Versions</span>
            <span class="badge con">Hard Rollback</span>
          </div>
          <div class="s-meta">Default in: <span>Kubernetes</span></div>
        </div>
        <div class="strategy-card bluegreen">
          <div class="s-name">Blue-Green</div>
          <div class="s-desc">Two identical environments: Blue (live) and Green (new). Switch traffic instantly via DNS or load balancer.</div>
          <div class="pro-con">
            <span class="badge pro">Zero Downtime</span>
            <span class="badge pro">Easy Rollback</span>
            <span class="badge con">Double Cost</span>
            <span class="badge con">Infrastructure</span>
          </div>
          <div class="s-meta">Best for: <span>Critical Systems</span></div>
        </div>
        <div class="strategy-card canary">
          <div class="s-name">Canary</div>
          <div class="s-desc">Release to a small percent of users first. Gradually increase traffic as confidence grows.</div>
          <div class="pro-con">
            <span class="badge pro">Very Low Risk</span>
            <span class="badge pro">Real Testing</span>
            <span class="badge con">Complex</span>
            <span class="badge con">Needs Monitoring</span>
          </div>
          <div class="s-meta">Used by: <span>Large organizations</span></div>
        </div>
      </div>
    </div>

    <div class="section" id="tab-compare">
      <div class="s-heading">Side-by-Side Comparison</div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Strategy</th>
              <th>Downtime</th>
              <th>Risk</th>
              <th>Cost</th>
              <th>Complexity</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="strat-name recreate">Recreate</span></td>
              <td><span class="pill yes">Yes</span></td>
              <td><span class="pill high">High</span></td>
              <td><span class="pill low">Low</span></td>
              <td><span class="pill low">Low</span></td>
            </tr>
            <tr>
              <td><span class="strat-name rolling">Rolling</span></td>
              <td><span class="pill no">No</span></td>
              <td><span class="pill medium">Medium</span></td>
              <td><span class="pill low">Low</span></td>
              <td><span class="pill medium">Medium</span></td>
            </tr>
            <tr>
              <td><span class="strat-name bluegreen">Blue-Green</span></td>
              <td><span class="pill no">No</span></td>
              <td><span class="pill low">Low</span></td>
              <td><span class="pill high">High</span></td>
              <td><span class="pill medium">Medium</span></td>
            </tr>
            <tr>
              <td><span class="strat-name canary">Canary</span></td>
              <td><span class="pill no">No</span></td>
              <td><span class="pill very-low">Very Low</span></td>
              <td><span class="pill medium">Medium</span></td>
              <td><span class="pill high">High</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="section" id="tab-when">
      <div class="s-heading">When to Use What</div>
      <div class="when-grid">
        <div class="when-card">
          <span class="badge-use" style="color: var(--rolling);">Startup / Small Apps</span>
          <h3>Rolling Deployment</h3>
          <p>Low overhead, no duplicate infrastructure. Kubernetes' native approach is good for most early-stage apps that can tolerate brief mixed-version states.</p>
        </div>
        <div class="when-card">
          <span class="badge-use" style="color: var(--bluegreen);">Enterprise / Critical Apps</span>
          <h3>Blue-Green Deployment</h3>
          <p>When instant rollback and zero-downtime are non-negotiable. The cost of duplicate infrastructure is justified when downtime means revenue loss.</p>
        </div>
        <div class="when-card">
          <span class="badge-use" style="color: var(--canary);">High-Scale Systems</span>
          <h3>Canary Deployment</h3>
          <p>When you serve many users and need real-world validation before full rollout. This catches production-only bugs safely.</p>
        </div>
      </div>
    </div>

    <div class="section" id="tab-tools">
      <div class="s-heading">Tools & Technologies</div>
      <div class="tools-grid">
        <div class="tool-chip"><div class="t-icon">K8s</div><div class="t-name">Kubernetes</div><div class="t-use">Rolling, Canary</div></div>
        <div class="tool-chip"><div class="t-icon">GitOps</div><div class="t-name">ArgoCD</div><div class="t-use">GitOps workflows</div></div>
        <div class="tool-chip"><div class="t-icon">Charts</div><div class="t-name">Helm</div><div class="t-use">K8s package manager</div></div>
        <div class="tool-chip"><div class="t-icon">AWS</div><div class="t-name">AWS CodeDeploy</div><div class="t-use">Blue/Green on AWS</div></div>
        <div class="tool-chip"><div class="t-icon">Traffic</div><div class="t-name">ALB</div><div class="t-use">Traffic shifting</div></div>
      </div>
    </div>

    <div class="section" id="tab-practices">
      <div class="s-heading">Best Practices</div>
      <div class="practices-list">
        <div class="practice-item">
          <div class="practice-num">01</div>
          <div><h3>Always Have a Rollback Strategy</h3><p>Before deploying, know exactly how you will revert. Blue-Green makes this trivial; Rolling requires more planning.</p></div>
        </div>
        <div class="practice-item">
          <div class="practice-num">02</div>
          <div><h3>Use Health Checks</h3><p>Automated readiness and liveness probes ensure traffic only routes to healthy instances.</p></div>
        </div>
        <div class="practice-item">
          <div class="practice-num">03</div>
          <div><h3>Monitor Errors, Latency, and Resources</h3><p>Track error rates, p99 latency, CPU, and memory during every deployment to catch regressions early.</p></div>
        </div>
        <div class="practice-item">
          <div class="practice-num">04</div>
          <div><h3>Automate CI/CD</h3><p>Manual deployments introduce delay and human error. Automate the full pipeline from commit to production.</p></div>
        </div>
        <div class="practice-item">
          <div class="practice-num">05</div>
          <div><h3>Test in Staging First</h3><p>Staging environments should mirror production as closely as possible to catch issues before real users are affected.</p></div>
        </div>
      </div>
    </div>

    <div class="section" id="tab-quiz">
      <div class="s-heading">Knowledge Check</div>
      <div class="quiz-card">
        <div id="quiz-main">
          <div class="quiz-progress">
            <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width:0%"></div></div>
            <div class="quiz-count" id="quiz-count">1 / 8</div>
          </div>
          <div class="quiz-q" id="quiz-q"></div>
          <div class="quiz-options" id="quiz-opts"></div>
          <div class="quiz-feedback" id="quiz-feedback"></div>
          <button class="quiz-next" id="quiz-next" onclick="nextQuestion()">NEXT -&gt;</button>
        </div>
        <div class="quiz-result" id="quiz-result">
          <div class="score" id="score-display"></div>
          <p id="score-msg"></p>
          <button class="quiz-restart" onclick="restartQuiz()">RESTART QUIZ</button>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // Tab switching tied to this page instance so other pages remain unaffected.
  function switchTab(id, targetBtn) {
    const root = targetBtn.closest('.deployment-strategies-page');
    root.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    root.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    root.querySelector('#tab-' + id).classList.add('active');
    targetBtn.classList.add('active');
  }

  const questions = [
    {
      q: "Which deployment strategy causes downtime during releases?",
      opts: ["Rolling", "Recreate", "Blue-Green", "Canary"],
      answer: 1,
      exp: "Recreate stops the old version before starting the new one, causing downtime. It is suitable only for non-critical systems."
    },
    {
      q: "What is the default deployment strategy in Kubernetes?",
      opts: ["Canary", "Blue-Green", "Rolling", "Recreate"],
      answer: 2,
      exp: "Rolling is Kubernetes' default strategy. It gradually replaces old pods with new ones while maintaining availability."
    },
    {
      q: "Blue-Green deployment requires two identical environments. What is the main downside?",
      opts: ["Causes downtime", "Double infrastructure cost", "Cannot rollback", "Only works on AWS"],
      answer: 1,
      exp: "Running two production environments doubles infrastructure costs."
    },
    {
      q: "A company releases to 5% of users first, monitors errors, then gradually increases traffic. Which strategy is this?",
      opts: ["Rolling", "Blue-Green", "Recreate", "Canary"],
      answer: 3,
      exp: "Canary deployment routes a small percentage of users to the new version first for low-risk validation."
    },
    {
      q: "Which deployment strategy is best suited for an enterprise banking application?",
      opts: ["Recreate", "Rolling", "Blue-Green", "Any of the above"],
      answer: 2,
      exp: "Blue-Green is ideal for critical systems because it provides zero downtime and fast rollback."
    },
    {
      q: "Which tool is associated with GitOps-style deployment workflows?",
      opts: ["Helm", "ArgoCD", "AWS CodeDeploy", "ALB"],
      answer: 1,
      exp: "ArgoCD is a GitOps continuous delivery tool for Kubernetes."
    },
    {
      q: "A Rolling deployment has which combination of attributes?",
      opts: ["Downtime: Yes, Risk: High", "Downtime: No, Risk: Medium", "Downtime: No, Risk: Low", "Downtime: Yes, Risk: Low"],
      answer: 1,
      exp: "Rolling has no downtime and medium risk due to mixed versions running simultaneously and more involved rollback."
    },
    {
      q: "Which best practice ensures traffic only reaches healthy instances during deployment?",
      opts: ["Automated CI/CD", "Staging environments", "Health checks", "Rollback strategy"],
      answer: 2,
      exp: "Health checks (readiness and liveness probes) validate an instance before routing traffic."
    }
  ];

  let current = 0;
  let score = 0;
  let answered = false;

  function byId(id) {
    return document.getElementById(id);
  }

  function renderQuestion() {
    const q = questions[current];
    byId('quiz-q').textContent = q.q;
    byId('quiz-count').textContent = `${current + 1} / ${questions.length}`;
    byId('progress-fill').style.width = `${(current / questions.length) * 100}%`;
    byId('quiz-feedback').className = 'quiz-feedback';
    byId('quiz-next').className = 'quiz-next';

    const letters = ['A', 'B', 'C', 'D'];
    const opts = byId('quiz-opts');
    opts.innerHTML = '';

    q.opts.forEach((opt, i) => {
      const btn = document.createElement('button');
      btn.className = 'quiz-opt';
      btn.innerHTML = `<span class="opt-letter">${letters[i]}</span>${opt}`;
      btn.onclick = () => selectAnswer(i);
      opts.appendChild(btn);
    });

    answered = false;
  }

  function selectAnswer(idx) {
    if (answered) return;

    answered = true;
    const q = questions[current];
    const btns = document.querySelectorAll('.deployment-strategies-page .quiz-opt');
    btns.forEach(b => { b.disabled = true; });

    if (idx === q.answer) {
      btns[idx].classList.add('correct');
      score++;
      const fb = byId('quiz-feedback');
      fb.textContent = 'Correct. ' + q.exp;
      fb.className = 'quiz-feedback correct show';
    } else {
      btns[idx].classList.add('wrong');
      btns[q.answer].classList.add('correct');
      const fb = byId('quiz-feedback');
      fb.textContent = 'Not quite. ' + q.exp;
      fb.className = 'quiz-feedback wrong show';
    }

    byId('quiz-next').className = 'quiz-next show';
  }

  function nextQuestion() {
    current++;
    if (current >= questions.length) {
      showResult();
    } else {
      renderQuestion();
    }
  }

  function showResult() {
    byId('quiz-main').style.display = 'none';
    const result = byId('quiz-result');
    result.className = 'quiz-result show';

    byId('score-display').textContent = `${score}/${questions.length}`;

    const pct = (score / questions.length) * 100;
    let msg = 'Keep studying. Review the comparison table and try again.';
    if (pct === 100) {
      msg = 'Perfect score. You know deployment strategies very well.';
    } else if (pct >= 75) {
      msg = 'Great work. You have a solid grasp of the material.';
    } else if (pct >= 50) {
      msg = 'Good start. Review the strategies and take the quiz again.';
    }

    byId('score-msg').textContent = msg;
    byId('progress-fill').style.width = '100%';
  }

  function restartQuiz() {
    current = 0;
    score = 0;
    answered = false;
    byId('quiz-main').style.display = 'block';
    byId('quiz-result').className = 'quiz-result';
    renderQuestion();
  }

  renderQuestion();
</script>
