iCloud 本地测试项目
这是一个用于测试 iCloud 同步 与 XAMPP 本地环境 兼容性的临时测试文件夹。

📌 项目信息
本地访问地址: http://localhost/iCloud测试/

创建日期: 2026-09-08

主要目的: 测试文件在 iCloud 云端同步时，是否会导致 XAMPP 本地运行或 Git 版本控制出现冲突。

📝 测试记录
[x] 基础环境搭建与页面访问测试

[ ] iCloud 同步延迟对本地热更新的影响测试

[ ] 大文件或多文件并发同步测试

⚙️ 注意事项
如果将此目录迁移到其他电脑或重新安装系统，请注意检查 XAMPP 的 Apache 根目录权限以及 iCloud 的本地文件占位符状态（确保文件已完全下载到本地）。
# BOON969 - Secure API Login Script

本项目是一个现代 API 接口登录的模拟脚本，支持动态签名（Signature）、时间戳防重放及会话保持（Session）。

## 🛠️ 依赖环境安装

本项目基于 Python 3，核心依赖 `requests` 库。

安装依赖：
```bash
pip install -r requirements.txt
