import os
import json
import google.generativeai as genai
from google.cloud import bigquery
import streamlit as st

# Configure Gemini API
genai.configure(api_key="AIzaSyABkPJSlnxv-YsFQUAvz704zHRT7gUQE10")

# Set up the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Function to fetch data from BigQuery
def fetch_trip_plan(city, time_available, budget, preferred_types):
    client = bigquery.Client(location="asia-south1")

    query = """
    SELECT 
    Name, 
    Type, 
    `Google review rating`, 
    `time needed to visit in hrs`, 
    `Entrance Fee in INR`, 
    `Best Time to visit`
    FROM 
        `trip-generator-444505.india.new1`
    WHERE 
        City = @city
        AND `time needed to visit in hrs` <= @time_available
        AND `Entrance Fee in INR` <= @budget
        AND Type IN UNNEST(@preferred_types)
    ORDER BY 
        `Google review rating` DESC
    LIMIT 10;
    """

    # Set query parameters
    query_params = [
        bigquery.ScalarQueryParameter("city", "STRING", city),
        bigquery.ScalarQueryParameter("time_available", "FLOAT", time_available),
        bigquery.ScalarQueryParameter("budget", "FLOAT", budget),
        bigquery.ArrayQueryParameter("preferred_types", "STRING", preferred_types),
    ]

    # Execute query
    job_config = bigquery.QueryJobConfig(query_parameters=query_params)
    query_job = client.query(query, job_config=job_config)

    return query_job.result().to_dataframe()

# Function to generate trip summary using Gemini 2.0 Flash
def generate_trip_summary_with_gemini(trip_data):
    attractions = trip_data.to_dict(orient="records")
    prompt = f"""
Please create a detailed travel summary (within 700 words) for the following attractions. The summary should include:

1. **Why visit**: A compelling reason for visiting each attraction.
2. **Cultural/Historical significance**: What makes this attraction culturally or historically important.
3. **What to expect**: What tourists can experience when visiting, including any unique features of the place (e.g., natural beauty, architecture, experiences).
4. **Best time to visit**: Mention the best time to visit and why.

Use an engaging and informative tone, and ensure the description helps travelers understand the value and experience of each attraction.

Here is the list of attractions to consider:
{json.dumps(attractions, indent=2)}
"""

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    return response.text

# Streamlit app
st.title("Trip Planner with Gemini 2.0 Flash AI")
st.markdown("Plan your trip with ease! Select your preferences to generate the best itinerary and get AI-generated recommendations.")

# Sidebar input fields
st.sidebar.header("Trip Preferences")
city = st.sidebar.text_input("Enter your city")
time_available = st.sidebar.slider("Available time (in hours)", 0.5, 12.0, 3.0)
budget = st.sidebar.number_input("Budget for entrance fees (INR)", min_value=0, value=500, step=50)
preferred_types = st.sidebar.multiselect(
    "Preferred types of attractions",
    ['War Memorial', 'Tomb', 'Temple', 'Theme Park', 'Observatory', 'Market', 'Fort', 
     'Stepwell', 'Park', 'Museum', 'Zoo', 'Monument', 'Science', 'Promenade', 
     'National Park', 'Religious Shrine', 'Beach', 'Amusement Park', 'Palace', 
     'Botanical Garden', 'Government Building', 'Landmark', 'Lake', 'Film Studio', 
     'Tombs', 'Bridge', 'Cricket Ground', 'Site', 'Church', 'Waterfall', 'Bird Sanctuary', 
     'Historical', 'Cultural', 'Urban Development Project', 'Wildlife Sanctuary', 'Shrine', 
     'Religious Site', 'Memorial', 'Border Crossing', 'Sculpture Garden', 'Scenic Area', 
     'Viewpoint', 'Mountain Peak', 'Cave', 'Mausoleum', 'Vineyard', 'Valley', 'Temples', 
     'Prehistoric Site', 'Scenic Point', 'Monastery', 'Tea Plantation', 'Adventure Sport', 
     'Trekking', 'Gurudwara', 'Ski Resort', 'Suspension Bridge', 'Ghat', 'Orchard', 
     'Confluence', 'Hill', 'Gravity Hill', 'Village', 'Sunrise Point', 'Dam', 'Spiritual Center', 
     'Aquarium', 'Religious Complex', 'Island', 'River Island', 'Rock Carvings', 'Township', 
     'Natural Feature', 'Entertainment', 'Mall', 'Commercial Complex', 'Mosque', 'Race Track']
)

# Fetch trip plan when the button is clicked
if st.sidebar.button("Generate Trip Plan"):
    with st.spinner("Fetching trip plan..."):
        try:
            # Fetch data from BigQuery
            results = fetch_trip_plan(city, time_available, budget, preferred_types)

            if not results.empty:
                with st.spinner("Generating AI-powered summary..."):
                    try:
                        summary = generate_trip_summary_with_gemini(results)
                        st.markdown("### AI-Powered Summary")
                        st.write(summary)
                    except Exception as e:
                        st.error(f"Error generating summary: {e}")
            else:
                with st.spinner("Generating input for city not in dataset..."):
                    chat_session = model.start_chat(history=[])
                    prompt = f"Generate a detailed itinerary for a city named {city}. Consider time available as {time_available},budget as {budget} and prefered locatin types as {preferred_types}."  
                    response = chat_session.send_message(prompt)
                    st.markdown(f"City not in database. Here's a suggested itinerary: {response.text}")
        except Exception as e:
            st.error(f"Error generating trip plan: {e}")

# About section
st.sidebar.markdown("---")
st.sidebar.info("This app uses Google Cloud's BigQuery and Gemini 2.0 Flash AI to fetch data and generate trip plans.")
