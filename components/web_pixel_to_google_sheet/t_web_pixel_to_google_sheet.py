
import typing
import pytest
from pydantic import BaseModel
from fastapi.testclient import TestClient
from .your_module_name import WebPixelToGoogleSheet, VisitorContactInfo, ContactAppendResult, web_pixel_to_google_sheet_app

client = TestClient(web_pixel_to_google_sheet_app)

# Replace these with your actual input and expected output values
test_cases = [
    # Test case 1
    {
        "input": {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        },
        "expected_output": {
            "status": "SUCCESS"
        }
    },
    # Test case 2
    {
        "input": {
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "phone": "0987654321"
        },
        "expected_output": {
            "status": "SUCCESS"
        }
    }
]

# Use pytest's parametrize decorator to create tests for multiple scenarios
@pytest.mark.parametrize("test_case", test_cases)
def test_web_pixel_to_google_sheet(test_case):
    # Create a VisitorContactInfo instance from the test case input
    visitor_contact_info = VisitorContactInfo(**test_case["input"])

    # Call the component's transform() method with the mocked input
    response = client.post("/transform/", json=visitor_contact_info.dict())

    # Extract the output JSON data from the FastAPI test client response
    output_data = response.json()

    # Create a ContactAppendResult instance from the output data
    contact_append_result = ContactAppendResult(**output_data)

    # Check if the response is successful
    assert response.status_code == 200

    # Assert that the output matches the expected output from the test case
    assert contact_append_result == ContactAppendResult(**test_case["expected_output"])

    # (Optional) Include error handling and edge case scenarios
    # ...
