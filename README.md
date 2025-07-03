# ✈️ Airline Market Demand Analyzer

This project is a Streamlit-based web application for analyzing airline market demand using real-time flight data from the [AviationStack API](https://aviationstack.com/).

## Features

- **Enter Departure Airport:** Input an airport IATA code (e.g., SYD, MEL, BNE) to analyze outgoing flights.
- **Fetch Real-Time Data:** Retrieves flight data from the AviationStack API.
- **Data Table:** View detailed information about flights including airline, flight number, departure/arrival airports, and scheduled time.
- **Visualizations:**
  - **Arrival Airport Distribution:** Bar chart showing the most common arrival airports.
  - **Flights by Airline:** Bar chart showing the number of flights by airline.
  - **Departure Time Distribution:** Histogram of flight departures by hour.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kaal-El/Flight_manager.git
   cd Flight_manager
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your AviationStack API key:**
   - Edit `app.py` and replace the `API_KEY` variable with your own key from [AviationStack](https://aviationstack.com/).

4. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. **Use the web interface:**
   - Enter a departure airport IATA code and click "Fetch Data" to view the data and charts.

## Requirements

- Python 3.x
- [Streamlit](https://streamlit.io/)
- pandas
- requests
- matplotlib
- seaborn

Install dependencies via:
```bash
pip install streamlit pandas requests matplotlib seaborn
```

## Notes

- The API key used in the code is for demonstration purposes only. Please obtain your own free key from [AviationStack](https://aviationstack.com/).
- Data availability depends on the API's rate limits and current coverage.

## License

MIT License
