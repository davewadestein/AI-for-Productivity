# Module 5 — Canned Problems for the Iteration Exercise

Use your own problem if you have one. These are for anyone who doesn't.

## How these work

Each problem comes in two parts.

**The problem statement** is what you paste into the AI first. It is
deliberately vague — about as vague as a real request arrives from a colleague.

**Your context card** is what *you* know about the situation and the AI doesn't.
Don't paste it up front. Hold it, see what the first answer assumes, and feed in
the pieces that turn out to matter.

That structure exists because iteration is impossible without someone who knows
more than the model. In real work that person is you. Here the context card
makes you that person.

**The exercise:** two to three rounds minimum. After each round, write down what
you changed and why. Before you settle, ask for at least one alternative
approach.

---

## 1. The slow report

**Paste this:** "Our nightly report generation takes four hours and it's getting
worse. How do we speed it up?"

**Your context card:** It's a Python script that pulls from a Postgres read
replica and writes Excel files. It was fine at 40 minutes a year ago. The team
has no data engineering staff. Migrating to a warehouse has been proposed twice
and rejected on cost. The report is used by twelve people, and eight of them
only look at one tab. Nobody has profiled it — the four hours is wall-clock time
from a cron log.

**What makes this interesting:** the first answer will propose infrastructure.
The most useful move is probably to ask what eight of twelve people actually
need.

---

## 2. The flaky test

**Paste this:** "We have a test that fails about one time in twenty and nobody
can figure out why. How should we approach it?"

**Your context card:** It's an integration test that hits a real local database.
It started failing intermittently after the team upgraded the test runner and
enabled parallel execution. It fails more often on CI than locally. Someone
added a retry three months ago and the team has mostly stopped thinking about
it. Two other tests in the same file touch the same table.

**What makes this interesting:** enough is in the card to point at a specific
cause. Watch whether the first answer gives you generic flaky-test advice or
asks you anything.

---

## 3. The onboarding problem

**Paste this:** "New engineers take too long to become productive. How do we fix
onboarding?"

**Your context card:** Team of nine, two hires in the last six months, both took
about ten weeks to ship anything non-trivial. The codebase is eight years old
with three distinct architectural eras in it. Documentation exists but is mostly
API reference, not orientation. Both recent hires said the hardest part was
knowing which of three similar-looking modules was the current one. There is no
budget for dedicated onboarding time.

**What makes this interesting:** the last constraint kills most standard
answers. Good practice at refining against a constraint rather than accepting a
plan you can't execute.

---

## 4. The alert nobody reads

**Paste this:** "Our on-call team is getting too many alerts and starting to
ignore them. What should we do?"

**Your context card:** Roughly 40 alerts per week reach a human. Historically
about three per week require action. The noisiest single alert fires on a disk
threshold that was set when the machines were half their current size. On-call
is a weekly rotation across six people. Two engineers have quietly built inbox
filters that hide alerts entirely. There's no formal alert review process, and
the last person who tried deleting alerts was overruled after an unrelated
incident.

**What makes this interesting:** partly technical, partly political. Watch
whether the first answer engages with the second part at all.

---

## 5. The document nobody updates

**Paste this:** "We have a runbook that's always out of date. How do we keep it
current?"

**Your context card:** It's a wiki page, about 4,000 words, last meaningfully
updated fourteen months ago. Four people have edit access, all senior, all busy.
The procedure it describes changed twice this year. It's read maybe twice a
quarter, almost always during an incident, which is the worst possible time to
discover it's wrong. A previous attempt to move it into the repo alongside the
code was abandoned because non-engineers couldn't edit it there.

**What makes this interesting:** the obvious answer was already tried and
failed, for a reason that's in the card. Practice at supplying a constraint the
model couldn't have guessed.

---

## 6. The vendor decision

**Paste this:** "We need to choose between building this ourselves and buying a
vendor solution. How should we decide?"

**Your context card:** The thing in question is internal search across four
document stores. Two vendors quoted, roughly $40,000 and $95,000 per year. A
build estimate came in at one engineer for four months, on a team of nine that
is already behind on committed work. Nobody has asked how many people would
actually use it — the request came from one director. There's a compliance
question about where documents would be indexed that nobody has answered yet.

**What makes this interesting:** two unanswered questions in the card matter
more than the build/buy framing. See whether iteration surfaces them or whether
you have to.

---

## 7. The meeting that should be an email

**Paste this:** "Our weekly team sync isn't useful anymore. How do we make it
better?"

**Your context card:** Nine people, one hour, weekly, running for two years.
Roughly forty minutes is status updates that nobody asks questions about. The
useful part is usually an unplanned discussion in the last fifteen minutes. Two
people are in a timezone where it lands at 7pm. The manager who runs it has said
they'd cancel it but people say they'd miss it. A written status doc was tried
for six weeks last year and quietly stopped.

**What makes this interesting:** the stated problem and the real problem differ.
Also a good non-technical option for a mixed room.

---

## 8. The number nobody trusts

**Paste this:** "Two of our dashboards report different values for the same
metric and people have stopped trusting both. How do we resolve it?"

**Your context card:** One dashboard reads from the production replica, the
other from a nightly export. The definitions of "active user" behind them were
written by different teams eighteen months apart, and neither is documented. The
gap is usually 3–8% but was 22% one week in March and nobody investigated. Both
dashboards appear in the same monthly board deck.

**What makes this interesting:** the technical fix is easy and doesn't solve the
actual problem. Watch how many rounds it takes to get there.

---

## If you finish early

Take the same problem, open a fresh conversation, and put everything from your
context card into a single first prompt. Compare it against what three rounds of
iteration produced.

Sometimes the one-shot version is better — that's a real and useful result. When
it is, it usually means the context was the whole problem and iteration was just
a slow way of supplying it.
