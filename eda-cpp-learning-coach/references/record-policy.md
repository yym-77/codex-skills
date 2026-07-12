# 记录策略

## 写入条件

仅在用户明确说“记录、保存、写入、更新、升级深度复盘”等表达时写入技术正文。分析、讲解、看看、复盘一下只授权对话内输出，除非同时明确要求保存。“开始间隔复习”只授权更新对应复习队列条目，不授权修改技术正文。

“结束今天”是有限本地整理授权，只允许：

1. 更新已经存在的本地草稿，不新建技术正文。
2. 更新 `state/active-topic.yaml` 中的 `updated_at`、`next_action` 和已取得的完成证据。
3. 更新已经存在的复习队列条目。
4. 重建可以从事实源恢复的派生索引。

“结束今天”不授权创建新技术记录、将快速记录升级为深度复盘、创建架构决策、commit 或 push。用户说“结束今天并同步记录”时，Git 操作仍必须通过 `git-sync.md` 的安全门禁。

任何写入前先读取 `privacy.md`，再执行：

1. 确认数据目录和目标文件。
2. 检索相似标题、主题 ID、错误模式和关键词，优先更新已有记录。
3. 生成脱敏草稿，区分事实、假设、结论和未知项。
4. 使用唯一记录 ID，写入一个权威文件。
5. 重新读取写入结果；失败时停止，不更新索引或复习状态。
6. 仅在记录值得复习且用户同意时加入复习队列。

## 权威路径

使用以下路径，避免 `quick/` 与 `deep/` 之间复制：

```text
records/YYYY/MM/YYYY-MM-DD-short-slug.md
```

在同一文件中用 `depth: quick | deep` 表示深度。升级深度复盘时修改原文件并保留 ID；其他索引只保存 ID、状态和链接。

## 模板选择

- 默认记录：复制 `assets/templates/quick-note.md`。
- 深度复盘：在原文件中采用 `assets/templates/deep-review.md` 的结构。
- 形成明确架构选择、备选方案和可复核代价时：在 `decisions/YYYY/MM/YYYY-MM-DD-short-slug.md` 创建独立决策记录，并从深度复盘链接过去，不重复问题正文。
- 学习旁支：更新由 `assets/templates/learning-backlog.md` 初始化的 `planning/learning-backlog.md`，只保存简短能力问题和权威链接。

## 元数据

由 Skill 维护元数据，用户不需要逐项填写。至少保存：

- `id`、`created_at`、`updated_at`
- `topic_id`、`depth`、`status`、`confidence`
- `source_class`、`confidentiality`
- `sync_allowed`、`redaction_checked`
- `tags`

复习阶段、到期时间、分数、弱点和稳定状态只保存在 `state/review-queue.yaml`，不得在技术记录中保存会随复习变化的 `review_state` 副本。

不得把真实公司、客户、项目、路径、类名或业务标识放进标题、slug、标签和提交信息。

`source_class` 只允许：

- `public`：公开标准、官方文档和开源实现。
- `personal`：用户自行编写的实验和个人资料。
- `work-derived`：从已授权工作经验重新抽象的规律，不包含原始材料。

工作衍生记录必须使用 `confidentiality: restricted-derived`；不得通过行尾注释或其他拼写扩展枚举值。

## 内容要求

快速记录回答六件事：背景、原判断、证据、结论与边界、认知修正、下一步。

深度复盘补充：影响、事实、假设、根因、修复或决策、回归验证、预防措施、可复用规律和变式场景。

架构决策的事实源是 `decisions/` 中对应文件。它只记录选择、驱动因素、代价、验证和重新评估条件；问题过程仍留在关联深度复盘中。

记录以帮助未来判断为目标，不默认添加个人贡献、岗位价值、面试表达或简历字段。
