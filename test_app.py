import pytest
from flask import Flask, session

# Import the Flask app (assuming the app is in the same directory)
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login' in response.data


def test_select_role_route(client):
    with client.session_transaction() as sess:
        sess['user'] = 'test@example.com'

    response = client.get('/select_role')
    assert response.status_code == 200
    assert b'Select Role' in response.data


def test_student_page_route(client):
    with client.session_transaction() as sess:
        sess['user'] = 'test@example.com'

    response = client.get('/student_page')
    assert response.status_code == 200
    assert b'action1' in response.data