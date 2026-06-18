# STORM 自适应研究引擎

> 基于 Stanford STORM 方法论的多视角研究 Skill，自动推断最优视角组合，嵌入偏见防御与信源验证，产出可自动沉淀的高质量研究报告。

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/RobinZorro86/storm-research)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 核心理念

传统研究的问题不在于方法论本身，而在于它仍然把人当作"搬运工"。固定的视角需要用户手动触发，上下文压缩产生的人工摘要做完即丢，最关键的自评环节流于形式。

**STORM 自适应研究引擎的愿景**：让 Agent 成为真正的研究搭档——根据研究主题的语义特征自动选择最优视角组合，在全过程嵌入偏见防御和信源验证，最终产出一份经过"知识闭合"的高质量研究报告。

---

## 五层架构

| 层级 | 名称 | 核心功能 | 效果 |
|------|------|----------|------|
| **L1** | 语义解析层 | 自动推断研究主题的领域归属和复杂度 | 无需手动指定视角 |
| **L2** | 视角引擎层 | 从 6 大类 30+ 视角中智能匹配 Top-5~7 | 自适应 + 张力校验 |
| **L3** | 偏见防御层 | 断言级来源标记 + 红队检验 + 知识冲突检测 | 全程自检，不流于形式 |
| **L4** | 工具编排层 | 自动执行搜索、验证、深度阅读 | 从"建议搜索"→"自动搜索" |
| **L5** | 知识闭合层 | 自动格式化、沉淀、索引 | 研究即资产 |

---

## 触发词

| 触发方式 | 关键词 |
|----------|--------|
| **完整启动** | `storm研究 {topic}` / `用 storm 方法研究 {topic}` / `多视角分析 {topic}` |
| **单阶段** | `"多角度扫描" {topic}` → Phase 1<br>`"矛盾地图"` → Phase 2<br>`"综合简报"` → Phase 3<br>`"同行评审"` → Phase 4 |
| **知识闭合** | `storm入库` → 将最近一次研究成果沉淀入库 |
| **状态检查** | `storm状态` → 显示当前研究的进度和质量指标 |

**边界**（明确不做什么）：
- ❌ 不执行超过 100 次连续搜索（防滥用上限）
- ❌ 不生成投资建议、医疗建议、法律意见（高风险决策需人工复核）
- ❌ 不覆盖已有沉淀内容而不提示确认（增量更新而非强制覆写）
- ❌ 不处理纯主观审美判断（艺术品味、个人偏好等非实证话题）

---

## 快速开始

```
user: storm研究 某个研究主题

Agent:
1. 【L1 语义解析】识别为特定领域 / 复杂度
2. 【L2 视角引擎】自动选取最优视角组合（含张力校验）
3. 【L3 偏见防御】全程来源标记 + 红队检验
4. 【L4 工具编排】自动执行搜索、验证、深度阅读
5. 【L5 知识闭合】产出格式化研究报告并沉淀入库
```

**总耗时**: 3-5 分钟（对比手工 STORM 的 30-60 分钟）

---

## 文件结构

```
storm-research/
├── README.md                          # 本文件
├── SKILL.md                           # Hermes Skill 主文件（触发词 + 详细用法）
├── references/
│   ├── theory.md                      # STORM 自适应架构完整理论
│   ├── perspective-library.md         # 6 大类 30+ 视角完整定义与张力关系
│   ├── bias-guardrails.md            # 偏见三级防御详细规则
│   └── tool-recipes.md               # 每阶段精确工具调用链
└── templates/
    ├── concept-output.md             # 标准概念页输出模板
    ├── storm-session.md              # 研究会话日志模板
    ├── synthesis-report.md           # 综合简报模板
    └── contradiction-map.md          # 分层矛盾地图模板
```

---

## 理论来源

- **Stanford OVAL Lab** — STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking (NAACL 2024)
- **Mr Panda** — Skill 设计与四阶段沉淀法（触发词 · 边界 · 步骤 · 参考文件）

---

## 质量指标验收标准

每次研究完成后，系统输出自动评分报告：

| 指标 | 及格线 | 优秀线 |
|------|--------|--------|
| 视角数量 | ≥3 | ≥5 |
| 有效矛盾 | ≥1 | ≥3 |
| 来源/断言 | ≥0.5 | ≥1.0 |
| 置信度均值 | ≥0.6 | ≥0.75 |
| 低置信度标注 | 100% | 100% |
| 反方覆盖 | ≥50% | ≥80% |
| 知识冲突检出 | 100% | 100% |

---

## 安装

### Hermes Agent

```bash
# 直接安装
hermes skills install https://github.com/RobinZorro86/storm-research/blob/main/SKILL.md

# 或手动复制到 skills 目录
cp -r storm-research ~/.hermes/skills/research/
```

### Claude Code / Codex / 其他 Agent

```bash
# 复制 references/ 和 templates/ 到工作目录
cp -r references/ ~/your-project/.agent-resources/
cp -r templates/ ~/your-project/.agent-templates/

# 直接使用 SKILL.md 中的 Prompt 模板（独立可用）
cat references/perspective-library.md   # 视角库
cat references/bias-guardrails.md      # 偏见防御规则
```

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.0** | 2026-06-19 | 初始版本：五层架构 + 自适应视角引擎 + 偏见三级防御 + 知识闭合 |

---

## 贡献

- 作者: Robin.Z / Luffy Team
- 方法论来源: Stanford OVAL Lab (NAACL 2024)
- 构建框架: Hermes Agent Skill System

## 许可证

MIT License — 详见 [LICENSE](LICENSE) 文件
