from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)


def test_link_creation(create_long_link):
    response = client.post(
        url="/",
        content=create_long_link
    )

    assert response.status_code == 201


def test_long_link_getting_200(get_any_short_link):
    response = client.get("/" + get_any_short_link)

    assert response.status_code == 200


def test_long_link_getting_404(get_any_short_link_fake):
    response = client.get("/" + get_any_short_link_fake)

    assert response.status_code == 404


def test_link_delete(get_any_short_link):
    response = client.delete(
        url="/" + get_any_short_link
    )

    assert response.status_code == 204

    response = client.get(
        url="/" + get_any_short_link
    )
    assert response.status_code == 404
