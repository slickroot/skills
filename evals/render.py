#!/usr/bin/env python3
"""Render a Claude Code .jsonl transcript into readable text for analysis.

Usage: python3 render.py <transcript.jsonl> [--full]

Default mode truncates tool inputs/results heavily (we care about the
conversation and the *shape* of tool use, not file contents).
--full keeps more of each tool call.
"""
import json, sys, os

path = sys.argv[1]
full = "--full" in sys.argv
CAP = 3000 if full else 400


def clip(s, cap=CAP):
    s = str(s).replace("\r", "")
    return s if len(s) <= cap else s[:cap] + f" …[+{len(s)-cap} chars]"


def render_content(content, role):
    out = []
    if isinstance(content, str):
        out.append(clip(content, 6000 if role == "user" else CAP * 4))
        return out
    for block in content or []:
        if not isinstance(block, dict):
            continue
        t = block.get("type")
        if t == "text":
            # user text and assistant prose are the meat: keep generously
            out.append(clip(block.get("text", ""), 8000))
        elif t == "thinking":
            out.append("[THINKING] " + clip(block.get("thinking", ""), 2000))
        elif t == "tool_use":
            name = block.get("name")
            inp = block.get("input", {})
            if name in ("Bash",):
                desc = inp.get("command", "")
            elif name in ("Read", "Edit", "Write"):
                desc = inp.get("file_path", "")
                if name == "Edit":
                    desc += " | " + clip(inp.get("new_string", ""), 200)
            elif name in ("Agent", "Task"):
                desc = f"subagent={inp.get('subagent_type')} :: " + clip(
                    inp.get("prompt", ""), 1500
                )
            else:
                desc = clip(json.dumps(inp, ensure_ascii=False), 600)
            out.append(f"[TOOL {name}] {clip(desc, 1500)}")
        elif t == "tool_result":
            c = block.get("content")
            if isinstance(c, list):
                c = " ".join(
                    b.get("text", "") for b in c if isinstance(b, dict)
                )
            out.append("[RESULT] " + clip(c, 300))
    return out


n = 0
for line in open(path, errors="replace"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    typ = d.get("type")
    if typ == "attachment":
        att = d.get("attachment", {})
        if att.get("type") == "skill_listing":
            continue
        continue
    msg = d.get("message")
    if not isinstance(msg, dict):
        continue
    role = msg.get("role")
    if role not in ("user", "assistant"):
        continue
    parts = render_content(msg.get("content"), role)
    parts = [p for p in parts if p and p.strip()]
    if not parts:
        continue
    n += 1
    side = "SIDECHAIN " if d.get("isSidechain") else ""
    print(f"\n===== [{n}] {side}{role.upper()} =====")
    for p in parts:
        print(p)
