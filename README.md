# Huawei Cup 23 Math Modeling

面向“华为杯”第二十三届中国研究生数学建模竞赛的 Codex 技能插件。它提供从官方规则核验、赛题拆解、可复现计算、论文写作与版式检查，到 AI 使用披露、PDF 和 MD5 提交审计的完整工作流。

## 安全边界

- 学校、队伍编号、成员姓名和联系方式默认只保存在本地，并在分析阶段使用占位符。
- 插件不会自动上传论文、附件或队伍信息。
- 所有数值结论必须来自真实运行且可追溯的计算产物。
- 竞赛官网及当届官方附件优先于插件内的日期化规则摘要。

## 安装

将本仓库添加为 Codex 插件市场：

```text
codex plugin marketplace add 2145602879/huawei-cup-23-math-modeling
```

重启 ChatGPT 桌面应用或 Codex，然后在插件目录中安装 **Huawei Cup 23 Math Modeling**。

## 使用

```text
使用 $huawei-cup-23-math-modeling 的 full-run 模式。
赛题与官方附件位于本地 <problem_files> 目录。
先建立规则矩阵，再进行建模、真实计算、验证、论文写作、AI 披露和提交审计。
队伍信息保持本地并使用占位符；不要上传任何文件；冻结最终 PDF 和 MD5 前先请求确认。
```

支持 `full-run`、`analysis`、`compute`、`paper`、`audit` 和 `submission` 模式。

## 重要说明

本项目不是自动获奖或自动答题工具。参赛队仍需独立理解问题、确认模型与推导、核验数据和结果，并遵守当届竞赛纪律及 AI 工具使用规定。

## 版本

首个公开版本：`v1.0.0`。

