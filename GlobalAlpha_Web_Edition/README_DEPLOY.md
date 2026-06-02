# GlobalAlpha Web Edition (Deployment Guide)

这是 **跨境出海智库 (GlobalAlpha)** 的独立网页版存档。该版本经过重构，移除了对复杂 Nginx 配置的依赖，将前后端集成在一个高效的 FastAPI 服务中，适合快速部署和存档。

## 目录结构
- `api/`: 后端核心逻辑、数据库模型及海关/合规数据集。
- `static/`: 前端网页界面及生成的调研报告存储区。
- `requirements.txt`: Python 依赖清单。
- `Dockerfile`: 容器化配置文件。

## 本地运行
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动服务：
   ```bash
   python api/main.py
   ```
3. 访问：`http://localhost:8000`

## 快速部署 (One-Click Deploy)
该目录已配置 `render.yaml`。您可以直接在 [Render.com](https://render.com) 关联此仓库，系统将自动识别配置并启动全栈服务。

## Docker 部署
1. 构建并运行：
   ```bash
   docker-compose up --build -d
   ```
2. 访问：`http://localhost` (映射至 80 端口)

## 核心特性
- **免注册使用**：移除了注册/登录环节，用户访问即可直接使用罗盘搜索、合规查询及报告生成功能。
- **一体化架构**：单个容器即可运行完整服务（含前后端）。
- **行业深度**：内置 29+ 海关品类合规数据。
- **团队协作**：支持多租户（Company ID）及团队调研报告共享。
- **商业闭环**：集成了 Stripe Webhook 支付与点数扣费逻辑（预置 999+ 公开点数）。

---
*存档日期：2026年6月2日*
