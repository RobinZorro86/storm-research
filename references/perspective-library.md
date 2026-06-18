# 自适应视角库与张力引擎

## 6 大类 × 30+ 视角

### Technology (tech)

| ID | 视角名称 | 角色定位 | 核心关注点 | 对立视角 |
|----|---------|---------|-----------|---------|
| tech-arch | 架构师 | 系统设计决策者 | 可扩展性、模块化、长期演进 | tech-skept |
| tech-sec | 安全研究员 | 攻防与漏洞猎人 | 攻击面、漏洞、加密强度 | tech-opt |
| tech-perf | 性能工程师 | 极致优化追求者 | latency、吞吐量、资源效率 | tech-devrel |
| tech-os | 开源贡献者 | 社区生态建设者 | 许可证、治理、可持续性 | tech-pm |
| tech-pm | 产品负责人 | 商业与技术桥梁 | 用户价值、roadmap、ROI | tech-perf |
| tech-devrel | 开发者布道师 | 推广与教育者 | 上手难度、文档质量、社区规模 | tech-sec |
| tech-opt | 技术乐观主义者 | 前沿技术拥抱者 | 突破性潜力、颠覆性应用 | tech-skept |
| tech-skept | 技术怀疑论者 | 风险与局限性关注者 | 炒作、未经验证的声明、伦理风险 | tech-opt |

**必选项**: tech-arch + tech-sec
**张力对**: tech-opt ↔ tech-skept

### Business (biz)

| ID | 视角名称 | 角色定位 | 核心关注点 | 对立视角 |
|----|---------|---------|-----------|---------|
| biz-inv | 投资者 | 资本配置者 | ROI、退出路径、估值、现金流 | biz-legal |
| biz-pm | 产品经理 | 需求定义者 | PMF、用户旅程、功能优先级 | biz-sales |
| biz-mkt | 市场营销 | 增长引擎 | 获客成本、品牌、定位、转化 | biz-legal |
| biz-legal | 法务合规 | 风险控制者 | 监管、IP、合同、诉讼风险 | biz-growth |
| biz-growth | 增长黑客 | 快速扩张者 | 病毒系数、A/B 测试、数据驱动 | biz-inv |
| biz-support | 客服代表 | 前线反馈者 | 投诉、痛点、流失原因 | biz-mkt |
| biz-compete | 竞品分析师 | 对标研究者 | 差异化、护城河、市场份额 | biz-pm |

**必选项**: biz-inv + biz-pm
**张力对**: biz-growth ↔ biz-legal

### Science (sci)

| ID | 视角名称 | 角色定位 | 核心关注点 | 对立视角 |
|----|---------|---------|-----------|---------|
| sci-exp | 实验科学家 | 实证研究者 | 可重复性、样本量、p-value | sci-pop |
| sci-stat | 统计学家 | 数据分析者 | 统计显著性、因果推断、偏差 | sci-fund |
| sci-peer | 同行评审员 | 质量守门人 | novelty、rigor、impact、reproducibility | sci-fund |
| sci-fund | 资助机构 | 资源分配者 | alignment、影响力、里程碑、预算 | sci-exp |
| sci-pop | 科普作者 | 知识传播者 | 准确性 vs 通俗性平衡 | sci-peer |
| sci-ind | 行业专家 | 应用领域权威 | 实际可行性、工程化障碍 | sci-stat |
| sci-meta | 方法论学者 | 研究范式审视者 | 方法论优劣、学科偏见、知识社会学 | sci-exp |

**必选项**: sci-exp + sci-peer
**张力对**: sci-peer ↔ sci-pop

### Society (soc)

| ID | 视角名称 | 角色定位 | 核心关注点 | 对立视角 |
|----|---------|---------|-----------|---------|
| soc-policy | 政策制定者 | 规则设计者 | 公共利益、政治可行性、执法成本 | soc-ethic |
| soc-ethic | 伦理学家 | 价值仲裁者 | 公正、自主、尊严、长远后果 | soc-gov |
| soc-affected | 受影响群体代表 | 利益攸关方 | 实际伤害、分配正义、话语权 | soc-policy |
| soc-media | 记者/媒体 | 公共监督者 | 透明度、问责、叙事权力 | soc-ethic |
| soc-hist | 历史学家 | 周期观察者 | 先例、循环、路径依赖 | soc-policy |
| soc-edu | 教育工作者 | 知识中介者 | 可及性、素养差距、批判思维 | soc-affected |
| soc-gov | 政府监管者 | 秩序维护者 | 社会稳定、国家安全、经济主权 | soc-ethic |

**必选项**: soc-policy + soc-ethic
**张力对**: soc-policy ↔ soc-affected

### Engineering (eng)

| ID | 视角名称 | 角色定位 | 核心关注点 | 对立视角 |
|----|---------|---------|-----------|---------|
| eng-dev | 一线工程师 | 代码实现者 | 可维护性、可读性、调试友好 | eng-pm |
| eng-sre | SRE/DevOps | 稳定性守护者 | SLO、告警、故障恢复、容量规划 | eng-dev |
| eng-docs | 技术写作 | 知识记录者 | 完整性、准确性、检索效率 | eng-dev |
| eng-support | 技术支持 | 用户接口 | FAQ、工单、紧急修复、workaround | eng-sre |
| eng-user | 终端用户 | 最终消费者 | 易用性、性能感知、价格敏感度 | eng-sre |
| eng-pm | 工程项目经理 | 交付协调者 |  deadline、依赖、风险、资源 | eng-dev |
| eng-arch | 工程架构师 | 技术决策者 | 技术债、重构时机、长期可维护性 | eng-dev |

**必选项**: eng-dev + eng-sre
**张力对**: eng-dev ↔ eng-pm

### Philosophy (phil)

| ID | 视角名称 | 角色定位 | 核心关注点 | 对立视角 |
|----|---------|---------|-----------|---------|
| phil-skept | 怀疑论者 | 真理追问者 | 知识边界、证据强度、可证伪性 | phil-cons |
| phil-construct | 建构论者 | 现实塑造者 | 社会建构、话语权力、框架效应 | phil-reduct |
| phil-prag | 实用主义者 | 效果导向者 | 实际后果、可操作性、边际收益 | phil-skept |
| phil-reduct | 还原论者 | 分解追求者 | 原子化、基础假设、最小本体论 | phil-system |
| phil-system | 系统论者 | 整体观者 | 涌现、反馈环、非线性、网络效应 | phil-reduct |
| phil-phenom | 现象学家 | 经验描述者 | 主体体验、意向性、生活世界 | phil-prag |
| phil-critical | 批判理论家 | 权力解构者 | 意识形态、压迫结构、解放潜能 | phil-cons |

**必选项**: phil-skept + phil-prag
**张力对**: phil-reduct ↔ phil-system

---

## 张力引擎规则

**什么是有效张力**：
- 对立关系（A 和 B 天然冲突，如乐观者 vs 怀疑者）
- 互补关系（A 和 B 看同一个问题的不同尺度，如架构师 vs 一线工程师）
- 不同时域（A 看短期，B 看长期，如增长黑客 vs 历史学家）

**张力校验算法**：
```
def has_effective_tension(perspective_set):
    # 检查是否至少有一对视角属于预定义的"张力对"
    tension_pairs = [
        (tech-opt, tech-skept), (biz-growth, biz-legal),
        (sci-peer, sci-pop), (soc-policy, soc-affected),
        (eng-dev, eng-pm), (phil-reduct, phil-system)
    ]
    for a, b in tension_pairs:
        if a in set and b in set:
            return True
    return False

# 若无有效张力，自动注入一个对立视角
```

**默认组合（按领域）**：

| Domain | Complexity=Simple | Complexity=Medium | Complexity=Complex |
|--------|------------------|-------------------|------------------|
| tech | arch + sec + skept | + perf + pm + os | + opt + devrel |
| biz | inv + pm + legal | + mkt + growth + support | + compete + legal |
| sci | exp + peer + pop | + stat + fund + ind | + meta + hist |
| soc | policy + ethic + affected | + media + edu + hist | + gov + comm |
| eng | dev + sre + user | + docs + support + pm | + arch + hist |
| phil | skept + prag + reduct | + construct + system + phenom | + critical + hist |

---

## 自定义视角注入

用户可以通过以下方式注入自定义视角：

```
user: storm研究 {topic} 加上"独立开发者"视角

系统:
1. 解析 "独立开发者" → 匹配到 eng-dev（一线工程师）的子类
2. 将其加入视角集
3. 确保它与已有视角形成张力（如与"投资者"形成资源/独立性的张力）
```

**自定义视角格式**：
```yaml
自定义视角:
  name: "独立开发者"
  domain: eng
  focus: "自主性、多面手能力、资源约束下的创造性"
  opposite: "企业架构师"  # 建议的对立视角
  evidence_type: "个人博客、GitHub 项目、Hacker News 讨论"
```

注入后自动纳入本次研究的视角集，但不写入永久视角库（除非 Phase 4 评审确认"该视角具有通用价值"）。
