import json 
import ollama

from models.bill import MedicineBill

SYSTEM_PROMPT = """
        You are an expert in extracting information from medicine bills. Your task is to analyze the provided bill data and extract the following details: -
        1. Bill Number
        2. Bill Date
        3. Chemist Name
        4. Amount
        5. GST
        6. Prescribed On
        7. Prescribed By

        Field mapping rules:

bill_number may appear on the bill as:
- Bill Number
- Bill No
- Bill #
- Invoice Number
- Invoice No
- Receipt Number
- Receipt No

bill_date may appear as:
- Bill Date
- Invoice Date
- Date
- Receipt Date

chemist_name may appear as:
- Chemist
- Pharmacy
- Medical Store
- Store Name
- Pharmacist
- Seller

amount may appear as:
- Amount
- Total
- Grand Total
- Net Amount
- Total Amount
- Payable Amount

gst may appear as:
- GST
- GST Amount
- GST Amt
- Tax
- Tax Amount

prescribed_on may appear as:
- Prescribed On
- Prescription Date
- Rx Date
- Date of Prescription

prescribed_by may appear as:
- Prescribed By
- Doctor
- Doctor Name
- Physician
- Prescribing Doctor

        Rules : -
        1. Do not invent any information. Only extract the details present in the bill.
        2. Ensure that the extracted information is accurate and matches the details in the bill.
        3. If any of the required details are missing in the bill, return None for that field.
        4. The output should be structured according to the MedicineBill model defined in models/bill.py.
        5. Preserve the values from the bill.
        6. Do not calculate values unless explicitly instructed to do so.
        7. Extract every medicine bill separately and return them as a list of MedicineBill objects.
    """

def extract_bill(image_path: str) -> MedicineBill:

    response = ollama.chat(
        model="qwen2.5vl:3b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Extract the medicine bill information.", "images": [image_path]}
        ]
    )

    content = response["message"]["content"]
    print("Extracted content:", str(content))  # Debugging line to see the extracted content
    data = json.loads(content)
    return MedicineBill.model_validate(data)
