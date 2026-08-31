# Capstone: Starting Points

You have about 20 minutes of working time and three requirements: use at least
three prompts, refine at least one response based on what you got back, and
validate the output before calling it done.

If you already have a task in mind, use it. This packet is for everyone else.
Nothing here is a test — the point is to have something concrete in front of
you so the 20 minutes go into practicing the process rather than into deciding
what to work on.

---

## First: can you generate your own in 60 seconds?

A capstone task from your own work is worth more than anything in this packet,
because you'll actually finish it on Monday. Try one of these prompts on
yourself before reaching for a canned scenario:

- What did you do last week that you'll have to do again this week?
- What's the task you keep putting off because it's tedious rather than hard?
- When you joined this team, what took you longest to understand?
- What do you copy-paste and then edit by hand every time?
- What's a piece of your codebase you avoid touching because you don't fully
  understand it?
- What question do people ask you repeatedly that you answer from memory?
- What's the last thing you read that you had to read twice?

If any of those produced an answer, that's your capstone. Scope it down until
it fits in 20 minutes and start.

---

## Scenario 1 — Debug & Document

**Materials:** `scenario1/inventory_report.py` and `scenario1/inventory.csv`

A small script that reads an inventory CSV and reports which items need
restocking. It has no comments and it doesn't work. Your job: diagnose it,
propose a fix, and write a short explanation of the root cause that a teammate
could read without your help.

Run it first. Read the traceback. Then start prompting.

**What "done" looks like:** the script runs on the provided CSV, produces
sensible output, and you can explain in three or four sentences what was wrong
and why the fix is correct.

**Fair warning:** the crash you'll see first is not the only problem in this
file. Some of what's wrong doesn't raise an error at all. If the AI hands you a
fix for the traceback and declares victory, that's the moment to push back —
and it's exactly the kind of moment this capstone exists to practice.

### Alternative if you'd rather use your own code

Bring a function from your own codebase that you didn't write, or wrote long
enough ago that you've forgotten it. Ask for an explanation, check it against
what the code actually does, then ask for one improvement with the trade-off
named.

---

## Scenario 2 — Research Brief

**Materials:** `scenario2/log-retention-proposal.md`

An internal proposal about changing log retention policy. It's about 900 words,
written the way real internal documents are written — the recommendation is
clear, but the risks and the unresolved questions are scattered through the
prose rather than collected anywhere.

Your job: summarize it, extract the key decisions and risks, and produce a
one-page brief for someone who has to approve or reject this and hasn't read
the original.

**What "done" looks like:** a brief that a decision-maker could act on. It
should make clear what's being proposed, what it saves, what could go wrong,
and what needs to happen first.

**Where to be careful:** this document contains several numbers that are
explicitly uncertain, and at least one figure the authors describe as a
placeholder. A summary that presents those as settled facts is wrong in a way
that matters — it would lead someone to approve something on a false basis.
Check your brief against the source specifically for this.

### Alternative if you'd rather use your own material

An RFC, a vendor comparison, a long design doc, or a standard you've been
meaning to read. Anything where you need the shape of it more than the detail.

---

## Scenario 3 — Build a Mini Workflow

This is the highest-value scenario and the easiest to under-scope. If you don't
have a task in mind already, pick one of these rather than spending five of
your twenty minutes deciding.

Each of these is small enough to design and test in the time available.

**Release notes from commit messages.** Input: a list of commits since the last
release. Transform: group them by type and rewrite for a non-engineering
audience. Refine: adjust tone and drop internal-only changes. Output: a
paragraph and a bulleted list. Validate: every user-visible change in the input
appears in the output, and nothing appears that isn't in the input.

**Ticket triage.** Input: a handful of raw bug reports. Transform: extract
severity, affected component, and whether reproduction steps are present.
Refine: tighten the severity criteria after seeing how it classifies the first
batch. Output: a table. Validate: re-run it on the same tickets and check the
classifications are stable.

**Error message rewriting.** Input: user-facing error strings from your app.
Transform: rewrite them to say what happened and what to do next. Refine: add
constraints on length and tone. Output: a before/after table. Validate: check
that no rewrite claims something the system doesn't actually do.

**Test case generation from a spec.** Input: a short function spec or
acceptance criteria. Transform: enumerate test cases including edge cases.
Refine: ask specifically for the cases it missed. Output: a checklist.
Validate: check each case against the spec — some will be plausible but not
actually implied by it.

**Meeting notes to action items.** Input: raw notes from a meeting. Transform:
extract decisions, action items, and owners. Refine: separate things that were
decided from things that were merely discussed. Output: a short structured
summary. Validate: check that nothing was assigned to someone who wasn't
mentioned, which is a very common failure.

**Onboarding explainer.** Input: a config file, build script, or CI pipeline
that new people find confusing. Transform: annotate it line by line. Refine:
target it at someone in their first week. Output: a commented version.
Validate: check every claim against what the file actually does.

**Log pattern summary.** Input: a chunk of log output. Transform: group by
pattern and count. Refine: ask it to distinguish routine noise from anomalies.
Output: a ranked list. Validate: spot-check three of its groupings against the
raw logs.

**Documentation gap check.** Input: a README plus the actual commands needed to
run the project. Transform: identify what the README omits or gets wrong.
Refine: ask what a new joiner would get stuck on specifically. Output: a list
of fixes. Validate: try to follow the README as written and see if it matches.

---

## A worked example

This is Scenario 1, done properly. Read it if you're stuck, or afterwards to
compare against what you did. The point isn't the specific wording — it's the
shape.

**Prompt 1 — orient before fixing.**

> Here's a Python script and the CSV it reads. Explain what it's trying to do,
> function by function. Don't suggest fixes yet.
>
> [paste script and a few rows of CSV]

*Why this first:* you can't evaluate a fix for code you don't understand. Read
the explanation against the actual script and confirm it matches. If the
explanation is wrong here, everything downstream is built on it.

**Prompt 2 — the specific failure.**

> Running it gives this traceback: [paste]. Explain the root cause. I want to
> understand why it happens with this data, not just what line to change.

*Why phrased this way:* asking for the root cause rather than the fix gets you
something you can verify against the CSV. You can point at the row that causes
it.

**Prompt 3 — widen the search.**

> Beyond that crash, what else in this script is wrong or fragile? Include
> problems that wouldn't raise an error. For each one, tell me how I could
> confirm it's real.

*Why this matters:* this is where you'll get a mix of genuine issues, things
that are technically true but irrelevant, and possibly something invented. The
"how would I confirm it" clause is what makes the list checkable rather than
something you have to take on faith.

**Refinement — push on one answer.**

Pick one item from the list and challenge it: *"Show me the specific input that
would trigger that."* If it can't produce one, it may not be a real problem. If
it produces one, you've verified it yourself rather than trusting the claim.

**Validation — the part that counts.**

Run the fixed script. Then check the things running it won't tell you: does the
output match what you'd compute by hand from the CSV? Feed it an edge case the
original data doesn't contain. Confirm the explanation you'd give a teammate is
one you actually believe, not one you're repeating.

**What you should be able to say at the end:** here's what was broken, here's
how I know the fix is correct, and here's what I checked that the model didn't
tell me to check.

---

## If you finish early

Try the same task again from scratch with a single prompt, and compare. The gap
between the two is the thing this course was about.
