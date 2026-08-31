# Planned Failover Procedure — Primary Database Cluster

**Operations guide, revision 7**
**Owner: Platform Reliability**

This document covers *planned* failover only — the procedure used during
maintenance windows and scheduled primary replacements. Unplanned failover
following a primary loss is a different procedure and is documented separately.
Do not follow this guide during an active outage.

## Before you begin

Failover requires two operators. One executes; the second confirms each
verification step independently. This is not a formality — the most severe
incident we have had in this system was a single operator misreading
replication lag and proceeding, so the second pair of eyes is a hard
requirement rather than a recommendation.

Confirm all of the following before touching anything. If any of these is not
true, stop and escalate rather than working around it.

Replication lag on the target replica must be under 5 seconds and must have
been stable under that threshold for at least 10 minutes. A momentary dip below
5 seconds is not sufficient. If lag is spiking, the underlying cause needs to be
understood before failover, because failing over to a replica that cannot keep
up under normal load will simply move the problem.

The target replica must be running the same major version as the current
primary. Minor version differences are acceptable in the direction of the
replica being *newer*, but never older. A replica on an older minor version can
fail to replay writes from the newer primary, and the failure is often silent
until hours later.

Confirm there is at least one additional healthy replica beyond the failover
target. Failing over when the target is the only remaining replica leaves the
cluster with no redundancy at the moment it is most fragile.

Check that no schema migration has run in the last 30 minutes and none is
scheduled to run in the next 60. Migrations in flight during failover are the
most common cause of the cluster ending up in an inconsistent state.

Finally, confirm the maintenance window is still open and has at least 45
minutes remaining. If less than 45 minutes remain, reschedule. A failover that
must be rolled back takes longer than the failover itself.

## Executing the failover

Announce in the operations channel before starting, including the expected
duration and the names of both operators.

Begin by putting the application into read-only mode. Wait for in-flight writes
to drain — the write queue depth metric should reach zero and stay there for 30
seconds. Do not skip the 30-second hold. A queue depth that touches zero
momentarily can still have writes in flight that have not yet registered.

Once writes have drained, stop replication on the target replica and record the
final replication position. Write this position down somewhere outside the
system. If the failover has to be rolled back, this figure is the only reliable
way to determine what was and was not replicated, and it is not recoverable
after promotion.

Promote the target replica. Promotion is not reversible through the tooling —
rolling back means restoring from backup and replaying, which is measured in
hours rather than minutes. Treat the promotion command as the point of no
return and confirm with the second operator immediately before running it.

Redirect application traffic to the new primary. Then, and only then, take the
old primary out of the load balancer pool. Doing these in the reverse order
produces a window in which the application has no database at all.

Bring the application out of read-only mode.

## After the failover

Reconfigure the remaining replicas to follow the new primary. They will not do
this automatically, and a replica still following the old primary will silently
diverge — it will appear healthy in monitoring while accumulating data that
exists nowhere else.

Verify write traffic is reaching the new primary by checking transaction rate
rather than by checking that the application appears to work. An application
can appear healthy while writing to a stale connection pool.

Leave the old primary running but isolated for at least 24 hours. Do not
decommission it immediately. If a problem surfaces that requires the pre-failover
state, the old primary is the fastest path to it, and 24 hours is roughly the
window in which such problems have historically appeared.

Update the cluster topology documentation the same day. An out-of-date topology
document is the most common cause of confusion during the *next* incident.

File the failover record within one business day, including the recorded
replication position, both operator names, and the actual duration. If anything
deviated from this procedure, note it explicitly — deviations that go unrecorded
tend to become informal practice.
