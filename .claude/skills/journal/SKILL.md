---
name: journal
description: Create or update the project journal (JOURNAL.md) and workspace production log (PRODUCTION_LOG.md). Invoke after any significant action — script approval, draft render, final render, delivery. Also invoke when the user asks to review project history or see what was done in a previous session.
---

# Journal — Production Record

Two records maintained in parallel:

- **`video-projects/<name>/JOURNAL.md`** — full session log for this project (decisions, issues, timing, next steps)
- **`PRODUCTION_LOG.md`** at workspace root — one line per session across all projects, for cross-project search

## When to update

Update the journal after any of these events:
- Script approved (`SCRIPT.md` written and confirmed)
- Draft render completed and reviewed
- Final render completed
- Thumbnails generated
- Delivery checklist signed off
- Any significant decision or course correction during the build

Do not wait until delivery to write the journal. Write an entry after each milestone so the record is useful if the session is interrupted.

## Entry format

Append to `JOURNAL.md` — never overwrite existing entries.

```markdown
## [YYYY-MM-DD] — [one-line session summary]

**Stage:** Script / Storyboard / Build / Draft render / Final render / Delivery
**Platform:** YouTube / LinkedIn / Both
**Duration:** Xs (if render exists)
**Renders produced:**
- `renders/<project>-youtube.mp4` — Xs, Xmb
- `renders/<project>-linkedin.mp4` — Xs, Xmb

**Decisions:**
- [What was decided and why — be specific. "Changed hook from X to Y because Z."]
- [Any visual or timing choice worth remembering]

**Issues:**
- [Anything that broke, required a workaround, or took longer than expected]
- [None] if clean session

**Next:**
- [What needs to happen before this project is done]
- [Any open questions]

---
```

## Creating the journal (first session)

If `JOURNAL.md` does not exist in the project folder, create it with this header before the first entry:

```markdown
# Production Journal — <project-name>

**Series:** [series name if applicable, or "standalone"]
**Platform:** YouTube / LinkedIn / Both
**Type:** Educational / Thought leadership / Personal
**Started:** [YYYY-MM-DD]

---
```

## Workspace production log

After writing a project journal entry, append a single line to `PRODUCTION_LOG.md` at the workspace root:

```
[YYYY-MM-DD] <project-name> — [stage] — [one-sentence summary]
```

Example:
```
2026-05-15 hihnala-intro — Final render — Delivered YouTube + LinkedIn, thumbnails done.
2026-05-18 clarity-framework — Draft render — Hook revised after draft review, retiming scenes 3–5.
```

If `PRODUCTION_LOG.md` does not exist at the workspace root, create it:

```markdown
# Framesmith — Production Log

One line per session. Full details in each project's JOURNAL.md.

---

```

## Reading the journal

When the user asks about a previous session or wants to continue work:

1. Read `video-projects/<name>/JOURNAL.md` — get full context for this project
2. If unsure which project: read `PRODUCTION_LOG.md` to identify the right one
3. Summarise the last entry before asking what to do next

Never rely on conversation memory for production decisions. The journal is the source of truth for what was decided and why.
