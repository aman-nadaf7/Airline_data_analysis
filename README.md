✈️ Flight Delay & Cancellation Analysis
📌 Project Overview

This project analyzes flight delay and cancellation patterns using real-world airline data.
The goal is to clean, preprocess, and visualize flight datasets to uncover insights such as:

Which airlines have the longest delays?

What are the common causes of cancellations?

Which airline is most punctual?

🔑 Key Steps in the Project

Data Cleaning & Preprocessing

Removed duplicate rows.

Handled missing values using mode imputation and zero-fill for delays.

Converted numeric time (e.g., 2354) into HH:MM format.

Filled missing categorical values (like cancellation reasons) with most frequent values.

Exploratory Data Analysis (EDA)

Average Departure Delay by Airline.

Average Arrival Delay by Airline.

Number of Cancelled Flights by Airline.

Distribution of Cancellation Reasons (Carrier, Weather, NAS, Security).

Punctuality (On-Time %) by Airline.

Visualization Techniques

Bar Charts (Seaborn)

Pie Charts (Matplotlib)

Horizontal Bar Charts for ranking airlines by punctuality

📊 Visual Insights

Average Departure & Arrival Delays → Identifies airlines with higher delays.

Cancellation Reasons Distribution → Shows major reasons like Weather, Carrier, or Air System.

Cancelled Flights Count by Airline → Helps compare operational efficiency.

Punctuality % by Airline → Highlights best-performing airlines for on-time arrivals.

🛠 Tools & Libraries

Python

Pandas – Data cleaning & manipulation

NumPy – Numerical operations

Matplotlib & Seaborn – Data visualization

📂 Files in this Repository

airlines.csv → Airline code to name mapping

airports.csv → Airport details (optional for further expansion)

flight.xlsx → Main dataset containing flight information

flight_analysis.py → Python script for data cleaning & visualization

README.md → Project documentation

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/your-username/flight-delay-analysis.git
cd flight-delay-analysis


Install dependencies:

pip install pandas numpy matplotlib seaborn


Run the Python script:

python flight_analysis.py

📈 Future Enhancements

Add Machine Learning models to predict flight delays.

Include Geospatial Analysis of airports using Folium/Plotly.

Automate daily reports with Jupyter Notebooks & dashboards.

👨‍💻 Author

Aman Nadaf
