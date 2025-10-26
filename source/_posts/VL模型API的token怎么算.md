---
title: VL模型API的token怎么算
tags:
  - AIGC
categories: AIGC
typora-root-url: ../../source
date: 2025-10-26 15:09:20
---

梳理从 GPT-4.1 到 GPT-5，再到 Qwen3-VL 的核心 API 知识点，帮助你真正驾驭这些强大的工具。

### 1\. API 的第一课：Token，以及那个神秘的 `reasoning_tokens`

你的每一次 API 调用都会返回一个 `usage` 对象，理解它就是理解你账单的第一步：

```
{
    "id": "chatcmpl-xxx",
    "object": "chat.completion",
    "created": xxx,
    "model": "gpt-4.1-2025-04-14",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "xxx",
                "refusal": null,
                "annotations": []
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 11840,
        "completion_tokens": 489,
        "total_tokens": 12329,
        "prompt_tokens_details": {
            "cached_tokens": 0,
            "audio_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 0,
            "audio_tokens": 0,
            "accepted_prediction_tokens": 0,
            "rejected_prediction_tokens": 0
        }
    },
    "service_tier": "default",
    "system_fingerprint": "xxx"
}
```

  * **`prompt_tokens` (输入 Token):** 你**发送给模型**的所有内容的成本。这**不是**指你刚刚输入的那句话，而是你 `messages` 数组中的**全部内容**，包括：
    1.  系统提示 (System Prompt)
    2.  所有的历史对话 (如果你为了保持上下文而传入了)
    3.  你当前发送的所有文本
    4.  你当前发送的所有**图片**（这往往是大头！）
  * **`completion_tokens` (输出 Token):** 模型**生成并返回给**你的内容的成本。
  * **`total_tokens` (总 Token):** `prompt` + `completion`，你本次调用的总计费 Token。

**那么 `reasoning_tokens` (思考 Token) 是什么？**

在 `gpt-4.1` 调用中，这个值是 `0`。这并不代表模型“没有思考”，而是代表它的架构是一站式生成最终答案的。

这个字段是为 **GPT-5** 这样的新模型准备的。GPT-5 引入了“思考深度”机制。当它处理复杂问题时，会先“打草稿”或进行中间推理，这个过程消耗的 Token 就算作 `reasoning_tokens`。在 GPT-5 的计费中，总输出成本 = `completion_tokens` + `reasoning_tokens`。

### 2\. API 的核心原则：它是“无状态”的

这是新手最容易犯的错误：**API 调用本身不具备上下文记忆。**

你不能像在 ChatGPT 网页版那样，先问“这是什么？”，再问“它是什么颜色的？”。服务器不会“记住”你上一次的调用。

**“上下文”是你作为开发者“手动”实现的。**

你必须在你的程序中维护一个 `messages` 列表（即对话历史），并且在**每一次**新请求中，都把**完整的历史记录**再次发送给 API。

```python
# 你的程序需要自己维护这个列表
messages = [
    {"role": "system", "content": "你是一个助手。"}
]

# 第一次提问
messages.append({"role": "user", "content": "你好，GPT-4.1 的上下文窗口多大？"})
response = client.chat.completions.create(model="gpt-4.1", messages=messages)
messages.append(response.choices[0].message) # 把 AI 的回答也存入历史

# 第二次提问
messages.append({"role": "user", "content": "那 GPT-5 呢？"})
# 这一次，你发送的是包含前 3 条消息的完整列表
response = client.chat.completions.create(model="gpt-4.1", messages=messages)
# AI 现在才能理解 "那 GPT-5 呢？" 是在和上一句做对比
```

### 3\. SDK vs. 手动请求：为什么你应该用 SDK

使用 `openai` 官方库（SDK）远优于自己用 `requests` 库手搓 HTTP 请求：

  * **流式处理 (Streaming):** SDK 将复杂的 SSE (Server-Sent Events) 数据流自动转换成一个简单的 Python 生成器，你只需一个 `for` 循环就能处理。
  * **错误处理 (Error Handling):** SDK 会将 API 的错误（如 `429` 速率限制、`401` 密钥错误）自动转换成明确的 Python 异常（如 `openai.RateLimitError`），方便你用 `try...except` 捕获。
  * **类型安全 (Type Safety):** SDK 返回的是 Pydantic 对象 (如 `response.choices[0].message.content`)，而不是字典 (如 `resp_dict['choices'][0]['message']['content']`)。这能享受 IDE 自动补全，避免拼写错误。
  * **自动重试 (Auto-Retry):** SDK 内置了对瞬时错误的指数退避重试逻辑。

### 4\. 深度指南：图片如何变成 Token

这可能是多模态 API 中最复杂的部分。图片 Token **不看文件大小 (KB/MB)**，而是看**分辨率 (像素)** 和**你的设置**。

#### A. OpenAI 的可变成本 (GPT-4.1 / 4o / 5)

通过 `detail` 参数控制成本：

```
  "image_url": {
      "url": f"data:image/jpeg;base64,{base64_image}",
      "detail": "low"
  }
```

  * **`detail: "low"` (低细节模式)**
  

      * **成本：** 固定的 85 Token。
      * **原理：** 无论图片多大，API 都会将其强制缩放到 512x512 像素再分析。
      * **适用：** 识别主要物体、场景（“这是一只猫”）。

  * **`detail: "high"` (高细节模式)**

      * **成本：** 可变，`85 + (170 * N)` 个 Token，`N` 是“瓦片”数量。
      * **原理：**
        1.  API 先将图片缩放，使其最长边不超过 2048px (或放大到 512x512)。
        2.  然后用 512x512 的“瓦片”去切割这张缩放后的图片。
        3.  一张 1024x1800 的图片可能会被切成 2x3=6 个瓦片，成本就是 `85 + (170 * 6) = 1105` Token。
      * **适用：** 识别图表文字、精细细节。

#### B. 终极技巧：如何处理超长图片（如网页截图）

如果你有一张 `1200 x 9000` 像素的长图，直接用 `detail: "high"` 发送会**导致失败**。API 会将其压缩成 `246 x 2048` 像素，所有细节都会丢失。

**正确的方法是“客户端手动切片”：**

1.  **在你的程序里**，将 `1200 x 9000` 的长图切割成 8 张图（7 张 `1200x1200` + 1 张 `1200x600`）。
2.  在**同一次 API 调用**中，按顺序传入这 8 张图片切片。
3.  在**文本提示**中明确告知 AI：`"我提供了一张长图，已按顺序切成8片，请你按顺序分析..."`。

#### C. URL vs. Base64：如何传入图片

API 两种都支持：

| 方式 | 优点 | 缺点 |
| :--- | :--- | :--- |
| **URL 链接** | 简单，API 请求体小 | 图片必须是**公网可访问**的 |
| **Base64 编码** | **可以处理本地/私有图片** | 请求体变大 (数据膨胀约33%) |

**Base64 格式：** `url` 字段必须是 `data:[MIME_TYPE];base64,[你的Base64字符串]`

### 5\. 高级策略：如何区分不同角色的图片

假设你有一批“商品介绍图”（用来理解）和一批“备选缩略图”（用来选择）。你不能把它们混在一起丢给 AI。

  * **方法一 (最可靠)：两次 API 调用**

    1.  **调用 1：** 只发送“介绍图”，Prompt 是“请详细总结这个商品”。
    2.  拿到总结 `summary`。
    3.  **调用 2：** 发送 `summary` 文本 + “备选缩略图”，Prompt 是“根据这份总结，请在以下图片中选出最好的缩略图”。

  * **方法二 (最高效)：单次调用 + 文本图片交错**
    利用 `messages` 数组可以混合 `text` 和 `image` 的特性，为图片“打标签”：

    ```json
    "content": [
      {"type": "text", "text": "--- 第一部分：商品介绍图 (用于理解) ---"},
      {"type": "image_url", "image_url": {"url": "..."}},
      {"type": "image_url", "image_url": {"url": "..."}},
      
      {"type": "text", "text": "--- 第二部分：备选缩略图 (用于选择) ---"},
      {"type": "text", "text": "【备选缩略图 1】:"},
      {"type": "image_url", "image_url": {"url": "..."}},
      {"type": "text", "text": "【备选缩略图 2】:"},
      {"type": "image_url", "image_url": {"url": "..."}},
      
      {"type": "text", "text": "--- 最终任务 --- \n 请根据第一部分的信息，从第二部分选择..."}
    ]
    ```

### 6\. 模型对比：GPT vs. Qwen

最后，不同的模型家族有截然不同的特性：

| 特性 | GPT-4.1 | GPT-5 | Qwen3-VL-30B |
| :--- | :--- | :--- | :--- |
| **最大上下文** | **1,000,000** (1M) | **400,000** (400K) | **262,144** (256K) |
| **思考机制** | 一站式生成 | **Reasoning 机制** (自动/手动调节) | 一站式生成 |
| **模型家族** | 单一模型 | **家族** (Pro, Standard, Mini, Nano) | **家族** (Instruct, Thinking 等) |
| **图片计费** | **可变** (Low: 85, High: 1000+) | **可变** (类似 4.1，但成本更低) | **固定** (约 **1,224** Token/每张) |
| **图片限制** | 总 Token 限制 | 总 Token 限制 | 总 Token + **50 张图片**数量限制 |

**核心差异：** OpenAI 的 `detail: "high"` 允许你通过消耗更多 Token 来获取超高图片细节，而 Qwen3-VL 采取了**固定 1224 Token** 的策略，这让成本非常可预测，但代价是（在 API 层面）无法对单张图片投入更多 Token 去“看清”微小细节。