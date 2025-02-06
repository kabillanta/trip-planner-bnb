# Trip Planner - Build and Blog Marathon

Planning a trip is exciting but can often be overwhelming. Wouldn’t it be great to have a personalized trip planner powered by Google technologies? In this guide, we’ll walk you through building your very own Trip Planner app, designed for beginners with step-by-step instructions.

## Introduction
Planning a journey involves juggling various tasks: destinations, budgets, and preferences. This guide will help you set up a Trip Planner app that simplifies this process using Google Cloud BigQuery and Gemini 2.0 Flash AI. By the end, you’ll have a working app to organize your trips and explore Google’s powerful services.

## Audience
This project is for beginners interested in learning how to use Google Cloud Platform (GCP), BigQuery, and AI tools. Some prior knowledge of Python and GitHub is helpful but not required.

## Outcome
By the end of this tutorial, you’ll have a functional trip planner that can:

- Suggest travel destinations based on preferences.
- Generate a personalized itinerary using AI.
- Provide recommendations even for cities not in the dataset.

## Design
### Architecture
- **Frontend:** Built with Streamlit for a user-friendly interface.
- **Backend:** Powered by Python for data processing and AI interactions.
- **Database:** BigQuery to store and fetch travel data.
- **AI:** Gemini 2.0 Flash for generating trip summaries and itineraries.

### Rationale
- **BigQuery:** Efficiently handles large datasets for travel information.
- **Gemini 2.0 Flash AI:** Provides engaging and detailed trip summaries.
- **Streamlit:** Simplifies the creation of an interactive web app.

## Prerequisites
Before you begin, make sure you have:

- A Google Cloud account ([Sign up here](https://cloud.google.com/)).
- Installed:
  - [Git](https://git-scm.com/downloads)
  - [Python](https://www.python.org/downloads/)
  - [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Cloned the Trip Planner GitHub repository:
  ```bash
  git clone https://github.com/kabillanta/trip-planner.git
  cd trip-planner
  ```
- Enabled BigQuery and configured a dataset with travel information.

## Step-by-Step Instructions

### 1. Set up Google Cloud Project
1. Log in to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and name it `TripPlanner`.
3. Enable the required APIs:
   - BigQuery API
   - Google Cloud Storage API

### 2. Configure BigQuery Dataset
1. Navigate to BigQuery in the Google Cloud Console.
2. Create a dataset named `trip_generator`.
3. Add a table (e.g., `india`) with columns for:
   - City
   - Attraction name
   - Type
   - Review ratings
   - Time needed
   - Entrance fees
   - Best time to visit

### 3. Set Up Gemini 2.0 Flash API
1. Obtain API access for Gemini 2.0 Flash ([Guide](https://gemini.google.com/)).
2. Configure the API key in your project:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

### 4. Deploy the Backend
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Deploy the backend locally or on a cloud service (e.g., Google Cloud Run).
3. Test the BigQuery query and Gemini integration with sample data.

### 5. Build the Streamlit App
1. Use Streamlit to create an interactive interface for users to input their preferences.
2. Fetch travel data from BigQuery based on user input:
   ```python
   def fetch_trip_plan(city, time_available, budget, preferred_types):
       # BigQuery client and query logic
       pass
   ```
3. Generate trip summaries using Gemini 2.0 Flash:
   ```python
   def generate_trip_summary_with_gemini(trip_data):
       # AI summary logic
       pass
   ```
4. Display results and AI-generated summaries in the app.

### 6. Run the App Locally
For local testing:
```bash
streamlit run app.py
```
Access the app at `http://localhost:8501`.

## Result / Demo
Once deployed, the Trip Planner will allow users to:

- Search and explore travel destinations.
- Get AI-generated summaries of attractions.
- Receive recommendations even for cities not in the database.

### Example Output
- A list of top-rated attractions tailored to the user’s preferences.
- An AI-generated itinerary for exploring the selected city.

## What’s Next?
Expand your Trip Planner with these ideas:

- Add a budget management feature.
- Include weather forecasts for the destinations.
- Integrate collaborative trip planning options.

## Additional Resources
To learn more about Google Cloud services and to create impactful work:

- [Register for Code Vipassana sessions](https://example.com/code-vipassana)
- [Join the meetup group Datapreneur Social](https://example.com/datapreneur-social)
- [Sign up to become a Google Cloud Innovator](https://example.com/google-cloud-innovator)

Happy coding!

