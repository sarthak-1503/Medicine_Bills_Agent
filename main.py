import asyncio
from agent.bill_agent import bill_agent
from agents import Runner

async def main():
    result = await Runner.run(bill_agent, "Please extract the details from the following medicine bill: [Insert Bill Data Here]")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())