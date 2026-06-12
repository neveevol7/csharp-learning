# C# 快速上手学习平台 (PM 转型版)

这是一个专门为你设计的 C# 学习平台，界面参考 Microsoft Learn 风格，内容针对产品经理转开发的需求进行了深度定制。

## 目录结构

- `Documents/CSharpLearning/` — 你的主练习目录
- `csharp-course-web/` — 交互式学习平台前端与代理

## 如何启动 (快速启动)

由于平台需要通过 JDoodle API 运行代码，你需要启动一个本地代理服务器。

1. **打开终端**，进入项目目录：
   ```bash
   cd ~/Documents/CSharpLearning/csharp-course-web
   ```

2. **启动代理服务器**：
   ```bash
   python3 proxy.py
   ```
   *（如果提示端口占用，可以在 .env 中修改 PORT）*

3. **在浏览器中打开**：
   直接双击打开 `index.html`，或者使用简单的 HTTP 服务：
   ```bash
   python3 -m http.server 8000
   ```
   然后在浏览器访问 `http://localhost:8000`

## 10 天学习计划

1. **Day 1**: Hello World & 基础语法
2. **Day 2**: 变量与基本数据类型
3. **Day 3**: 控制流：If 与 Switch
4. **Day 4**: 循环与数组
5. **Day 5**: 方法与逻辑封装
6. **Day 6**: 类与对象 (OOP 基础)
7. **Day 8**: 集合与 LINQ
8. **Day 10**: 异步编程 (Async/Await)

---
*祝你在 C# 的世界里玩得愉快！有任何问题随时问我。*
