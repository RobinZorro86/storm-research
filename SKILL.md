---
name: storm-research
description: "自适应多视角研究引擎：基于 STORM 方法论，自动推断最优视角组合，嵌入偏见防御与信源验证，产出自动入库 Wiki 的高质量研究报告。"
version: 1.0.0
author: Robin.Z / Luffy Team
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, storm, multi_perspective, adaptive, knowledge_closure, compiled_truth]
    related_skills: [obsidian, anysearch, browser, web]
    wiki_concept: "[[concepts/C-092-STORM自适应研究Skill架构设计]]"
---

# STORM 自适应研究引擎 (storm-research)

基于 Stanford STORM 多视角研究方法论的 Hermes Skill 实现。**核心价值**：不是给你 4 个 Prompt 模板让你手动复制粘贴，而是一个**自适应推理引擎**——自动推断视角组合、自动执行搜索验证、自动检测偏见、自动将成果写入 Wiki。

---

## 触发词

| 触发方式 | 关键词 |
|----------|--------|
| **完整启动** | `storm研究 {topic}` / `用 storm 方法研究 {topic}` / `多视角分析 {topic}` |
| **单阶段** | `"多角度扫描" {topic}` → Phase 1<br>`"矛盾地图"` → Phase 2<br>`"综合简报"` → Phase 3<br>`"同行评审"` → Phase 4 |
| **知识闭合** | `storm入库` → 将最近一次研究成果写入 Wiki |
| **状态检查** | `storm状态` → 显示当前研究的进度和质量指标 |

**边界**（明确不做什么）：
- ❌ 不执行超过 100 次连续搜索（防滥用上限）
- ❌ 不生成投资建议、医疗建议、法律意见（高风险决策需人工复核）
- ❌ 不覆盖已有 Wiki 概念页而不提示用户确认（增量更新而非强制覆写）
- ❌ 不处理纯主观审美判断（艺术品味、个人偏好等非实证话题）

---

## 快速开始

```
user: storm研究 MiniMax M3 模型架构

Luffy:
1. 【L1 语义解析】识别为 technology / deep_technical / 高复杂度
2. 【L2 视角引擎】选取: 架构师 + 安全研究员 + 开源贡献者 + 产品经理 + 学者 + 怀疑者
3. 【L3 偏见防御】全程来源标记 + 红队检验 + 置信度阈值
4. 【L4 工具编排】自动执行 web_search + x_search + browser + Wiki 知识预检
5. 【L5 知识闭合】产出 concepts/C-093-MiniMax-M3-多视角研究.md + 更新 index.md
```

**总耗时**: 3-5 分钟（对比手工 STORM 的 30-60 分钟）

---

## 实战案例

**C-093: 10-15 岁孩子是否应该尽早学习 AI Agent**（2026-06-19）

| 阶段 | 产出 |
|------|------|
| **L1** | 语义解析: domain=society, complexity=complex, 涉及教育伦理、认知发展、商业利益多重张力 |
| **L2** | 7 个视角：技术乐观者(CodaKid) / 技术怀疑论者(Brookings) / 教育工作者 / 家长(Reddit) / 终端用户(哈佛) / 教育伦理学家 / 哲学怀疑论者 |
| **L3** | 5 个有效矛盾，含 🔴 严重矛盾（"早学有益"vs"已造成认知损伤"） |
| **L4** | web_search ×2 + x_search ×1 + search_files(Wiki) + browser_深度阅读 |
| **L5** | 产出 C-093 + 更新 index.md + 创建 entities/codakid.md + entities/brookings-institution.md + entities/children-and-screens.md |

**核心结论**: 10-12 岁不建议全面投入 AI Agent；13-15 岁可引导学原理而非操作。详见 [[concepts/C-093-少儿AI教育最佳时机与认知风险]]

**评审评分**: 7.5/10 — 弱点包括缺乏纵向数据、厂商来源偏多、Reddit 为 anecdotal 证据。完整日志见 [[raw/storm-logs/2026-06-19-ai-education-children-full-log]]

---

## 五层架构速查

| 层级 | 功能 | 关键产出 |
|------|------|----------|
| **L1 语义解析** | 主题分类 + 复杂度评估 | domain_tag, complexity_score |
| **L2 视角引擎** | 从 6 大类 30+ 视角中自动匹配 Top-5~7 | perspective_cards[] |
| **L3 偏见防御** | 断言级来源标记 + 红队检验 + 知识冲突检测 | annotated_assertions[], contradiction_map |
| **L4 工具编排** | 每阶段内嵌 web_search/x_search/skill_view/browser | enriched_evidence[] |
| **L5 知识闭合** | 自动写入 C-XXX + index.md + entity + storm-log | compiled_concept_page |

详见理论文档: `references/theory.md`

---

## 详细用法

### Phase 1: Multi-Perspective Scan（多视角扫描）

**触发**: `storm研究 {topic}` 或 `"多角度扫描" {topic}`

**自动执行步骤**:
1. 语义解析 → 判定 domain 和 complexity
2. 查询 Wiki 已有知识 → `skill_view("obsidian")` + `read_file("concepts/index.md")`
   - 若发现已有 C-XXX，加载作为基线（避免重复劳动）
3. 实时信息获取 → `web_search("{topic} 最新进展 争议")` + `x_search("{topic}")`
   - 取 Top 3 结果，用 `browser_navigate` 深度阅读
4. 自适应视角生成 → 根据 domain 匹配视角库，生成 5-7 个视角卡片
   - 每张卡片包含：核心立场（≤30 字）+ 最强证据（1 条）+ 独特洞见（≤100 字）+ 来源标记

**用户可干预点**:
- 视角生成后询问："是否需要追加自定义视角？" → 接受或跳过
- 发现已有 Wiki 知识时提示："发现已有 [[concepts/C-XXX-xxx]]，是否以其为基线？"

---

### Phase 2: Contradiction Map（矛盾地图）

**触发**: `"矛盾地图"`（通常在 Phase 1 完成后自动衔接）

**自动执行步骤**:
1. 提取 Phase 1 所有关键断言
2. **红队检验**：对每个断言自动检索反方观点
   - `web_search("{assertion} 反驳 反对 counterargument")`
   - 每个正向社会视角自动配对 Devil's Advocate
3. **知识冲突检测**：对比 Phase 1 结论与 Wiki 已有知识
   - `read_file("已有相关概念.md")` → 标记 ✅一致 / ⚠️部分冲突 / 🔴严重矛盾
   - 严重矛盾时暂停，提示用户裁决
4. 生成分层矛盾地图:
   - **Layer 1**: 事实矛盾（A 说 X，B 说 ¬X）
   - **Layer 2**: 解释矛盾（同意事实但解释不同）
   - **Layer 3**: 价值观矛盾（同意事实和解释但评价相反）
5. 生成置信度矩阵：每个断言标注 [置信度:x.x] + [来源:xxx]

**产出**: `contradiction_map.md`（使用模板 `templates/contradiction-map.md`）

---

### Phase 3: Synthesis（综合简报）

**触发**: `"综合简报"`（通常自动衔接 Phase 2）

**自动执行步骤**:
1. 整合 Phase 1 视角卡片 + Phase 2 矛盾地图
2. 生成 CEO 级摘要（3 段式：现状 → 核心矛盾 → 关键判断）
3. 提取隐藏联系：跨视角的意外关联（通常是最有价值的洞察）
4. 生成可执行洞见：对用户的直接行动建议
5. 提出前沿问题：研究缺口和未来方向

**格式化输出**: 使用 `templates/synthesis-report.md`
- Executive Summary（≤200 字）
- Key Findings（≤5 条，每条带来源）
- Hidden Connections（≥1 条）
- Actionable Insights（≥1 条）
- Frontiers（≥2 个开放问题）

---

### Phase 4: Peer Review（同行评审）

**触发**: `"同行评审"` 或 Phase 3 完成后自动执行

**自动执行步骤**:
1. **元认知审查**:
   - 检查所有置信度 <0.7 的断言是否已被标注
   - 检查是否每个视角都有来源支撑
   - 检查是否存在 Phase 2 未捕获的隐性偏见
2. **质量指标评分**（0-10 分制）:
   - 视角多样性（≥5 个不同视角）
   - 矛盾检出率（≥3 个有效矛盾）
   - 来源密度（每个断言 ≥1 来源）
   - 置信度均值（≥0.75）
   - 低置信度标注率（100%）
   - 反方覆盖（≥80% 断言有反方观点）
   - 知识冲突检出（100%）
3. **生成评审报告**:
   - Overall Score
   - Top 3 Weaknesses
   - Bias Check (Detected/Undetected)
   - Missing Perspectives
   - Improvement Suggestions
4. **Skill 自进化**:
   - 若本次发现新有效视角 → `skill_manage` 更新 `references/perspective-library.md`
   - 若发现新偏见模式 → 更新 `references/bias-guardrails.md`
   - 记录本次研究轨迹到 `storm-log.md`

---

### L5: 知识闭合（自动入库）

**触发**: `storm入库` 或 Phase 4 完成后自动执行

**自动执行步骤**:
1. 确定 C-XXX 编号：`grep "C-0" /Users/robin.z/Documents/Wiki/concepts/index.md | sort -V | tail -1` → +1
2. 用 `templates/concept-output.md` 格式化研究产出
3. 写入 `concepts/C-XXX-{slug}.md`
4. 更新 `concepts/index.md`（追加索引条目）
5. 检查所有提及实体 → 不存在则在 `entities/` 创建
6. 更新实体页面的 timeline
7. 在 `raw/storm-logs/` 记录完整研究轨迹
8. 可选：`git add && git commit -m "storm-research: C-XXX {topic}"`

**用户确认点**:
- 写入前展示预览 → 用户确认/修改/取消
- 若与已有 C-XXX 冲突 → 提示"增量更新 vs 新建"

---

## 视角库速查

**6 大类 × 5-6 视角**（完整定义见 `references/perspective-library.md`）

| Domain | Core Pair | Extended Pool |
|--------|-----------|---------------|
| Technology (tech) | 架构师 + 安全研究员 | 性能工程师、开源贡献者、产品负责人、运维/SRE、终端用户 |
| Business (biz) | 投资者 + 产品经理 | 市场营销、法务合规、增长黑客、客服代表、竞品分析师 |
| Science (sci) | 实验科学家 + 统计学家 | 同行评审员、资助机构、科普作者、行业专家、方法论学者 |
| Society (soc) | 政策制定者 + 伦理学家 | 受影响群体代表、记者、历史学家、社区组织者、教育工作者 |
| Engineering (eng) | 一线工程师 + DevOps/SRE | 技术写作、技术支持、终端用户、项目经理、架构师 |
| Philosophy (phil) | 怀疑论者 + 建构论者 | 实用主义者、还原论者、系统论者、现象学家、批判理论家 |

**关键规则**: 每次选取必须包含至少一对"张力视角"（天然对立，如从业者 ↔ 怀疑者）

---

## 质量指标与自检

每次研究完成后，系统输出自动评分报告:

| 指标 | 及格线 | 优秀线 |
|------|--------|--------|
| 视角数量 | ≥3 | ≥5 |
| 有效矛盾 | ≥1 | ≥3 |
| 来源/断言 | ≥0.5 | ≥1.0 |
| 置信度均值 | ≥0.6 | ≥0.75 |
| 低置信度标注 | 100% | 100% |
| 反方覆盖 | ≥50% | ≥80% |
| 知识冲突检出 | 100% | 100% |
| 入库完整 | 是 | 是 |

**未达标处理**: 评审报告明确标出"⚠️ 本次研究在 XX 方面未达建议标准"，并给出具体改进建议。

---

## 与其他技能的协同

| 协同技能 | 作用 | 触发时机 |
|----------|------|----------|
| `obsidian` | 知识库读写、概念页格式化 | Phase 1 知识预检 + L5 入库 |
| `anysearch` | 实时网络搜索 | Phase 1 信息获取 |
| `browser` | 深度阅读原始论文/报道 | Phase 1/2 来源验证 |
| `web_extract` | 提取网页核心内容 | Phase 1 长文摘要 |
| `x_search` | 社媒视角补充 | Phase 1 多元声音 |
| `baoyu-danger-x-to-markdown` | 推文入库（若研究对象含推文） | Phase 1 素材捕获 |
| `markitdown` | PDF/文档转 Markdown | Phase 1 文档预处理 |
| `defuddle` | 网页清洗（markitdown fallback） | Phase 1 网页提纯 |

---

## 关键限制

1. **模型幻觉**: 即使有多层防御，LLM 仍可能产生幻觉。所有置信度 <0.8 的断言应视为"参考意见"而非"事实"
2. **时效性**: 实时信息受限于搜索返回结果的时效性。研究深度取决于公开信息的可获取性
3. **中文语料**: 部分领域的英文资料更丰富，研究某些国际前沿技术时，系统可能自动切换为主要检索英文源
4. **成本**: 完整 STORM 流程涉及 10-15 次模型调用（含辅助搜索验证），预估 token 消耗约 30K-80K

---

## References

- `references/theory.md` — STORM 自适应架构完整理论（链接 [[concepts/C-092]]）
- `references/perspective-library.md` — 6 大类 30+ 视角完整定义与张力关系
- `references/bias-guardrails.md` — 偏见三级防御详细规则与红队配对表
- `references/tool-recipes.md` — 每阶段精确工具调用链（可复制的 tool call 序列）
- `references/adaptive-algorithm.md` — 自适应视角选择算法的伪代码和边界条件

## Templates

- `templates/storm-session.md` — 新研究会话模板（frontmatter + 结构）
- `templates/contradiction-map.md` — 分层矛盾地图标准格式
- `templates/synthesis-report.md` — 综合简报标准格式（CEO 摘要 + 发现 + 洞见 + 前沿问题）
- `templates/peer-review-checklist.md` — 同行评审打分表（0-10 分项评分）
- `templates/concept-output.md` — Wiki 概念页输出模板（符合 C-XXX 格式规范）

## Related

- [[concepts/C-092-STORM自适应研究Skill架构设计]] — 本 Skill 的理论基础和设计文档
- [[concepts/C-091-STORM多视角研究方法]] — 原始 STORM 方法论
- [[concepts/C-090-Skill设计与四阶段沉淀法]] — Skill 构建方法论
- [[concepts/C-001-知识编译]] — 知识格式规范（Compiled Truth + Timeline）
- [[concepts/C-038-批判性思维]] — 批判性思维框架（红队检验的理论基础）
