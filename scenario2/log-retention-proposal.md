# Proposal: Revising Application Log Retention

**Internal working document — Platform Engineering**
**Circulated for comment. Not yet approved.**

## Background

We currently retain all application logs in hot storage for 400 days. This
policy was set in 2021, when our log volume was roughly 40 GB per day and the
cost of retention was not material. Volume is now approximately 1.9 TB per day,
driven mostly by the migration of the payments and notifications services onto
structured logging, and by debug-level output that several teams enabled during
incident response and never turned back off.

Hot storage now accounts for a little over a third of our observability spend.
At current growth, it will pass half within three quarters. This proposal
recommends a tiered retention model. It does not recommend reducing what we
log, which is a separate conversation that should involve the service owners
rather than the platform team alone.

## Proposed model

Logs would move through three tiers:

**Hot (searchable, sub-second queries): 30 days.** Covers the overwhelming
majority of real queries. Our sampling of the query log over the last quarter
found that 94% of searches touched data less than three weeks old, and 98%
touched data less than 30 days old.

**Warm (searchable, queries may take several minutes): 31–180 days.** Same
data, cheaper storage, slower retrieval. Suitable for trend analysis and
post-incident review, not for live debugging.

**Cold (archival, restore required): 181 days–7 years.** Compressed object
storage. Restoring a day of logs would take an estimated 4–6 hours and require
a ticket to the platform team.

Estimated annual saving is between $310,000 and $360,000, most of it from the
hot-to-warm transition rather than from cold archival.

## Complications

**The 7-year figure is not ours to choose.** Payments logs are subject to a
regulatory retention requirement that our compliance team reads as seven years.
Two of our peer companies interpret the same rule as five. We have asked
outside counsel for a written opinion and do not have it yet. Until we do, the
seven-year figure should be treated as a placeholder, and the cold tier cost
estimate carries corresponding uncertainty.

**Not all services can be treated identically.** The fraud detection team runs
retrospective model training against logs up to 90 days old on a regular
cadence. Moving their data to warm at 30 days would make that job substantially
slower, though not impossible. They have asked for a 90-day hot window as an
exception. If granted, roughly 40% of the projected saving disappears, because
fraud detection is one of our largest log producers.

**The restore path is untested.** We have never restored a full day of logs
from cold storage in this architecture. The 4–6 hour estimate is derived from
vendor documentation and a single test with a much smaller dataset. Before this
policy takes effect, we should run a realistic restore drill, and we should
treat the estimate as unvalidated until we do.

**Deletion is irreversible and partly unaudited.** We do not currently have a
reliable inventory of which teams depend on logs older than 30 days for
scheduled jobs. A search of the internal job scheduler found eleven jobs
referencing log data, but that search would not catch jobs that query through
the API layer.

## Recommended sequence

1. Obtain the written opinion on the payments retention requirement before
   committing to any cold-tier timeline.
2. Run a full-scale restore drill and publish the measured timing.
3. Circulate a request to all service owners asking them to identify jobs that
   read logs older than 30 days. Allow four weeks for responses.
4. Apply the tiered policy to non-payments, non-fraud services first, as a
   pilot, for one quarter.
5. Revisit the fraud detection exception with measured data from the pilot
   rather than with estimates.

We would not recommend applying the policy globally in a single change. The
combination of an untested restore path and an incomplete dependency inventory
means the failure mode — discovering after deletion that something needed the
data — is unrecoverable.

## Open questions for reviewers

- Is a 30-day hot window acceptable for on-call debugging in your service? If
  not, what is the shortest window that would be?
- Does your team run any scheduled job that reads log data older than 30 days?
- Would a 6-hour restore time be acceptable during an active incident, or does
  your service need a faster path?
