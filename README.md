# trae_auto_sign
⭐️ TraeCN桌面版的自动签到
GitHub stars GitHub forks License Last Commit GitHub Actions

🎉 本项目实现了TraeCN桌面版的自动签到功能，通过 GitHub Actions 自动执行，领取每日签到领取积分，让用户无需手动操作！

本项目禁止传播，有缘人自会看到。给个星标再 fork 吧，求求了

🚀 功能简介
每日自动签到：定时运行脚本完成每日签到，领取积分奖励。
新增：每日两次签到尝试：分别在北京时间早上 9 点和下午 3 点左右尝试签到，增加成功率。
新增：随机延迟执行：每次签到前加入随机延迟，模拟人工操作，降低被检测风险。
GitHub Actions 托管：一键配置后，脚本每天自动运行，实现真正的“一劳永逸”。

📋 使用指南
1️⃣ Fork 项目
点击右上角的 Fork 按钮，将本项目复制到自己的 GitHub 仓库。

🛠️ 获取 登录信息
打开抓包工具,例如:Fiddle等(因为是https的接口所以需要安装证书,具体工具使用步骤可自行百度)。
找到接口 https://api.trae.cn/trae/api/v2/ug/checkin_credits/claim 的请求信息。
在请求头中找到authorization的值,可能是以Cloud-IDE-JWT开头的,去掉Cloud-IDE-JWT只要后面的

🔐 添加到 GitHub Secrets
打开 Fork 后的仓库，进入 Settings -> Secrets and variables -> Actions。
点击 Repository secrets 分区下的 New repository secret 按钮。
创建名为 TRAE_AUTH 的 Secret。
将上一步获取到的 authorization 信息粘贴到 "Secret" 输入框中并保存。

3️⃣ 启用 GitHub Actions 及设置权限
打开 Fork 后的仓库，进入 Actions 选项卡。如果看到黄色的提示条 "Workflows aren't right ....... enable them"，点击 "I understand my workflows, go ahead and enable them" 按钮启用 Actions。
重要：设置 Workflow 权限
进入仓库的 Settings -> Actions -> General 页面。
在 "Workflow permissions" 部分，选择 "Read and write permissions"。
点击 "Save" 保存。
此步骤是必需的，以便 Actions 能够执行“保持仓库活跃”（空提交）和“清理旧的工作流记录”等操作。
脚本将按预设时间（北京时间每日约 9:00 和 15:00）自动运行。
运行时间说明：默认设置在北京时间上午 9 点和下午 1 点左右运行。由于 GitHub Actions 的计划任务调度机制，实际运行时间可能会有几分钟到几十分钟的延迟，这是正常现象。随机延迟的加入也会影响确切的启动时间。
执行逻辑：脚本会先检查当天是否已成功签到。如果已签到，则跳过后续的签到操作。

⚠️ 注意事项
本项目仅供学习交流，请勿用于非法用途。
频繁手动触发可能会被目标服务限制，请谨慎操作。

📜 免责声明
本项目为开源项目，作者不对任何因使用本项目产生的后果负责。
