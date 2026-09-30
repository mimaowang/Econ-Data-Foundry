# Econ-DataKnowhow

[简体中文](#简体中文) · [English](#english)

> **把研究想法交给你的 agent，找到合适的经济研究数据，以及取得和使用它的方法。**

[![CI](https://github.com/mimaowang/Econ-Data-Foundry/actions/workflows/validate.yml/badge.svg)](https://github.com/mimaowang/Econ-Data-Foundry/actions/workflows/validate.yml)
[![Guide](https://img.shields.io/badge/Guide-usage-0969da)](guides/usage.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)
[![Software license: Apache 2.0](https://img.shields.io/badge/Software-Apache%202.0-2da44e)](LICENSE)
[![Content license: CC BY 4.0](https://img.shields.io/badge/Content-CC%20BY%204.0-2da44e)](LICENSE-CC-BY-4.0.md)

<p align="center"><img src="assets/econ-dataknowhow-hero.png" alt="Papers and data knowledge connect with a research idea" width="75%"></p>

## 简体中文

Econ-DataKnowhow 是面向实证研究者和学生的开源数据知识库。用你在 Codex、Claude Code 等工具中的 agent 打开项目文件夹，告诉它你的研究想法，它就能依据有来源的记录比较数据选择，解释哪些数据更合适、怎样取得或重建、哪些限制可能让方案行不通。你也可以让 agent 针对自己关注的领域，继续查证并整理新的数据知识。

目前收录的内容以中国实证研究为主，包括调查、行政与商业数据、公开统计资料，以及研究者从原始材料构建的数据。项目保存的是帮助你判断和使用这些数据的知识，而不是动辄数 GB 的原始数据文件；查询已有记录不需要安装 Python，也不需要配置作者使用的模型或 API。

[开始查询](#用研究想法查询) · [浏览数据索引](DATASET_INDEX.md) · [理解项目思路](guides/mental-model.md) · [参与完善](CONTRIBUTING.md)

### 用研究想法查询

克隆或下载项目，用你的 agent 打开文件夹，然后发送：

> 请先阅读 AGENTS.md 和 guides/mental-model.md，理解这个知识库如何帮助研究者选择数据。我的研究想法是：【问题、研究对象、地区和年份；不确定的地方也可以直接说】。请根据相关正式记录，用中文解释最适合的数据或组合、为什么优于相近选择、我实际能拿到什么、从哪里开始，以及哪些覆盖或权限限制会使方案不可行。如果记录不足，请说明缺口。此次先回答研究问题，不启动采集或修改文件。

agent 会从[索引](DATASET_INDEX.md)找到相关记录，再阅读正式的数据说明，而不是仅凭数据名称或论文摘要猜测。它应当解释为什么选择某项数据、相近选择为何不合适、实际能拿到什么、从哪里开始，以及哪些未知条件需要先核实。

### 这里记录的是什么

每份数据说明尽量保留观察单位、覆盖范围、关键变量、已核实的论文使用、取得或重建步骤、连接条件和不适用的研究问题。现成数据集、公开材料加工而成的数据、研究者自行收集的数据会分别说明；能打开来源网页，不等于能取得论文所用的最终分析文件。

`ready` 表示某项数据**在记录写明的条件下**可以推荐，不表示免费、立即可下载或适合所有研究。尚未确认的重要事实会留在 `grounding`、`needs-review` 或候选记录里。阅读时既要看结论，也要看来源、核验日期与仍然未知的地方。[使用指南](guides/usage.md)解释 agent 怎样把这些知识用于具体想法。

### 让知识库继续生长

如果你希望补充某个领域，可以让 agent 先阅读 [AGENTS.md](AGENTS.md)、[项目思路](guides/mental-model.md)和[维护指南](guides/operations.md)，从现有任务和来源继续，选择一项有边界的查证或修复工作。好的新增记录应让下一位研究者更容易做出数据选择，而不只是多收一篇论文或多填几栏。项目的记录格式见[模板](datasets/template.md)，将方法迁移到其他地区或领域可参照[适配指南](guides/adaptation.md)。

软件采用 [Apache 2.0](LICENSE)，原创目录内容采用 [CC BY 4.0](LICENSE-CC-BY-4.0.md)；这不授予第三方数据或[主视觉中的期刊标识](assets/README.md)的再使用权。引用信息见 [CITATION.cff](CITATION.cff)。

## English

> **Give your agent a research idea. Get a reasoned data choice, a practical acquisition path, and the limits that matter.**

Econ-DataKnowhow is an open knowledge base for choosing and obtaining economic research data. It brings together evidence from papers and data producers so your agent can explain which asset fits a question, what you can actually obtain or reconstruct, and where the plan may fail.

The catalog focuses on Chinese empirical research. It includes surveys, administrative and commercial products, public statistical releases, and researcher-built data. It stores knowledge about these assets, not copies of their underlying data. You use your own agent—such as Codex or Claude Code—to read and reason over the repository.

[Try it with your agent](#start-with-a-research-question) · [Browse the catalog](DATASET_INDEX.md) · [Understand the reasoning](guides/mental-model.md) · [Contribute](CONTRIBUTING.md)

### Start with a research question

Clone or download the repository and open its folder in your coding agent. Give it this prompt:

> Read AGENTS.md and guides/mental-model.md to understand the project. My research idea is **[question, population, place and period, including anything still undecided]**. Use the relevant catalog records to recommend a dataset or combination, explain why close alternatives lose, and tell me what I can obtain, where to start and what could make the plan infeasible. Cite the records you used and preserve their unknowns. Answer the question without editing the repository or starting collection.

This also works when your tool does not automatically load project instructions: the prompt explicitly names the entry files. Reading the knowledge base requires file access, not a Python installation or a particular model. Answer quality still depends on the agent and the evidence available.

The agent searches the [index](DATASET_INDEX.md), opens a few relevant records in [datasets/](datasets/), and compares coverage, access, research fit and joining conditions. See the [usage guide](guides/usage.md) for the reasoning path.

### What a useful answer looks like

Suppose you ask:

> “I want to study how health changes relate to household employment and consumption in mainland China after 2010. Where should I start?”

A repository-grounded answer should explain:

> **CFPS is a starting point** for an all-age household panel with income, employment, consumption and health measures. **CHARLS is the closer choice** if the question centers on people aged 45 and older and needs deeper aging and health measures. The choice depends on the population and variables you need.
>
> The CFPS record documents an application through its official data platform: register, state the research purpose and accept the data-use agreement, then obtain the approved waves and documentation. Its recorded confirmed waves run through 2022; that is the record's verification boundary, not a claim that later releases do not exist.
>
> The two-year survey interval cannot measure monthly responses. A city- or county-policy match depends on the geography you are actually permitted to receive. Having a panel does not itself establish a causal effect.

This illustration draws on the [CFPS](datasets/cfps.md) and [CHARLS](datasets/charls.md) records and their verification dates. For a constructed-data example, the [mental model](guides/mental-model.md#follow-one-research-decision) walks through land transactions and household outcomes—and why that combination remains conditional.

### What the records preserve

A useful data choice needs more than a name and a homepage. Each record aims to explain what one observation represents, which populations and years it covers, why it fits some questions better than nearby alternatives, and how a researcher starts obtaining or producing the asset.

The acquisition route may be a download, an application, a documented subscription, or a construction process. For constructed data, the record separates the public inputs from the final research table and preserves consequential sampling, cleaning, matching and validation choices. Access to public inputs does not promise exact reproduction of a paper's analysis file.

Papers establish particular research uses; producer documentation establishes products and access routes. Some useful public products are documented from producer evidence without a verified paper-use entry. A title, abstract or secondary account remains a lead rather than proof of detailed paper use. Read the evidence scope alongside the claim.

### How much can I rely on a record?

`ready` means the documented asset can be recommended **within its recorded conditions**. It does not mean free, immediately downloadable, suitable for every design, or that every associated paper has been checked in full. A public aggregate series can be ready while failing a question that requires individual or city-level observations.

`grounding` records retain useful knowledge with a material unresolved gap; `needs-review` records need rechecking. Candidates remain leads, and deprecated records direct you to replacements. The [quality card](ledgers/quality-card.md) reports current statuses and maintenance signals. Record counts and complete evidence fields are not a measure of research accuracy.

The knowledge base preserves sources, verification dates and unknowns so an agent can explain its recommendation. Current provider availability and terms may still need checking before acquisition.

### Help the knowledge base improve

The most valuable contribution makes a future research decision better: clarify a dataset identity, recover an acquisition step, explain a joining restriction, correct a claim, or ground a useful new asset. Expanding the catalog is a separate task from asking it a question.

For a collection task, give your agent a bounded request:

> Read AGENTS.md, guides/mental-model.md and guides/operations.md. Recover the current scope and task state, then finish one useful collection or repair task. Prefer closing an existing evidence gap. Explain the decision improved and what remains unknown, and run the project checks before completing the task.

The [discovery map](sources/discovery-sources.md) holds the current collection focus and staged journal directory. The [operations guide](guides/operations.md) explains maintenance and context recovery; the [record template](datasets/template.md) supports writing. Researchers adapting the project to another country or field can use the [adaptation guide](guides/adaptation.md). The author's model-specific supervision notes are optional local operating context, not setup requirements for other users.

Maintenance requires Python 3.10+ and the development dependencies:

```sh
python -m pip install -r requirements-dev.txt
```

Then follow the [release gate](guides/operations.md#release-gate). Generated indexes, exports and the static site are rebuilt from the canonical records. Use the [idea-routing](benchmarks/idea-routing/README.md) and [collection](benchmarks/collection/README.md) benchmarks to evaluate how an agent uses and maintains the knowledge.

### Find your way around

| Start here | What it gives you |
|---|---|
| [AGENTS.md](AGENTS.md) → [mental model](guides/mental-model.md) | The purpose and judgment a new agent should understand |
| [Usage guide](guides/usage.md) → [dataset index](DATASET_INDEX.md) | A path from research question to relevant records |
| [datasets/](datasets/) | Canonical data knowledge, sources and limitations |
| [Operations](guides/operations.md) → [ledgers/](ledgers/) | Maintenance instructions and durable work state |
| [dist/](dist/) and [docs/](docs/) | Generated machine-readable exports and the static catalog |

### Contributing, license and citation

See [CONTRIBUTING.md](CONTRIBUTING.md) for focused corrections and additions. The software is licensed under [Apache 2.0](LICENSE), and original catalog content under [CC BY 4.0](LICENSE-CC-BY-4.0.md). These licenses do not grant rights to third-party datasets or the journal marks in the [hero artwork](assets/README.md); their owners' terms still apply. [CITATION.cff](CITATION.cff) provides citation metadata.
