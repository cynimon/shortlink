from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)


def test_link_creation(create_long_link):
    response = client.post(
        url="/shortlink/",
        content=create_long_link
    )

    assert response.status_code == 201

    response = client.post(
        url="/shortlink/",
        content=create_long_link
    )

    assert response.status_code == 409


def test_long_link_getting_200(get_any_short_link):
    response = client.get("/shortlink/?short_url=" + get_any_short_link)

    assert response.status_code == 200


def test_long_link_getting_404(get_any_short_link_fake):
    response = client.get("/shortlink/?short_url=" + get_any_short_link_fake)

    assert response.status_code == 404


def test_link_delete(get_any_short_link):
    response = client.delete(
        url="/shortlink/?short_url=" + get_any_short_link
    )

    assert response.status_code == 204

    response = client.get(
        url="/shortlink/?short_url=" + get_any_short_link
    )
    assert response.status_code == 404
