---
title: "STORM 研究会话: {{topic}}"
created: "{{YYYY-MM-DD HH:MM}}"
type: storm_session
status: active
phase: "{{current_phase}}"  # L1/L2/L3/L4/L5
quality_score: "{{pending}}"
---

# STORM 研究会话: {{topic}}

## 会话元数据

| 属性 | 值 |
|------|-----|
| **主题** | {{topic}} |
| **启动时间** | {{YYYY-MM-DD HH:MM}} |
| **当前阶段** | {{L1/L2/L3/L4/L5}} |
| **Domain** | {{tech/biz/sci/soc/eng/phil}} |
| **复杂度** | {{simple/medium/complex}} |
| **选用视角** | {{perspective list}} |
| **质量评分** | {{pending}} |
| **预计 Token 消耗** | {{estimated_tokens}} |

---

## L1: 语义解析

**解析结果**:
```yaml
domain: {{domain}}
complexity: {{complexity}}
key_entities: {{entity_list}}
controversy_risk: {{low/medium/high}}
confidence: {{0.XX}}
```

**用户意图澄清**: {{若有 clarifying question，记录在这里}}

---

## L2: 视角扫描

### 视角卡片

{{repeat for each perspective}}

#### {{视角名称}} ({{domain}})

- **核心立场**: {{≤30字}}
- **最强证据**: {{1条，带来源}}
- **独特洞见**: {{≤100字}}
- **来源标记**: [来源:{{url}}] [置信度:{{0.XX}}]

### 自定义视角

{{若有用户注入的自定义视角}}

---

## L3: 矛盾地图

### 事实矛盾 (Layer 1)

| 断言 A | 断言 B | 冲突等级 | 置信度 | 裁决 |
|--------|--------|---------|--------|------|
| {{}} | {{}} | {{high/med/low}} | {{A/B}} | {{pending/resolved}} |

### 解释矛盾 (Layer 2)

{{同上格式}}

### 价值观矛盾 (Layer 3)

{{同上格式}}

### 红队批注

{{每个正对社会视角的红队反驳}}

### Wiki 知识冲突

| 涉及实体 | 已有知识 | 新研究结论 | 冲突等级 | 处理方式 |
|---------|---------|-----------|---------|---------|
| {{}} | {{}} | {{}} | {{}} | {{}} |

---

## L4: 综合

### CEO 级摘要

{{3段式}}

### 隐藏联系

{{≥1条}}

### 可执行洞见

{{≥1条}}

### 前沿问题

{{≥2个}}

---

## L5: 知识闭合

### 入库文件

| 文件 | 状态 | 备注 |
|------|------|------|
| concepts/C-XXX-{{slug}}.md | {{pending/committed}} | |
| concepts/index.md | {{pending/committed}} | |
| entities/{{entity}}.md | {{pending/committed}} | |

### Git 记录

```
commit {{hash}}
Author: storm-research skill
Date: {{YYYY-MM-DD HH:MM}}

storm-research: C-XXX {{topic}}
```

---

## 研究轨迹

{{记录所有工具调用和重要决策的时序}}
