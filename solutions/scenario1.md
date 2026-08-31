## Scenario 1 Solution

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

