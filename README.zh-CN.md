# Research Poster · 计算机科学论文海报知识库

> 将学术论文转化为**可核验、可编辑、可复现、可浏览**的学术会议 Research Poster。

[English README](README.md) · [海报画廊](https://1998x-stack.github.io/Research-Poster/) · [完整 SKILL](.agents/skills/research-poster/SKILL.md) · [分类体系](catalog/taxonomy.json)

## 项目目标

Research Poster 不只是存储 PDF 的文件夹，而是一个长期演进的计算机科学论文海报仓库：**原始论文 → 证据清单 → 研究叙事 → 技术图表 → SVG/PPTX/PDF/PNG → 自动化质量检查 → GitHub Pages 画廊**。

- **科学性**：每个指标应能追溯到原论文的特定版本、章节和表格；保留重要局限，不混淆不同版本的数据。
- **设计性**：采用视觉叙事型研究海报；突出一个核心思想、一张方法架构图和少量准确的实验结果。
- **可编辑**：保留原生 PPTX、SVG 和生成脚本，而不只是一个不可修改的截图。
- **可扩展**：按学科和子领域归类，新增 `poster.json` 即自动加入画廊索引，不需要手动维护卡片。
- **跨 Agent**：标准 SKILL 支持 Codex、Claude Code、OpenCode、Pi。

## 首篇示例：Attention Is All You Need

路径：[`posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need/`](posters/artificial-intelligence/natural-language-processing/attention-is-all-you-need/)。

包含文件：`poster.svg`（可直接预览）、`poster.pptx`（可编辑）、`poster.pdf`（高清印刷）、`preview.png`（缩略图）、`make_poster.py`（源代码）、`poster.json`（元数据）、`evidence.md`（证据清单）。

原论文采用 NeurIPS 2017 正式版本；WMT14 英德 28.4 BLEU、英法 41.0 BLEU。后续 arXiv 修订中英法 41.8 BLEU 的差异必须单独标注。

## 一段 Prompt 自动制作新的论文海报

将以下内容粘贴到使用该仓库的 Agent 中：

```text
阅读 .agents/skills/research-poster/SKILL.md，完整遵守 references 中的科研
证据、可视化、排版、导出和发布规范。基于下面的论文 URL/PDF，首先验证
官方来源、版本、作者、数据集与实验数据，生成 claim/evidence ledger；
然后在 catalog/taxonomy.json 中选择正确类别，建立独立的论文目录；
设计 48×36 英寸学术会议海报，要求方法架构为视觉中心、结果清晰且有
局限性说明。输出 editable PPTX、打印 PDF、SVG 和预览 PNG；创建
poster.json、源脚本和 evidence.md；执行仓库验证和画廊构建；
只在通过检查后提交更改，不覆盖已有论文。
论文：<在这里粘贴 URL/PDF>
```

## 快速开始

```bash
git clone https://github.com/1998x-stack/Research-Poster.git
cd Research-Poster

# 先看学科和子领域
cat catalog/taxonomy.json

# 为下一篇论文创建“草稿占位目录”，不会覆盖已有文件
python scripts/new_poster.py --title "Paper Title" \
  --category artificial-intelligence \
  --subcategory natural-language-processing \
  --year 2026 --venue "Conference" \
  --authors "Author One; Author Two" \
  --url "https://example.org/paper"

# 验证内容并在本地生成画廊
python scripts/validate_catalog.py
python scripts/build_site.py --output _site
python -m http.server 8000 --directory _site
```

海报仍处于 `draft` 时不显示在公开网站。只有图形文件、引文和元数据准备完毕且 `status=published` 时才会被收录。

## 计算机科学分层分类

当前一级领域：Artificial Intelligence、Machine Learning、Algorithms & Theory、Computer Systems、Data & Information、Networks、Security & Privacy、Software Engineering、Human–Computer Interaction、Graphics & Visualization、Robotics、Interdisciplinary Computing。每个一级领域细分多个子领域，空目录保留 `.gitkeep`。

存储规范：`posters/<一级领域>/<二级领域>/<paper-slug>/`。同一论文只存一个主目录；交叉研究主题使用 `tags`，避免重复资产。

## GitHub Pages

仓库的 `.github/workflows/pages.yml` 会自动渲染源代码、生成 PDF/PPTX/缩略图、核验资产、构建网站，最后尝试部署到 Pages。首次启用仍需进入 **[Settings → Pages](https://github.com/1998x-stack/Research-Poster/settings/pages)**，在 **Build and deployment → Source** 选择 **GitHub Actions**。随后在 **Actions → Publish Research Poster gallery → Run workflow** 重新触发部署。

预期地址：<https://1998x-stack.github.io/Research-Poster/>。只有实际访问成功才代表发布完成。

## 质量门槛

主张必须有具体来源；实验数字必须匹配模型版本、数据集与基线；方法图不应遗漏关键模块；PDF 必须检查单页尺寸、可读性和文字溢出；需要保留版权说明并避免发布受限论文、用户隐私、token 和凭据。

项目代码、脚本和原创样式遵守 MIT License；原始论文的知识产权归论文作者及出版方所有。