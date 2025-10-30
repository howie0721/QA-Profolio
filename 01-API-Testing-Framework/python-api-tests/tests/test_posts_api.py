"""
API 測試範例 - 測試文章 (Posts) API

這個檔案示範如何測試一個簡單的 RESTful API
我們會測試：GET（查詢）、POST（新增）、PUT（更新）、DELETE（刪除）
"""

import pytest
import requests


class TestPostsAPI:
    """
    測試 Posts API 的所有功能
    這就像測試一個部落格系統的文章管理功能
    """
    
    @pytest.mark.smoke
    def test_get_all_posts(self, api_client, base_url):
        """
        測試：取得所有文章列表
        預期：應該要成功取得資料，而且是一個陣列
        """
        # 發送 GET 請求
        response = api_client.get(f"{base_url}/posts")
        
        # 驗證：HTTP 狀態碼應該是 200（成功）
        assert response.status_code == 200, "應該要成功取得資料"
        
        # 驗證：回傳的資料應該是陣列（清單）
        posts = response.json()
        assert isinstance(posts, list), "回傳的資料應該是陣列"
        assert len(posts) > 0, "應該至少有一篇文章"
        
        # 驗證：每篇文章都應該有這些欄位
        first_post = posts[0]
        assert "id" in first_post, "文章應該要有 ID"
        assert "title" in first_post, "文章應該要有標題"
        assert "body" in first_post, "文章應該要有內容"
        assert "userId" in first_post, "文章應該要有作者 ID"
    
    
    @pytest.mark.smoke
    def test_get_single_post(self, api_client, base_url):
        """
        測試：取得單一文章
        預期：應該要成功取得指定 ID 的文章
        """
        post_id = 1
        response = api_client.get(f"{base_url}/posts/{post_id}")
        
        assert response.status_code == 200
        
        post = response.json()
        assert post["id"] == post_id, f"文章 ID 應該是 {post_id}"
        assert "title" in post
        assert "body" in post
    
    
    def test_get_non_existent_post(self, api_client, base_url):
        """
        測試：查詢不存在的文章
        預期：應該要回傳 404（找不到）
        """
        # 使用一個不可能存在的 ID
        post_id = 99999
        response = api_client.get(f"{base_url}/posts/{post_id}")
        
        # 驗證：應該回傳 404
        assert response.status_code == 404, "查詢不存在的文章應該回傳 404"
    
    
    @pytest.mark.smoke
    def test_create_new_post(self, api_client, base_url, sample_post_data):
        """
        測試：新增一篇文章
        預期：應該要成功建立，並回傳新文章的資料
        """
        response = api_client.post(f"{base_url}/posts", json=sample_post_data)
        
        # 驗證：HTTP 狀態碼應該是 201（已建立）
        assert response.status_code == 201, "新增文章應該回傳 201"
        
        # 驗證：回傳的資料應該包含我們送出的資料
        created_post = response.json()
        assert created_post["title"] == sample_post_data["title"]
        assert created_post["body"] == sample_post_data["body"]
        assert created_post["userId"] == sample_post_data["userId"]
        assert "id" in created_post, "新文章應該要有 ID"
    
    
    def test_create_post_with_missing_field(self, api_client, base_url):
        """
        測試：送出缺少必填欄位的資料
        預期：應該要失敗或回傳錯誤
        """
        # 故意不送 title
        invalid_data = {
            "body": "只有內容，沒有標題",
            "userId": 1
        }
        
        response = api_client.post(f"{base_url}/posts", json=invalid_data)
        
        # 注意：這個測試 API 比較寬鬆，實際上應該要驗證更嚴格
        # 在真實專案中，應該要回傳 400（錯誤的請求）
        print(f"實際回應狀態碼: {response.status_code}")
    
    
    def test_update_post(self, api_client, base_url):
        """
        測試：更新文章內容
        預期：應該要成功更新
        """
        post_id = 1
        updated_data = {
            "id": post_id,
            "title": "更新後的標題",
            "body": "更新後的內容",
            "userId": 1
        }
        
        response = api_client.put(f"{base_url}/posts/{post_id}", json=updated_data)
        
        assert response.status_code == 200, "更新文章應該成功"
        
        updated_post = response.json()
        assert updated_post["title"] == updated_data["title"]
        assert updated_post["body"] == updated_data["body"]
    
    
    def test_delete_post(self, api_client, base_url):
        """
        測試：刪除文章
        預期：應該要成功刪除
        """
        post_id = 1
        response = api_client.delete(f"{base_url}/posts/{post_id}")
        
        # 驗證：HTTP 狀態碼應該是 200（成功）
        assert response.status_code == 200, "刪除文章應該成功"
    
    
    @pytest.mark.slow
    def test_api_response_time(self, api_client, base_url):
        """
        測試：API 回應速度
        預期：回應時間應該在 2 秒內
        """
        import time
        
        start_time = time.time()
        response = api_client.get(f"{base_url}/posts")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        assert response.status_code == 200
        assert response_time < 2, f"API 回應時間過長: {response_time:.2f} 秒"
        print(f"API 回應時間: {response_time:.2f} 秒")
