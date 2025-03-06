import streamlit as st
import streamlit.components.v1 as components
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.text import MIMEText

# Set page configuration
st.set_page_config(page_title="Air Quality Visualization App", layout="wide")

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "enter your email"
SMTP_PASSWORD = "enter your smtp password"  # ⚠️ Store this securely using environment variables or Streamlit secrets!
SENDER_EMAIL = SMTP_USER
RECEIVER_EMAIL = "enter your email"

def send_email(username, user_email, rating, feedback):
    """Function to send feedback via email with username included."""
    try:
        feedback_message = f"Feedback from {username} ({user_email}):\n\nRating: {rating} ⭐\n\n{feedback}"
        msg = MIMEText(feedback_message)
        msg["Subject"] = "New Feedback Received"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        
        st.success("✅ Thank you for your feedback! 😊")
    except Exception as e:
        st.error(f"❌ Error sending feedback: {e}")

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def apply_theme():
    if st.session_state.theme == "light":
        return """
            <style>
                body, .stApp { background-color: white; color: black; }
                .stSidebar, .sidebar-content { background-color: #f0f0f0 !important; color: black !important; }
                .stButton > button { background-color: #e0e0e0; color: black; border-radius: 8px; }
                h1, h2, h3, h4, h5, h6 { color: black !important; text-align: left; }
                .stSlider { color: black !important; }
            </style>
        """
    else:
        return """
            <style>
                body, .stApp { background-color: black; color: white; }
                .stSidebar, .sidebar-content { background-color: #111 !important; color: white !important; }
                .stButton > button { background-color: #333; color: white; border-radius: 8px; }
                h1, h2, h3, h4, h5, h6 { color: #ffcc00 !important; text-align: left; }
                .stSlider { color: white !important; }
            </style>
        """

st.markdown(apply_theme(), unsafe_allow_html=True)

def main():
    """Main function to handle authentication and navigation."""
    if not st.session_state.authenticated:
        show_signup()
    else:
        show_main_app()

def show_signup():
    """Display the signup page."""
    st.markdown("<h2 style='text-align: center;'>🔐 Sign Up</h2>", unsafe_allow_html=True)
    
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.button("Sign Up"):
        if not username or not password:
            st.warning("⚠️ Please fill in both fields.")
            time.sleep(2)
            st.rerun()
        else:
            st.session_state.username = username
            st.success(f"✅ Welcome, {username}! Successfully signed in!")
            st.session_state.authenticated = True
            time.sleep(2)
            st.rerun()

def show_main_app():
    """Display the main app with navigation and pages."""
    st.sidebar.title("Navigation")
    
    # Theme switch buttons
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("🌞 Light Mode"):
            st.session_state.theme = "light"
            st.session_state.theme_message = "☀️ Switched to Light Mode!"
            st.rerun()
    with col2:
        if st.button("🌙 Dark Mode"):
            st.session_state.theme = "dark"
            st.session_state.theme_message = "🌑 Switched to Dark Mode!"
            st.rerun()
    
    if "theme_message" in st.session_state:
        st.success(st.session_state.theme_message)
        time.sleep(2)
        del st.session_state.theme_message
        st.rerun()
    
    # Sidebar navigation
    st.sidebar.markdown("---")
    if st.sidebar.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.sidebar.button("📊 Dashboard"):
        st.session_state.page = "Dashboard"
    if st.sidebar.button("📈 Insights"):
        st.session_state.page = "Insights"
    if st.sidebar.button("💬 Feedback"):
        st.session_state.page = "Feedback"
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()
    
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    
    # Page content
    if st.session_state.page == "Home":
        st.header("🏠 Project Overview")
        st.write("""
            Air pollution is a critical environmental issue in India, affecting millions of people across cities and rural areas. Rapid urbanization, industrialization, and vehicular emissions have significantly contributed to the rising levels of pollutants such as Suspended Particulate Matter (SPM), Respirable Suspended Particulate Matter (RSPM/PM10), Sulfur Dioxide (SO₂), and Nitrogen Dioxide (NO₂). Poor air quality has severe health implications, including respiratory diseases, cardiovascular issues, and reduced life expectancy.

            This dashboard provides an interactive visualization of air quality data collected from various monitoring stations across India. It helps analyze pollutant trends across different states and cities, enabling users to explore maximum and minimum pollution levels, seasonal variations, and geographical patterns. The insights gained from this analysis can assist policymakers, environmental agencies, and citizens in understanding pollution hotspots and taking preventive measures.

            Our visualization enables users to:
            ✅ Identify the most and least polluted cities.
            ✅ Track air pollution trends over time.
            ✅ Compare pollution levels across different states.
            ✅ Analyze the impact of urbanization on air quality.
        """)
    elif st.session_state.page == "Dashboard":
        st.header("📊 Power BI Dashboard")
        powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZTdhMDA1ZjYtNzUzNS00OTU4LTllNTAtZmEwN2Y1YWQ1Njk5IiwidCI6IjlkOTI5ODkyLTJlMGMtNGJhMS1iOWNjLTA0YmJlNjFlZjc1NSJ9"
        components.html(
            f'<iframe width="600" height="373.5" src="{powerbi_url}" frameborder="0" allowFullScreen></iframe>',
            height=500
        )
    elif st.session_state.page == "Insights":
        st.header("📈 Insights")
        
        data = pd.DataFrame({
            'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Hyderabad'],
            'PM2.5': [140, 90, 60, 110, 85]
        })
        
        st.markdown("### 🏙️ Top 5 Polluted Cities")
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.barplot(data=data, x='City', y='PM2.5', hue='City', palette='Reds', legend=False, ax=ax)
        st.pyplot(fig)
        st.write("Higher PM2.5 levels indicate poorer air quality, which can have serious health impacts, especially in metropolitan areas. Delhi has the highest PM2.5 level among the selected cities.")
        
        st.markdown("### 🌦️ Seasonal Air Pollution")
        seasons = ['Winter', 'Summer', 'Monsoon', 'Post-Monsoon']
        pm_values = [150, 90, 50, 100]
        
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.lineplot(x=seasons, y=pm_values, marker='o', color='blue', linewidth=2, ax=ax)
        ax.set_ylabel("Avg PM2.5", fontsize=9)
        ax.set_xlabel("Seasons", fontsize=9)
        ax.set_title("PM2.5 Seasonal Variation", fontsize=11, fontweight='bold')
        st.pyplot(fig)
        st.write("Air pollution levels fluctuate across seasons, with winter experiencing the highest PM2.5 concentrations due to increased heating, industrial emissions, and weather conditions that trap pollutants near the ground.")
        st.subheader("🚗 Impact of Traffic Density on Air Pollution")
        traffic_data = pd.DataFrame({
        'Traffic Density': ['Low', 'Medium', 'High', 'Very High'],
        'PM2.5': [50, 85, 120, 160]
    })

        fig, ax = plt.subplots(figsize=(6, 3))  # Reduced size
        sns.barplot(data=traffic_data, x='Traffic Density', y='PM2.5', hue='Traffic Density', palette='Blues', legend=False, ax=ax)
        ax.set_ylabel("PM2.5 Level", fontsize=9)
        ax.set_xlabel("Traffic Density", fontsize=9)
        ax.set_title("Traffic Density vs PM2.5", fontsize=11, fontweight='bold')
        ax.tick_params(axis='both', labelsize=9)
        st.pyplot(fig)

        st.write("""
        Higher traffic density correlates with **higher air pollution levels**. 
        Areas with **very high traffic congestion** tend to have nearly **3x more PM2.5 pollution** than low-density areas. 
        Implementing better traffic management can help reduce pollution.
    """)

    
        st.subheader("🏭 Industrial vs Residential Pollution Levels")
        area_data = pd.DataFrame({
        'Area Type': ['Residential', 'Commercial', 'Industrial'],
        'PM2.5': [60, 100, 180]
        })

        fig, ax = plt.subplots(figsize=(6, 3))  # Reduced size
        sns.barplot(data=area_data, x='Area Type', y='PM2.5', hue='Area Type', palette='Greens', legend=False, ax=ax)
        ax.set_ylabel("PM2.5 Level", fontsize=9)
        ax.set_xlabel("Area Type", fontsize=9)
        ax.set_title("Pollution Levels: Industrial vs Residential", fontsize=11, fontweight='bold')
        ax.tick_params(axis='both', labelsize=9)
        st.pyplot(fig)

        st.write("""
        Industrial areas experience **significantly higher pollution** than residential areas, often exceeding **180 µg/m³** in PM2.5 levels. 
        This highlights the need for **stricter regulations** and **pollution control measures** in heavily industrialized zones.
       """)

    elif st.session_state.page == "Feedback":
        st.header("💬 Feedback")
        user_email = st.text_input("Your Email", placeholder="Enter your email")
        feedback = st.text_area("We'd love to hear your thoughts!")
        rating = st.slider("⭐ Rate our app:", min_value=1, max_value=5, value=5)
        
        if st.button("Submit Feedback"):
            if not user_email.strip():
                st.warning("⚠️ Please enter your email before submitting.")
            elif not feedback.strip():
                st.warning("⚠️ Please enter your feedback before submitting.")
            else:
                send_email(st.session_state.username, user_email, rating, feedback)
if __name__ == "__main__":
    main()
