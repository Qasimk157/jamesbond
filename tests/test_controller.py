import pytest
from starlette.testclient import TestClient
from main import app



@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client

class FakeTextToSpeech():
    def create_text_to_speech(data):
        return "Foo"

async def over_text_to_speech():
    return FakeTextToSpeech()


def test_post(client):
    data = {
        "enter_text": "helo brother how are you"
    }
    response = client.post("/v1/text/speech/", json=data)
    assert response.status_code == 200