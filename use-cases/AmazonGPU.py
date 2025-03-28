from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    # Get search term from user
    search_term = input("Enter your search term for Amazon: ")
    
    agent = Agent(
        task=f"""Navigate to Amazon and search for {search_term}.

        Follow these steps precisely:
        1. Go to https://www.amazon.com
        2. Find the search bar at the top of the page
        3. Type "{search_term}" and press Enter
        4. Wait for the search results to load
        5. Look for the price filter on the left sidebar
        6. Set the minimum price to $2000
        7. Wait for the filtered results to load
        8. For each product that matches the criteria, collect:
            - Product title
            - Brand name
            - CPU model
            - CPU speed
            - Graphics card details
            - RAM memory specifications
            - Price
            - Rateing
        9. Only collect information for products that are actually desktop computers
           (ignore accessories or other irrelevant items)
        10. Return the collected information in a structured format.

        Important:
        - Wait for each element to load before interacting
        - Make sure to verify the specifications are complete
        - Only collect information from products that show all required specifications
        - If a product doesn't show all required specs, skip it
        - Collect information for the first 10 valid products you find
        """,
        llm=ChatOpenAI(model="gpt-4-turbo"),
    )
    result = await agent.run()
    print("#################################################")
    print(result)
    print("#################################################")
    
asyncio.run(main())