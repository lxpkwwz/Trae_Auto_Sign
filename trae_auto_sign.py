import requests
import os

# ---------- 从环境变量读取敏感信息 ----------
AUTH_TOKEN = os.environ.get('TRAE_AUTH')  # 对应 GitHub Secret 中的 TRAE_AUTH
if not AUTH_TOKEN:
    raise ValueError("环境变量 TRAE_AUTH 未设置，请在 GitHub Secrets 中配置！")

# ---------- 定义请求头 ----------
headers = {
    'Host': 'api.trae.cn',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN',
    'authorization': f'Cloud-IDE-JWT {AUTH_TOKEN}',          # 动态注入
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
    'x-cloudide-token': AUTH_TOKEN,                          # 复用同一个 token
}

# ---------- 发起请求 ----------
session = requests.Session()
session.headers.update(headers)

# 第一步：获取第三方 token（可忽略返回值）
print(f"第一步: 调用获取第三方token接口(此接口不确定对签到是否有影响,先执行再说)...")
resp1 = session.post('https://api.trae.cn/trae/api/v3/GetThirdPartyToken', json={"Types": ["feishu", "lark"]})
print(f"第一步完成...")
# 第二步：签到
print(f"第二步: 准备签到...")
resp2 = session.post('https://api.trae.cn/trae/api/v2/ug/checkin_credits/claim', json={})
print(f"第二步:签到完成，结果 = {resp2.json()}")
