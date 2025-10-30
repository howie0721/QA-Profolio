"""
pytest 設定檔
這個檔案會自動被 pytest 讀取，用來設定測試環境
"""

import pytest
import requests


# 定義測試用的 API 基礎網址
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_client():
    """
    建立一個 API 客戶端（就像建立一個專門打電話的工具）
    scope="session" 表示整個測試過程只建立一次
    """
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    yield session
    session.close()


@pytest.fixture(scope="session")
def base_url():
    """
    提供 API 基礎網址
    """
    return BASE_URL


@pytest.fixture
def sample_post_data():
    """
    提供測試用的文章資料
    """
    return {
        "title": "測試文章標題",
        "body": "這是測試文章的內容",
        "userId": 1
    }
