
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class VisitorContactInfo(BaseModel):
    name: str
    email: str
    phone: str


class ContactAppendResult(BaseModel):
    status: str


class WebPixelToGoogleSheet(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: VisitorContactInfo, callbacks: typing.Any
    ) -> ContactAppendResult:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        # Retrieve the input data from the VisitorContactInfo model
        contact_info = args.dict()
        
        # Make an API call to the Google Sheets API to append the contact information to the specified spreadsheet
        # You need to implement the function to interact with Google Sheets API
        append_status = await append_contact_to_google_sheet(contact_info)
        
        # Check the status of the appending process and create a ContactAppendResult model based on the status
        result = ContactAppendResult(status=append_status)
        
        return result


async def append_contact_to_google_sheet(contact_info: dict) -> str:
    # Implement the function to interact with Google Sheets API
    # For example, you can use google-auth and google-api-python-client libraries to work with Google Sheets API
    # Remember to replace "your_spreadsheet_id" and "your_range" with the appropriate values for your use case
    pass


load_dotenv()
web_pixel_to_google_sheet_app = FastAPI()


@web_pixel_to_google_sheet_app.post("/transform/")
async def transform(args: VisitorContactInfo) -> ContactAppendResult:
    web_pixel_to_google_sheet = WebPixelToGoogleSheet()
    return await web_pixel_to_google_sheet.transform(args, callbacks=None)

