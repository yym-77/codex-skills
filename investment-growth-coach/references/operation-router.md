# Operation Router

Use this file to decide what to do before answering.

## Read Current State First

When the repository is available, read in this order:

1. `state/current-plan.yaml`
2. `state/current-portfolio.yaml`
3. `state/learning-progress.yaml`
4. the latest relevant market data

Historical plans, reviews and snapshots provide context but do not override active state files.

## Minimum Inputs For Operation Advice

For "add/reduce/hold today" questions, require as many as possible:

- Current tool: off-exchange fund, ETF, stock, convertible bond, or other.
- Current position: amount, weight, profit/loss, and whether there is a base plan.
- Available cash: total spare investment cash and today's usable cash.
- Existing plan: whether regular investment already happened today.
- Target direction: exact fund/theme/ETF/stock the user wants to act on.
- Fresh market data: screenshot or text with date/time, whether intraday or after close.
- User intent: add, reduce, pause, switch, or just learn.

If position, cash, tool or timing is missing, do not provide strong action. Use operation code O0 or O1 and risk state CAUTION/STOP as appropriate.

If `state/current-portfolio.yaml` says `reconciliation_required: true`, do not calculate exact position percentages from an older snapshot. Give only bounded observation until a fresh snapshot is available.

## Data Freshness Check

When the user provides a chart or screenshot:

- Identify the trading day and timestamp if visible.
- Distinguish intraday data from close data.
- Treat pre-14:30 data as provisional for off-exchange fund decisions.
- Treat unclear or stale screenshots as observation only.
- After the close, confirm the review rather than pretending intraday estimates were final.

## Scene Routing

- 14:50 or "today add?" -> quick operation mode + operation code + risk state.
- Evening review -> learning/review mode + daily journal or decision review.
- "Is this a main theme?" -> theme scorecard + industry chain map.
- "My holdings reasonable?" -> current state + portfolio checkup + rebalancing rules.
- "Can I buy ETF/stock/convertible bond?" -> learning progress + tool upgrade path first.
- "I panicked / afraid of missing out / want all-in" -> STOP risk state first.
- "Teach me" -> level-based learning path, one small task.

## Record Routing

- Full learning answer and correction -> `learning-tasks/`.
- Daily execution and operation summary -> `decision-review/`.
- Mature rule -> `learning-notes/`.
- Current plan/portfolio/level/review due date -> `state/`.
