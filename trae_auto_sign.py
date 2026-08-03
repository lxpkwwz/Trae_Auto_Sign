import requests
import os

# 定义请求头字典
headers = {
    'Host': 'api.trae.cn',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN',
    'authorization': 'Cloud-IDE-JWT eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoiMjg5MTAzMTUxNTc2MjcyOCIsInNvdXJjZSI6InJlZnJlc2hfdG9rZW4iLCJzb3VyY2VfaWQiOiJDMXpMMFNrNHZ3VWs3SklBM2YyRmR6ajVDVjBZYUZXRi1IcXZDSTRJeDVFPS4xOGM4MmQ1NzU5OGNlZmE1IiwidGVuYW50X2lkIjoiN28yZDg5NHA3ZHIwbzQiLCJ0eXBlIjoidXNlciJ9LCJleHAiOjE3ODY5MzY3MDUsImlhdCI6MTc4NTcyNzEwNX0.tqrVbMGYZyTRk_j-l6-ZJdB6Jnugt8RrzrJWsece0FoADhBU3khuKynRWXO1czOqKOBwhI8Rn8kPGKw5hrPvh7pPKtkrlMnEBx3jppeg02l0f2gPWsTTZMdS0CUmtHSIEcaQaxhSK2SVPWagWAiAW5R8aYqX07R1R1N3ncPV9DJ4xk898lLaXLK1aVigpX__E_L1z13s89-_Qms3YlgI4AlE5XP7C4ZJ8rnXlBcGhETguRYPSEtO_RyhDZ7vPWB3vd0BO1v20K9Eh985IVOPIsV_y6-3nys3IEhcgZ6oRS8C-J504LfrmtiPX_ZCKqc3BYC_cwXkfa8X2JG7U8dorposiTdI7Y3w7TWSGYXj89BjPzK7KAlht8e2OKQod7QYNEccJINFwowdDsJ-W-0dQAjZaFsaqrDwLy34Pr6sGv9MiqUl3H-0AsHZef14ArxLp63Car20T1b7pvKBbhA_lxvZBdVU4A--Z5ZEyJ4NIis7y3xySPY5DeG7zo5ly8ps5fU8DIm3U-xZ8kMXPTIrfGT_P8FJUCNmyihLfoqu1llMw2-HmuTs-xdrjjFKMQwcQd_zTTGF1GhF4p4OoxwrXCOKnIL_CHFsc6Sl7LQnqVVxlZqhtXBrPh9BQ6-EMcBc9JYTuR8HdRGonwFOkGh-MZezq7E8f5PsjShIV5UCutQ',
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
    'x-cloudide-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoiMjg5MTAzMTUxNTc2MjcyOCIsInNvdXJjZSI6InJlZnJlc2hfdG9rZW4iLCJzb3VyY2VfaWQiOiJDMXpMMFNrNHZ3VWs3SklBM2YyRmR6ajVDVjBZYUZXRi1IcXZDSTRJeDVFPS4xOGM4MmQ1NzU5OGNlZmE1IiwidGVuYW50X2lkIjoiN28yZDg5NHA3ZHIwbzQiLCJ0eXBlIjoidXNlciJ9LCJleHAiOjE3ODY5MzY3MDUsImlhdCI6MTc4NTcyNzEwNX0.tqrVbMGYZyTRk_j-l6-ZJdB6Jnugt8RrzrJWsece0FoADhBU3khuKynRWXO1czOqKOBwhI8Rn8kPGKw5hrPvh7pPKtkrlMnEBx3jppeg02l0f2gPWsTTZMdS0CUmtHSIEcaQaxhSK2SVPWagWAiAW5R8aYqX07R1R1N3ncPV9DJ4xk898lLaXLK1aVigpX__E_L1z13s89-_Qms3YlgI4AlE5XP7C4ZJ8rnXlBcGhETguRYPSEtO_RyhDZ7vPWB3vd0BO1v20K9Eh985IVOPIsV_y6-3nys3IEhcgZ6oRS8C-J504LfrmtiPX_ZCKqc3BYC_cwXkfa8X2JG7U8dorposiTdI7Y3w7TWSGYXj89BjPzK7KAlht8e2OKQod7QYNEccJINFwowdDsJ-W-0dQAjZaFsaqrDwLy34Pr6sGv9MiqUl3H-0AsHZef14ArxLp63Car20T1b7pvKBbhA_lxvZBdVU4A--Z5ZEyJ4NIis7y3xySPY5DeG7zo5ly8ps5fU8DIm3U-xZ8kMXPTIrfGT_P8FJUCNmyihLfoqu1llMw2-HmuTs-xdrjjFKMQwcQd_zTTGF1GhF4p4OoxwrXCOKnIL_CHFsc6Sl7LQnqVVxlZqhtXBrPh9BQ6-EMcBc9JYTuR8HdRGonwFOkGh-MZezq7E8f5PsjShIV5UCutQ'
}

session = requests.Session()
session.headers.update(headers)
# 之后所有请求自动带上这些头
response = session.post('https://api.trae.cn/trae/api/v3/GetThirdPartyToken', json={"Types": ["feishu", "lark"]})
# print(response.json())
response = session.post('https://api.trae.cn/trae/api/v2/ug/checkin_credits/claim', json={})
print(f"签到完成,结果 = {response.json()}")
