# 数据目录与状态

## 目录约定

Skill 安装目录只保存规则、模板和脚本。个人数据保存在独立的私有成长仓库：

```text
growth-data/
├─ state/
│  ├─ config.yaml
│  ├─ active-topic.yaml
│  ├─ learning-progress.yaml
│  ├─ review-queue.yaml
│  └─ source-registry.yaml
├─ records/
├─ decisions/
├─ planning/
│  └─ learning-backlog.md
├─ indexes/
│  ├─ topics.md
│  └─ progress.md
├─ experiments/
├─ local-only/
├─ profile.md
└─ skill-source.yaml
```

首次使用时确认数据目录和时区。不得把个人记录写入 Skill 安装目录或真实工作源码仓库。

## 事实源

- 技术正文、结论和证据：`records/`。
- 架构选择和代价：`decisions/`。
- 当前主题和完成证据：`state/active-topic.yaml`。
- 整体能力阶段、优势、缺口和下一步：`state/learning-progress.yaml`。
- 复习阶段、日期、分数和弱点：`state/review-queue.yaml`。
- 公开源码登记、版本和访问方式：`state/source-registry.yaml`。
- 待学能力问题：`planning/learning-backlog.md`。
- 行为偏好和同步配置：`state/config.yaml`。
- `indexes/` 只保存可以重建的派生视图。

机器专属源码路径保存在 `local-only/source-paths.yaml`，不得同步。

## 配置字段

- `timezone`：用户确认的 IANA 时区。
- `data_root`：成长记录仓库根目录。
- `context_linking`：`off | active-topic-only`。
- `teaching_style`：`direct | coach`。
- `storage_mode`：`local-first`。
- `auto_record`：`off | suggest`。
- `work_source_access`：`deny-by-default`。
- `git_sync`：`off | on`。
- `push_mode`：`explicit`。
- `allowed_remotes`：明确允许的私有成长仓库列表。

## 活动主题

同时只允许一个活动主题。状态使用：

```text
active | paused | stable | dropped
```

主题完成由证据决定：能独立解释核心不变量，完成最小实验，处理变化场景，并说明边界和反例。开始新主题前必须处理原主题状态，不能静默覆盖。

## 复习队列

```text
stage: D1 | D7 | D30 | relearn
status: pending | due | reviewed | relearn | stable | archived
recall: 0 | 1 | 2 | null
application: 0 | 1 | 2 | null
verification: true | false
```

复习结果只更新队列条目，不复制技术正文。

## 写入与恢复

- 写入前重新读取目标文件；检测到并发变化时停止覆盖。
- 先更新权威事实源，再按授权更新关联状态，最后重建索引。
- 任一步骤失败时如实报告，不伪造后续成功状态。
- 重复 ID、损坏 YAML、非法枚举或事实源冲突时停止自动更新。
