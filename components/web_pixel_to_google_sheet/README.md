markdown
# Component Name
WebPixelToGoogleSheet

# Description
This component serves as a bridge between a Web Pixel tracking system and Google Sheets by appending received visitor contact information to a specified Google Sheets document. It receives contact information in a specific format, processes it, and makes an API call to Google Sheets to save the data.

# Input and Output Models
## Input Model:
- **VisitorContactInfo**: A Pydantic BaseModel containing three fields - `name`, `email`, and `phone` (all of which are required and of type `str`).

## Output Model:
- **ContactAppendResult**: Another Pydantic BaseModel, containing a single field, `status` (type `str`). This field indicates the outcome of the appending process.

# Parameters
- **args**: A `VisitorContactInfo` object that includes the visitor's name, email, and phone number.
- **callbacks**: Currently unused in this component.

# Transform Function
The `transform()` method of the WebPixelToGoogleSheet component is an asynchronous function that performs the following steps:
1. Call the parent class `transform()` method to retrieve the processed input data.
2. Extract the input data from the `VisitorContactInfo` BaseModel using the `.dict()` method.
3. Make an API call to the Google Sheets API by invoking the `append_contact_to_google_sheet()` function, passing the extracted contact_info object.
4. Check the status of the data appending process and create a `ContactAppendResult` object reflecting the status.
5. Return the newly created `ContactAppendResult` object.

# External Dependencies
This component relies on the following external libraries:
- dotenv (for loading environment variables)
- fastapi (for creating a FastAPI application)
- pydantic (for creating input and output models)
- typing (for providing type hint support)

# API Calls
The `append_contact_to_google_sheet()` function makes an API call to the Google Sheets API. This function is yet to be implemented, but it should interact with the Google Sheets API (you can use the `google-auth` and `google-api-python-client` libraries) to append contact information to the target spreadsheet (replace "your_spreadsheet_id" and "your_range" with the appropriate values for your use case).

# Error Handling
Currently, there is no specific error handling implemented in this component. You may want to extend the error handling by catching exceptions and providing appropriate responses.

# Examples
Here's an example of using the WebPixelToGoogleSheet component within a Yeager Workflow:

