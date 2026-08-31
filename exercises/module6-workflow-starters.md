# Module 6 — Canned Workflow Starters

Use a repetitive task from your own work if you have one. These are for anyone
who doesn't, and they're deliberately generic enough to adapt.

You have about seven minutes. **Sketch, don't build.** Four boxes: what goes in,
what the AI transforms, what you refine, how you check before it leaves your
hands.

The validation box is the one that matters. If you only fill in one, fill in
that one.

---

## Track A — Coding tasks

### A1. Bug report → verified fix

- **Input:** a bug report with reproduction steps, plus the relevant code.
- **Transform:** ask for the likely cause and a proposed fix.
- **Refine:** ask what else could produce the same symptom, and rule those out.
- **Validate:** reproduce the bug first, apply the fix, confirm it stops. Then
  check that the existing tests still pass.

The refine step is the one people skip. A fix that resolves the symptom without
confirming the cause is how the same bug returns in a different shape.

### A2. Unfamiliar code → onboarding notes

- **Input:** a module or service you didn't write.
- **Transform:** ask for a plain-language walkthrough plus a list of what it
  depends on.
- **Refine:** ask specifically what would surprise someone in their first week.
- **Validate:** check every claimed dependency against the actual imports and
  config. Explanations of unfamiliar code are confident whether or not they're
  right.

### A3. Spec → test cases

- **Input:** acceptance criteria or a function signature with a description.
- **Transform:** ask for a list of test cases including edge cases.
- **Refine:** ask what it missed, then ask again — the second pass usually finds
  something.
- **Validate:** check each case against the spec. Some will be plausible but not
  actually implied by what you wrote, and those are the ones that quietly expand
  scope.

### A4. Error strings → user-facing messages

- **Input:** raw error messages from your application.
- **Transform:** rewrite each to say what happened and what to do next.
- **Refine:** add constraints on length and tone, and ban anything that
  speculates about cause.
- **Validate:** confirm no rewrite promises behavior the system doesn't have.
  "Try again in a few minutes" is a lie if nothing retries.

---

## Track B — Research and writing tasks

### B1. Sources → decision brief

- **Input:** three to five documents on a decision you need to make.
- **Transform:** ask for each source's position and the evidence behind it.
- **Refine:** ask where the sources disagree, and what none of them addresses.
- **Validate:** check every specific claim against its source. Confirm that
  hedged statements are still hedged in the summary — that's where compression
  does the most damage.

### B2. Long thread → decision record

- **Input:** a long email or chat thread where something was decided.
- **Transform:** extract the decision, the alternatives considered, and the
  reasoning.
- **Refine:** separate what was decided from what was merely discussed.
- **Validate:** check that no decision is attributed to someone who didn't make
  it, and that nothing marked "decided" was actually still open.

### B3. Meeting notes → action items

- **Input:** raw notes from a meeting.
- **Transform:** extract actions, owners, and dates.
- **Refine:** flag anything with no clear owner rather than guessing one.
- **Validate:** confirm each owner was actually present and actually agreed.
  Invented owners are the most common failure here and the most embarrassing.

### B4. Documentation → gap list

- **Input:** a README or setup guide, plus the commands you actually ran.
- **Transform:** ask what the documentation omits or gets wrong.
- **Refine:** ask what a first-week joiner would get stuck on specifically.
- **Validate:** follow the documentation as written on a clean machine. This is
  the only validation step here you can't fake.

---

## A worked sketch

For anyone who wants to see the level of detail expected. This is A1, filled in:

> **Input:** the bug report as filed, plus the file it points at and its test
> file.
>
> **Transform:** one prompt with the report, the code, and the observed versus
> expected behavior. Ask for likely cause and a minimal fix.
>
> **Refine:** ask for two other explanations that fit the same symptom. Check
> whether the reproduction steps distinguish between them. If they don't, that's
> a gap in the bug report, not in the fix.
>
> **Validate:** reproduce before fixing — if I can't reproduce it, I can't
> confirm anything. Apply the fix, confirm the reproduction now fails to
> reproduce. Run the existing test suite. Add a test that would have caught this.
> Read the diff line by line before opening a pull request.

Note the shape: the transform step is one prompt, the validation step is five
checks. That ratio is roughly right, and it's the opposite of how most people
first sketch it.

---

## The question to ask yourself

Before you call the sketch done: *if this workflow produced a wrong answer,
which box would have caught it?*

If the answer is "none of them," the workflow isn't finished — no matter how
good the transform step looks.
