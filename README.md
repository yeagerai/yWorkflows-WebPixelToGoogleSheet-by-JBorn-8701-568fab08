
# WebPixelToGoogleSheet

This workflow creates a web pixel that, when embedded into a website, collects visitor contact information and saves it directly into a Google Spreadsheet. The workflow consists of the following steps: 1. Visitors enter their contact information on the website form. 2. The web pixel sends this data to the backend endpoint. 3. Data is parsed and validated using Pydantic models. 4. Using Google Sheets API, the contact information is appended to the specified Google Spreadsheet.
## Initial generation prompt
build a pixel that I can insert on my website which drops the visitors contact information directly into a google spreadsheet

## Authors: 
- yWorkflows
- JBorn#8701
        