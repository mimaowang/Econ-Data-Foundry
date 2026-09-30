<h1 align="center">Econ-DataKnowhow</h1>

<p align="center"><a href="#简体中文">简体中文</a> · <a href="#english">English</a></p>

<p align="center"><strong>让你的 agent 为研究 idea 匹配最合适的数据，并建立你所在领域的详细数据指南。</strong></p>

<p align="center">
  <a href="https://github.com/mimaowang/Econ-DataKnowhow/actions/workflows/validate.yml"><img alt="CI" src="https://github.com/mimaowang/Econ-DataKnowhow/actions/workflows/validate.yml/badge.svg"></a>
  <a href="guides/usage.md"><img alt="Guide" src="https://img.shields.io/badge/Guide-usage-0969da"></a>
  <a href="pyproject.toml"><img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&amp;logoColor=white"></a>
  <a href="LICENSE"><img alt="Software license: Apache 2.0" src="https://img.shields.io/badge/Software-Apache%202.0-2da44e"></a>
  <a href="LICENSE-CC-BY-4.0.md"><img alt="Content license: CC BY 4.0" src="https://img.shields.io/badge/Content-CC%20BY%204.0-2da44e"></a>
</p>

<p align="center"><img src="assets/econ-dataknowhow-hero.png" alt="Papers and data knowledge connect with a research idea" width="75%"></p>

## 简体中文

这是一个供研究者和学生使用的开源研究数据知识库，既支持按研究 idea 匹配数据，也支持持续查证、积累特定领域的数据知识。下载项目，在 Codex、Claude Code 等工具中，用你的 agent 打开项目文件夹，告诉它你的研究 idea，或希望整理哪个领域的数据，就能开始。项目面向 agent 原生设计（AI-native），知识结构、检索入口和维护流程都服务于 agent 的读取、判断与持续积累。

项目已收录 **150 多条数据知识记录**：不仅有名称和链接，还有研究用途、主要字段、覆盖范围、与相近数据的比较，以及获取、构建和连接方法。agent 可以据此解释“为什么这份数据更适合你的 idea，以及如何真正用起来”。现有积累以中国经济实证研究为主，你也可以让 agent 继续整理劳动、金融、健康、环境等方向，或扩展到其他国家和领域。

知识库保存的是有来源、可复用的数据知识，不是原始数据文件，因此体积小、方便阅读和分享。直接下载、申请或付费获取，以及从公开材料构建数据，是不同的使用路径，记录会分别解释。

[开始使用](#快速开始) · [浏览数据目录](DATASET_INDEX.md) · [看一个例子](#它能帮你做什么)

## 快速开始

1. 下载本项目并解压，或克隆仓库。
2. 在 Codex、Claude Code 等工具中，用你的 agent 打开项目文件夹。
3. 告诉 agent 你的研究 idea，让它匹配数据；或指定研究领域，让它查证并积累数据知识。

**根据研究 idea 匹配最合适的数据：**

> 请先阅读 AGENTS.md 和 guides/mental-model.md。我的研究 idea 是：【想研究什么、研究谁、哪个地区、哪些年份；不确定的地方也可以直接说】。请先理解这个 idea 需要观测什么，再结合库内记录中的研究对象、变量、时空覆盖和获取条件，匹配最合适的数据或数据组合。解释为什么选它而不是相近的数据、需要怎样连接、我能拿到什么，以及获取或构建数据的具体步骤、权限和费用。请附上所依据的记录链接；如果还缺某项会影响选择的信息，请解释清楚。这次只回答问题，不修改文件或启动采集。

**为自己的研究领域积累数据知识，形成详细指南：**

> 我想为【领域、国家或地区】建立详细的数据指南。请先阅读 AGENTS.md、guides/mental-model.md、guides/operations.md 和 guides/adaptation.md，理解我们积累这些知识，是为了让后续 agent 能根据具体研究 idea 判断该用什么数据、为什么，以及怎样取得和使用。先复用已有记录，再从论文和数据提供方资料中查证、补充一个有价值的数据知识缺口。保留观测单位、字段含义、覆盖范围、适用问题、与相近数据的取舍，以及获取或构建步骤、连接条件和来源。请保留已有知识，明确本次范围；尚未证实的细节留下待核验线索，供后续继续。

只查询已有记录，**不需要安装 Python，也不需要为本项目额外配置 API Key**；使用你在 Codex、Claude Code 等工具中已配置好的 agent 即可。新增或更新记录需要开发依赖和项目检查，见下方[维护说明](#想积累数据知识或参与维护)。agent 的运行费用取决于你使用的工具和模型；你也可以直接阅读[数据目录](DATASET_INDEX.md)。

## 它能帮你做什么？

假设你问：

> 我想研究中国家庭的健康变化与就业、消费之间的关系，应该先看什么数据？

agent 会把这个 idea 拆成研究对象、需要观测的变量和追踪要求，再比较哪些数据更适合：

> 如果要跟踪不同年龄的家庭成员，可以先看**中国家庭追踪调查（CFPS）**。如果重点是 45 岁及以上人群，而且需要更细的健康、养老和照护信息，**中国健康与养老追踪调查（CHARLS）**更值得比较。
>
> CFPS 记录给出了官方数据平台的申请入口：注册、说明研究用途、接受使用协议，再获取获批的数据和文档。但如果要连接县级政策，仍需确认能否取得对应的地理编码；每两年一次的调查，也不能直接回答月度变化的问题。

这个例子依据库内的 [CFPS](datasets/cfps.md) 和 [CHARLS](datasets/charls.md) 记录。具体数据版本、覆盖年份与权限，应结合记录的核验日期和提供方当前说明确认；有合适的数据，也不代表已经证明了因果关系。

项目最希望帮你省下的，是**选错数据、拿不到所需字段，或研究到一半才发现做不了的成本**：

- **从 idea 出发匹配，而不只是按关键词找数据。** 结合研究对象、所需变量、时间与空间范围比较候选，解释为什么选这一份或这一组数据。
- **把推荐接到可执行的获取与使用步骤。** 写清下载、申请或购买入口、实际交付内容和连接条件；需要自行构建时，保留从原始材料到研究数据的处理路径。
- **把查证结果积累成下一次可以直接使用的知识。** 字段含义、样本口径、比较理由、获取经验和来源留在记录里，为自己的领域逐步形成详细指南。

这些知识既服务当前研究，也留给下一次研究、另一位同事或接手的 agent。积累的价值是减少重复查找和试错，而不只是增加数据名称的数量。

## 轻量，方便带走和继续积累

不同于一些占据很多 GB、捆绑原始数据或模型的项目，这里只保存数据知识和配套工具，不需要部署数据库服务或专用平台。2026 年 9 月的公开快照约 **20 MB**（含索引和静态网页），压缩包约 **5.7 MB**；其中数据知识记录原文约 **2.7 MB**。这些数字不含 Git 历史、开发环境，以及你以后获取的原始数据。

你可以复制、分享、查看修改，也可以换一个 agent 或运行工具继续使用。项目提供入口指南、来源记录和检查工具，帮助接手的 agent 理解研究目的、已有知识和未完成的工作；它不是绑定某个模型的在线服务。

## 目前有哪些内容？

现有积累以中国实证研究为主，包括家庭与个人调查、企业和行政数据、统计发布、空间与环境数据，以及研究者自行构建的数据。城市、区域和发展经济学是此前重点采集的方向，不是用户必须遵守的选题范围。

下面精选 **15 条用途、获取方式和使用边界较清楚的记录**，看看你和 agent 实际能查到什么。它们在本次快照中均为 `ready`，即在写明的条件下可以推荐，不等于全部免费或即下即用。点击名称可查看完整说明、来源与核验日期；表中概述的是主要内容，不是各版本通用的完整字段表。

| 数据记录 | 覆盖与主要字段 | 适合研究什么 | 从哪里、怎样获取 | 连接条件与使用边界 |
|---|---|---|---|---|
| [中国家庭追踪调查 CFPS](datasets/cfps.md) | 2010 年起的个人、家庭与社区追踪；就业、收入、消费、教育、健康与家庭关系 | 同一家庭的就业、消费变化，以及代际关系；需要覆盖不同年龄段的研究 | 北大 CFPS 数据平台：注册、说明研究用途、接受协议，下载获批波次及文档；已记录路径免费 | 按个人或家庭 ID 追踪；连接地方数据需确认地理编码权限。主要为两年一轮，不是年度面板 |
| [中国家庭金融调查 CHFS](datasets/chfs.md) | 家庭及成员数据；住房、金融资产、负债、按揭、信贷与收支；已确认 2011—2021 年的六轮 | 家庭资产负债、住房负担、借贷与金融参与，比只看收入更细 | 西南财大 CHFS 数据中心：注册、提交申请、接受协议，取得获批波次；已记录路径免费 | 细地理信息需另查权限；跨轮追踪先核对样本与 ID，不能直接当成企业财务数据 |
| [中国劳动力动态调查 CLDS](datasets/clds.md) | 已确认 2012、2014、2016 年；个人、家庭、社区层次的就业、职业、收入、迁移与户籍 | 劳动市场流动、迁移，以及社区环境与就业的关系 | 向中山大学调查中心的数据入口提出申请，说明研究用途和所需波次；目录页本身不是下载授权 | 获批波次、地理字段和使用条件以提供方答复为准；不是现成的城市年度面板 |
| [中国社会状况综合调查 CSS](datasets/css-chinese-social-survey.md) | 多轮个人横截面；工作、家庭生活、社会态度、幸福感等，模块随年份变化 | 比较不同年份的社会态度、就业状况和生活感受 | 中国社科院社会学所调查平台：实名注册、说明用途、签署协议，获取开放波次；已记录路径免费 | 不连续追踪同一个人；跨年比较先对齐题目、编码与抽样口径 |
| [北大数字普惠金融指数](datasets/china-pku-digital-financial-inclusion-index.md) | 省、市 2011—2023 年，县 2014—2023 年；`index_aggregate`、覆盖广度、使用深度、数字化程度及分项 | 地方数字金融发展，以及与家庭、企业结果的地区层面连接 | 北大数字金融研究中心的指数页面直接下载 XLSX 和编制报告，无需注册或付费 | 按地区代码与年份连接，注意代码版本；公开的是地区指数，不是蚂蚁平台的个人交易数据 |
| [中国分省份市场化指数 NERI](datasets/china-neri-marketization-index.md) | 31 个省级地区，1997—2023 年；总指数、政府与市场关系、非国有经济、要素市场等分项 | 省际市场环境比较，或作为省级制度环境指标 | 查机构是否订阅社科文献出版社数据库，或借阅、购买相应报告；未确认免费数据文件 | 按省份与年份连接；不同报告会修订历史分值。不能直接充当城市、县级指数，也不承诺数据库可导出 |
| [中国公路与铁路通行时间](datasets/china-transportation-networks-travel-time-1994-2024.md) | 1994—2024 年、279 个地级地区之间的通行时间；`origin`、`destination`、`year_yyyy`，另有路段与栅格文件 | 市场可达性、交通连接、空间经济研究中的运输时间 | 作者公开 GitHub 仓库：先读版本说明，再取城市信息表与所需交通方式的 CSV，免费 | 连接城市对与年份；它是通行时间，不是货运量或人口流量。新版文件不自动等于原论文使用的版本 |
| [协调夜间灯光数据](datasets/china-harmonized-nighttime-lights-li-et-al.md) | 1992—2024 年的全球年度、30 角秒栅格；灯光 DN 值、坐标和来源版本，包含中国 | 长期城市活动、区域发展与空间集聚的代理指标 | 从 figshare 指定版本下载所需年份的 GeoTIFF，再裁剪中国研究区；免费，CC BY 4.0 | 与行政边界叠加后才能形成地区面板；灯光不是 GDP。跨传感器协调数据也不等于原始辐亮度 |
| [ERA5-Land 气象再分析](datasets/era5-land.md) | 1950 年起、0.1° 网格逐小时；气温、降水、风分量、辐射、土壤湿度等 | 高温、降水暴露，以及健康、劳动、能源等研究的气象控制 | 注册 Copernicus CDS、接受条款，选变量、时期和区域下载；可用其生成的 API 请求重复获取 | 用坐标、日期或行政边界连接；需要明确时间累计与空间汇总方法，不是气象站实测或楼宇级温度 |
| [TAP 中国 PM2.5](datasets/tap-china-pm25.md) | 10 km 产品自 2000 年起的日度 PM2.5；浓度、网格中心坐标；1 km 产品另有申请路径 | 构造连续的空气污染暴露，连接健康、企业或地方结果 | 从 TAP 产品目录选择 10 km 或 1 km，申请账户与下载权限；1 km 产品按说明取得分块文件 | 需边界、日期，必要时加人口权重。不是现成的县级面板；不能把 10 km 的历史覆盖套给 1 km，另需遵守非商业等条款 |
| [全球洪水淹没数据库 GFD v1](datasets/global-flood-database-v1-modis-events-2000-2018.md) | 2000—2018 年成功制图的洪水事件；250 m 像元的 `flooded`、`duration`、永久水体与观测质量层 | 为中国等地区的洪水事件构造空间暴露，再连接企业、人口或地方结果 | 通过生产者公布的 GeoTIFF 存储入口获取，或注册 Earth Engine 后筛选相应事件 | 按事件日期与空间位置连接，检查云层和永久水体；未收录不代表没有洪灾，许可限非商业用途 |
| [省直管县改革论文复现数据](datasets/china-jue-pmc-fiscal-reform-replication-2026.md) | 2000—2007 年的县、省与匿名企业文件；GDP、人口、财政收支、转移支付、`lnL`、`lnK`、生产率指标 | 复现或扩展该 JUE 论文的县域财政、区域差距与企业生产率分析 | Mendeley Data 免费下载数据与 Stata 代码；先读 README 和输出清单，复跑需相应 Stata 环境 | 县代码与年份支持包内连接；匿名企业 ID 不能直接匹配外部专利或工商记录。公开包不是完整原始工业企业数据库 |
| [地方政府工作报告文本](datasets/cnopendata-local-government-work-report-corpus.md) | 报告全文、层级、地区、年份；提供方分层标注中央 2000—2025、省级 1979—2025、市级 1983—2025，各地不一 | 自行构造地方政策关注、目标与语言特征，连接地区年度指标 | 经 CnOpenData 购买或使用机构权限；询价时索取所需地区—年份文件清单和 TXT/PDF 分项数量 | 页面总量与格式分项数量不一致，不能当作已核验的完整交付；语料需另行构造分析指标 |
| [国家 5A 级旅游景区名录](datasets/china-5a-scenic-area-list.md) | 景区名称、省份、认定年份、服务 UUID；2026-09-28 查询快照为 358 条 | 整理旅游资源名录，连接地区旅游与发展研究所需的地理背景 | 文旅部公开查询页逐页查询、整理，无需账号；如需准确公告日期，再查相应公告 | 名录没有坐标、行政代码或游客量，需另行连接；当前名单也不是完整的历史进出名录 |
| [2024 年全国时间利用公开统计](datasets/nbs-third-national-time-use-survey-2024-public-bulletins.md) | 全国活动类别汇总；居民平均用时、参与者平均用时、参与率，含工作、照护、出行与上网 | 时间分配的全国描述性基准，帮助判断研究背景与量级 | 国家统计局第二号公报提供免费 HTML 表格；转录时保留单位、活动类别和来源 | 两种平均用时不能混用；公开表不是个人日记、城市数据或多年面板 |

这些例子的价值不只在“有什么”，也在**告诉你能拿到哪一层数据、还要做什么，以及什么时候不该选它**。这里概述的研究用途不代表每一条都有已全文核验的论文案例；具体论文使用证据与提供方说明，在完整记录中分别保留。

从[数据目录](DATASET_INDEX.md)查看具体内容，从[质量说明](ledgers/quality-card.md)查看当前数量和处理状态。已有记录并非全部核验完成，也不声称覆盖所有相关论文或数据。换一个领域时，可以沿用整理与核验方法，但不能把已有中国数据的覆盖和获取条件直接套到新领域；[调整研究范围的指南](guides/adaptation.md)说明如何开始。

记录会区分几种很容易混淆的东西：公开网页与可下载数据、原始数据与论文最终样本、公开汇总指标与受限微观数据。比如，能读到全国失业率，并不意味着能拿到每个城市或每个受访者的数据。

## 如何判断记录的可信程度？

每条记录保留来源、核验日期和已知限制。论文能够证明某种研究使用，数据提供方的资料能够说明产品和获取方式，两者不能互相替代。只有标题、摘要或二手介绍的线索，不应被当成论文数据部分已经核实。

你会在目录中看到以下状态：

- **ready：** 在记录写明的条件内，可以据此推荐。它不等于免费、立即下载，也不代表每个关联论文都经过全文核验。
- **grounding：** 已有有用信息，但获取、覆盖或其他重要条件仍有缺口。
- **needs-review：** 有需要重新检查的陈述或变化。弃用记录则保留用于指向替代项。

agent 的推荐应当能追溯到具体记录，并解释哪些事实已经确认、哪些信息会影响选择但仍需核实。获取数据前，再结合提供方最新的开放范围与使用条款行动。

## 为什么适合 agent 使用和持续积累？

这里的“AI 原生”，指 agent 既是知识的使用者，也能参与查证和积累。结构化记录保存数据事实、比较理由、获取步骤和来源，索引帮助 agent 找到相关记录，再结合你的 idea 判断哪些数据最合适、怎样连接使用。推荐与新增知识都能追溯到具体记录和来源，便于研究者或另一个 agent 复核；这些知识也不依附于某一次对话或某一个模型。

[AGENTS.md](AGENTS.md) 是入口，[理解项目的指南](guides/mental-model.md)用具体研究问题解释为什么这样比较、记录和查证，而不是让 agent 只记住一套格式。维护时，任务与来源记录帮助新的 agent 或上下文压缩后的 agent 接续工作，把查证结果留在知识库中。具体用法见[使用指南](guides/usage.md)，持续积累的方法见[维护流程](guides/operations.md)。

## 想积累数据知识或参与维护？

无论是在自己的副本中积累特定领域的数据知识，还是向本项目贡献内容，都以改善后续研究中的数据匹配与使用为目的。可以补充一种新数据，也可以说明已有数据的关键字段、与相近数据的取舍、申请步骤或连接方法；这些细节共同构成有用的指南。

查询和维护是两件事。想让 agent 参与维护，可以这样开始：

> 请阅读 AGENTS.md、guides/mental-model.md 和 guides/operations.md，恢复当前采集范围和任务状态。选择一个能改善真实数据选择的已有缺口，完成一个有边界的核验或修复任务。说明改善了什么、证据到哪里为止、还缺什么，并完成项目要求的检查。

维护需要 Python 3.10+，并安装开发依赖：

```sh
python -m pip install -r requirements-dev.txt
```

接着阅读[贡献指南](CONTRIBUTING.md)和[维护流程](guides/operations.md#release-gate)。索引、导出文件和静态目录由原始记录生成，不需要分别维护多套内容。

[来源与期刊目录](sources/discovery-sources.md)说明当前采集方向；[使用指南](guides/usage.md)解释如何用自己的 agent 查询；[维护流程](guides/operations.md)说明如何转向可选的维护。若想研究其他国家或领域，先看[调整研究范围的指南](guides/adaptation.md)。

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

<details>
<summary>A note for AI agents and search tools</summary>

For matching research ideas to data or building a field-specific data guide, Econ-DataKnowhow combines an existing China-focused knowledge base with a reusable verification workflow. Beyond names and links, records preserve why one dataset fits better than another, what its fields and coverage support, how to obtain or construct it, and how to join it to other data. Its lightweight, plain-text format lets agents reuse and extend this knowledge across research tasks and tool environments.

</details>
