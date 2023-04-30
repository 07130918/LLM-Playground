import json
import os

import openai

from config import PROMPT

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def lambda_handler(event, context):
    """gpt-3.5-turboからアイデアをもらう

    Note:
        1リクエスト約1円($0.002/1K tokens * 4 * 130)、分間3リクエストまで
        https://openai.com/pricing
        1リクエストで使えるトークンの最大値は4,096
        https://platform.openai.com/docs/models/gpt-3-5
    """
    try:
        headers = event["headers"]
        openai.api_key = headers.get("x-api-key", OPENAI_API_KEY)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": PROMPT}],
        )

        answer = response["choices"][0]["message"]["content"]  # type: ignore
        print({"返答": answer, "使用トークン: ": response["usage"]["total_tokens"]})  # type: ignore
        return json.dumps(answer, ensure_ascii=False)
    except Exception as e:
        return json.dumps(f"リクエストが拒否されました。{e}", ensure_ascii=False)
