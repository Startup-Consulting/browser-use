from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()

#  https://github.com/browser-use/browser-use

async def main():
    # Get LinkedIn credentials from environment variables
    linkedin_email = os.getenv("LINKEDIN_EMAIL")
    linkedin_password = os.getenv("LINKEDIN_PASSWORD")
    
    # Get Google API key from environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    if not linkedin_email or not linkedin_password:
        print("Error: LinkedIn credentials not found in environment variables.")
        print("Please set LINKEDIN_EMAIL and LINKEDIN_PASSWORD in your .env file.")
        return
    
    if not google_api_key:
        print("Error: Google API key not found in environment variables.")
        print("Please set GOOGLE_API_KEY in your .env file.")
        return
    
    agent = Agent(
        task=f"""Visit LinkedIn and search for Data Engineer jobs in the Greater Seattle Area.

        Follow these steps precisely:
        1. Visit linkedin.com
        2. Log in with the following credentials:
           - Email: {linkedin_email}
           - Password: {linkedin_password}
        3. Click on the search bar and search "AI Engineer" 
        4. Filter the results:
           - click on "Jobs"
           - click on "All Filters"
           - check "Mid-Senior level" and "Director" and "Executive" in  "Experience level"
           - check "Remote" and "Hybrid" in "Remote"
           - check "Greater Seattle Area" in "Location"
           - check "$140,000" in "Salary"
           - check "Full-time" in "Job type"
        5. Go through the top 10 positions and collect the following information for each:
           - Name of Employer
           - Job Title
           - Method of contact: LinkedIn
           - Type of contact: Application
           - Result of contact: waiting for the response
           - Location
           - Summary of the job
        6. Return the results in a markdown format with a table structure like this:
           
           ```markdown
           | Employer | Job Title | Method of Contact | Type of Contact | Result of Contact | Location | Summary of the job |
           |----------|-----------|------------------|----------------|------------------|----------|------------------|
           | Company1 | Data Engineer | LinkedIn | Application | Waiting for response | Seattle, WA | Summary of the job |
           | Company2 | Senior Data Engineer | LinkedIn | Application | Waiting for response | Seattle, WA | Summary of the job |
           ```

        Important:
        - Wait for each element to load before interacting
        - Make sure to apply all filters correctly
        - If you encounter any login prompts, handle them appropriately
        - Verify all selections before proceeding to the next step
        - Make sure to format the results in proper markdown
        """,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", google_api_key=google_api_key),
    )
    result = await agent.run()
    
    # Check if result is not empty
    if not result:
        print("Error: Agent returned empty results.")
        return
      
    # Parse markdown table and save to Excel
    try:
        # Extract table content from markdown
        table_lines = []
        capture = False
        for line in result.split('\n'):
            if line.startswith('|'):
                capture = True
                table_lines.append(line)
            elif capture and not line.strip():
                capture = False
        
        # Skip header separator line (the line with |---|---|...)
        data_lines = [line for line in table_lines if '---' not in line and line.strip() != '']
        
        # Parse header and data
        if len(data_lines) >= 2:  # At least header and one data row
            header = [col.strip() for col in data_lines[0].split('|')[1:-1]]  # Skip first and last empty elements
            
            # Parse data rows
            rows = []
            for line in data_lines[1:]:
                columns = [col.strip() for col in line.split('|')[1:-1]]
                rows.append(columns)
            
            # Create DataFrame and save to Excel
            df = pd.DataFrame(rows, columns=header)
            df.to_excel('jobsearch.xlsx', index=False)
            print(f"\nResults saved to jobsearch.xlsx")
        else:
            print("\nNo job data found in the results")
    except Exception as e:
        print(f"\nError saving results to Excel: {e}")
        print(f"\nRaw results from agent:")
        print(result)

asyncio.run(main())
