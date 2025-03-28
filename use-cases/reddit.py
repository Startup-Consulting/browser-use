from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="""Go to Reddit, search for 'AGI', click on singularity community, get 20 negative opinions and summarize"
              Once done with singularity community, do with technology community, continue with ArtificialInteligence community as well.
              One you complete with all communities, return them by communities in a json format.""",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
