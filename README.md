# ⭐️ Trae_Auto_Sign

🎉 **TraeCN 桌面版自动签到**  
通过 GitHub Actions 定时执行，每日自动领取签到积分，让你彻底解放双手！

> ⚠️ **本项目禁止传播，有缘人自会看到。给个星标再 fork 吧，求求了 🙏**

---

## 🚀 功能简介

- ✅ **每日自动签到**：定时运行脚本，自动完成每日签到，领取积分奖励。
- ⏰ **每日两次签到尝试**：分别在北京时间 **早上 9 点** 和 **下午 3 点** 左右执行，增加成功率。
- 🎲 **随机延迟执行**：每次签到前加入随机延迟（模拟人工操作），有效降低被检测风险。
- ☁️ **GitHub Actions 托管**：一键配置，脚本每日自动运行，实现真正的“一劳永逸”。

---

## 📋 使用指南

### 1️⃣ Fork 本项目
点击右上角的 **Fork** 按钮，将本仓库复制到你的 GitHub 账户下。

---

### 2️⃣ 获取登录凭证（Token）

1. 打开抓包工具（如 **Fiddler** 等，由于是 HTTPS 接口，需安装证书，具体步骤请自行搜索）。
2. 定位到接口：  
   `https://api.trae.cn/trae/api/v2/ug/checkin_credits/claim`
3. 在请求头（Headers）中找到 `authorization` 字段，其值类似 `Cloud-IDE-JWT <一串JWT>`。
4. **复制 JWT 部分**（去掉 `Cloud-IDE-JWT ` 前缀，只保留后面的 JWT 字符串）。

---

### 3️⃣ 将 Token 添加到 GitHub Secrets

1. 进入你 Fork 后的仓库 → **Settings** → **Secrets and variables** → **Actions**。
2. 点击 **Repository secrets** 分区下的 **New repository secret** 按钮。
3. 名称填写 `TRAE_AUTH`，值粘贴上一步获取的 JWT 字符串。
4. 点击 **Add secret** 保存。

---

### 4️⃣ 启用 GitHub Actions 并设置权限

1. 进入你 Fork 后的仓库 → **Actions** 选项卡。
2. 若看到黄色提示条 “Workflows aren't right ... enable them”，点击 **“I understand my workflows, go ahead and enable them”** 启用 Actions。
3. **设置 Workflow 权限**（重要！）：
   - 进入仓库 **Settings** → **Actions** → **General**。
   - 在 **Workflow permissions** 部分，选择 **Read and write permissions**。
   - 点击 **Save** 保存。

> 💡 此权限是必需的，以便 Actions 能够执行“保持仓库活跃”（空提交）或“清理旧工作流记录”等操作（如需要）。

---

### ⏱️ 自动运行时间说明

- 默认配置为北京时间 **每日 09:00** 和 **15:00** 左右运行。
- 由于 GitHub Actions 的调度机制，实际执行时间可能会有几分钟到几十分钟的延迟，属正常现象。
- 随机延迟的加入也会影响确切启动时间。

---

## ⚠️ 注意事项

- 本项目仅供学习交流，**请勿用于非法用途**。
- 频繁手动触发可能被目标服务限制，请按默认配置使用。

---

## 📜 免责声明

本项目为开源项目，作者不对任何因使用本项目而产生的后果负责。使用即代表您已阅读并同意本声明。

---

> 如果你觉得这个项目对你有帮助，请给个 **Star** 支持一下，谢谢！ 😊
