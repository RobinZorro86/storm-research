# STORM 研究工具调用编排

Phase-by-phase tool chains with exact fallbacks and retry logic.

---

## Phase 1: Multi-Perspective Scan

### 前置检查
```
skill_view('obsidian')          # 确认 Wiki 路径可用
read_file('/Wiki/concepts/index.md') # 获取当前最大概念编号
```

### 主链
```
Step 1: web_search("{{TOPIC}} 最新 争议 观点")
    ├─✅ 成功 → 提取 top-5 网页
    └─❌ 失败 → fallback: x_search("{{TOPIC}}")
              └─❌ 仍然失败 → 跳过实时信息，仅依赖已有知识

Step 2: x_search("{{TOPIC}}")
    ├─✅ 成功 → 提取近期讨论
    └─❌ 失败 → skip

Step 3: search_files(pattern="{{TOPIC}}", path="/Wiki/concepts/")
    ├─✅ 命中 → read_file(匹配的 C-XXX)
    └─❌ 无命中 → 标记为新话题

Step 4: 调用 LLM 生成自适应视角列表
    Input: topic + domain classification + 已有概念摘要
    Output: 5 个视角标签

Step 5: 对每个视角执行独立 web_search
    query: "{{TOPIC}} from {{PERSPECTIVE}} perspective"
    
Step 6: web_extract(原始来源 URL)
    ├─✅ 成功 → 提取核心主张
    └─❌ 失败 → fallback: browser_navigate(url) → browser_snapshot()
              └─❌ 仍然失败 → 标记为 [来源:URL, 置信度:0.40, 未验证]

Step 7: 组装 Perspective Cards
    每卡必须包含: name, stance, evidence, insight, confidence, source
```

### 质量门
- 视角数量 ≥5 → 否则重试一次
- 至少 1 个 adversarial → 否则随机替换一个为 skeptic
- 置信度自评完整 → 否则强制 LLM 重新评估
- 来源标签完整 → 否则降级该卡片

---

## Phase 2: Contradiction Map

### 主链
```
Step 1: Pairwise comparison (C(5,2)=10 pairs)
    对每对视角: stance_A vs stance_B → classify: agree / partial / contradict / orthogonal

Step 2: 对 contradict 对执行深度分析
    web_search("{{TOPIC}} {{ASSERTION_A}} vs {{ASSERTION_B}} 争论")
    ├─✅ 命中 → web_extract(争议原文)
    └─❌ 无命中 → browser_navigate(学术论坛/Reddit/知乎) 寻找讨论

Step 3: Wiki 交叉检索
    read_file(已有 C-XXX)
    ├─✅ 发现冲突 → 记录冲突类型(empirical/definitional/incentive)
    └─❌ 无冲突 → 标记 "与现有知识无冲突"

Step 4: 构建矛盾矩阵
    Output: Markdown table (Assertion / Side A / Conf A / Side B / Conf B / Conflict Type)
```

---

## Phase 3: Synthesis

### 主链
```
Step 1: 偏见防御预检
    if 来源多样性 <3 domains → 触发补充搜索
    if 无反方视角 → 暂停并询问用户
    if 任何断言置信度未标 → 强制补标

Step 2: 综合写作
    使用模板 templates/concept-output.md
    填充变量: {{TOPIC}}, {{NEXT}}, {{DATE}}, {{P1-P5_FIELDS}}, {{CONFLICTS}}, {{CLAIMS}}

Step 3: 时效标注
    每个断言追加 [时效:YYYY-MM]

Step 4: 写入 Wiki
    write_file(path="/Wiki/concepts/C-{{NEXT}}-{{TOPIC}}.md", content=compiled)
    ├─✅ 成功 → 进入 Step 5
    └─❌ 失败 → 使用 mcp_obsidian_write_file 或 terminal(cat) 作为 fallback

Step 5: 更新索引
    read_file("/Wiki/concepts/index.md")
    patch(index.md, 在末尾追加新条目)

Step 6: 实体创建/更新
    提取所有人名、机构名
    对每个: search_files("entities/") → 如果不存在 → write_file("entities/name.md")
    实体文件格式见 obsidian skill
```

---

## Phase 4: Peer Review

### 主链
```
Step 1: 自检清单 (4层偏见防御)
    - Layer 1: 是否有 Adversary 反方？
    - Layer 2: 所有断言置信度 ≥0.40？
    - Layer 3: Wiki 冲突已显性呈现？
    - Layer 4: 时效标签完整？

Step 2: 质量打分
    按 rubric (Source 20%, Logic 25%, Bias 25%, Action 20%, Present 10%)
    
Step 3: 判定
    ├─总分 ≥80 → 接受，标记 "✅ 通过同行评审"
    ├─60–79 → 部分接受，向用户展示弱点清单，询问是否补充
    └─<60 → 拒绝，返回 Phase 1 重扫，附带具体改进指令

Step 4: 研究日志
    write_file("/Wiki/raw/storm-logs/{{DATE}}-{{TOPIC}}.md")
    记录: 触发词、视角列表、总分、关键决策点、耗时
```

---

## Fallback 树汇总

| 工具 | 首选 | Fallback 1 | Fallback 2 |
|------|------|-----------|-----------|
| web_search | ✅ | x_search | 跳过实时 |
| web_extract | ✅ | browser_navigate | [未验证] |
| write_file(Wiki) | ✅ | mcp_obsidian_write | terminal(cat >>) |
| read_file | ✅ | mcp_obsidian_read | search_files |
| browser_vision | ✅ | vision_analyze | "[图片未解析]" |

---

## 单次会话最大资源预算

| 资源 | 预算 | 理由 |
|------|------|------|
| web_search 调用 | ≤10 次 | 避免搜索疲劳 |
| web_extract 调用 | ≤5 次 | 长网页提取慢 |
| browser 调用 | ≤3 次 | 头部浏览最重 |
| LLM tokens | ≤8000 (per phase) | 保留上下文空间 |
| 总耗时 | ≤10 分钟 | 效率目标 |

超出预算时：截断视角数量、跳过低优先级来源、将 Phase 4 简化为快速自检而非全量评审。