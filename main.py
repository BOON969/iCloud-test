import time
import hmac
import hashlib
import json
import requests

class SecureAPIClient:
    def __init__(self, base_url, api_key, api_secret):
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret.encode('utf-8')
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15",
            "Content-Type": "application/json"
        })

    def _generate_signature(self, timestamp: str, body_str: str) -> str:
        payload = f"{self.api_key}{timestamp}{body_str}"
        signature = hmac.new(
            self.api_secret, 
            payload.encode('utf-8'), 
            hashlib.sha256
        ).hexdigest()
        return signature

    def login(self, username, password):
        endpoint = "/api/v1/auth/login"
        url = self.base_url + endpoint
        
        raw_data = {
            "username": username,
            "password": password,
            "device_id": "iOS_UUID_Mock_12345"
        }
        body_str = json.dumps(raw_data, separators=(',', ':'))
        
        timestamp = str(int(time.time()))
        signature = self._generate_signature(timestamp, body_str)
        
        headers = {
            "X-API-Key": self.api_key,
            "X-Timestamp": timestamp,
            "X-Sign": signature
        }
        
        try:
            response = self.session.post(url, data=body_str, headers=headers, timeout=10)
            if response.status_code == 200:
                res_json = response.json()
                print("[+] 登录请求成功！")
                return res_json
            else:
                print(f"[-] 登录失败，状态码: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"[-] 网络异常: {e}")
            return None

if __name__ == "__main__":
    print("API Security Client Script Initialized.")
