# 自适应视角引擎规范

## 预设 Domain Taxonomy

### 1. Technology（技术/工程）
| 视角 | 代号 | 核心关切 |
|------|------|---------|
| 工程师 | `engineer` | 实现可行性、技术债务、性能瓶颈、维护成本 |
| 学术研究者 | `academic` | 理论突破、可复现性、同行评审质量、引用网络 |
| 怀疑者 | `skeptic` | 过度承诺、营销话术、基准测试作弊、长期可靠性 |
| 投资人 | `investor` | ROI、市场规模、竞争壁垒、退出路径 |
| 监管者 | `regulator` | 合规风险、数据隐私、安全标准、伦理审查 |

### 2. Business（商业/市场）
| 视角 | 代号 | 核心关切 |
|------|------|---------|
| 从业者 | `practitioner` | 落地难度、客户反馈、运营摩擦、组织变革 |
| 经济学家 | `economist` | 激励结构、外部性、定价策略、规模效应 |
| 客户 | `customer` | 性价比、切换成本、服务质量、替代品 |
| 竞争对手 | `competitor` | 差异化优势、护城河、反应策略、专利布局 |
| 监管者 | `regulator` | 反垄断、消费者权益、信息披露、行业标准 |

### 3. Society/Policy（社会/政策）
| 视角 | 代号 | 核心关切 |
|------|------|---------|
| 受益者 | `beneficiary` | 谁获利？如何扩大受益面？公平性？ |
| 受害者 | `victim` | 谁受损？隐性成本？不可逆伤害？ |
| 政策制定者 | `policymaker` | 法律依据、执行成本、国际协调、民意压力 |
| 媒体观察者 | `media_observer` | 叙事框架、议程设置、情绪化传播、回音室 |
| 历史学家 | `historian` | 类似先例、周期律、技术与社会互动的历史模式 |

### 4. Science（自然科学）
| 视角 | 代号 | 核心关切 |
|------|------|---------|
| 实验主义者 | `experimentalist` | 数据采集、统计显著性、实验设计、可复现性 |
| 理论家 | `theorist` | 模型解释力、数学严谨性、预测能力、范式兼容性 |
| 同行 | `peer` | 社区共识、引用规范、合作网络、学术声誉 |
| 怀疑者 | `skeptic` | 证伪可能性、p-hacking、发表偏倚、replication crisis |
| 历史学家 | `historian` | 科学史先例、范式转换条件、资助结构变迁 |

### 5. Other（兜底）
当 domain classifier 置信度 < 0.70 时，退回到经典 5 视角：
- Practitioner, Academic, Skeptic, Economist, Historian

## Domain Classification Prompt

```
Classify the following topic into exactly one domain. Respond ONLY with a JSON object.

Topic: "{{TOPIC}}"

Rules:
- technology: 涉及技术实现、软件、硬件、算法、工程、代码、系统架构
- business: 涉及商业模式、市场、销售、投资、竞争、客户、利润
- society: 涉及公共政策、社会伦理、文化影响、权力结构、群体利益
- science: 涉及自然科学、医学、物理、化学、生物学、实验数据
- other: 不属于以上四类，或跨度过大难以归类

Output format (strict JSON, no markdown fences):
{"domain": "technology|business|society|science|other", "confidence": 0.0-1.0, "reasoning": "one sentence"}
```

## 自定义视角扩展

用户可以在触发时注入第 6 个视角：

```
/storm {{TOPIC}} with extra-perspective: "一线客服代表"
```

自定义视角会被包装为标准格式加入 Phase 1：
```yaml
name: "用户自定义"
role: "一线客服代表"
source: "user-injected"
priority: "append"
```

## 视角质量自检清单

| 检查项 | 通过标准 |
|--------|---------|
| 多样性 | 5 个视角来自 ≥3 个不同利益阵营（得利/失利/中立） |
| 对抗性 | 至少 1 个视角明确持反对或怀疑立场 |
| 专业性 | 至少 2 个视角具备该领域的专业知识背景 |
| 利益相关 | 至少 2 个视角与该话题有直接利益关系 |
| 距离感 | 至少 1 个视角具有"局外人"距离（如历史学家、哲学家） |

如果自检失败，重新抽样视角直到通过。