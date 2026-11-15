# 说透 · shuotou

笔记整理得再好，也不代表你有了自己的看法。笔记是别人理解之后的结果，不是你的。

这个仓库用来**练习**：把阅读、剧集、动漫、综艺、见闻——生活的原材料——用自己的话讲透，落到有结构的文字里。目标不是存档，而是练到：行外人记者追问时，你能有来龙去脉地回答，而不是支支吾吾想到哪说到哪。

## 和现有项目的分工

| 仓库 | 干什么 |
|------|--------|
| video-notes / drama-analysis | 把别人讲过的内容整理成可复习笔记 |
| express_system | 表达技巧课：情绪、练嘴、场景、技法 |
| **shuotou** | **看法操场**：对生活原材料形成「我的说法」 |

## 结构

```
shuotou/
├── docs/                 # GitHub Pages 根目录
│   ├── index.html        # 首页：主张 + 练习墙
│   ├── method.html       # 六段写法（强制结构）
│   ├── index.json        # 条目索引
│   ├── style.css
│   └── entries/          # 每篇练习
├── templates/entry.html  # 新条目骨架
├── scripts/generate.py   # 校验 / 排序 index.json
└── .github/workflows/    # Pages 部署
```

## 一篇练习写什么

强制六段（详见 [method.html](docs/method.html)）：

1. **原材料** — 今天碰了什么
2. **外行一问** — 记者问「这是啥」，你怎么答
3. **来龙去脉** — 背景 → 发生了什么 → 为什么值得说
4. **我的看法** — 立场，不是摘要
5. **追问预演** — 对方再问一句，你怎么接
6. **卡词备忘** — 磕巴时想不起的词，事后补上

## 本地预览

```bash
cd ~/Projects/shuotou
python3 scripts/generate.py --check
python3 -m http.server 8790 --directory docs
# 打开 http://localhost:8790
```

## 新增一篇

1. 复制 `templates/entry.html` → `docs/entries/{date}-{slug}.html`，填六段
2. 在 `docs/index.json` 顶部插入一条（字段见下）
3. 运行 `python3 scripts/generate.py --write`

`index.json` 字段：

```json
{
  "date": "2026-11-15",
  "title": "标题（你的说法，不是原作标题照搬）",
  "one_liner": "给外行人的一句话",
  "source": "原材料简述",
  "tags": ["阅读", "剧集", "动漫", "综艺", "见闻", "工作"],
  "slug": "date-slug",
  "html": "entries/date-slug.html"
}
```

## GitHub Pages

推到 GitHub 后：Settings → Pages → Source 选 GitHub Actions（本仓已含 workflow），或 `main` + `/docs`。

预期地址：`https://czh55.github.io/shuotou/`（或挂到 `chenzhiheng.cn/shuotou/`）。
