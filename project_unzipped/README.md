# 跨境出海智库 (Cross-border Export Intelligence App)

## 项目简介
本项目是一个为中国商家量身定制的跨境服务 APP，旨在解决出海过程中的情报获取、合规查询及选品决策难题。

### 核心功能
1. **全球 80% 消费地图罗盘**：通过算法自动识别利润市场、规模市场与蓝海市场。
2. **跨境智库**：深度国别报告、行业趋势及风险预警。
3. **合规百科**：基于品类的全球准入红线与转型锦囊（已集成建材、电子、母婴等行业）。
4. **AI 趋势选品**：聚合 Amazon、TikTok 等多平台数据，提供 AI 驱动的选品策略。
5. **实时金融看板**：对接真实 API，实时监控伦敦金及主流货币汇率。
6. **PDF 报告导出**：一键生成专业的商业出海白皮书（PDF 格式）。
7. **数据持久化**：使用 SQLite 存储用户信息、收藏夹与历史记录。

---

## 项目架构
- `backend/`: 基于 Python FastAPI 的核心 API 服务。
- `frontend/`: 基于 Tailwind CSS 的 Web 端数据看板。
- `mobile/`: 基于 Flutter 的 iOS/Android 移动端应用框架。
- `data/`: 结构化的行业合规与宏观经济数据库。

---

## 快速启动

### 后端 API
```bash
cd backend/app
pip install fastapi uvicorn pydantic requests
uvicorn main:app --reload
```

### 前端 Web
直接在浏览器中打开 `frontend/index.html` 即可查看。

### 移动端 App
```bash
cd mobile
flutter pub get
flutter run
```

---

## 后续规划
- 接入更多行业的合规数据（电子、服装等）。
- 实现真实的 PDF 商业报告渲染引擎。
- 增加用户收藏夹与个人出海足迹。
