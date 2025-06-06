import requests
import streamlit as st

# Function to fetch data using pincode
def post(pincode):
    url = f"https://api.postalpincode.in/pincode/{pincode}"
    response = requests.get(url)
    return response.json()

# Function to fetch data using city name
def city(city_name):
    url = f"https://api.postalpincode.in/postoffice/{city_name}"
    response = requests.get(url)
    return response.json()

# Main Streamlit app
def main():
    st.title("📮 Indian Post Office Finder")

    # Input from user
    user_input = st.text_input("Enter your **Pincode** or **City Name**")

    # When user clicks submit
    if st.button("Submit"):
        if user_input.strip():
            # If the input is digits, treat as pincode
            if user_input.isdigit():
                result = post(user_input)
            else:
                result = city(user_input)

            # Check if result is valid
            if result and result[0]['Status'] == "Success":
                post_offices = result[0]['PostOffice']
                for office in post_offices:
                    st.subheader(f"{office['Name']}")
                    st.markdown(f"""
                        **District**: {office['District']}  
                        **State**: {office['State']}  
                        **Pincode**: {office['Pincode']}  
                        **Branch Type**: {office['BranchType']}  
                        **Delivery Status**: {office['DeliveryStatus']}  
                    """)
            else:
                st.warning("❌ No data found. Please enter a valid Pincode or City name.")
        else:
            st.warning("⚠️ Please enter something to search.")

if __name__ == "__main__":
    main()
