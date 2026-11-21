# JKU Mensa Price Tracker

A simple data project to track food prices at the JKU cafeteria (Mensa). The main goal is to see exactly how much money the student discount saves us over time.

## Files
* fetch_live_data.py: Gets today's menu and prices from the website.
* clean_data.py: Cleans up the old data files.
* app.py: The app that shows the charts.
* data/: Folder for the data files.

## Tools
* Python
* Get Web Data: BeautifulSoup, Requests
* Clean Data: Pandas, PyArrow
* App: Streamlit, Plotly

## Quick Start

1. Turn on the sandbox:
.\venv\Scripts\activate

2. Install the tools:
pip install requests beautifulsoup4 pandas pyarrow streamlit plotly

3. Start the app:
streamlit run app.py