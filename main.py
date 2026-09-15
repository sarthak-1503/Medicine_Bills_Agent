import asyncio
# from agent.bill_agent import bill_agent
# from agents import Runner
from dotenv import load_dotenv
from services.extractor import extract_bill
from services.excel_service import save_to_excel
from services.image_utility import resize_bill

load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

async def main():
#     bill_text = """
# MEDICINE BILL

# Chemist: Apollo Pharmacy
# Bill Number: APH-2026-008742
# Bill Date: 12-09-2026

# Patient: Rahul Sharma

# Prescribed On: 10-09-2026
# Prescribed By: Dr. Ankit Mehra

# --------------------------------------------------
# Medicine                    Qty       Amount
# --------------------------------------------------
# Dolo 650                    10        35.00
# Azithromycin 500mg           3       120.00
# Pantoprazole 40mg            5        85.00
# --------------------------------------------------

# Subtotal:                              240.00
# GST (5%):                              12.00
# --------------------------------------------------
# TOTAL AMOUNT:                          252.00
# --------------------------------------------------

# Payment Mode: Cash

# Thank you for visiting Apollo Pharmacy.
# """
    # result = await Runner.run(bill_agent, "Please extract the details from the following medicine bill: " + bill_text)
    # print(result.final_output)
    image_paths = [
        "sample_bills/input/sampleBill.jpg"]
    bills = []
    for image_path in image_paths:
        output_path = resize_bill(image_path, "sample_bills/input/resized_sampleBill.jpg")
        bill = extract_bill(output_path)
        bills.append(bill)

    save_to_excel(bills)

if __name__ == "__main__":
    asyncio.run(main())