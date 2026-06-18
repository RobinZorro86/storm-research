# Phase 精确工具调用链

## 设计原则

每个 Phase 都有**可复制的工具调用序列**。用户触发 Skill 后，系统自动按顺序调用工具，无需用户逐一手动操作。

---

## Phase 1: Multi-Perspective Scan

### 触发条件

`storm研究 {topic}` / `多角度扫描 {topic}`

### 工具调用序列

```
Step 1: 语义解析 → 无工具，模型内部推理
  output: {domain, complexity, key_entities, controversy_risk}

Step 2: Wiki 知识预检
  ├─ read_file("/Users/robin.z/Documents/Wiki/concepts/index.md")
  │   → 搜索 C-XXX 列表中是否有 {topic} 关键词
  │   → 若命中，read_file("匹配的 C-XXX.md") 加载基线
  │
  └─ search_files(pattern="{topic}", path="/Users/robin.z/Documents/Wiki", target="content")
      → 发现所有涉及 {topic} 的 Wiki 页面
      → 按相关性排序，Top 3 摘要读入上下文

Step 3: 实时信息获取
  ├─ web_search("{topic} 最新进展 2026")
  │   → limit=5，取前 3 个结果摘要
  │
  ├─ web_search("{topic} 争议 批评")
  │   → limit=5，取反对观点摘要
  │
  ├─ x_search("{topic}")
  │   → limit=5，取社媒讨论摘要（补充大众声音）
  │
  └─ browser_navigate("前 3 个 web_search 结果中最权威的 URL")
      → 深度阅读，提取关键论点和数据
      → 若原始内容为英文，保留英文原文但提供中文摘要

Step 4: 视角生成（内部推理，无工具调用）
  → 根据 Step 1 的 domain + Step 2 的已有知识 + Step 3 的实时信息
  → 从 perspective-library 选择 Top-5~7 视角
  → 生成每个视角的"核心立场 + 最强证据 + 独特洞见"

Step 5: 用户确认
  ├─ 展示生成的视角卡片
  └─ clarify(question="是否需要追加自定义视角或调整某个视角？")
      → 用户回答后，微调视角集

Output: Phase 1 产出物
  - perspective_cards[5-7]（含来源标记）
  - baseline_knowledge（若有已有 C-XXX）
  - real_time_evidence[]（网络检索摘要）
```

### 边界条件

- 若 `{topic}` 过于宽泛（如"AI"），clarify("请缩小范围，例如'AI在医疗影像中的应用'")
- 若 web_search 无结果，尝试英文搜索 + 自动翻译
- 若 Wiki 已有高度相关的 C-XXX，提示用户"是否基于已有知识深化研究？"

---

## Phase 2: Contradiction Map

### 触发条件

Phase 1 完成后自动衔接 / 用户说"矛盾地图"

### 工具调用序列

```
Step 1: 提取断言
  无工具，内部推理：从 Phase 1 的 perspective_cards 提取所有关键断言

Step 2: 红队检索（对每个断言）
  循环遍历 assertions[]:
    ├─ web_search("{assertion} 反驳 counterargument 批评")
    │   → limit=3，取最强反方论点
    │
    └─ browser_navigate("最强反方论点的 URL")
        → 深度阅读，提取反驳证据

Step 3: 知识冲突检测
  循环遍历涉及的关键实体 entities[]:
    ├─ search_files(pattern="{entity}", path="/Users/robin.z/Documents/Wikir(Wiki", target="content")
    │   → 发现 Wiki 中所有提及该实体的页面
    │
    └─ read_file("最相关的 Wiki 页面")
        → 对比已有结论与 Phase 1 的新结论
        → 标记冲突等级：✅ / 🟢 / ⚠️ / 🔴

Step 4: 生成分层矛盾地图
  无工具，内部推理
  → Layer 1: 事实矛盾
  → Layer 2: 解释矛盾
  → Layer 3: 价值观矛盾

Step 5: 生成置信度矩阵
  无工具，内部推理
  → 每个断言 × 每个维度的置信度打分

Step 6: 中断条件检查
  若存在 🔴 严重矛盾:
    → clarify(question="检测到与已有知识的严重冲突，请选择处理方式：1.覆盖更新 2.并存记录 3.暂缓入库")

Output: Phase 2 产出物
  - contradiction_map.md（分层格式）
  - red_team_notes[]（红队批注）
  - knowledge_conflicts[]（Wiki 冲突检测报告）
  - confidence_matrix[]
```

### 边界条件

- 红队检索最多执行 10 次 web_search（防滥用）
- 若断言本身是主观判断（如"这是最好的设计"），跳过红队检索，标记为"主观，不参与矛盾检测"
- 知识冲突检测最多读取 5 个 Wiki 页面（防滥用）

---

## Phase 3: Synthesis

### 触发条件

Phase 2 完成后自动衔接 / 用户说"综合简报"

### 工具调用序列

```
Step 1-4: 综合推理（无工具调用，模型内部完成）
  → 整合 Phase 1 卡片 + Phase 2 地图
  → 生成 CEO 级摘要 + 隐藏联系 + 可执行洞见 + 前沿问题

Step 5: 格式化输出
  ├─ write_file("/Users/robin.z/Documents/Wiki/raw/storm-logs/{YYYY-MM-DD}-{slug}-synthesis.md", synthesis_report)
  │   → 使用 templates/synthesis-report.md 格式
  │   → 这是草稿，不入主库
  │
  └─ 展示给用户预览

Step 6: 用户确认
  clarify(question="综合简报已生成，是否满意？还是需要调整？")
  → 不满意：收集反馈 → 回到 Step 1 重新综合
  → 满意：进入 Phase 4

Output: Phase 3 产出物
  - synthesis_report.md（草稿）
```

### 边界条件

- 综合报告超过 3000 字时，summary 压缩到 2000 字以内，完整版附在 raw/storm-logs/
- 若用户要求"只给我要点"，输出 bullet-point 版本

---

## Phase 4: Peer Review

### 触发条件

Phase 3 完成后自动衔接 / 用户说"同行评审"

### 工具调用序列

```
Step 1: 元认知审查（内部推理）
  逐项检查质量指标（见 SKILL.md 质量指标表）

Step 2: 生成评审报告
  无工具，内部推理
  → Overall Score (0-10)
  → Top 3 Weaknesses
  → Bias Check
  → Missing Perspectives
  → Improvement Suggestions

Step 3: Skill 自进化
  若发现新有效视角:
    ├─ skill_manage(action="patch", name="storm-research",
    │   old_string="旧视角库片段",
    │   new_string="新增视角定义")
    │   → 更新 perspective-library.md
    │
  若发现新偏见模式:
    └─ skill_manage(action="patch", name="storm-research",
        old_string="旧偏见检测清单",
        new_string="新增偏见类型和检测信号")
        → 更新 bias-guardrails.md

Step 4: 记录研究轨迹
  write_file("/Users/robin.z/Documents/Wiki/raw/storm-logs/{YYYY-MM-DD}-{slug}-review.md", review_log)

Step 5: 用户确认
  clarify(question="评审完成，评分 {score}/10。是否满意？是否准备入库？")
  → 不满意：收集反馈 → 回到相应 Phase 修改
  → 满意 + 准备入库：触发 L5 知识闭合

Output: Phase 4 产出物
  - peer_review_report.md
  - storm-log.md（完整研究轨迹）
```

### 边界条件

- 总分 <5 分时，强制要求回到 Phase 1 补充视角或 Phase 2 加深矛盾挖掘
- Skill 自进化只在评分 ≥7 分时执行（避免低质量研究污染视角库）

---

## L5: 知识闭合

### 触发条件

Phase 4 通过 + 用户确认入库 / 用户说"storm入库"

### 工具调用序列

```
Step 1: 确定 C-XXX 编号
  ├─ **首选方法（更可靠）**: terminal("ls /Users/robin.z/Documents/Wiki/concepts/C-*.md | grep -oE 'C-[0-9]{3}' | sort -V | tail -1")
  │   → 提取文件名中的最大编号（如 C-092）
  │   → 新编号 = 093
  │
  ├─ **备选方法**: read_file("/Users/robin.z/Documents/Wiki/concepts/index.md")
  │   → 从正文索引中提取最大编号
  │   → ⚠️ 注意：index.md 可能存在缺失编号（如 C-092 后直接 C-094），此时优先填补 gap
  │
  └─ **编号冲突处理**: 若计算出的编号已被占用（concurrent writes）
      → clarify("C-XXX 已被占用，选择：1.填补下一个 gap 2.使用最大编号+1 3.取消")

**实战经验**: 实践发现从 `index.md` 提取编号不如直接从文件名提取可靠，因为 index.md 的正文可能滞后于实际文件。始终以 `ls concepts/C-*.md | grep -oE 'C-[0-9]{3}'` 为准。

Step 2: 格式化概念页
  使用 templates/concept-output.md:
    → frontmatter: title, created, updated, type, aliases([c-XXX]), tags, status
    → Compiled Truth: 综合报告的精炼版（≤1500 字）
    → Sources: Phase 1 的所有来源链接
    → Related: 双向链接到涉及的实体和相关概念
    → Timeline: 本次研究的时间线记录

Step 3: 写入概念页
  write_file("/Users/robin.z/Documents/Wiki/concepts/C-XXX-{slug}.md", concept_page)

Step 4: 更新索引
  patch("/Users/robin.z/Documents/Wiki/concepts/index.md",
    old_string="### AI 研究方法\n\n- [[concepts/C-091",
    new_string="### AI 研究方法\n\n- [[concepts/C-091" + "\n- [[concepts/C-XXX-{slug}]]")

Step 5: 实体处理
  循环遍历研究涉及的所有实体:
    ├─ search_files(pattern="{entity}", path="/Users/robin.z/Documents/Wikientities", target="files")
    │   → 若存在：patch 追加 timeline
    │   → 若不存在：write_file("/Users/robin.z/Documents/Wiki/entities/{entity-slug}.md", new_entity_page)
    │     → 新实体页格式：frontmatter + 简介 + Timeline + Related

Step 6: 记录研究轨迹
  write_file("/Users/robin.z/Documents/Wiki/raw/storm-logs/{YYYY-MM-DD}-{slug}-full-log.md", complete_trace)
  → 包含：触发条件、所有工具调用记录、模型推理摘要、质量评分

Step 7: Git 提交（可选）
  terminal("cd /Users/robin.z/Documents/Wiki && git add concepts/C-XXX-{slug}.md concepts/index.md entities/* raw/storm-logs/* && git commit -m 'storm-research: C-XXX {topic}'")

Output: L5 完成
  - concepts/C-XXX-{slug}.md ✅
  - concepts/index.md 更新 ✅
  - entities/ 更新/创建 ✅
  - raw/storm-logs/ 记录 ✅
```

### 边界条件

- 编号冲突：若 C-XXX 已被占用（并发情况），clarify("C-XXX 已被占用，选择：1.使用 C-XXX+1 2.覆盖 3.取消")
- 实体过多（>10 个）：只创建最核心的 5 个实体，其余放入"待创建实体清单"
- 用户取消：保留 raw/storm-logs/ 但不写入 concepts/

---

## 工具调用总量估算

| Phase | 平均工具调用次数 | 主要消耗 |
|-------|------------------|----------|
| Phase 1 | 5-8 次 | web_search(2-3) + x_search(1) + browser(1-2) + read_file(2-3) |
| Phase 2 | 8-15 次 | web_search(5-10 红队检索) + read_file(3-5 知识冲突检测) |
| Phase 3 | 1-2 次 | write_file(1) + clarify(1) |
| Phase 4 | 0-2 次 | skill_manage(0-1) + write_file(1) |
| L5 | 3-6 次 | read_file(1) + write_file(1-2) + patch(1-2) + search_files(1-3) |
| **总计** | **17-33 次** | |

**Token 预估**: 30K-80K（取决于 topic 复杂度和搜索返回内容长度）
