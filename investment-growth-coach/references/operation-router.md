# Operation Router

Use this file to decide what to do before answering.

## Minimum Inputs For Operation Advice

For "add/reduce/hold today" questions, require as many as possible:

- Current tool: off-exchange fund, ETF, stock, convertible bond, or other.
- Current position: amount, weight, profit/loss, and whether there is a base plan.
- Available cash: total spare investment cash and today's usable cash.
- Existing plan: whether regular investment already happened today.
- Target direction: exact fund/theme/ETF/stock the user wants to act on.
- Fresh market data: screenshot or text with date/time, whether intraday or after close.
- User intent: add, reduce, pause, switch, or just learn.

If position/cash/tool/timing are missing, do not provide strong action. Provide observation and ask for missing inputs.

## Data Freshness Check

When the user provides a chart or screenshot:

- Identify the trading day and timestamp if visible.
- Distinguish intraday data from close data.
- Treat pre-14:30 data as provisional for off-exchange fund decisions.
- Treat unclear or stale screenshots as observation only.
- After the close, encourage review confirmation rather than pretending intraday estimates were final.

## Scene Routing

- 14:50 or "today add?" -> quick operation mode + operation levels.
- Evening review -> learning/review mode + daily journal or decision review.
- "Is this a main theme?" -> theme scorecard + industry chain map.
- "My holdings reasonable?" -> portfolio checkup + rebalancing rules.
- "Can I buy ETF/stock/convertible bond?" -> tool upgrade path first.
- "I panicked / afraid of missing out / want all-in" -> risk-boundary file first.
- "Teach me" -> level-based learning path, one small task.
