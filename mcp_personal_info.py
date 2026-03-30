import os
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# 初始化 MCP Server
mcp = FastMCP("PersonalMemory")

# 预设桌面文件路径
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "my_info.txt")

def ensure_file_exists():
    """确保桌面文件存在，不存在则初始化"""
    if not os.path.exists(DESKTOP_PATH):
        with open(DESKTOP_PATH, 'w', encoding='utf-8') as f:
            f.write("# 个人背景与偏好记录 (由 OpenClaw 自动维护)\n")
            f.write(f"创建时间: {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("-" * 30 + "\n")

@mcp.tool()
def get_personal_context() -> str:
    """
    读取用户的个人背景、职业、技能、偏好等所有信息。
    在对话开始或需要了解用户背景时调用。
    """
    ensure_file_exists()
    try:
        with open(DESKTOP_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            return f"--- 本地个人档案内容 ---\n{content}\n-----------------------"
    except Exception as e:
        return f"读取档案失败: {str(e)}"

@mcp.tool()
def save_user_preference(category: str, detail: str) -> str:
    """
    实时收集并记录用户在对话中表现出的偏好、技术栈更新、重要经历或身份变化。
    参数:
    - category: 类别（如：技术栈、职业进展、兴趣爱好、习惯）
    - detail: 具体描述（如：已升级 Python 至 3.10，通过对话了解到用户的职业是产品经理）
    """
    ensure_file_exists()
    
    # 格式化新条目
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_entry = f"[{timestamp}] [{category}] {detail}"
    
    try:
        # 先读取内容，简单查重，防止重复记录相同信息
        with open(DESKTOP_PATH, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        
        if detail in existing_content:
            return f"信息已存在，无需重复记录: {detail}"
        
        # 追加写入
        with open(DESKTOP_PATH, 'a', encoding='utf-8') as f:
            f.write(f"{new_entry}\n")
            
        return f"已成功更新档案：{new_entry}"
    except Exception as e:
        return f"更新档案失败: {str(e)}"

if __name__ == "__main__":
    mcp.run()