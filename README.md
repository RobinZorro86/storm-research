# STORM 自适应研究引擎

> 基于 Stanford STORM 方法论的多视角研究 Skill，自动推断最优视角组合，嵌入偏见防御与信源验证，产出自动入库 Wiki 的高质量研究报告。

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/RobinZorro86/storm-research)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 核心能力

| 层级 | 功能 | 效果 |
|------|------|------|
| **L1 语义解析** | 自动推断研究主题的 domain 和复杂度 | 无需手动指定视角 |
| **L2 视角引擎** | 从 6 大类 30+ 视角中智能匹配 Top-5~7 | 自适应 + 张力校验 |
| **L3 偏见防御** | 断言级来源标记 + 红队检验 + 知识冲突检测 | 解决 STORM 不自检弱点 |
| **L4 工具编排** | 自动执行 web_search/x_search/skill_view/browser | 从"建议搜索"→"自动搜索" |
| **L5 知识闭合** | 自动写入 C-XXX + index.md + entity + storm-log | 研究即入库 |

## 触发词

```
storm研究 {topic}              → 完整启动
"多角度扫描" {topic}           → Phase 1
"矛盾地图"                   → Phase 2
"综合简报"                   → Phase 3
"同行评审"                   → Phase 4
storm入库                    → L5 知识闭合
storm状态                    → 显示研究进度
```

## 快速示例

```
user: storm研究 10-15岁孩子是否应该尽早学习AI Agent

Luffy:
1. 【L1】识别为 society/education / complex
2. 【L2】选取: 技术乐观者 + 怀疑论者 + 教育工作者 + 家长 + 伦理学家 + 哲学怀疑论者
3. 【L3】全程来源标记 + 红队检验 + 知识冲突检测
4. 【L4】自动搜索验证 + Wiki 知识预检
5. 【L5】产出 concepts/C-093-少儿AI教育最佳时机与认知风险.md
```

完整研究案例：[C-093 Wiki 概念页](https://github.com/RobinZorro86/Wiki/blob/main/concepts/C-093-少儿AI教育最佳时机与认知风险.md)

## 文件结构

```
storm-research/
├── README.md                          # 本文件
├── SKILL.md                           # Hermes Skill 主文件（触发词 + 详细用法）
├── references/
│   ├── theory.md                      # STORM 自适应架构完整理论
│   ├── perspective-library.md         # 6 大类 30+ 视角完整定义
│   ├── bias-guardrails.md            # 偏见三级防御详细规则
│   └── tool-recipes.md               # 每阶段精确工具调用链
└── templates/
    ├── concept-output.md             # Wiki 概念页输出模板
    ├── storm-session.md              # 研究会话日志模板
    ├── synthesis-report.md           # 综合简报模板
    └── contradiction-map.md          # 分层矛盾地图模板
```

## 理论来源

- **Stanford OVAL Lab** — STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking (NAACL 2024)
- **Wiki 概念** — [C-091 STORM 多视角研究方法](https://github.com/RobinZorro86/Wiki/blob/main/concepts/C-091-STORM多视角研究方法.md)
- **Wiki 概念** — [C-092 STORM 自适应 Skill 架构设计](https://github.com/RobinZorro86/Wiki/blob/main/concepts/C-092-STORM自适应研究Skill架构设计.md)
- **Wiki 概念** — [C-090 Skill 设计与四阶段沉淀法](https://github.com/RobinZorro86/Wiki/blob/main/concepts/C-090-Skill设计与四阶段沉淀法.md)

## 质量指标

| 指标 | 目标 | 实际（C-093 测试） |
|------|------|------------------|
| 视角数量 | ≥5 | 7 ✅ |
| 有效矛盾 | ≥3 | 5 ✅ |
| 来源/断言 | ≥1.0 | 1.2 ✅ |
| 置信度均值 | ≥0.75 | 0.72 |
| 低置信度标注 | 100% | 100% ✅ |
| 反方覆盖 | ≥80% | 85% ✅ |
| 知识冲突检出 | 100% | 100% ✅ |
| 入库完整 | 100% | 100% ✅ |

## 安装

### Hermes Agent

```bash
# 直接安装（Hermes 支持从 URL 安装 Skill）
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

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.0** | 2026-06-19 | 初始版本：五层架构 + 自适应视角引擎 + 偏见三级防御 + 自动入库闭环 |

## 贡献

- 作者: Robin.Z / Luffy Team
- 方法论来源: Stanford OVAL Lab (NAACL 2024)
- 构建框架: Hermes Agent Skill System
- 知识库: [Wiki Compiled Truth](https://github.com/RobinZorro86/Wiki)

## 许可证

MIT License — 详见 [LICENSE](LICENSE) 文件
