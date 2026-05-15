import requests

class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def create_post(self, title, body, user_id):
        response = requests.post(
            f"{self.BASE_URL}/posts",
            json={
                "title": title,
                "body": body,
                "userId": user_id,
            },
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    def get_post(self, post_id):
        response = requests.get(
            f"{self.BASE_URL}/posts/{post_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()