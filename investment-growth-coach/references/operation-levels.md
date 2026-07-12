# Operation Codes And Risk States

Do not mix action strength with risk protection. Express every operation with two independent fields:

```text
Operation code: O0-O4
Risk state: NORMAL / CAUTION / STOP
```

## Operation Code

| Code | Meaning | Typical output |
| --- | --- | --- |
| O0 | No action, observe only | Data insufficient, setup unclear, or no need to act. |
| O1 | Execute original base plan only | Continue the active regular-investment plan; no extra action. |
| O2 | Pause or reduce base plan | Position is near a cap, the original logic is weakening, or risk is rising. |
| O3 | Small extra add | Inputs are sufficient, position and cash allow it, and evidence supports a bounded trial. |
| O4 | Small reduce or take profit | Position is overweight, the thesis is weakening, or risk/reward has deteriorated. |

## Risk State

| State | Meaning | Required behavior |
| --- | --- | --- |
| NORMAL | No exceptional emotional or information risk | Follow the normal router and position rules. |
| CAUTION | Evidence is mixed, data is approximate, or emotion is elevated | Downgrade action size; prefer O0 or O1. |
| STOP | Panic, FOMO, all-in/all-sell intent, severe uncertainty, or missing critical inputs | Do not make a large decision. Delay, observe, review, or simulate. |

Rules:

- `STOP` is not a higher or more aggressive operation level. It is a protection state.
- Read `state/current-plan.yaml` and `state/current-portfolio.yaml` before assigning an operation code.
- Do not attach fixed money amounts unless current capital, cash, position and caps are sufficiently fresh.
- When portfolio data is approximate or requires reconciliation, the default risk state is at least `CAUTION`.
- A single market signal cannot independently upgrade O0/O1 to O3 or trigger O4.
