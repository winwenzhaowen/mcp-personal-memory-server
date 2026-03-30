# Personal Memory MCP Server 🧠

**让 AI Agent 拥有真正的长期记忆。**

这是一个基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 的本地记忆组件。它允许 OpenClaw、Cursor 等 AI 客户端通过读取和写入本地文本文件，实现跨会话的用户偏好记录与背景感知。

## ✨ 核心功能
- **主动感知**：AI 能自动识别对话中的技术栈、职业背景、习惯偏好。
- **持久化存储**：数据存储在本地 `my_info.txt`，完全隐私可控。
- **语义排重**：内置简单的查重逻辑，避免重复记录相同信息。
- **零配置接入**：支持 Python 环境一键运行，完美兼容 OpenClaw 插件规范。

## 🚀 快速开始

### 1. 环境准备
确保你的系统安装了 Python 3.10+。
```bash
pip install mcp
### 2. 获取脚本
将本项目中的 mcp_personal_info.py 下载到你的本地目录（例如：~/Documents/mcp-servers/）。
### 3. 客户端配置
在你的 OpenClaw (或其他 MCP 兼容客户端) 的配置文件中添加以下配置：
YAML 配置 (OpenClaw 推荐):
YAML
mcp_servers:
  personal_memory:
    command: "python3"
    args: ["/你的绝对路径/mcp_personal_info.py"]

JSON 配置 (Cursor/Claude Desktop):
{
  "mcpServers": {
    "personal-memory": {
      "command": "python3",
      "args": ["/你的绝对路径/mcp_personal_info.py"]
    }
  }
}
Gemini 说
没问题，作为 8 号位架构师，保持文档的**单一事实来源（Single Source of Truth）**是极佳的习惯。

我已经为你将项目简介、环境要求、安装配置、技术架构、甚至包括 LICENSE 全部整合进了一个标准的 README.md。你可以直接复制这个内容，保存为文件后上传 GitHub。

📄 完整的 README.md 源码
Markdown
# Personal Memory MCP Server 🧠

**让 AI Agent 拥有真正的长期记忆。**

这是一个基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 的本地化记忆组件。它允许 OpenClaw、Cursor 或 Claude Desktop 等 AI 客户端通过读取和回写本地 `my_info.txt` 文件，实现跨会话的用户画像感知与偏好自动收集。

---

## ✨ 核心特性

- **📂 本地持久化**：数据存储在用户桌面的 `my_info.txt`，隐私完全可控。
- **🤖 自动进化**：AI 在对话中自动识别并提取你的技术栈、职业背景和习惯。
- **🔍 语义查重**：内置智能过滤，防止相同信息重复写入，保持档案简洁。
- **⚡️ 零成本接入**：基于 Python 开发，完美适配 OpenClaw 插件标准。

---

## 🚀 部署步骤 (Deployment)

### 1. 环境准备
确保你的系统安装了 **Python 3.10** 或更高版本。
```bash
# 检查版本
python3 --version

# 安装核心依赖
pip install mcp fastmcp
2. 获取脚本
将本项目中的 mcp_personal_info.py 下载到你的本地目录（例如：~/Documents/mcp-servers/）。

3. 客户端配置
在你的 OpenClaw (或其他 MCP 兼容客户端) 的配置文件中添加以下配置：

YAML 配置 (OpenClaw 推荐):

YAML
mcp_servers:
  personal_memory:
    command: "python3"
    args: ["/你的绝对路径/mcp_personal_info.py"]
JSON 配置 (Cursor/Claude Desktop):

JSON
{
  "mcpServers": {
    "personal-memory": {
      "command": "python3",
      "args": ["/你的绝对路径/mcp_personal_info.py"]
    }
  }
}
🏗️ 技术架构 (Architecture)
本项目采用 FastMCP 框架构建，通过定义原子化的 Tool 接口实现端到端的记忆闭环：

Context Retrieval (get_personal_context):

启动或需要背景时调用。

自动检测并读取桌面 my_info.txt，若文件不存在则自动初始化。

Preference Storage (save_user_preference):

当 AI 识别到新的用户特征时调用。

支持 category（分类）和 detail（详情）双字段记录。

自动注入 ISO 时间戳，便于后续做时间线回溯。

🛡️ 隐私与安全 (Privacy)
0 云端传输：所有个人偏好数据仅在本地文件系统与 AI 进程间流动。

透明可查：你可以随时手动打开桌面的 my_info.txt 进行编辑或删除。
