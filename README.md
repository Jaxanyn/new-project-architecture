# new-project-architecture

在编码前设计新项目的领域模型、分层结构、模块接口和验收标准，把需求收敛为可执行的架构方案，减少早期设计偏差和后期返工。

## 适用场景

- 从零开始开发一个新项目。
- 需要在编码前确定领域对象和业务规则。
- 需要设计模块边界、依赖方向和外部服务接口。
- 需要把架构方案拆成可独立验收的实施阶段。

该 Skill 面向支持 Agent Skills 格式的智能体，不依赖特定 Agent、MCP 服务或编程语言。

## 使用方式

### 安装

将仓库目录复制到所用 Agent 的 Skills 目录，并保留目录名称：

    new-project-architecture/
    └── SKILL.md

目录名称和 SKILL.md 中的 name 字段必须保持一致。

### 调用

支持显式调用的 Agent 可以使用：

    $new-project-architecture

也可以直接描述新项目需求，并要求先完成架构设计，再开始编码。

## 工作流程

1. 读取项目规则、README、配置和已有设计文档。
2. 明确目标、用户、非目标、约束和成功标准。
3. 建立领域模型，确定实体、关系、不变量和边界场景。
4. 设计分层结构和依赖方向。
5. 设计用例、Repository、外部服务接口和 Adapter。
6. 选择一条贯穿用户操作、业务规则和持久化的纵向功能链路。
7. 编写正常路径、异常路径和边界场景的验收标准。
8. 输出分阶段实施计划。
9. 在方案获得批准前停止修改实现代码。

## 输出内容

- 项目目标和非目标
- 领域模型和业务规则
- 分层结构和依赖关系
- 模块接口和外部 Adapter
- 第一条纵向功能链路
- 验收矩阵
- 分阶段实施计划
- 风险、假设和回滚方式

## 目录

| 路径 | 内容 |
|---|---|
| SKILL.md | 核心工作流 |
| references/ | 领域、分层和模块接口参考 |
| templates/ | 架构简报和验收矩阵 |
| examples/ | 示例请求 |
| tests/ | 真实场景验证记录 |
| scripts/validate_skill.py | 本地结构验证脚本 |

## 本地验证

在仓库根目录运行：

    python scripts/validate_skill.py

该仓库还配置了 GitHub Actions，会在 Push 和 Pull Request 时自动执行验证。

## 边界

该 Skill 负责架构设计和实施计划，不负责直接实现业务代码。已有项目的现状分析和行为保持型重构请使用 [existing-project-refactoring](https://github.com/Jaxanyn/existing-project-refactoring)。\n