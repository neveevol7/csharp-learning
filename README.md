# C# Learning — Interactive Web Course

这是你的 C# 学习仓库，包含一个交互式的 Web 学习平台（Day 1-4 MVP）。

- Web 学习目录：`csharp-course-web/`（打开此目录中的 `README.md` 查看使用说明与代理启动步骤）
- 本仓库已包含：
  - `csharp-course-web/index.html` — 教学页面（Vue + CodeMirror）
  - `csharp-course-web/proxy.py` — 本地代理用于转发 JDoodle API（避免 CORS）
  - `.gitignore` — 忽略构建产物和虚拟环境

如何本地运行（快速）：

```bash
# 1. 启动静态服务器
cd csharp-course-web
python3 -m http.server 8000
# 打开 http://localhost:8000

# 2. （可选）启动代理以便稳定执行（见 csharp-course-web/README.md）
```

更多信息请参见：`csharp-course-web/README.md`。
