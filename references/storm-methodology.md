# STORM 方法论理论基础

来源：Stanford OVAL Lab, "STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking" (NAACL 2024)

## 核心实验结果

| 指标 | 传统单提示 | STORM 多视角 | 提升 |
|------|----------|-------------|------|
| 组织度 | baseline | +25% | 文章结构更清晰 |
| 覆盖面 | baseline | +10% | 遗漏论点更少 |

## STORM 原始 3 阶段

```
Phase 1: Perspective-Guided Question Asking
  → 模拟不同角色向搜索引擎提问，收集多维信息

Phase 2: Simulated Conversation (Information Gathering)
  → 用 GPT-4 扮演作者和不同视角的"采访者"进行对话

Phase 3: Discourse Planning + Article Generation
  → 基于对话历史生成大纲，再逐节写作
```

**原始系统的局限**（本 skill 已修复）：
1. ❌ 不自检偏见（来源选择和事实验证无反馈回路）
2. ❌ 预设视角固定（没有根据主题自适应）
3. ❌ 无置信度量化（所有结论平级呈现）
4. ❌ 无现有知识对比（每次从零开始，无法增量积累）

## 本 skill 的改进

| 原版问题 | 我们的修复 |
|---------|-----------|
| 不自检 | 添加 4 层偏见防御（红队/置信度地板/Wiki冲突/时效衰减） |
| 固定视角 | 自适应视角引擎（按 domain 智能选择） |
| 无置信度 | 每个断言携带 [来源:XXX][置信度:X.X] |
| 从零开始 | 自动检索 Wiki 已有概念，增量构建 |
| 纯文本输出 | 标准化概念页面（C-XXX 格式），自动入库 |

## 关键直觉

单提示查询得到的是"多数观点的最大公约数"。真正的深度理解需要**主动寻找分歧**——因为分歧所在之处才是知识增长的真实前沿。

> "The most productive disagreements are not between people who disagree about conclusions, but between people who disagree about what constitutes evidence." — Paul Graham

## Live Demo

storm.genie.stanford.edu

## 原始 Prompt（参考）

NAACL 论文中 Stage 1 的核心 prompt（精简版）：

```
You are an expert Wikipedia author researching the topic: {topic}.

Step 1 — Brainstorm 5 different perspectives that would ask different questions about this topic.
Step 2 — For each perspective, generate 2 deep questions that only that perspective would care about.
Step 3 — Use a search engine to find answers to each question.
Step 4 — Summarize what you learned from each perspective.
```

本 skill 将此扩展为 4 阶段 + 自适应视角 + 偏见防御 + 自动入库。