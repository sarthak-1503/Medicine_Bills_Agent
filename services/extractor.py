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
    data = json.loads(content)
    return MedicineBill.model_validate(data)
