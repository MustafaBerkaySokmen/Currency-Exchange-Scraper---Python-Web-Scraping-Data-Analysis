# Currency Exchange Scraper - Python Web Scraping & Data Analysis

## Overview
The **Currency Exchange Scraper** is a **Python-based web scraping project** that retrieves **historical USD to TRY exchange rates** from X-Rates.com. The project processes and visualizes the data using **Pandas and Matplotlib**, making it useful for financial analysis and trend forecasting.

## Features
- **Automated Data Extraction**: Scrapes exchange rate data for USD to TRY.
- **Historical Data Analysis**: Fetches exchange rates for a given date range.
- **Data Processing with Pandas**: Converts extracted tables into structured DataFrames.
- **Graphical Data Visualization**: Uses Matplotlib to plot exchange rate trends.

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/Currency-Exchange-Scraper.git
cd Currency-Exchange-Scraper
```

### **2. Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**
```bash
pip install requests beautifulsoup4 pandas matplotlib
```

## How It Works
1. **User Inputs Date Range**
   - The script prompts the user to enter **start and end dates** for scraping.

2. **Scrapes Historical Exchange Rate Data**
   - Fetches USD to TRY exchange rates from **X-Rates.com**.
   - Parses the **HTML table** using **BeautifulSoup**.

3. **Processes and Stores Data**
   - Converts extracted data into a Pandas **DataFrame**.
   - Handles missing values and cleans up formatting.

4. **Visualizes the Data**
   - Plots exchange rate trends over time using Matplotlib.

## Running the Scraper
```bash
python currency_exchange_scraper.py
```

## Example Output
```
Fetching exchange rates from 2024-01-01 to 2024-01-10...
Data successfully scraped and saved to exchange_rates.csv
Generating visualization...
```
📊 **Graph Output:** A line chart displaying exchange rate fluctuations.

## Future Enhancements
- **Multi-Currency Support**: Extend to EUR, GBP, and other currencies.
- **Live Data Updates**: Implement API-based exchange rate retrieval.
- **Machine Learning Predictions**: Forecast future exchange rates.

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

