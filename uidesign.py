import streamlit as st
from streamlit_option_menu import option_menu
import base64
from openai import OpenAI
import pandas as pd
OPENAI_API_KEY=""
# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Function to set background image
def add_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your local image file
add_bg_from_local("test1.jpg")  # Ensure the correct path and format

# Sidebar menu
def navigation_menu():
    menu_items = ["Home", "Login", "Dashboard","ChatBot" ,"Conclusion"]
    if st.session_state["logged_in"]:
        menu_items.append("Logout")  # Show Logout only when logged in

    with st.sidebar:
        
        selected = option_menu(
            "Main Menu",
            menu_items,
            icons=["house-fill", "person-fill", "bar-chart-fill","chat-dots-fill", "lightbulb-fill","box-arrow-right"],
            menu_icon="cast",
            default_index=menu_items.index(st.session_state["page"]),
            styles={
                "container": {"padding": "2!important", "background-color": "pink"},
                "icon": {"color": "black", "font-size": "24px"},
                "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "1px", "--hover-color": "#87CEFA"},
                "nav-link-selected": {"background-color": "white"},
            }
        )
        st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-image: url('https://t4.ftcdn.net/jpg/09/05/85/47/360_F_905854715_5Vv9qPdHKos9gG9FW0AhFz8wuMqTnROW.jpg'); /* Replace with your image path */
            background-size: cover; /* Ensure the image covers the sidebar */
            background-repeat: no-repeat; /* Avoid repeating the image */
            background-position: centre; /* Center the image */
        }
        </style>
        """,
        unsafe_allow_html=True
    )  
        st.markdown( 
    """
    <style>
    div.stButton > button {
        background-color: #87CEFA; /* Set button background color */
        color: white; /* Set text color */
        border-radius: 10px; /* Optional: Add rounded corners */
        border: 1px solid white; /* Optional: Add a white border */
        font-size: 16px; /* Optional: Adjust font size */
        padding: 8px 20px; /* Optional: Adjust padding */
    }
    div.stButton > button:hover {
        background-color: #3E8EDE; /* Change color on hover */
        color: white; /* Optional: Change text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    
    st.session_state["page"] = selected

# Home Page Function
def home_page():
    st.title("_AQI_ :red[Data Visualization] :cloud:")
    st.markdown("""
    <h4 style='text-align: center; color:rgb(24, 23, 23);'>
    Empowering communities with actionable air quality data
    </h4>
    <h6 style='text-align: center; color:rgb(10, 10, 10);font-size: 30px'>
    <em>Breathe Easy, Stay Informed.</em>
    </h6>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Introduction
    st.header("Introduction")
    st.write("""  
                The ClearView Air Quality Insights Dashboard is designed to empower users with a 
                deeper understanding of air quality across various regions. This project uses historical
                 data on Air Quality Index (AQI) and key pollutants such as PM2.5, PM10, NO2, SO2,NH3,CO,NO and O3 
                 to provide meaningful insights. With data sourced from real-world observations,
                  ClearView aims to bridge the gap between raw data and actionable insights, enabling 
                  users to make informed decisions about environmental quality.
""")
    
     # Project Overview Section
    st.markdown("<h2 style='color: #0070BB;font-size: 25px'>🌟 Project Overview</h2>", unsafe_allow_html=True)
    st.markdown("""
       ClearView is an innovative project designed to provide comprehensive air quality insights through an advanced interactive dashboard. By harnessing historical air quality and meteorological data, ClearView aims to transform complex datasets into accessible and actionable visualizations, empowering users to understand and respond to environmental challenges effectively.
        """)
        
        # Objectives Section
    st.markdown("<h2 style='color: #0070BB;font-size: 25px'>🎯 Objectives</h2>", unsafe_allow_html=True)
    st.markdown("""
        - **Visualize Air Quality Index (AQI) trends** and pollutant levels across various regions.
        - **Enable users to explore historical data, monitor changes,** and identify regional disparities in air quality.
        - **Provide actionable insights and forecasts** to support informed decision-making by individuals, organizations, and policymakers.
        """)

        # Mission Section
    st.markdown("<h2 style='color: #0070BB;font-size: 25px'>🚀 Mission</h2>", unsafe_allow_html=True)
    st.markdown("""
        ClearView's mission is to promote environmental awareness and proactive engagement by delivering intuitive tools that simplify air quality analysis. 
        Through this platform, we aspire to foster healthier communities and encourage sustainable practices for a cleaner future.
        """)

        # Comprehensive and User-Friendly Platform Section
    st.markdown("<h2 style='color: #0070BB;font-size: 25px'>💻 A Comprehensive and User-Friendly Platform</h2>", unsafe_allow_html=True)
    st.write("""
        The dashboard leverages interactive visualizations to allow users to analyze AQI trends over time, monitor changes, 
        and compare air quality across different regions. Embedded within a Streamlit web application, the platform ensures 
        an intuitive and accessible interface suitable for environmental analysts, policymakers, and the general public. 
        Users can effortlessly explore air quality disparities, historical trends, and regional insights, fostering a better 
        understanding of how air quality evolves and its implications.
        """)

        # Reliable and Actionable Insights Section
    st.markdown("<h2 style='color: #0070BB;font-size: 25px'>🔍 Reliable and Actionable Insights</h2>", unsafe_allow_html=True)
    st.write("""
        As part of the development process, the data is meticulously preprocessed and structured to ensure accuracy and relevance. 
        The final dashboard undergoes comprehensive testing to validate its functionality and reliability, ensuring a seamless user experience. 
        Detailed documentation accompanies the project, supporting both immediate use and future enhancements. 
        ClearView is not just a tool but a step towards promoting environmental awareness and action.
        """)
        # Footer with centered text
    st.markdown("---")
    st.markdown("<p style='text-align: center;font-size: 20px'>🌍 Let's work together for a cleaner, greener future! 🌱</p>", unsafe_allow_html=True)
             
    if st.button("🔑 Log in to continue"):
        st.session_state["page"] = "Login"
        st.rerun()

# Login Page Function
def login_page():
    st.header("Login")
    
    if st.session_state["logged_in"]:
        st.success("✅ Successfully logged in!")
        st.session_state["page"] = "Dashboard"
        st.rerun()
    
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    
    if st.button("Log in"):
        if username == "admin" and password == "1234":  # Dummy credentials
            st.success("✅ Login successful! Redirecting to Dashboard...")
            st.session_state["logged_in"] = True
            st.session_state["page"] = "Dashboard"
            st.rerun()
        else:
            st.error("❌ Incorrect username or password!")

# Dashboard Page Function
def dashboard_page():
    if not st.session_state["logged_in"]:
        st.warning("⚠️ Please log in to access the dashboard!")
        st.session_state["page"] = "Login"
        st.rerun()
    
    st.header("🌍 ClearView Dashboard")
    st.write("Explore the **interactive dashboards** below...")
    
    with st.expander("📊 **Air Quality Index**"):
        st.markdown(
                """
                - **Overview**: Interactive map and statistics for AQI levels across regions.
                - **Trend Analysis**: Visualize AQI trends over time.
                - **City-level Summaries**: Compare AQI levels across major cities.
                """
            )

    
    with st.expander("🌫️ **Pollutant Trends and State-wise Analysis**"):
         st.markdown(
                """
                - **Pollutant Trends**: Analyze PM2.5, PM10, NO2, SO2,NH3,CO,NO and O3 trends.
                - **State Comparisons**: Compare the most and least polluted states.
                - **Visual Insights**: Clear, interactive charts for pollutant data.
                """
            )
    
    with st.expander("⚠️ **Risk Analysis**"):
         st.markdown(
                """
                - **Top Risk Areas**: Identify cities and states with the highest risk levels.
                - **Category Distribution**: Understand AQI category-wise breakdown.
                - **Historical Trends**: Track risk index trends over time by region.
                """
            )
    
    Dashboard = """
    <iframe title="Air Quality Index" width="100%" height="400" 
    src="https://app.powerbi.com/reportEmbed?reportId=27593732-2221-4d97-ac2d-ef72312ff4a7&autoAuth=true&ctid=a5319c4e-3735-4286-aae1-86195a1fea0f" 
    frameborder="2" style="border: 5px; width: 100%; height: 500px;" allowFullScreen="true">
    </iframe>
    """
    st.components.v1.html(Dashboard, height=500)

    selected = "Insights"
    if st.button("➡️ Go to ChatBot"):
        st.session_state["page"] = "ChatBot"
        st.rerun()

# Load the dataset with caching
@st.cache_data
def load_data():
    df = pd.read_csv("air_pollution_data.csv")
    
    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    
    # Extract month names
    df["month"] = df["date"].dt.month_name()
    
    return df

data = load_data()

# Define function for answering questions
def get_answer(question):
    if question == "What is the average AQI for each city?":
        return data.groupby("city")["aqi"].mean().to_string()

    elif question == "Which city has the highest average AQI?":
        return data.groupby("city")["aqi"].mean().idxmax()

    elif question == "What is the highest recorded AQI and in which city?":
        highest = data.loc[data["aqi"].idxmax(), ["city", "aqi", "date"]]
        return f"City: {highest['city']}, AQI: {highest['aqi']}, Date: {highest['date']}"

    elif question == "What is the lowest recorded AQI and in which city?":
        lowest = data.loc[data["aqi"].idxmin(), ["city", "aqi", "date"]]
        return f"City: {lowest['city']}, AQI: {lowest['aqi']}, Date: {lowest['date']}"

    elif question == "What is the average AQI for each month?":
        return data.groupby("month")["aqi"].mean().to_string()

    elif question == "Which month had the worst air quality?":
        return data.groupby("month")["aqi"].mean().idxmax()

    elif question == "Which month had the best air quality?":
        return data.groupby("month")["aqi"].mean().idxmin()

    elif question == "Which city has the highest PM2.5 levels on average?":
        return data.groupby("city")["pm2_5"].mean().idxmax()

    elif question == "Which city has the highest PM10 levels?":
        return data.groupby("city")["pm10"].mean().idxmax()

    elif question == "Which city has the highest NO2 levels?":
        return data.groupby("city")["no2"].mean().idxmax()

    elif question == "Which city has the highest CO levels?":
        return data.groupby("city")["co"].mean().idxmax()

    elif question == "What is the correlation between AQI and PM2.5 levels?":
        correlation = data[['aqi', 'pm2_5']].corr().iloc[0, 1]
        return f"Correlation between AQI and PM2.5: {correlation:.2f}"

    elif question == "How does NO2 concentration vary across cities?":
        return data.groupby("city")["no2"].mean().to_string()

    elif question == "Which city has the highest SO2 pollution?":
        return data.groupby("city")["so2"].mean().idxmax()

    return "Sorry, I don't have an answer for that."

# Streamlit Chatbot Page
def chatbot_page():
    st.title("Air Quality Index Visualization Chatbot")
    
    st.markdown("<h5 style='color:red;'>Chat with ChatBot🤖 or Go to Conclusion Below 🏁⬇️</h5>", unsafe_allow_html=True)

    # Dropdown for predefined questions
    predefined_questions = [
        "What is the average AQI for each city?",
        "Which city has the highest average AQI?",
        "What is the highest recorded AQI and in which city?",
        "What is the lowest recorded AQI and in which city?",
        "What is the average AQI for each month?",
        "Which month had the worst air quality?",
        "Which month had the best air quality?",
        "Which city has the highest PM2.5 levels on average?",
        "Which city has the highest PM10 levels?",
        "Which city has the highest NO2 levels?",
        "Which city has the highest CO levels?",
        "What is the correlation between AQI and PM2.5 levels?",
        "How does NO2 concentration vary across cities?",
        "Which city has the highest SO2 pollution?"
    ]
    
    selected_question = st.selectbox("Choose a question:", ["Type your own question..."] + predefined_questions)

    # Chat input
    prompt = st.chat_input("Type your message here...") if selected_question == "Type your own question..." else selected_question

    if prompt:
        # Display user's question
        st.write(f"**User:** {prompt}")

        # Get the appropriate response
        answer = get_answer(prompt)

        # Display chatbot response
        st.write(f"**Chatbot:** {answer}")


        if st.button("➡️ Go to Conclusion"):
          st.session_state["page"] = "Conclusion"
          st.rerun()

# Conclusion Page Function
def conclusion_page():
        st.markdown("<h2 style='color:black;'>Conclusion📖</h2>", unsafe_allow_html=True)
    # Sample AQI Data (Replace with real calculations)
        max_aqi = 5
        min_aqi = 1
        avg_aqi = 3.92

# Conclusion Section
        st.header("📊 AQI Statistics")

        st.success(f"✅ **Maximum AQI:** {max_aqi}")
        st.success(f"✅ **Minimum AQI:** {min_aqi}")
        st.success(f"✅ **Average AQI:** {avg_aqi:.2f}")

        st.markdown("""
    <div style='padding: 20px; border-radius: 8px;'>
        <p style='font-size: 20px; color: #333;'>
            Air quality remains a <b>critical issue</b> in India, with significant disparities observed across regions.
        </p>
        <ul style='font-size: 18px; color: #555;'>
            <li><b>Delhi, Jorapokhar, and Amritsar</b> rank among the most polluted cities, with high PM2.5 and PM10 levels.</li>
            <li>In contrast, <b>Aizawl, Coimbatore, and Bengaluru</b> exhibit significantly cleaner air quality.</li>
            <li><b>Kolkata</b> records the highest PM10 and PM2.5 concentrations, surpassing all other regions.</li>
        </ul>
        <p style='font-size: 20px; color: #333;'>
            While some cities show improvements, the high pollutant concentrations in northern states highlight the need for stricter measures.
        </p>
        <h3 style='color: #2A3F54;'>Key Recommendations:</h3>
        <ul style='font-size: 18px; color: #555;'>
            <li>Enhance <b>pollution control policies</b> in high-risk areas like Delhi, Kolkata, and Patna.</li>
            <li>Reduce particulate matter emissions (PM2.5, PM10) through strict regulations.</li>
            <li>Encourage the adoption of <b>clean energy solutions</b> and public awareness programs.</li>
        </ul>
        <p style='font-size: 18px; color: #333;'>
            A region-specific approach is necessary to mitigate air pollution and protect public health across India.
        </p>
    </div>
    """, unsafe_allow_html=True)

        if st.button("🚪Log Out"):
         st.session_state["page"] = "Home"
         st.rerun()
# Logout Page Function
def logout():
    st.session_state["logged_in"] = False
    st.session_state["page"] = "Home"
    st.success("✅ Logged out successfully! Redirecting to Home...")
    st.rerun()
   
# Call the navigation menu function
navigation_menu()

# Render the selected page
if st.session_state["page"] == "Home":
    home_page()
elif st.session_state["page"] == "Login":
    login_page()
elif st.session_state["page"] == "Dashboard":
    dashboard_page()
elif st.session_state["page"] == "ChatBot":
    chatbot_page()
elif st.session_state["page"] == "Conclusion":
    conclusion_page()
elif st.session_state["page"] == "Logout":
    logout()