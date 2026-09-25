# new-project-architecture

面向通用 AI Agent 的新项目架构设计 Skill。它要求 Agent 在写代码前先澄清目标、建立领域模型、划分模块边界并制定验收标准，把一次性想法转成可执行、可验证的架构方案，减少早期设计偏差和后期返工。

## 解决什么问题

AI Agent 擅长快速生成代码，但在项目刚开始时容易直接进入实现，导致：

- 领域规则没有明确归属。
- 模块边界和依赖方向反复变化。
- 外部服务、数据访问与业务逻辑相互耦合。
- 方案缺少验收标准，后续难以判断是否完成。

这个 Skill 为新项目提供一条固定工作流：需求澄清 → 领域建模 → 架构设计 → 纵向切片 → 验收定义 → 分阶段计划。它只加载与当前任务相关的参考资料，适合在具体项目或功能上显式调用。

## 适用场景

- 从零开始开发一个应用、服务、库或工具。
- 在编码前确定领域对象、业务规则和模块职责。
- 设计分层结构、依赖方向、Repository、外部服务接口和 Adapter。
- 把大功能拆成可以独立实现、验证和回滚的阶段。
- 希望多个不同 Agent 使用同一套架构决策流程。

该 Skill 遵循通用 Agent Skills 格式，不依赖特定 Agent、MCP 服务、编程语言或框架。

## 快速开始

### 安装

将仓库目录复制到目标 Agent 支持的 Skills 目录，并保留 SKILL.md：

~~~text
new-project-architecture/
└── SKILL.md
~~~

目录名称和 SKILL.md 的 name 字段应保持一致。不同 Agent 的发现路径请参阅其官方文档；本仓库提供的内容是纯 Markdown、模板和验证脚本。

### 调用

支持显式 Skill 调用的 Agent 可以使用：

~~~text
$new-project-architecture
~~~

也可以使用自然语言：

~~~text
使用 new-project-architecture。请先完成需求澄清、领域建模和架构方案，
在我确认前不要修改业务实现代码。
~~~

## 工作方式

1. 读取项目规则、README、配置和已有设计文档。
2. 明确目标、用户、非目标、约束和成功标准。
3. 建立领域模型，确定实体、关系、不变量和边界场景。
4. 设计分层结构、模块职责和依赖方向。
5. 定义用例、Repository、外部服务接口和 Adapter。
6. 选择一条贯穿用户操作、业务规则和持久化的纵向功能链路。
7. 编写正常路径、异常路径和边界场景的验收标准。
8. 输出分阶段实施计划、风险、假设和停止条件。
9. 在方案获得确认前停止修改实现代码。

## 典型输出

- 项目目标、非目标和约束。
- 领域模型、业务规则和术语。
- 分层结构、模块职责和依赖关系。
- 用例接口、Repository 和外部 Adapter。
- 第一条纵向功能链路。
- 验收矩阵和验证命令。
- 分阶段实施计划、风险、假设和回滚方式。

## 示例请求

~~~text
使用 new-project-architecture 设计一个个人旅行规划应用。
先询问目标用户、核心场景、数据边界和非目标，再建立领域模型，
设计模块接口和第一条纵向功能链路，最后给出验收矩阵与分阶段计划。
在方案确认前不要写实现代码。
~~~

## 仓库内容

| 路径 | 内容 |
|---|---|
| SKILL.md | 核心触发条件和工作流 |
| references/ | 领域建模、分层和模块接口参考 |
| templates/ | 架构简报和验收矩阵模板 |
| examples/ | 可直接改写的示例请求 |
| tests/ | 真实场景验证记录 |
| scripts/validate_skill.py | 本地结构验证脚本 |

## 本地验证

在仓库根目录运行：

~~~bash
python scripts/validate_skill.py
~~~

还可以运行通用 Skill 格式检查：

~~~bash
python <skill-creator>/scripts/quick_validate.py .
~~~

GitHub Actions 会在 Push 和 Pull Request 时自动执行仓库验证。

## 边界

该 Skill 负责新项目的架构设计和实施计划，不默认直接实现业务代码。已有项目的现状分析和行为保持型重构请使用 [existing-project-refactoring](https://github.com/Jaxanyn/existing-project-refactoring)。

## 许可

MIT
