from api.api_client import ApiClient


def test_create_post_and_verify_response():
    api = ApiClient()

    post = api.create_post(
        title="Appium test",
        body="Created from pytest",
        user_id=1
    )

    print("Created post:", post)

    assert post["title"] == "Appium test"
    assert post["body"] == "Created from pytest"
    assert post["userId"] == 1