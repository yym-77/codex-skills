# 数据目录与状态

## 目录约定

Skill 安装目录只保存规则、模板和脚本。用户数据放在明确配置的独立目录：

```text
growth-data/
├─ state/
│  ├─ config.yaml
│  ├─ active-topic.yaml
│  └─ review-queue.yaml
├─ records/
│  └─ YYYY/MM/*.md
├─ decisions/
│  └─ YYYY/MM/*.md
├─ planning/
│  └─ learning-backlog.md
├─ indexes/
│  ├─ topics.md
│  └─ progress.md
└─ local-only/
```

首次使用时先询问数据目录和时区；用户未指定时，不擅自在 Skill 安装目录或工作源码仓库中创建记录，也不把时区写死为运行环境推测值。

若数据目录使用 Git，将 `assets/templates/growth.gitignore` 复制为数据目录的 `.gitignore`，默认排除 `state/`、`planning/`、`indexes/` 和 `local-only/`。

## 每类字段的事实源

- 技术正文、结论、证据和边界：对应 `records/` 文件。
- 当前主题、完成证据和主题状态：`state/active-topic.yaml`。
- 到期日期、复习阶段、分数、弱点和稳定状态：`state/review-queue.yaml`。
- 待学能力问题、优先级和选择状态：`planning/learning-backlog.md`。
- 架构选择、代价和重新评估条件：`decisions/` 中对应文件。
- 行为偏好、时区、数据根目录和 Git 允许名单：`state/config.yaml`。
- `indexes/`：可从上述事实源重建，不保存独有信息。

技术记录中不得保存会随复习变化的 `review_state` 副本。记录是否进入复习、当前阶段和稳定状态都以 `state/review-queue.yaml` 为准。

## 配置字段

`state/config.yaml` 使用 `assets/templates/config.yaml` 初始化。重要字段约束：

- `timezone`：必须是用户确认的 IANA 时区，例如 `Asia/Shanghai`；为空时不得计算复习到期日或日期文件名。
- `data_root`：用户确认的成长数据目录，不得指向 Skill 安装目录或工作源码仓库。
- `context_linking`：`off | active-topic-only`。
- `teaching_style`：`direct | coach`。
- `storage_mode`：首版只允许 `local-first`。
- `auto_record`：`off | suggest`，不得设为自动写入。
- `work_source_access`：首版只允许 `deny-by-default`。
- `git_sync`：`off | on`。
- `push_mode`：首版只允许 `explicit`。
- `allowed_remotes`：字符串列表；为空时禁止 commit 后的远端同步。

比较 Git remote 时先规范化 SSH 与 HTTPS 表达，但不得因为仓库名称相同就忽略所有者、主机或路径差异。

## 活动主题

同时只允许一个 `active` 主题。`status` 合法值为：

```text
active | paused | stable | dropped
```

结束主题不按七天计时，而按证据判断：

- 能独立解释核心不变量。
- 能完成一个最小实验。
- 能处理一个变化场景。
- 能说明适用边界和反例。

开始新主题时，将原主题标记为 `paused`、`stable` 或 `dropped`，不能静默覆盖。

## 复习队列

复习条目使用以下枚举：

```text
stage: D1 | D7 | D30 | relearn
status: pending | due | reviewed | relearn | stable | archived
recall: 0 | 1 | 2 | null
application: 0 | 1 | 2 | null
verification: true | false
```

复习结果只更新对应条目，不复制技术正文。发现新反例或重复问题时复用同一 `record_id`，将状态恢复为 `relearn`。

## “结束今天”的有限状态更新

“结束今天”只允许：

- 更新既有草稿；
- 更新活动主题的 `updated_at`、`next_action` 和已有完成证据；
- 更新已经存在的复习队列条目；
- 重建派生索引。

不得新建技术记录、升级深度复盘、创建架构决策、commit 或 push。

## 写入与恢复

- 写入前重新读取目标文件；若更新时间或内容已变化，停止覆盖并报告并发修改。
- 先写权威记录或决策，再按明确授权更新活动主题、积压或复习状态，最后更新派生索引。
- 任一步骤失败时保留已写结果并报告，不伪造后续成功状态。
- 发现重复 ID、损坏 YAML、未知 schema 版本、非法枚举或相互矛盾的路径时停止自动更新。
- 多窗口或多 Agent 同时工作时只允许一个归档写入者；冲突交由用户决定。

推荐用 `assets/templates/` 中的 YAML 与 Markdown 模板初始化状态和积压文件。
