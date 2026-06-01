import os
import shutil
from dotenv import load_dotenv

load_dotenv()

FEISHU_APP_ID = os.environ["FEISHU_APP_ID"]
FEISHU_APP_SECRET = os.environ["FEISHU_APP_SECRET"]

CLAUDE_CLI = os.getenv("CLAUDE_CLI_PATH") or shutil.which("claude") or "claude"

DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-sonnet-4-6")
DEFAULT_CWD = os.path.expanduser(os.getenv("DEFAULT_CWD", "~"))
PERMISSION_MODE = os.getenv("PERMISSION_MODE", "bypassPermissions")

SESSIONS_DIR = os.path.expanduser("~/.feishu-claude")

# 卡片按钮回调 HTTP 端口（需 ngrok 暴露）
CALLBACK_PORT = int(os.getenv("CALLBACK_PORT", "9981"))

# 流式卡片更新：每积累多少字符推送一次
STREAM_CHUNK_SIZE = int(os.getenv("STREAM_CHUNK_SIZE", "20"))

# ── 代码问答助手专用配置 ──────────────────────────────────────

# 追加到 Claude 默认系统提示的额外指令（角色约束）
APPEND_SYSTEM_PROMPT = os.getenv("APPEND_SYSTEM_PROMPT", "")

# 禁止使用的工具（逗号分隔），如 "Write,Edit,NotebookEdit"
DISALLOWED_TOOLS = os.getenv("DISALLOWED_TOOLS", "")

# 额外允许访问的目录（逗号分隔），让 Claude 同时能看到多个仓库
ADD_DIRS = os.getenv("ADD_DIRS", "")

# 定时 git pull 更新的仓库目录（逗号分隔），留空则不自动更新
GIT_PULL_DIRS = os.getenv("GIT_PULL_DIRS", "")
# git pull 间隔（秒），默认 30 分钟
GIT_PULL_INTERVAL = int(os.getenv("GIT_PULL_INTERVAL", "1800"))
