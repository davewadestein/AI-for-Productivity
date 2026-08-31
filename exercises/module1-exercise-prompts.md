# Module 1 Exercise — Concepts That Reliably Expose Errors

For the facilitator, and for participants who need a topic.

The exercise asks people to have AI explain something they know well, then ask a
pointed follow-up. It fails in a specific way: someone picks a topic, gets a
fluent answer, and concludes it was correct — either because it was, or because
they didn't know enough to catch what was wrong.

These prompts are chosen to make that harder. Each pairs a concept where the
popular explanation is subtly wrong with a follow-up question that forces the
issue.

**Test two or three of these yourself the week before.** Model behavior shifts,
and some of these get fixed over time. If one comes out clean in your testing,
swap it. Nothing here is guaranteed to fail — it's weighted toward topics where
errors are common, not certain.

---

## Why these particular topics fail

Six patterns account for most of it. Naming them during the debrief is more
useful than any individual example, because participants can apply the pattern
to their own domain afterward.

**Folk explanations.** When the widely repeated version of a concept is wrong,
the training data is full of the wrong version. Popularity and correctness come
apart, and the model follows popularity.

**Spec versus implementation.** Models blur what a standard requires with what
one popular implementation happens to do, and state both with equal confidence.

**Cross-system blending.** Ask about a concept that behaves differently in
PostgreSQL and MySQL and you may get a coherent answer describing neither.

**Version drift.** Behavior that changed recently, or defaults that moved. The
answer describes a version that's no longer current.

**Precise numbers.** Limits, thresholds, complexity bounds, sizes. Approximate
recall of an exact figure reads as confident and is often slightly off.

**Proprietary and internal.** Anything specific to your organization. The model
has nothing to draw on, but the question looks answerable, so it produces
something.

---

## Ready-to-use prompts

Each entry: what to ask, then the follow-up, then what to watch for.

### Immediately verifiable — best for skeptics

These can be checked in a console in under a minute, which makes them the
strongest choices. No expertise required to confirm the error.

**1. JavaScript coercion**

> Ask: Explain how `==` type coercion works in JavaScript. Include a table of
> what happens when comparing `[]`, `null`, `0`, and `""` against each other.
>
> Follow up: For each row, tell me what the actual result is. I'm going to run
> these in a console.

Watch for: `null == 0` is `false`, but `null >= 0` is `true`. `[] == false` is
`true`. `NaN == NaN` is `false`. Coercion tables generated from memory
frequently contain at least one wrong cell, and the console settles it
instantly.

**2. Unicode length**

> Ask: Explain the difference between characters, code points, and grapheme
> clusters in Unicode.
>
> Follow up: What does Python's `len()` return for "👨‍👩‍👧"? What about
> `len()` on "é" written as e + combining accent?

Watch for: specific counts that are off by one or two. The concept explanation
is usually fine; the concrete number is where it breaks.

**3. Python integer identity**

> Ask: Explain the difference between `is` and `==` in Python.
>
> Follow up: Is the small-integer caching behavior guaranteed by the language
> spec, or is it a CPython implementation detail? What's the exact cached range?

Watch for: presenting an implementation detail as a language guarantee, and
stating the cached range with more confidence than warranted.

### Folk explanations

**4. CAP theorem**

> Ask: Explain the CAP theorem.
>
> Follow up: In a system experiencing no network partition, what does CAP say
> you must give up?

Watch for: "pick two of three," which is the popular framing and is wrong. With
no partition, CAP requires giving up nothing. The theorem is about what happens
*during* a partition. This one is reliable and the correction is crisp.

**5. JWTs**

> Ask: Explain what a JWT is and how it keeps data secure.
>
> Follow up: Can someone who intercepts my JWT read its contents without the
> signing key?

Watch for: any implication that JWTs are encrypted. A standard signed JWT is
base64-encoded, not encrypted — anyone can read the payload. The phrasing "keeps
data secure" in the first prompt is deliberate bait.

**6. HTTPS and privacy**

> Ask: Explain what HTTPS encrypts when I visit a website.
>
> Follow up: Can my network operator tell which specific site I visited? What
> about which page on that site?

Watch for: over-claiming. The hostname typically leaks via SNI and DNS even when
the path doesn't. Answers often omit this entirely.

**7. Mutex versus semaphore**

> Ask: Explain the difference between a mutex and a semaphore.
>
> Follow up: Is a mutex just a binary semaphore? Does either have an ownership
> requirement?

Watch for: "a mutex is a binary semaphore," which is common and glosses over
ownership — a mutex must generally be released by the thread that acquired it.

**8. REST**

> Ask: What makes an API RESTful?
>
> Follow up: By Fielding's original constraints, is a JSON-over-HTTP API with no
> hypermedia controls actually REST?

Watch for: the folk definition (JSON, HTTP verbs, nouns in URLs) presented as
the real one. Useful because most participants hold the folk definition too.

### Spec versus implementation

**9. HTTP method idempotency**

> Ask: Explain which HTTP methods are idempotent and why.
>
> Follow up: Is PATCH idempotent according to the RFC? Is it idempotent in
> practice?

Watch for: PATCH described as idempotent. The spec doesn't require it. DELETE is
also worth probing — idempotent by spec, though response codes may differ
between calls.

**10. HTTP 401 versus 403**

> Ask: When should an API return 401 versus 403?
>
> Follow up: The status text for 401 is "Unauthorized." Does 401 actually mean
> the user isn't authorized?

Watch for: 401 means *unauthenticated*, despite its name. The naming is a known
wart in the spec and answers often repeat the misreading.

### Cross-system blending

**11. Database isolation levels**

> Ask: Explain the SQL isolation levels and which anomalies each prevents.
>
> Follow up: Does REPEATABLE READ prevent phantom reads in PostgreSQL? In MySQL
> InnoDB? Are those the same answer?

Watch for: a single answer that describes neither system correctly. The
databases genuinely differ here, and answers tend to blend them.

**12. Index performance**

> Ask: Explain when adding a database index will speed up a query.
>
> Follow up: Give me three cases where adding an index makes things worse or
> does nothing.

Watch for: the first answer is usually competent but one-sided. The follow-up
tests whether it can argue against the thing it just recommended — a useful
demonstration in itself.

### Version drift

**13. Python's GIL**

> Ask: Explain the GIL and what it means for Python concurrency.
>
> Follow up: What's the current status of free-threaded Python? Which version
> introduced it, and is it the default?

Watch for: outdated framing, or confident claims about current status. This
tests the knowledge-cutoff problem directly, which sets up the retrieval slide
well.

**14. Anything with a version number**

> Ask about the default behavior of a tool your team uses, naming the version.
>
> Follow up: Did that default change in a recent release? Which one?

Watch for: defaults described as they were two years ago. This generalizes to
whatever stack your participants actually use.

### Precise numbers

**15. Limits and thresholds**

> Ask: What are the size and rate limits for [a service your team uses]?
>
> Follow up: Where is that documented? I want to check the exact figure.

Watch for: plausible round numbers. Then check the actual docs. This is a good
one for the debrief because the gap between "sounds right" and "is right" is so
visible.

### Proprietary and internal

**16. Your own systems**

> Ask: Explain how [internal system name] handles [something specific].

Watch for: a confident, detailed, entirely invented answer — especially if your
internal tool has a name that sounds like a public product. This is the most
memorable version of the exercise for most rooms, and the one that most directly
changes behavior afterward.

Don't paste any actual internal detail to set it up. The point is what happens
when the model has nothing, so an unadorned name is all you need.

---

## Running the debrief

Two questions, as in the speaker notes. Then, if the room needs a push:

- "Who got something that was *technically* true but misleading?" Often more
  interesting than outright errors, and closer to what people will actually
  encounter.
- "Did the follow-up change the first answer?" If yes: neither version came with
  a confidence signal. That's the observation the whole module is built on.
- "Did anyone's follow-up get a wrong answer *defended* rather than corrected?"
  Worth naming when it happens — it previews the pitfalls slide's point about
  self-verification.

If someone reports the model handled everything correctly: that's a legitimate
result, and the response is "notice that you had to check in order to know
that." The habit is the lesson, not the error count.
