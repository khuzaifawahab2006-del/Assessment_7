
from app import run_exam_system

def test_exam_system():
    # Verify that the system initializes properly
    assert run_exam_system() is True
