# Social Media Engagement Dashboard

## Overview

The Social Media Engagement Dashboard is a data analytics project that collects and analyzes YouTube channel engagement metrics using the YouTube Data API v3. The dashboard helps users understand content performance through interactive visualizations and provides recommendations for improving engagement.

---

## Features

* Fetches YouTube channel data using the YouTube Data API
* Displays total videos, views, likes, and comments
* Interactive dashboard built with Streamlit
* Visualizes engagement using charts and graphs
* Shows top-performing videos
* Recommends the best posting days and times
* Search videos by title
* Download analyzed data as a CSV file

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib
* Google YouTube Data API v3

---

## Project Structure

```
Social Media Engagement Dashboard/
│
├── app.py
├── analysis.py
├── youtube_data.py
├── requirements.txt
├── README.md
└── data/
    └── youtube_data.csv
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/social-media-engagement-dashboard.git
```

2. Navigate to the project folder:

```bash
cd social-media-engagement-dashboard
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## API Setup

1. Create a Google Cloud project.
2. Enable the **YouTube Data API v3**.
3. Generate an API key.
4. Open `youtube_data.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

---

## Usage

Generate the dataset:

```bash
python youtube_data.py
```

Run the dashboard:

```bash
streamlit run app.py
```

---

## Dashboard Features

* Total Views
* Total Likes
* Total Comments
* Top Performing Videos
* Engagement Analysis
* Best Posting Time Recommendation
* CSV Download Option

---

## Future Improvements

* Instagram integration
* Facebook analytics
* Power BI dashboard
* Sentiment analysis of comments
* Automatic daily data updates

---

## Author

**Arya Kamdi**

B.Tech Computer Science & Engineering (Cyber Security)

St. Vincent Pallotti College of Engineering & Technology, Nagpur
