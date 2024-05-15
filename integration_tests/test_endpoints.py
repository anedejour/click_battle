import pytest
from uuid import uuid4
from starlette.testclient import TestClient
from click_battle.app import create_app


@pytest.fixture
def app():
    id = str(uuid4())
    return create_app(prefix=f"test_{id}")


@pytest.fixture
def client(app):
    return TestClient(app)


def test_main_page(client):
    response = client.get("/")
    assert b"<p>0:0</p>" in response.content


def test_click_left(client):
    response = client.get("/")
    assert b"<p>0:0</p>" in response.content

    response = client.post("/score_left")
    assert b"<p>1:0</p>" in response.content


def test_click_right(client):
    response = client.get("/")
    assert b"<p>0:0</p>" in response.content

    response = client.post("/score_right")
    assert b"<p>0:1</p>" in response.content
