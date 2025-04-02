import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from myApp import app
def test_hello_world():
    client = app.test_client()  
    response = client.get('/')  
    assert response.data == b'Hello, World!'  
