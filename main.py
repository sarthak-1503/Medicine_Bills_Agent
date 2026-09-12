import asyncio
from agent.bill_agent import bill_agent
from agents import Runner

async def main():
    bill_text = """
    ABC Medical Store

    Invoice No: INV-1001
    Date: 25-08-2026

    Dolo 650       2    35.00    70.00
    Azithromycin   1    120.00   120.00

    Subtotal: 190.00
    GST: 9.50
    Total: 199.50
    """
    result = await Runner.run(bill_agent, "Please extract the details from the following medicine bill: " + bill_text)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())