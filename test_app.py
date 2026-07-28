from app import app

def test_app_exists():
    assert app is not None

def test_layout_exists():
    assert app.layout is not None

def test_title():
    assert "Pink Morsel Sales Dashboard" in str(app.layout)