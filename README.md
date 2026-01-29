# Flask 任务管理系统项目

基于 Flask 框架开发的轻量级企业任务管理系统原型。本项目采用 MVC 架构设计，旨在通过模块化开发实现任务生命周期的全流程管理。

## 核心架构设计 (Architecture)

本项目严格遵循生产环境的解耦原则，将系统划分为以下层次，以便于后续向 `Java Spring Boot` 体系进行逻辑映射：

接入层 (Controller): 基于 `Flask Blueprints` 实现，处理 HTTP 请求生命周期与路由分发。

业务逻辑层 (Business Logic): 封装任务的状态流转逻辑（如：切换完成状态、逻辑删除）。

持久化层 (Persistence): 采用 ORM (Object-Relational Mapping) 技术，通过 `SQLAlchemy` 屏蔽底层数据库差异，当前适配 `SQLite`。

设计模式库 (Patterns Library): 预集成了 3-tier (三层架构) 与 Facade (外观模式) 的基准实现，为系统扩展性提供底层结构支持。

## 技术栈选型 (Tech Stack)

```
Backend: Python / Flask

Database: SQLite (SQLAlchemy ORM)

Frontend: Semantic-UI / Jinja2 Templating

Architecture: Application Factory Pattern

环境搭建与运行 (Setup & Execution): Bash (环境初始化)
```

## 创建并激活虚拟环境
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 2. 依赖安装
```
Bash
pip install Flask Flask-SQLAlchemy
```
### 3. 启动应用（自动触发数据库表结构初始化）
```
Bash
python app.py
应用将运行在 http://127.0.0.1:5000。
```

<!-- ## 模块说明 (Project Modules)
`core/`: 存放系统核心初始化代码与应用工厂函数。

`core/models.py`: 定义任务实体结构，对应关系数据库 Schema。

core/routes.py: 实现 RESTful 风格的路由接口。

patterns/: 存放结构型设计模式的标准化实现，用于提升系统架构的健壮性。 -->