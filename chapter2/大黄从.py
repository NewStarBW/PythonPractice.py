import openai

openai.api_key = "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"  # 替换为你的 OpenAI API 密钥

account_info = openai.api_key_info()
account_name = account_info['name']

print("Account Name:", account_name)
