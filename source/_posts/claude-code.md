---
title: claude code
tags:
  - claude
categories: claude
typora-root-url: ../../source
date: 2025-10-07 20:07:06
---

# claude-code命令行

```
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```

通过环境变量修改成kimi的模型
```
export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
export ANTHROPIC_AUTH_TOKEN=${YOUR_MOONSHOT_API_KEY}
export ANTHROPIC_MODEL=kimi-k2-turbo-preview
export ANTHROPIC_SMALL_FAST_MODEL=kimi-k2-turbo-preview
```

或者在claude配置文件中添加环境变量
`~/.claude/settings.json`
```
{
    "env": {
        "ANTHROPIC_BASE_URL": "https://www.sophnet.com/api/open-apis/7TxazXiOf8xHVzgbxY2o6w/anthropic",
        "ANTHROPIC_AUTH_TOKEN": "${YOUR_API_KEY}",
        "ANTHROPIC_MODEL": "Kimi-K2-0905",
        "ANTHROPIC_SMALL_FAST_MODEL": "Kimi-K2-0905"
    }
}
```

添加mcp，`mcp-chrome-bridge`确实好用，就是费token

```
claude mcp add --transport http mcp-chrome-bridge http://127.0.0.1:12306/mcp
```


# claude-code的vscode插件
应用市场安装先安装一个
在设置中搜索`Claude Code: Environment Variables`，编辑`setting.json`

```
{
    ...
    "claude-code.environmentVariables": [
        { "name": "ANTHROPIC_BASE_URL", "value": "https://www.sophnet.com/api/open-apis/7TxazXiOf8xHVzgbxY2o6w/anthropic" },
        { "name": "ANTHROPIC_AUTH_TOKEN", "value": "${YOUR_API_KEY}" },
        { "name": "ANTHROPIC_MODEL", "value": "Kimi-K2-0905" },
        { "name": "ANTHROPIC_SMALL_FAST_MODEL", "value": "Kimi-K2-0905" }
    ]
}
```

vscode的ai插件真多啊，有官方copilot，有早期的cline，claude code也有了



