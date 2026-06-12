# C# 10天学习之旅 - 交互式编程平台

## 🚀 功能特性

- ✅ **在线编写代码**：集成 CodeMirror 编辑器，支持 C# 语法高亮
- ✅ **实时执行**：点击"运行代码"即可在网页上看到程序输出
- ✅ **官方内容融合**：基于 Microsoft Learn 官方教程的结构化学习内容
- ✅ **Day 1-4 完整课程**：从基础到数组，循序渐进
- ✅ **交互式练习**：每个章节配有实操练习题
- ✅ **无需切换应用**：边读讲解，边写代码，边运行

## 📖 课程内容

### Day 1: 环境准备与第一个控制台程序
- 理解 C# 的基本结构
- 学习 Main() 方法和 Console.WriteLine()
- 练习：打印个人信息

### Day 2: 变量与数据类型
- 变量声明和基本数据类型（int, double, string, bool）
- 常量 const
- 类型转换（int.Parse(), Convert.ToDouble()）
- 字符串格式化 ($"...")

### Day 3: 条件语句与分支
- if/else 和 if/else if/else 语句
- switch 语句
- 比较和逻辑运算符
- 练习：分数等级判断

### Day 4: 循环与数组
- for、while、foreach 循环
- 数组的声明和使用
- 数组操作（求和、最大值、最小值）
- 练习：数组统计

## 🎯 使用方法

### 方式一：直接在浏览器打开（最简单）

```bash
# 进入项目目录
cd /Users/yu/CSharpLearning/csharp-course-web

# 使用 Python 启动简单 HTTP 服务器
python3 -m http.server 8000

# 或使用 Node.js
npx http-server
```

然后在浏览器中打开：`http://localhost:8000`

### 方式二：直接打开本地文件

```bash
# 在 macOS 中直接打开
open /Users/yu/CSharpLearning/csharp-course-web/index.html

# 或用任意浏览器打开此路径
```

## 💡 学习流程

1. **阅读左侧讲解**：理解当前章节的核心概念
2. **查看代码示例**：了解如何写出相应的代码
3. **修改编辑器代码**：根据练习题要求修改代码
4. **点击"运行代码"**：查看程序输出
5. **点击"重置"**：恢复初始代码模板
6. **切换 Day**：点击顶部 Day 按钮切换到下一章节

## 🔧 技术栈

- **前端框架**：Vue.js 3
- **代码编辑器**：CodeMirror 5
- **在线编译**：JDoodle API（免费，无需安装）
- **样式**：原生 CSS + Dracula 主题

## 📝 如何扩展（Day 5-10）

如果你想添加更多章节，按照以下步骤：

1. 编辑 `index.html` 中的 `courseDays` 对象，添加新的 Day
2. 在 `codeTemplates` 对象中添加对应的代码模板
3. 确保 `progress-btn` 循环中的 Day 数量与课程天数一致

### 示例：添加 Day 5

```javascript
5: {
    title: 'Day 5: 方法与代码复用',
    content: `<h2>📌 今天的目标</h2><p>...</p>...`
},

// 在 codeTemplates 中
5: `using System;
namespace CSharpLearning {
    // 你的 Day 5 代码...
}`
```

## ⚠️ 注意事项

- **首次加载**：编辑器初始化需要几秒钟，请耐心等待
- **网络要求**：需要互联网连接才能使用 JDoodle API 执行代码
- **API 限制**：JDoodle 免费版本有请求限制，如果频繁出错可考虑自建后端
- **跨域问题**：某些浏览器可能因为跨域限制而无法调用 API，此时可启动本地 HTTP 服务器

## 🔐 本地代理（可选，推荐用于稳定执行）

浏览器直接调用 JDoodle 可能遇到 CORS 或网络限制。推荐在本地运行一个小代理，将浏览器请求转发到 JDoodle。

1. 复制示例环境文件并填写你的 JDoodle 凭证（不要提交这些凭证）：

```bash
cd /Users/yu/CSharpLearning/csharp-course-web
cp .env.example .env
# 编辑 .env，填入 JD_CLIENT_ID 和 JD_CLIENT_SECRET
```

2. 推荐使用虚拟环境并安装依赖：

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install flask requests python-dotenv
```

3. 启动代理：

```bash
export JD_CLIENT_ID=你的_jdoodle_client_id
export JD_CLIENT_SECRET=你的_jdoodle_client_secret
export PORT=5000   # 可选
python3 proxy.py
```

4. 在另一个终端启动静态服务器并打开页面：

```bash
# 在 web 目录启动
cd /Users/yu/CSharpLearning/csharp-course-web
python3 -m http.server 8000
# 打开 http://localhost:8000
```

代理会在收到请求时将代码转发给 JDoodle 并返回结果到前端页面。若你不想配置代理，页面仍然可以通过直接网络请求 JDoodle，但可能因 CORS 或 JDoodle 限制失败。

## 🚀 后续优化建议

- [ ] 添加代码自动保存到浏览器本地存储
- [ ] 添加题目自动判题功能
- [ ] 添加进度追踪（已完成 Day 数）
- [ ] 集成 Blazor WebAssembly，在浏览器本地编译执行（无需网络）
- [ ] 添加更多进阶章节（Day 5-10）
- [ ] 实现代码版本控制和对比

## 📚 参考资源

- [Microsoft Learn C# 官方教程](https://learn.microsoft.com/zh-cn/dotnet/csharp/)
- [CodeMirror 文档](https://codemirror.net/)
- [Vue.js 3 官方文档](https://vuejs.org/)

---

**祝你学习愉快！** 🎉 有问题或建议，欢迎反馈。
