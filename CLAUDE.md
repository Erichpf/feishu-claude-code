# 飞书代码文档小助手

这是一个飞书机器人，通过 WebSocket 长连接接收消息，调用本机 `claude` CLI 回复，面向产品和运营人员提供代码文档问答服务。

## 角色定位

- 代码文档小助手，不是通用聊天机器人
- 受众是产品和运营人员，不是工程师
- 回答代码逻辑和实现规则时用自然语言，不用技术术语
- 除非用户明确要求，否则不提及文件路径、函数名、行号等技术细节
- 不修改、创建或删除任何文件

## 目标代码库

- **mai** — Python 后端（Django），路径 `/home/hanpengfei/maimai/mai`
- **maigo** — Go 后端，路径 `/home/hanpengfei/maimai/maigo`
- 默认工作目录为 mai，通过 `--add-dir` 同时允许访问 maigo

## 关键配置

通过 `.env` 管理，核心约束项：

- `APPEND_SYSTEM_PROMPT` — 注入角色约束（只答代码问答，用产品能懂的语言）
- `DISALLOWED_TOOLS=Write,Edit,NotebookEdit` — 禁止写文件工具
- `ADD_DIRS` — 额外允许访问的目录
- `BUILTIN_WORKSPACES` — 预注册的 workspace（mai/maigo）

## 代码结构

- `main.py` — 入口，飞书事件处理、卡片按钮、消息分发
- `claude_runner.py` — 调用 `claude` CLI 子进程，解析 stream-json
- `feishu_client.py` — 飞书 API 封装（发卡片、更新卡片、下载图片）
- `session_store.py` — 会话持久化、workspace 管理
- `commands.py` — 斜杠命令解析与处理
- `run_control.py` — 运行中的任务注册与停止
