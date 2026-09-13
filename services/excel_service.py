from openpyxl import Workbook
from models.bill import MedicineBill


def save_to_excel(
    bills: list[MedicineBill],
    filename: str = "medicine_bills.xlsx"
):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Medicine Bills"

    # Header
    sheet.append([
        "Bill Number",
        "Bill Date",
        "Chemist Name",
        "Amount",
        "GST",
        "Prescribed On",
        "Prescribed By"
    ])

    # One row per bill
    for bill in bills:
        sheet.append([
            bill.bill_number,
            bill.bill_date,
            bill.chemist_name,
            bill.amount,
            bill.gst,
            bill.prescribed_on,
            bill.prescribed_by
        ])

    workbook.save(filename)
