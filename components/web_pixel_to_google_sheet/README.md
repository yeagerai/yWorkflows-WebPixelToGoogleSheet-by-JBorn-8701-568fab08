
# WebPixelToGoogleSheet

This component takes input as VisitorContactInfo, which is a Pydantic model containing fields like name, email, and phone. It is responsible for appending the contact information to a specified Google Sheets spreadsheet. The output of this component is a ContactAppendResult, which is also a Pydantic model containing the status of appending the contact to the spreadsheet.

## Initial generation prompt
description: "IOs - 'Input: VisitorContactInfo, a pydantic model including fields\
  \ like name, email, phone.\n  Output: ContactAppendResult, a pydantic model containing\
  \ the status of appending\n  the contact to the spreadsheet.'\n"
name: WebPixelToGoogleSheet


## Transformer breakdown
- 1. Retrieve the input data from the VisitorContactInfo model.
- 2. Append the contact details (name, email, and phone) to the target Google Sheets spreadsheet.
- 3. Check the status of the appending process and create a ContactAppendResult model based on the status.
- 4. Return the ContactAppendResult as output.

## Parameters
[]

        