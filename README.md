# STORM 自适应研究引擎

> 基于 Stanford STORM 方法论的多视角研究 Skill，自动推断最优视角组合，嵌入偏见防御与信源验证，产出可自动沉淀的高质量研究报告。

[![Version](https://img.shields.io/badge/version-1.1.1-blue.svg)](https://github.com/RobinZorro86/storm-research)
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

```text
storm-research/
├── README.md                          # 本文件
├── LICENSE                            # MIT 许可证
├── SKILL.md                           # Hermes Skill 主文件（触发词 + 详细用法）
├── agents/
│   └── openai.yaml                    # OpenAI Agent 配置示例
├── references/
│   ├── theory.md                      # STORM 自适应架构完整理论
│   ├── adaptive-algorithm.md        # 视角选择算法伪代码
│   ├── perspective-library.md       # 6 大类 30+ 视角完整定义
│   ├── perspectives.json            # 机器可读视角库（供脚本使用）
│   ├── bias-guardrails.md          # 偏见三级防御详细规则
│   └── tool-recipes.md             # 每阶段精确工具调用链
├── schemas/
│   └── session.schema.json          # 研究会话 JSON Schema
├── scripts/
│   ├── select_perspectives.py       # 确定性视角选择脚本
│   ├── validate_session.py          # 会话验证 + 覆盖率指标
│   ├── validate_skill.py            # Skill 完整性校验
│   ├── render_report.py             # 报告渲染
│   └── check_links.py               # 来源链接有效性检查
├── templates/
│   ├── storm-session.md             # 研究会话日志模板
│   ├── concept-output.md            # 标准概念页输出模板
│   ├── synthesis-report.md          # 综合简报模板
│   ├── contradiction-map.md         # 分层矛盾地图模板
│   └── peer-review-checklist.md     # 同行评审打分表
└── tests/
    ├── fixtures/
    │   ├── valid-session.json
    │   └── invalid-session.json
    └── test_workflow.py             # 工作流单元测试
```

---

## 理论来源

- **Stanford OVAL Lab** — STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking (NAACL 2024)
- **Mr Panda** — Skill 设计与四阶段沉淀法（触发词 · 边界 · 步骤 · 参考文件）

Stanford STORM 本身通过视角发现、模拟源讨论、大纲生成和文章生成来撰写类似 Wikipedia 的文章。本仓库的四阶段工作流并非原始 Stanford 架构，而是基于其方法论并结合社区实践演化而来。

---

## 安装

### Hermes Agent

```bash
# 直接安装
hermes skills install https://github.com/RobinZorro86/storm-research/blob/main/SKILL.md

# 或手动复制到 skills 目录
git clone https://github.com/RobinZorro86/storm-research.git
cp -r storm-research ~/.hermes/skills/research/
```

### Claude Code / Codex / 其他 Agent

```bash
git clone https://github.com/RobinZorro86/storm-research.git
cp -r storm-research "${CODEX_HOME:-$HOME/.codex}/skills/storm-research"
```

对于其他运行时，将整个目录放置在该运行时的 skill 位置即可。[tool-recipes.md](references/tool-recipes.md) 中的能力契约可映射到你实际可用的工具；工具名称有意不硬编码。

---

## 使用方式

### 在 Agent 中触发

```text
用 storm-research 调查我们团队是否应该采用这个构建系统
对这个政策提案进行多视角分析
为这个论断周围的证据构建矛盾地图
审查这份研究简报中未经支持的论断和缺失的反证
```

### 独立运行脚本

**确定性视角选择**（无需 LLM）：

```bash
python3 scripts/select_perspectives.py --domains tech,biz --complexity medium
```

**验证研究会话并输出覆盖率指标**：

```bash
python3 scripts/validate_session.py tests/fixtures/valid-session.json
```

**渲染 QA 报告**：

```bash
python3 scripts/render_report.py \
  tests/fixtures/valid-session.json \
  outputs/qa/example-report.md
```

---

## 安全知识闭合

默认写入目标是 `outputs/qa/`。Skill **不会自动修改**：

- 编译后的概念页面
- 实体记录
- 不可变的原始证据
- 自身的视角或偏见规则
- Git 历史

正式入库仍由活跃的知识库工作流负责，并需要其授权。

### 自定义输出路径

默认情况下研究输出写入 `outputs/qa/`。你可以通过环境变量自定义输出目录：

```bash
export STORM_OUTPUT_ROOT="/your/custom/path"
# 例如指向私有知识库
export STORM_OUTPUT_ROOT="$HOME/Documents/Wiki"
```

这会覆盖当前会话的默认路径。要持久化配置，可添加到 Agent profile 的环境变量或 `.env` 文件中：

```bash
# ~/.hermes/profiles/your-profile/.env
STORM_OUTPUT_ROOT=/Users/username/Documents/Wiki
```

---

## 质量指标

验证器报告的是**过程覆盖率**而非不可校准的准确性分数：

| 指标 | 说明 |
|------|------|
| 断言引用覆盖率 | 有多少断言至少有一个来源 |
| 独立佐证覆盖率 | 有多少断言有多个独立来源支持 |
| 一手来源覆盖率 | 有多少断言引用原始研究/数据 |
| 反证覆盖率 | 有多少断言检索并记录了反方证据 |
| 未解决断言率 | 有多少断言无法在现阶段做出可信裁决 |
| 来源开放成功率 | 来源链接是否可正常访问 |

这些指标是**诊断性的**，它们不是校准的概率，也不证明结论一定正确。

---

## 开发

需要 Python 3.9 或更高版本。运行时脚本仅使用标准库；验证依赖仅在 CI 中使用。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_links.py
python3 scripts/validate_session.py tests/fixtures/valid-session.json
```

CI 还会验证 session fixture 是否符合 JSON Schema，并检查 Skill frontmatter。

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.1.1** | 2026-06-19 | 合并 Codex 优化（可执行脚本 + JSON Schema + 测试 + CI），恢复中文 README 格式，添加自定义输出路径指南 |
| **1.1.0** | 2026-06-19 | Codex 评审优化：确定性视角选择、断言级证据记录、反证门控、可审计覆盖率指标、安全 QA 草稿闭合 |
| **1.0.0** | 2026-06-19 | 初始版本：五层架构 + 自适应视角引擎 + 偏见三级防御 + 知识闭合 |

---

## 贡献

- 作者: Robin.Z / Luffy Team
- 方法论来源: Stanford OVAL Lab (NAACL 2024)
- 构建框架: Hermes Agent Skill System

## 许可证

MIT License — 详见 [LICENSE](LICENSE) 文件
