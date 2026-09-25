# new-project-architecture

在编码前把新项目从模糊需求收敛为清晰、可验证的架构，明确领域模型、分层依赖、模块接口和验收标准，减少早期设计错误与后期返工。

该通用 Agent Skill 适用于支持 Agent Skills 格式的智能体。它帮助你在实现前理清领域模型、架构层次、模块接口、依赖方向和验收场景。

## 使用

安装说明见 INSTALL.md。运行本地验证：

    python scripts/validate_skill.py

调用 Skill 后，先完成架构计划并等待批准，再开始编码。

## 目录

- SKILL.md: 核心工作流
- references/: 按需加载的设计参考
- templates/: 架构简报和验收矩阵
- examples/: 示例请求
- tests/: 真实场景验证记录
