# Browser Automation Demo Collection

This repository contains a collection of demonstration scripts showcasing the capabilities of the [browser-use](https://github.com/browser-use/browser-use) package for AI-powered browser automation.

## Overview

The browser-use package enables AI agents to interact with web browsers, performing complex tasks that would typically require human intervention. This repository showcases practical examples of automated web browsing, data collection, and web-based research.

## Demonstrations

### 1. Amazon GPU Search (`AmazonGPU.py`)

This script demonstrates how to:
- Navigate to Amazon.com
- Search for specific products (high-performance desktop computers)
- Apply price filters
- Extract detailed product information including:
  - Product title
  - Brand name
  - CPU specifications
  - Graphics card details
  - RAM memory specifications
  - Price
  - Rating

### 2. Google Flights Search (`GoogleFlight.py`)

This script demonstrates how to:
- Navigate to Google Flights
- Set departure and arrival locations
- Select specific travel dates
- Filter for evening departure flights
- Extract comprehensive flight information including:
  - Departure and arrival times
  - Airlines
  - Prices
  - Number of stops

### 3. Reddit Research (`reddit.py`)

This script demonstrates how to:
- Navigate to Reddit
- Search for specific topics (in this case, "AGI")
- Visit multiple relevant communities (subreddits)
- Extract and analyze opinions
- Generate summaries of findings
- Format collected data in JSON format

## Prerequisites

- Python 3.8 or higher
- Required packages:
  ```
  langchain-openai
  browser-use
  python-dotenv
  ```
- A valid OpenAI API key stored in a `.env` file

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Startup-Consulting/browser-automation-demos.git
   cd browser-automation-demos
   ```

2. Install required dependencies:
   ```bash
   pip install langchain-openai browser-use python-dotenv
   ```

3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run any of the demo scripts:

```bash
python AmazonGPU.py
# or
python GoogleFlight.py
# or
python reddit.py
```

Each script will:
1. Initialize the browser automation agent
2. Define a specific task to perform
3. Execute the task through automated browser interaction
4. Output the collected information

## How It Works

The browser-use package enables AI models (in this case, GPT-4) to:

1. Observe the browser screen
2. Understand the web content and UI elements
3. Make decisions about navigation and interaction
4. Execute actions such as clicking, typing, and data extraction
5. Return structured results

## Customization

You can customize any of the demo scripts by modifying:
- The search parameters
- The websites to visit
- The data collection requirements
- The output format

## Credits

This project uses the [browser-use](https://github.com/browser-use/browser-use) package, which provides a powerful framework for AI agents to interact with web browsers.

## License

[MIT License](LICENSE)

