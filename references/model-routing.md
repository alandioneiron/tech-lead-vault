# Model routing (only when roles are enabled)

Goal: spend the fewest tokens without losing quality. The Tech Lead (the most capable model) decides who does what.

Cost order: small/fast model << mid model << top model. Check the provider's current rate card before any financial estimate.

## Score the task on 3 axes (1 low - 3 high)
1. **Ambiguity** - is the requirement closed?
2. **Context breadth** - how many files or subsystems must be understood?
3. **Risk** - security, personal data, money, hard to reverse?

| Sum | Who |
|---|---|
| 3-4 | small/fast model: mechanical work (renames, stubs, formatting, log and checklist updates, repetitive CRUD from a given pattern) |
| 5-6 | mid model: implement a well-specified endpoint or screen, write tests, fix a bug with a clear repro, functional QA |
| 7-9 | Tech Lead / top model: architecture, security, data model, ambiguous or critical work, final review, ADRs |

## Break-even rule
If delegating needs so much specification, review and rework that it costs about the same as doing it, the Tech Lead does it. Signs: the task needs context only the Tech Lead has cached; writing the brief takes more tokens than the work; the output would need two or more review rounds.

## Delegation brief
Goal, files to touch, acceptance criteria, what was already ruled out, and a request for a short summary. Never put two agents on the same file at once. Log who did what in the AI Session Log.
