import os
from IMS import create_app

def test_index_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set testing configuration before creating app object
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using app
    with flask_app.test_client() as test_client:
        # Create response
        response = test_client.get('/')

        # Check that the response is correct
        assert response.status_code ==  302
        assert b"Login" in response.data
        assert b"Employee ID" in response.data
        assert b"Sign In" in response.data
