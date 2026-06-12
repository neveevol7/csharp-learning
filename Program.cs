using System;
using System.Collections.Generic;
using System.Linq;

namespace HelloWorld
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, C# 学习者！");
            Console.WriteLine("这是你的第一个 C# 控制台项目。");
            
            // 简短示例：`TaskItem` 类与 LINQ 查询演示
            var tasks = new List<TaskItem> {
                new TaskItem { Id = 1, Title = "买牛奶" },
                new TaskItem { Id = 2, Title = "学习 C#" },
                new TaskItem { Id = 3, Title = "提交作业", Done = true }
            };

            Console.WriteLine("任务列表：");
            foreach (var t in tasks)
            {
                Console.WriteLine($"{t.Id}: {t.Title} - {(t.Done ? "已完成" : "未完成")}");
            }

            Console.WriteLine("\n切换第 2 项状态（Toggle）...");
            tasks[1].Toggle();

            var completed = tasks.Where(t => t.Done).ToList();
            Console.WriteLine("\n已完成的任务：");
            foreach (var t in completed)
            {
                Console.WriteLine($"{t.Id}: {t.Title}");
            }
        }
    }

    class TaskItem
    {
        public int Id { get; set; }
        public string Title { get; set; } = string.Empty;
        public bool Done { get; set; }

        public void Toggle()
        {
            Done = !Done;
        }
    }
}
