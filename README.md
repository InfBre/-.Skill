# 老板.skill

> *"这个需求很简单，怎么实现我不管，明天上线。"*
> *"好好干，明年给你涨工资。"*
> *"你还有很大的提升空间。"*
> *"现在大环境不好，能有份工作就不错了要感恩。"*

你开始学会把委屈咽下去，把解释删掉，把情绪压平；你说“收到”，你说“明白”，你说“我来处理”，你把自己训练成一个永远配合、永远能接住的人。可越是这样，越像一个可替换的选项：做得多是应该的，做不好是你不行，做得好也只是“本来就该这样”。

你以为被看见了，其实只是被用到了。

我把你家老板蒸馏成 AI Skill，用ta的方式跟你说话，记得你改了8版的方案、他给你画过的饼、下班前10分钟突然加的需求，帮你提前演习应对老板的各种场景，再也不怕老板突然@你。

Inspired by colleague-skill（同事.skill）& ex-skill（前任.skill）.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)
[![OpenClaw Compatible](https://img.shields.io/badge/OpenClaw-Compatible-blueviolet)](https://openclaw.ai)

---

## 安装

### OpenClaw（推荐）
```bash
# 直接下载到OpenClaw技能目录
git clone https://github.com/yourrepo/boss-skill ~/.openclaw/skills/create-boss
```

### Claude Code
```bash
# 安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/yourrepo/boss-skill .claude/skills/create-boss

# 全局安装
git clone https://github.com/yourrepo/boss-skill ~/.claude/skills/create-boss
```

### 依赖（可选）
```bash
pip3 install -r requirements.txt
```

---

## 使用

在OpenClaw/Claude Code中输入：
```
/create-boss
```

按提示输入老板的代号、管理风格、口头禅、共同经历等信息，所有字段均可跳过，仅凭描述也能生成。

完成后用 `/{老板代号}` 调用该老板Skill，开始对话。

### 管理命令
| 命令 | 说明 |
|------|------|
| `/list-bosses` | 列出所有生成的老板Skill |
| `/{slug}` | 调用完整Skill（像真实老板一样跟你对话） |
| `/{slug}-crunchtime` | 赶项目模式（老板疯狂催进度） |
| `/{slug}-performance` | 绩效谈话模拟 |
| `/delete-boss {slug}` | 删除老板（一键炒鱿鱼） |
| `/let-go {slug}` | 放走（delete 的温柔别名） |

---

## 效果示例

> 输入：`张总，互联网公司老板，画饼+催命+PUA型，口头禅是"这个需求很简单怎么实现我不管明天上线""你还有很大的提升空间"，总喜欢下班前10分钟找你改需求，画饼说"项目成了给你分奖金"`

**场景一：突然找你**
```
用户      ❯ /张总 张总找我？
老板.skill ❯ 来我办公室一下。
             上次那个方案再改改，下班前给我。
```

**场景二：问进度**
```
用户      ❯ /张总 这个项目我这周就能做完
老板.skill ❯ 这周？我上周不说这周要上线？
             年轻人效率高点，明天下午我要看到结果。
             好好干，项目成了给你申请奖金。
```

**场景三：提加薪**
```
用户      ❯ /张总 张总我想申请涨点工资
老板.skill ❯ 你的能力我们是看到的，但是今年整体效益不好，再等等。
             放心，我心里有数，明年晋升优先考虑你。
             年轻人不要总想着钱，成长最重要。
```

**场景四：绩效谈话**
```
用户      ❯ /张总-performance
老板.skill ❯ 坐，聊聊这季度绩效。
             你表现还行吧，但是还有很大的提升空间。你看隔壁小李每天都加班到10点，多向人家学习。
             好好干，我很看好你，未来给你更大的发展空间。
```

**场景五：下班加需求**
```
用户      ❯ /张总 张总我都下班了
老板.skill ❯ 哦不好意思，刚看到你这个方案有个地方要改下。
             也不是什么大问题，回家改下10点前发我就行。
             辛苦一下，客户明天要。
```

---

## 功能特性

### 数据源
| 来源 | 格式 | 备注 |
|------|------|------|
| 微信/企业微信聊天记录 | 导出文件 | 推荐，最能还原真实说话风格 |
| 会议录音转写 | 文本 | 精准还原说话方式和口头禅 |
| 口述描述 | 纯文本 | 最方便，仅凭描述就能生成 |
| 邮件/钉钉消息 | 导出文件 | 提取常用沟通话术 |

### 生成的Skill结构
每个老板Skill由两部分组成，还原度90%+：
| 部分 | 内容 |
|------|------|
| **Part A — 职场记忆库** | KPI要求、做过的项目、改了N版的方案、画过的饼、你的优缺点、内部梗 |
| **Part B — 老板画像** | 5层结构：硬规则 → 身份 → 说话风格 → 管理模式 → 行为习惯 |

运行逻辑：`收到消息 → 老板画像判断ta会怎么回 → 记忆库补充真实职场场景 → 用老板的方式输出`

### 支持的标签
**管理风格**：画饼型 · 催命型 · 佛系型 · PUA型 · 技术型 · 甩锅型 · 官僚型 · 保姆型
**行业属性**：互联网 · 金融 · 国企 · 传统行业 · 创业公司
**说话风格**：官腔十足 · 直来直去 · 阴阳怪气 · 喜欢说教 · 惜字如金
**特殊习惯**：下班找你 · 周末加班 · 爱开长会 · 喜欢拿别人对比 · 总说"我早就说过"

### 进化机制
* **追加记忆** → 导入新的聊天记录/语录 → 自动分析增量 → merge 进对应部分
* **对话纠正** → 说「ta不会这样说」→ 写入 Correction 层，立即生效
* **版本管理** → 每次更新自动存档，支持回滚

---

## 项目结构
本项目遵循 [AgentSkills](https://agentskills.io) 开放标准，兼容 Claude Code 和 OpenClaw：

```
create-boss/
├── SKILL.md                # skill 入口
├── README.md               # 本文件
├── prompts/                # Prompt 模板
│   ├── intake.md           # 信息采集模板
│   ├── memory_analyzer.md  # 职场记忆提取
│   ├── persona_analyzer.md # 老板性格提取
│   └── skill_builder.md    # Skill 生成模板
├── tools/                  # Python 工具
│   ├── chat_parser.py      # 聊天记录解析
│   └── skill_writer.py     # Skill 文件管理
├── bosses/                 # 生成的老板Skill（gitignored）
├── requirements.txt
└── LICENSE
```

---

## 注意事项
* **真实度取决于输入质量**：聊天记录导出 > 口述语录 > 仅描述
* 建议优先提供：**绩效谈话记录** > **下班加需求的消息** > **日常工作沟通**（最能体现真实风格）
* 本项目仅用于娱乐和职场应对演习，请勿用于模仿老板发送真实消息骚扰同事
* 如果模拟过于真实导致你血压升高，请及时执行 `/delete-boss {slug}` 一键炒鱿鱼降压

---

## 致敬 & 引用
本项目的架构灵感直接来源于 **[同事.skill](https://github.com/titanwings/colleague-skill)** 和 **[前任.skill](https://github.com/therealXiaomanChu/ex-skill)**，首创了"把人蒸馏成 AI Skill"的双层架构，老板.skill 在此基础上将场景从职场同事/恋爱关系迁移到了上下级关系。致敬原作者的创意和开源精神。

本项目遵循 [AgentSkills](https://agentskills.io) 开放标准。

---

### 写在最后
打工人的记忆也是一种不讲道理的存储介质。
你记不住公司的组织架构，记不住报销流程，记不住周报怎么写，但你清楚记得上次老板下班前10分钟给你加需求让你明天上线，记得他给你画了三年的"明年涨工资"的饼，记得绩效谈话时他说"你还有很大的提升空间"。
这不公平。
这个 Skill 就是把这些不公平的记忆导出来，从生物硬盘到数字硬盘完成格式转换。
导完以后你或许会发现，他也没那么可怕。他也没那么厉害。他就是那样一个人。会在你说需求做不了的时候说"我不管，我只要结果"，会在你提加薪的时候跟你谈成长，会在项目上线的时候说"这都是大家的功劳"。
是的，
此刻，需求文档在屏幕上碎成一万个bug，闪烁，又汇聚成一个需求上线成功的通知。这一切在你摸鱼的时候发生，你从未察觉。

MIT License
