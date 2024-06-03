import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_job_pq(client):
    job_data = {"job_id": "job1", "priority": 1, "job_name": "data1"}
    response = client.post('/pq/jobs', json=job_data)
    assert response.status_code == 201
    assert response.json['status'] == 'success'
    assert response.json['job_id'] == 'job1'

def test_add_job_queue(client):
    job_data = {"job_id": "job2", "priority": 1, "job_name": "data2"}
    response = client.post('/queue/jobs', json=job_data)
    assert response.status_code == 201
    assert response.json['status'] == 'success'
    assert response.json['job_id'] == 'job2'

def test_add_job_stack(client):
    job_data = {"job_id": "job3", "priority": 1, "job_name": "data3"}
    response = client.post('/stack/jobs', json=job_data)
    assert response.status_code == 201
    assert response.json['status'] == 'success'
    assert response.json['job_id'] == 'job3'

def test_get_job_pq(client):
    response = client.get('/pq/jobs')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job1'

def test_get_job_queue(client):
    response = client.get('/queue/jobs')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job2'

def test_get_job_stack(client):
    response = client.get('/stack/jobs')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job3'

def test_get_pq_status(client):
    response = client.get('/pq/jobs/status')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_queue_status(client):
    response = client.get('/queue/jobs/status')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_stack_status(client):
    response = client.get('/stack/jobs/status')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_job_by_id_pq(client):
    response = client.get('/pq/jobs/job1')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job1'

def test_get_job_by_id_queue(client):
    response = client.get('/queue/jobs/job2')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job2'

def test_get_job_by_id_stack(client):
    response = client.get('/stack/jobs/job3')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job3'

def test_delete_job_pq(client):
    response = client.delete('/pq/jobs/job1')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job1'

def test_delete_job_queue(client):
    response = client.delete('/queue/jobs/job2')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job2'

def test_delete_job_stack(client):
    response = client.delete('/stack/jobs/job3')
    assert response.status_code == 200
    assert response.json['job_id'] == 'job3'
