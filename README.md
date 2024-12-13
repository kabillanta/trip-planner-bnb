# Trip Planner - Build and Blog Marathon

A streamlined web app for planning trips using AI-generated summaries and real-time data from BigQuery.

## Features
- **AI-Powered Recommendations**: Uses Gemini 2.0 Flash AI to generate detailed summaries for trip attractions.
- **Customizable Preferences**: Choose your city, available time, budget, and attraction types.
- **Data from BigQuery**: Fetches real-time data for attractions based on your preferences.
- **Engaging User Interface**: Built with Streamlit for an intuitive and interactive experience.

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/kabillanta/trip-planner-bnb.git
   cd trip-planner-bnb
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   streamlit run app.py
   ```

## Deployment on Cloud Run
1. Push the code to a GitHub repository.
2. Connect your GitHub repo to Google Cloud Build.
3. Deploy the app using the `Dockerfile` provided.

## About
This app leverages Google Cloud BigQuery and Gemini 2.0 Flash AI for intelligent trip planning. Perfect for travelers looking for personalized, efficient, and AI-enhanced recommendations.


This app is built during Build and Blog marathon Bengaluru.
