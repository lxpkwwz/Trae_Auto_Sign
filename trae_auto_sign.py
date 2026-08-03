import requests
import os
import time
import random

# ---------- 从环境变量读取敏感信息 ----------
AUTH_TOKEN = os.environ.get('TRAE_AUTH')
if not AUTH_TOKEN:
    raise ValueError("环境变量 TRAE_AUTH 未设置，请在 GitHub Secrets 中配置！")

# ---------- 随机延迟（0 ~ 5 分钟） ----------
delay_seconds = random.randint(0, 300)
print(f"⏳ 随机延迟 {delay_seconds} 秒后开始签到...")
time.sleep(delay_seconds)

# ---------- 定义请求头 ----------
headers = {
    'Host': 'api.trae.cn',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN',
    'authorization': f'Cloud-IDE-JWT {AUTH_TOKEN}',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'none',
    'user-agent': 'VSCode 1.107.1 (TRAE SOLO CN)',
    'vscode-sessionid': 'd95f29a878290c3c0d7720b1da65a054af39b6bb0b4dd07477b19327c074ba3b',
    'x-market-client-id': 'VSCode 1.107.1',
    'x-market-user-id': '7ab0d2ad-c72e-42cb-85f2-8b78cf546624',
    'x-user-region': 'CN',
    'content-type': 'application/json',
    'x-device-id': '1452892708975145',
    'x-lgw-req-sdk-type': '3',
    'package-type': 'stable_cn',
    'x-request-id': '0f90fbb6-bae5-47f4-b0c2-b1e25b3b6a88',
    'x-lscbd-aid': '787976',
    'x-lscbd-platform': 'windows',
    'app-version': '0.1.43',
    'x-cloudide-token': AUTH_TOKEN,
}

# ---------- 发起请求 ----------
session = requests.Session()
session.headers.update(headers)

print("📡 第一步：获取第三方 token（预热）...")
resp1 = session.post('https://api.trae.cn/trae/api/v3/GetThirdPartyToken', json={"Types": ["feishu", "lark"]})
# 忽略返回值

print("✅ 第二步：执行签到...")
resp2 = session.post('https://api.trae.cn/trae/api/v2/ug/checkin_credits/claim', json={})
print(f"🎯 签到完成，结果 = {resp2.json()}")
