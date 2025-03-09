import streamlit as st
from zxcvbn import zxcvbn

def get_password_strength(password):
    result = zxcvbn(password)
    score = result['score']  
    feedback = result['feedback']['suggestions'] 
    
    return score, feedback

def main():
    st.title("💪Password Strength Meter")
    
    password = st.text_input("Enter your password", type="password")

    if password:
        score, feedback = get_password_strength(password)
        

        if score == 0:
            strength = "Very Weak😩"
            color = "red"
        elif score == 1:
            strength = "Weak😞"
            color = "orange"
        elif score == 2:
            strength = "Moderate😊"
            color = "yellow"
        elif score == 3:
            strength = "Strong🔩"
            color = "green"
        else:
            strength = "Very Strong🔥"
            color = "darkgreen"

      
        st.markdown(f"<h3 style='color:{color};'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

 
        if feedback:
            st.write("Suggestions to improve your password:")
            for suggestion in feedback:
                st.write(f"- {suggestion}")
        else:
            st.write("Your password is strong💪!")
if __name__ == "__main__":
    main()
