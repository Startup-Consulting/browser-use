from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

#  https://github.com/browser-use/browser-use

async def main():
    agent = Agent(
        task="""Navigate to Google Flights and search for specific flights.

        Follow these steps precisely:
        1. Go to https://www.google.com/travel/flights
        2. Look for the departure city field and click it
        3. Type "Seattle" and select "Seattle-Tacoma International Airport (SEA)"
        4. Look for the arrival city field and click it
        5. Type "Salt Lake City" and select "Salt Lake City International Airport (SLC)"
        6. Click on the departure date field
        7. Navigate to and select February 23, 2025
        8. Click on the return date field
        9. Navigate to and select March 1, 2025
        10. Wait for the search results to load
        11. Look for evening flights (after 4 PM) on the departure date
        12. Collect and return all available flights with:
            - Departure times
            - Arrival times
            - Airlines
            - Prices
            - Number of stops

        Important:
        - Wait for each element to load before interacting
        - Make sure to select evening flights for departure
        - Verify all selections before proceeding to the next step
        - If a calendar month isn't visible, use the arrow buttons to navigate
        """,
        llm=ChatOpenAI(model="gpt-4-turbo"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
