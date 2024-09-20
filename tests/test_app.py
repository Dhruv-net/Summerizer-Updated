from fastapi.testclient import TestClient
from summerizer.app import app

client = TestClient(app)

def test_summarize_json():
    response = client.post("/summarize-json/", json={"data": {"name": "John Doe", "contact": {"email": "john@example.com", "phone": "1234567890"}, "skills": ["Python", "FastAPI"]}})
    assert response.status_code == 200
    assert "summary" in response.json()

def test_summarize_resume():
    resume_text = """
    John Doe
    Email: john@example.com
    Phone: 123-456-7890
    Skills: Python, FastAPI, Machine Learning
    Experience: Worked on various projects involving data science and web development.
    """
    response = client.post("/summarize-resume/", json={"text": resume_text})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) > 0  # Check if there's a summary generated
