def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Smart File Organizer Pro API"}

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_list_files_empty(client):
    response = client.get("/files")
    assert response.status_code == 200
    assert response.json() == {"files": []}
