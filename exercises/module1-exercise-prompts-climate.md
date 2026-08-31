# Module 1 Exercise — Non-Coding Prompts (Science, Climate, and General)

A companion to the coding sheet, for participants whose expertise isn't in a
codebase. Same structure: a concept where the popular version is wrong, paired
with a follow-up that forces the issue.

## One design difference worth knowing

The coding prompts have an advantage — you can run the code and the console
settles the argument. Nothing here has that. A participant who isn't an expert
in the topic can't tell a correct explanation from a confident wrong one just by
reading it.

So these are weighted toward claims a single authoritative source can settle in
one search: a NOAA or NASA page, an IPCC summary, a DOI lookup. Tell people that
checking is part of the exercise, not an optional extra. **The point isn't to
catch the model out — it's to notice that reading carefully wasn't enough.**

**Test two or three yourself the week before.** Model behavior shifts and some of
these get fixed. Nothing here is guaranteed to fail.

---

## The strongest one for this audience

**Ask for sources, then check them.**

> Ask: Give me five peer-reviewed papers on [any topic you know something
> about]. Include authors, journal, year, and DOI.
>
> Then: look up each DOI.

If the tool has no search available, expect a mix — some real, some composites
of a real author and a plausible-but-nonexistent title, all delivered with
identical confidence. If it does search, the papers should be real, and the
check becomes: does each paper actually say what the summary claims?

This is the single best prompt on either sheet. It's checkable by anyone, it
takes three minutes, and it sets up the retrieval slide directly. If you only
have time to point non-technical participants at one thing, point them here.

---

## Climate and environment

**1. The greenhouse analogy**

> Ask: Explain how the greenhouse effect warms the planet.
>
> Follow up: Does an actual glass greenhouse stay warm by the same mechanism?

Watch for: the analogy presented as if the physics match. A real greenhouse works
mainly by preventing warm air from convecting away, not by trapping infrared. The
naming is a historical accident, and explanations often paper over it.

**2. Amazon oxygen**

> Ask: How much of the world's oxygen does the Amazon rainforest produce?
>
> Follow up: What's the *net* figure, once you account for decomposition and
> respiration in the forest itself?

Watch for: the widely repeated "20% of the world's oxygen." A mature forest's net
oxygen contribution is close to zero — it consumes roughly what it produces. Good
example of a number that's everywhere and still wrong.

**3. Melting ice and sea level**

> Ask: Does melting sea ice raise sea level? What about melting land ice?
>
> Follow up: Is the sea ice contribution exactly zero, or just very small?

Watch for: "floating ice displaces its own weight, so the effect is zero." Nearly
right — but melting fresh sea ice into salt water produces a small nonzero rise.
A good demonstration of an answer that's correct at the level it's usually taught
and wrong in the detail.

**4. Ozone versus climate**

> Ask: Explain the relationship between the ozone hole and climate change.
>
> Follow up: When is the ozone layer projected to recover, and is the Antarctic
> hole closing or still forming each year?

Watch for: conflating the two problems, and over-simplifying recovery. The layer
is on a recovery trajectory while the hole still forms annually and varies
substantially year to year. Recovery projections differ by region and are decades
out.

**5. Cloud seeding**

> Ask: How effective is cloud seeding at increasing precipitation? Give me a
> percentage.
>
> Follow up: How confident is that figure, and how was it measured?

Watch for: a crisp single number. Published estimates span a wide range and the
central difficulty is attribution — separating seeded precipitation from what
would have fallen anyway. An answer that gives a percentage without that caveat
has dropped the most important part.

**6. Event attribution**

> Ask: Can scientists say whether a specific hurricane or heatwave was caused by
> climate change?
>
> Follow up: Has that changed in the last decade? What does attribution science
> do now?

Watch for: the outdated "no single event can be attributed" line. Attribution
science has moved considerably. This is a version-drift example in a
non-technical domain.

---

## Health, nutrition, and the body

**7. Metabolism and age**

> Ask: How does metabolism change as you age?
>
> Follow up: What did the large 2021 study in *Science* on total energy
> expenditure across the lifespan find?

Watch for: "metabolism slows in your thirties," which is the folk version. The
large-scale data suggest it's roughly stable from about 20 to 60. Popular health
writing dominates the training data here.

**8. Herd immunity**

> Ask: What percentage of a population needs immunity to achieve herd immunity?
>
> Follow up: Does that number depend on the disease? What determines it?

Watch for: a single figure like 70%. The threshold depends on transmissibility
and varies enormously between diseases.

---

## Statistics and interpretation

These two are worth including for any audience. Both are misstated constantly,
including in published work.

**9. Confidence intervals**

> Ask: What does a 95% confidence interval mean?
>
> Follow up: Does it mean there's a 95% probability the true value lies inside
> this particular interval?

Watch for: agreeing with the follow-up. Under the standard frequentist
definition, that's not what it means — the 95% describes the long-run behavior of
the procedure, not the probability for one computed interval. Answers often give
the correct definition first and then endorse the wrong one when prompted, which
is a striking thing for a room to watch.

**10. P-values**

> Ask: Explain what a p-value tells you.
>
> Follow up: Does a p-value of 0.03 mean there's a 3% chance the result is due to
> chance?

Watch for: the same pattern. It doesn't, and the wrong version is extremely
common.

---

## Physical sciences

**11. Earthquake magnitude**

> Ask: Explain the Richter scale and what a magnitude 7 means compared to a 6.
>
> Follow up: Is the Richter scale still what agencies use? And is the difference
> between 6 and 7 a factor of 10 in shaking, in energy, or both?

Watch for: two errors at once. Agencies generally report moment magnitude now,
not Richter; and the factor of 10 applies to wave amplitude, while energy scales
by roughly 32× per unit.

**12. Carbon numbers**

> Ask: How much CO2 does a mature tree absorb per year?
>
> Follow up: What's the range across species, climate, and age, and where does
> your figure come from?

Watch for: a confident single number. The real range is wide enough that any
single figure is close to meaningless without conditions attached.

---

## Local and regulatory

Especially good because the answer is checkable against a government page, and
because rules change.

**13. Rainwater collection in Colorado**

> Ask: Is it legal to collect rainwater in a barrel at a home in Colorado?
>
> Follow up: Has that changed? What does current state law allow, and what are
> the limits?

Watch for: outdated answers. Residential rain barrels were prohibited for a long
time under Colorado's prior-appropriation water law, and the rules changed in
2016 with specific limits on barrels and volume. Verify current law against the
state's own page — that verification *is* the exercise.

**14. Any local rule you know cold**

> Ask about a permitting requirement, a local ordinance, or a state regulation
> you deal with professionally.
>
> Follow up: What's the citation? I want to read the actual text.

Watch for: confident specifics with vague or invented citations. Substitute
whatever your participants actually know — the pattern generalizes.

---

## Organizational and internal

**15. Your own institution**

> Ask: Explain how [your organization's internal process, policy, or system]
> works.

Watch for: a detailed, confident, entirely invented answer. This is the most
memorable version for most rooms and works regardless of technical background.

Don't paste any real internal detail to set it up — the point is what happens
when the model has nothing to go on, so the name alone is enough.

---

## Debrief notes specific to this group

The coding participants can point at a console. This group can't, so steer the
debrief toward *how they checked* rather than *what was wrong*:

- "How did you confirm it?" Someone who says "it sounded right" has found the
  actual lesson, and should say so out loud.
- "Who got something technically true but misleading?" Usually more common here
  than outright falsehood, and closer to real use.
- "Did the follow-up change the first answer?" When it does, note that neither
  version arrived with a confidence signal attached.
- If someone's follow-up got the wrong answer defended rather than corrected,
  name it — it previews the pitfalls slide's point about self-verification.

If a participant reports everything checked out, that's a fine result: they had
to check in order to know that, and the checking is the habit.
