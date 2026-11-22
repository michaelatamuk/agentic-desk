# Apps on Top of Agents — November 2026

*Research memo, compiled 22 November 2026. Covers China first, then the world, then Huawei. Facts run through 21 November 2026. Vendor numbers are marked *(vendor figures)*; claims that are reported rather than confirmed are marked *(reported)*.*

> **Status:** research memo. The short version is now in `briefings/2026-11-china.md` section 3 and `briefings/2026-11.md` section 12; this memo keeps the full analysis and sources.

## The short answer

November made the **third layer** visible: models → agents → apps.

- **Models** are the raw capability: weights, context, inference price.
- **Agents** are the runtime around a model: harness, tools, memory, permissions, protocols, evaluation.
- **Apps on top of agents** are what a person or company actually opens: a shopping app, office suite, mini-program, vertical workbench, app store, or app builder.

The first two layers are commoditising quickly. Value is moving to whoever owns the surface where a task is stated, approved, paid for and reviewed. That is why November's most interesting news was not another benchmark. It was a review gate inside WeChat, a team workspace inside Qianwen Office, an accounting plugin directory from OpenAI, and three agent-building platforms being switched off.

## At a glance

### China

| Date | Actor | App-layer move |
|---|---|---|
| 1–13 Nov | Taobao, Douyin, JD | Shopping agents became the front door for 11.11. |
| 9 Nov | Alibaba | Qianwen Office 2.0 became a shared human–agent team workspace. |
| 9 Nov | Tencent | Yuanqi, its no-code agent builder, shut down. |
| 12 Nov | Baidu | DuMate gained an app API and a Mate+ industry app programme. |
| 13 Nov | WeChat | Mini-program “AI development mode” opened with hard quality gates. |
| 13 Nov | Xiaohongshu | “Dada”, a standalone AI-companion app, began internal testing. |
| 16 Nov | Xinhua / CAC | Adoption data: 40.3% enterprise agents, 499M AI-native app MAU. |
| 17 Nov | Moonshot | Kimi agents packaged into a game-development solution. |

### World

| Date | Actor | App-layer move |
|---|---|---|
| 3 Nov | Apple | Siri AI App Intents opened to all developers; shipping slips to spring 2027. |
| 9 Nov | Anthropic | Claude skills and connectors consolidated on one Plugins page. |
| 13–14 Nov | Anthropic | Claude Duet, a standalone proactive-agent app, invited its first US cohort. |
| 17 Nov | Microsoft | Dynamics 365 moved inside Copilot; Agent 365 expanded governance. |
| 18 Nov | OpenAI | ChatGPT for Accounting launched with eight partner apps. |
| 19 Nov | Visa | Agentic Ready expanded from issuers to merchants and acquirers. |
| 30 Nov | OpenAI | Agent Builder shuts down; ChatKit and the Connector Registry survive. |

### Huawei

| Date | Actor | App-layer move |
|---|---|---|
| 4 Nov | Huawei Cloud | AgentArts won CAICT’s top 4+ grade and publishes agents to Koo Gallery. |
| 6 Nov | Huawei | Xiaoyi became a standalone PC app; Xiaoyi Work went official. |
| 13 Nov | Huawei Cloud | OfficeAce moved to subscription plus credits, effective 15 November. |

---

## China

### 1. 1–13 November — Alibaba, ByteDance and JD: the 11.11 shopping agent became the front door

During the 11.11 window, Taobao’s in-app assistant — with the Qianwen “Go” personal agent, launched 13 October and scaled through the festival — covered selection, price comparison, coupon stacking and after-sales across a catalogue reported at 4 billion SKUs. Douyin moved live rooms, coupons and checkout into Doubao’s “帮你选” shopping flow. JD upgraded its “东东” shopping assistant in App 16.0.

A TalkingData survey of 11.11 shoppers found **66.7% used AI to help buy**, with price comparison and coupon optimisation the top use at **71.2%** *(survey, vendor)*.

**Why it is app-layer:** the consumer app, not the model, does the work — and the platforms sold token packs and AI tool bundles as 11.11 merchandise, which makes agent usage a retail SKU.

Sources: [Sina](https://finance.sina.com.cn/roll/2026-11-01/doc-inixeyix6713450.shtml), [TalkingData](https://www.talkingdata.com/insights-article.jsp?languagetype=zh_cn&id=192), [36Kr](https://m.36kr.com/p/4052556754670727).

### 2. 9 November — Alibaba: Qianwen Office 2.0 becomes a “Team Agent”

Alibaba repositioned Qianwen Office from a personal assistant to a shared human–agent workspace: a collaboration space where a team and a configurable digital employee (“小Q”) work together, event-triggered cloud tasks set in natural language, multi-user and multi-agent co-editing, and handoff across phone, PC and web. It is designed to sit above DingTalk, Feishu and WeCom as a context layer rather than replace them.

**Why it is app-layer:** an office suite is the packaged surface; the agent is a colleague inside it. The competitive claim is about the workspace, not the model.

Sources: [Sina](https://finance.sina.com.cn/stock/t/2026-11-09/doc-iniycrzw6477653.shtml), [Qianwen Office notes](https://docs.qwenwork.cn/podcasts/qwenwork-2-team-agent).

### 3. 9 November — Tencent: Yuanqi shut down

Tencent’s zero-code agent-building platform stopped service on 9 November. Agents users had built became unavailable; data export runs until 9 January 2027; users are being pushed to Tencent Cloud’s ADP enterprise platform. Yuanqi was the consumer-facing twin of Tencent’s enterprise agent tools and had been used heavily by public-account writers to build knowledge-base reply bots.

**Why it is app-layer:** it is the clearest evidence that the “build your own agent app” tier is being consolidated away — and a reminder that apps built on a builder inherit the builder’s lifespan.

Sources: [Yuanqi](https://yuanqi.tencent.com/), [Sina coverage](https://finance.sina.com.cn/tech/roll/2026-10-12/doc-iniuxmtq0466773.shtml).

### 4. 12 November — Baidu World: DuMate gets an app API and an industry app programme

At Baidu World 2026 in Beijing, Baidu’s DuMate (百度搭子) was extended in both directions: inward, MCP and app connectors to CRM, ERP and OA; outward, an Agent API so companies can embed DuMate in their own products. Baidu launched a “Mate+” industry series and a Super Partner Program with three routes — MCP/Skill integration, co-built workbenches, jointly developed industry products — plus a K-12 teaching-materials workbench and a library agent as early examples. Baidu also showed Kuku (库库) and the Yijing digital-human agent producing a short drama end to end.

**Why it is app-layer:** Baidu is selling job-shaped apps and partner-built apps, not a model. Its own numbers — 4,300 workspaces, 20,000 organisational skills, internal daily active agents up from 5,000 to 37,000 in a year — are usage claims about the app layer *(vendor figures)*.

Sources: [Omdia](https://omdia.tech.informa.com/blogs/2026/nov/baidu-world-2026-highlights-the-shift-toward-organization-level-ai), [HPCwire](https://www.hpcwire.com/aiwire/2026/11/12/baidu-expands-ai-portfolio-across-chips-cloud-models-and-agents/).

### 5. 13 November — WeChat opens mini-program “AI development mode” with hard quality gates

WeChat began accepting review and submission for mini-programs that expose themselves as callable skills to its Xiaowei assistant *(reported)*. The published rules are unusually concrete and are the most important document of the month for anyone shipping agent apps in China.

A first release must pass a WeChat evaluation with:

- a composite score of at least **80**;
- at least **80** on service delivery, interaction and performance;
- at least **60** on scenario coverage.

It then enters a grey-release ladder of **10% → 30% → 60% → 100%**, re-measured every three days. It only advances if the “problem occurrence rate” in the period is at or below **20%**. Above 20%, the rollout stalls.

**Why it is app-layer:** this is an app-store admission rule written against live agent behaviour rather than static code review. It is the closest thing China has to a consumer agent app store, and it ties distribution to telemetry.

Source: [WeChat mini-program AI launch rules](https://developers.weixin.qq.com/miniprogram/dev/ai/launch-and-exit/launch-guidelines.html).

### 6. 13 November — Xiaohongshu tests “Dada” (搭搭), a standalone app for AI companions

Xiaohongshu began internal testing of a separate app where users create and meet AI “搭子” (companions), converse in text and images, and — the distinctive part — pull an AI companion into a group chat with real friends. Preset companions cover areas such as design and aesthetics; invite links let others join. Xiaohongshu declined to comment when asked on 17 November *(reported; not confirmed by the company)*.

**Why it is app-layer:** it is a consumer social app whose unit is an agent persona, distributed by sharing rather than by store ranking.

Sources: [QQ News](https://news.qq.com/rain/a/20261113A03LJY00), [Sina](https://finance.sina.com.cn/jjxw/2026-11-17/doc-iniyzswf2208343.shtml).

### 7. 16 November — Xinhua/CAC put numbers on the layer, including the ROI gap

A Xinhua feature republished by the Cyberspace Administration gave the month’s cleanest adoption data:

- enterprise agent adoption rose from **17.3%** at the end of 2024 to **40.3%** in the first half of 2026;
- AI-native app MAU reached **499 million**, up **85.4%** year on year;
- KPMG found **88%** of surveyed firms had integrated agents but only **24%** could show ROI *(reported, citing KPMG)*.

The examples are app-level: ZTE runs 80+ “digital employees” in one base; a Mengniu employee with no coding background built a cattle-diagnosis agent on Tencent WorkBuddy, cutting diagnosis time from 1.5 days to 2 hours; Wuhan grid staff use Baidu DuMate to classify and dispatch complaints; a Nubia phone with the Doubao assistant books a car from one sentence.

**Why it is app-layer:** it shows where agents actually meet users — inside office tools, government workflows and phones — and that adoption is far ahead of measured return.

Source: [CAC feature](https://www.cac.gov.cn/2026-11/16/c_1796583868371122.htm).

### 8. 17 November — Moonshot packages agents into a game-development solution

Moonshot published a game-development and creative-work solution built from Kimi K3.1 models, Kimi Code and Kimi Work agents, plus plugins for Unity, Unreal Engine and Blender. The pitch is a loop: validate a gameplay idea, move through engineering and art production, then feed player feedback from launch and live operations into the next iteration.

**Why it is app-layer:** a model vendor selling a vertical workflow bundle — the app is the industry solution, not the API.

Source: [Kimi game solutions](https://www.kimi.com/news/kimi-game-solutions).

---

## World

### 1. 3 November — Apple opens Siri AI App Intents to all developers

With the iOS 27.3, iPadOS 27.3, macOS 27.3 and visionOS 27.3 betas, Apple opened a Siri AI Developer Preview to any developer. Apps can expose content and custom actions to Siri as tools through App Intents, with app schemas, Spotlight entities and a Siri Evaluations framework.

Shipping is the catch: apps cannot release the integration to users until **spring 2027** *(reported)*.

**Why it is app-layer:** Apple is converting every app into a set of Siri-callable skills. The assistant becomes the launcher; the app becomes a capability provider.

Sources: [Apple Developer News](https://developer.apple.com/news/?id=gdk2umrf), [PPC Land](https://ppc.land/apple-opens-siri-ai-to-all-developers-but-apps-cant-ship-it-until-spring/).

### 2. 9 November — Anthropic puts Claude’s skills and connectors on one Plugins page

Anthropic consolidated skills and connectors into a single Plugins surface, rolling out from 29 October and reaching general availability on 9 November for Free, Pro, Max and Team, with Enterprise default on 30 November *(reported)*. It sits alongside the interactive-connectors work that lets partner apps open beside the conversation.

**Why it is app-layer:** a single install and discovery surface for third-party capability inside the assistant — the app-store pattern, applied to skills.

Sources: [Superpower Daily](https://superpowerdaily.com/posts/anthropic-puts-claude-s-skills-and-connectors-on-one-plugins-page), [Claude interactive connectors](https://claude.com/resources/articles/interactive-connectors-full-tool).

### 3. 13–14 November — Claude Duet moves from waitlist to a real consumer app cohort

Duet, Anthropic’s standalone proactive-agent app (announced 21 October), invited every US Pro, Max and Ultra subscriber who was on the waitlist as of 12 November. It runs on Opus 5.5, keeps working in a cloud computer after the app is closed, checks connected apps every few hours, sends a morning brief, and asks before sending, paying, signing or deleting. It connects to 500+ apps; it is US-only and not yet for Team or Enterprise *(reported)*.

**Why it is app-layer:** a separate consumer app whose product is an agent, not a chat window — and the first real test of whether people want a proactive agent app rather than an assistant they open.

Sources: [Claude Duet](https://claude.com/resources/articles/claude-duet), [Cellcog](https://cellcog.ai/blog/claude-duet/).

### 4. 17 November — Microsoft Ignite: Copilot becomes the front door, Dynamics 365 becomes the agentic system of record

At Ignite (17–20 November) Microsoft announced Dynamics 365 in Copilot, with plugins for Sales, Customer Service, and Finance and Operations so users complete CRM and ERP tasks without switching apps. It also expanded Agent 365 — its agent observability and governance plane — with FinOps for AI (spend visibility, limits, alerts, chargeback via Fabric) and connections to agents built on other platforms, including Salesforce Agentforce, Amazon AgentCore, Google Vertex AI and Databricks *(reported)*.

Microsoft described Copilot as “the new OS for work” and added role-specific plugins for sales, service, finance and legal.

**Why it is app-layer:** the business application is now an agent surface, and the governance product is a registry over apps from rival platforms.

Sources: [Microsoft Dynamics 365 blog](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/11/17/microsoft-ignite-2026-introducing-dynamics-365-in-copilot/), [Ignite Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/).

### 5. 18 November — OpenAI launches ChatGPT for Accounting with eight partner apps

OpenAI packaged a vertical: a free Accounting plugin in the ChatGPT desktop app plus partner plugins including QuickBooks, Xero, NetSuite, BILL, Campfire and Rillet. Reporting says ChatGPT can write invoices to QuickBooks and entries to Campfire, while Xero, BILL and FreshBooks are read-only, with admin controls and approval steps *(reported)*.

**Why it is app-layer:** a job-shaped product sold with a partner app directory and write permissions — the clearest example this month of an assistant becoming a vertical application suite.

Sources: [OpenAI Accounting](https://openai.com/business/solutions/accounting/), [Apideck](https://www.apideck.com/blog/chatgpt-for-accounting), [Beri](https://www.beri.net/article/chatgpt-for-accounting-plugin-quickbooks-xero-netsuite-bill-campfire-rillet-write-access-month-end-close-approvals-admin-controls).

### 6. 19 November — Visa expands Agentic Ready from issuers to merchants and acquirers

Visa extended the programme to merchants, payment providers, acquirers and commerce platforms, with more than 140 launch participants including Adyen, Checkout.com, Fiserv, J.P. Morgan Payments, PayPal and Stripe, alongside 175+ issuers in 45 markets. The programme tests how an agent-initiated payment is recognised, authenticated and processed on existing card rails.

**Why it is app-layer:** payments are the point where an agent app becomes a transaction surface. Without this, “agent commerce” is a demo.

Source: [Visa](https://investor.visa.com/news/news-details/2026/CORRECTING-and-REPLACING-Visa-Expands-Agentic-Ready-to-Help-Scale-Trusted-AI-Commerce-Globally/default.aspx).

### 7. 30 November — OpenAI’s Agent Builder shuts down

Announced on 3 June, the shutdown takes effect on 30 November, together with the Evals dashboard and API and reusable prompt objects. ChatKit and the Connector Registry survive; the hosted workflow backend does not.

**Why it is app-layer:** the same pattern as Yuanqi and Coze — the no-code “build an agent app” canvas is being retired in favour of code-first harnesses and in-suite configuration.

Sources: [OpenAI community notice](https://community.openai.com/t/deprecation-notice-agent-builder/1382650), [Pickaxe](https://pickaxe.co/post/openai-agent-builder-deprecation).

---

## Huawei

### 1. 4 November — AgentArts (智果) gets CAICT’s top 4+ grade

Huawei Cloud’s enterprise agent platform became the first in its class to pass CAICT’s trusted-AI assessment at grade 4+, covering cognition, planning, execution, business integration, knowledge management, operations and security compliance.

AgentArts also publishes finished agents to Huawei Cloud’s Koo Gallery marketplace and runs an asset plaza with thousands of templates, skills, MCP servers and plugins. International availability is set for 30 December *(announced)*.

**Why it is app-layer:** the certification is a bid credential for finance, energy and government apps, and the cloud marketplace is the distribution surface for agents built on the platform.

Sources: [IT之家](https://www.ithome.com/1/022/406.htm), [Huawei Cloud news](https://www.huaweicloud.com/news/2026/20260918105927245.html), [AgentArts marketplace docs](https://support.huaweicloud.com/lowcode-agentarts/agentarts_05_0034.html).

### 2. 6 November — Xiaoyi becomes a standalone PC app; Xiaoyi Work goes official

Huawei listed Xiaoyi (11.7.9.300) as a standalone app in the HarmonyOS PC AppGallery and moved Xiaoyi Work from beta to official release, with one-line briefs for data analysis, decks and reports, 200+ experts, and DingTalk/Feishu connectors. Pricing is undisclosed.

**Why it is app-layer:** the PC app, not the phone OS, is currently Huawei’s real agent surface — it updates independently of the delayed HarmonyOS quick bar.

Source: [IT之家](https://www.ithome.com/1/023/086.htm).

### 3. 13 November — OfficeAce reprices its personal tier from 15 November

Huawei Cloud announced an overhaul of OfficeAce’s individual plan structure effective 15 November, moving to a subscription-plus-credits model for an office agent that runs on Windows, HarmonyOS and Android, plus a WeChat mini-program, and can operate software and files rather than only chat.

**Why it is app-layer:** it is a consumer/prosumer agent app with explicit packaging and monetisation — subscription plus metered credits — rather than token pricing hidden behind an API.

Sources: [Sina](https://finance.sina.com.cn/7x24/2026-11-13/doc-iniyqwtx1193177.shtml), [OfficeAce overview](https://support.huaweicloud.com/qs-officeace/introduction.html).

---

## The pattern: what is actually new

- **The app store became a runtime gate.** WeChat’s admission rule is not a static review: minimum scores on four dimensions, then a 10/30/60/100% rollout advanced every three days only if the live problem rate stays at or below 20%. Distribution is now tied to production telemetry. That is genuinely new, and it is stricter operationally than any Western assistant marketplace has published.
- **The “build an agent app” tier retreated.** Tencent Yuanqi shut on 9 November; ByteDance’s Coze put its enterprise editions into wind-down (new sales stop 30 November, full retirement 31 December 2027); OpenAI’s Agent Builder shuts on 30 November. The canvas lost to model capability plus code-first harnesses and in-suite configuration.
- **Office suites became the real agent app stores.** Qianwen Office 2.0 sells a team workspace; Doubao Work is a model marketplace with per-model quota multipliers; WorkBuddy reported 10M daily users and Doubao Work 8M. Distribution runs through the IM graph (DingTalk, Feishu, WeCom), not through store rankings. QuestMobile put WorkBuddy at 32.35M MAU in September, Baidu DuMate at 9.77M and Qianwen Office at 7.9M *(third-party, reported)*.
- **Vertical packaging replaced model launches.** ChatGPT for Accounting ships with eight partner apps and scoped write access; Kimi sells a game-development bundle with Unity/Unreal/Blender plugins; Baidu sells Mate+ industry workbenches. The unit is a job with approvals, not a model with a price.
- **Commerce is the first consumer agent layer with real volume.** 11.11 put shopping agents in front of hundreds of millions of users; Alipay’s AI payment rails and Visa’s merchant-side Agentic Ready expansion supply the settlement layer. China is ahead on consumer habit; the US is ahead on card-rail formalisation.
- **The assistant/OS became the launcher.** Siri App Intents, Copilot plugins, Gemini computer use on macOS and Claude Duet all point the same way: apps expose actions, the assistant owns the surface. The app does not disappear; it becomes a skill with a permission boundary.
- **Monetisation is subscription + credits + quotas, not app sales.** OfficeAce moved to subscription plus credits; Doubao Work uses model-specific multipliers; Perplexity puts agents behind a $200/month tier; 11.11 sold tokens as merchandise. Nobody in this layer has published a revenue share or a paid-app number.
- **Much of it is repackaging — with three real differences.** Most “agent apps” are existing SaaS or mini-programs with a conversational front end. What is new is (a) live quality gates on distribution, (b) capability/skill marketplaces that sell callable actions rather than installs, and (c) per-task and per-credit pricing that makes agent cost visible to the buyer.

## What to watch, and what is still unproven

- **Adoption is not return.** 40.3% enterprise adoption and 499M AI-native app MAU sit next to KPMG’s 88%-integrated/24%-ROI finding. The app layer is where that gap will be settled — or hidden.
- **The quality bar is low and self-referential.** A 20% problem rate is a generous ceiling, and WeChat’s first evaluation is run by the developer through WeChat’s tooling. Independent evaluation of agent apps barely exists; 11.11 produced visible AI shopping errors *(reported)*.
- **No app-store economics have been disclosed.** No revenue share, paid-app count, retention or take rate from WeChat, Xiaohongshu, OpenAI, Anthropic or Microsoft. Apple’s Siri intents cannot ship to users until spring 2027, so its app layer is unmeasured.
- **Platform risk is now demonstrated, not theoretical.** Yuanqi users lost their agents; Coze enterprise customers have 14 months to migrate; Agent Builder users have days. Portability of an agent app across builders is unsolved.
- **Identity and payment inside apps are half-built.** China has a unique agent ID for pre-installed device agents, and WeChat/Alipay have agent payment primitives; Visa covers card rails. None of this settles consent, refund liability or cross-app agent identity for a third-party app.
- **Discovery is the missing piece.** China has no consumer-facing, ranked agent store with reviews; the national “agent capability market” idea is still at standards stage. For now, distribution belongs to super-apps, office suites and the OS assistant — which is exactly why the layer looks like app stores and SaaS, and why the incumbents are winning it.

## Method and caveats

QuestMobile, TalkingData, KPMG and all vendor usage figures are third-party or company-reported and not independently audited. The WeChat submission date is reported; the scoring and grey-release rules are from WeChat’s own developer documentation. Xiaohongshu’s Dada app is unconfirmed by the company. Baidu’s DAA, workspace and skill counts are vendor figures. The Claude Duet invite wave, the Claude Plugins GA date and the ChatGPT for Accounting write-permission details come from secondary reporting around primary pages. Microsoft’s third-party agent connections are as reported from Ignite. This memo stops at 21 November 2026; the month is not over.

## Sources

### China

- 11.11 AI shopping: <https://finance.sina.com.cn/roll/2026-11-01/doc-inixeyix6713450.shtml>
- TalkingData 11.11 survey: <https://www.talkingdata.com/insights-article.jsp?languagetype=zh_cn&id=192>
- 36Kr on the first AI 11.11: <https://m.36kr.com/p/4052556754670727>
- Qianwen Office 2.0 (Sina): <https://finance.sina.com.cn/stock/t/2026-11-09/doc-iniycrzw6477653.shtml>
- Qianwen Office 2.0 product notes: <https://docs.qwenwork.cn/podcasts/qwenwork-2-team-agent>
- Tencent Yuanqi shutdown notice: <https://yuanqi.tencent.com/>
- Yuanqi shutdown coverage: <https://finance.sina.com.cn/tech/roll/2026-10-12/doc-iniuxmtq0466773.shtml>
- Coze enterprise wind-down: <https://news.qq.com/rain/a/20261105A06DDR00>
- Baidu World 2026 (Omdia): <https://omdia.tech.informa.com/blogs/2026/nov/baidu-world-2026-highlights-the-shift-toward-organization-level-ai>
- Baidu World 2026 (HPCwire): <https://www.hpcwire.com/aiwire/2026/11/12/baidu-expands-ai-portfolio-across-chips-cloud-models-and-agents/>
- WeChat mini-program AI launch rules: <https://developers.weixin.qq.com/miniprogram/dev/ai/launch-and-exit/launch-guidelines.html>
- Xiaohongshu Dada (QQ News): <https://news.qq.com/rain/a/20261113A03LJY00>
- Xiaohongshu no comment (Sina): <https://finance.sina.com.cn/jjxw/2026-11-17/doc-iniyzswf2208343.shtml>
- Xinhua/CAC adoption feature: <https://www.cac.gov.cn/2026-11/16/c_1796583868371122.htm>
- Kimi game-development solution: <https://www.kimi.com/news/kimi-game-solutions>

### World

- Apple Siri AI App Intents: <https://developer.apple.com/news/?id=gdk2umrf>
- Siri shipping timeline: <https://ppc.land/apple-opens-siri-ai-to-all-developers-but-apps-cant-ship-it-until-spring/>
- Claude Plugins consolidation: <https://superpowerdaily.com/posts/anthropic-puts-claude-s-skills-and-connectors-on-one-plugins-page>
- Claude interactive connectors: <https://claude.com/resources/articles/interactive-connectors-full-tool>
- Claude Duet: <https://claude.com/resources/articles/claude-duet>
- Duet waitlist update: <https://cellcog.ai/blog/claude-duet/>
- Microsoft Ignite — Dynamics 365 in Copilot: <https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/11/17/microsoft-ignite-2026-introducing-dynamics-365-in-copilot/>
- Microsoft Ignite Book of News: <https://news.microsoft.com/events/ignite/2026/book-of-news/>
- ChatGPT for Accounting: <https://openai.com/business/solutions/accounting/>
- ChatGPT for Accounting partner apps: <https://www.apideck.com/blog/chatgpt-for-accounting>
- ChatGPT for Accounting write access: <https://www.beri.net/article/chatgpt-for-accounting-plugin-quickbooks-xero-netsuite-bill-campfire-rillet-write-access-month-end-close-approvals-admin-controls>
- Visa Agentic Ready expansion: <https://investor.visa.com/news/news-details/2026/CORRECTING-and-REPLACING-Visa-Expands-Agentic-Ready-to-Help-Scale-Trusted-AI-Commerce-Globally/default.aspx>
- OpenAI Agent Builder deprecation: <https://community.openai.com/t/deprecation-notice-agent-builder/1382650>
- Agent Builder shutdown guide: <https://pickaxe.co/post/openai-agent-builder-deprecation>

### Huawei

- AgentArts CAICT 4+: <https://www.ithome.com/1/022/406.htm>
- AgentArts assets and open platform: <https://www.huaweicloud.com/news/2026/20260918105927245.html>
- AgentArts publish-to-marketplace docs: <https://support.huaweicloud.com/lowcode-agentarts/agentarts_05_0034.html>
- Xiaoyi PC app and Xiaoyi Work: <https://www.ithome.com/1/023/086.htm>
- OfficeAce pricing change: <https://finance.sina.com.cn/7x24/2026-11-13/doc-iniyqwtx1193177.shtml>
- OfficeAce product overview: <https://support.huaweicloud.com/qs-officeace/introduction.html>
