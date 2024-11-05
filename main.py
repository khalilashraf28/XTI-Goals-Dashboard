from time import sleep
import streamlit as st

st.markdown('''<style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stSidebar {
        display: none !important;
    }
    </style>''',unsafe_allow_html=True)
import streamlit as st

# Your existing CSS styling
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
    color: #6c757d;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}
.stApp {
    margin-bottom: 50px;
}
/* Background */
#root > div:nth-child(1) > div.withScreencast > div > div > div {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    background: linear-gradient(#46187091, #461870);            
}
/* Button */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(3) > div > button {
    display: flex;
    background: linear-gradient(180deg, #461870, #a31ba582);
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    transition: background 0.3s ease;
    margin: 0 auto;
    width: 400px;
    border-radius: 30px;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(3) > div > button:hover {
    background: linear-gradient(#a31ba582, #461870);
}
/* Title */
#welcome-to-xti-goals-dashboard {
    color: aliceblue;
    text-align: center;
    font-size: 34px; /* Increase font size */
    font-weight: bold;
    text-shadow: 2px 2px 8px rgb(72 4 88 / 37%), 0px 0px 5px #ffffff; /* Text shadow for a glowing effect */
    letter-spacing: 1.5px; /* Increase letter spacing for a refined look */
    font-family: 'Poppins', sans-serif; /* Change font to a modern, stylish font */
    background: -webkit-linear-gradient(#ffffff, #000000); /* Gradient effect within the text */
    -webkit-background-clip: text; /* Clip background to text */
    -webkit-text-fill-color: transparent; /* Make background gradient visible */
}
/* Username and password text */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(1) > div > label > div > p {
    color: floralwhite;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(2) > div > label > div > p {
    color: floralwhite;
}
/* Div */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px) saturate(150%);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    padding: 20px;
    transition: all 0.3s ease;
    margin-top: -40px;
}
/* Alert */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(4) > div > div {
    background: linear-gradient(45deg, #f5a6233d, #ff06062e);
    padding-top: 8px; padding-bottom: 8px;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(4) > div > div > div > div > div > div > p {
    color: white;
}
@media only screen and (max-width: 805px) {
    /* Div */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 {
        margin-top: 50px;
    }
    /* Button */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(3) > div > button {
        width: 300px;
    }
    /* Title */
    #welcome-to-xti-goals-dashboard {
        text-shadow: 2px 2px 2px rgb(72 4 88 / 37%), 0px 0px 2px #ffffff; /* Text shadow for a glowing effect */
    }
}
@media only screen and (max-width: 430px) {
    /* Button */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(3) > div > button {
        width: 100px;
    }
}
@media only screen and (max-width: 480px) {
    /* Div */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 {
        margin-top: 0px;
    }
    /* Button */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(3) > div > button {
        width: 100%;
    }
    /* Title */
    #welcome-to-xti-goals-dashboard {
        font-size: 28px; /* Reduce font size */
        margin-top: -100px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 {
        margin-top: 0px; 
    }

          
}
</style>
""", unsafe_allow_html=True)

# Footer HTML
st.markdown("""
<div class="footer">
    <p>© 2024 Xclusive Trading Inc. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)



#For Dark Theme
st.markdown("""
<style>
/* Footer styles */
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    /* background-color: #1f1f1f;  Darker background for the footer */
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
    /*color: #cfcfcf; /* Lighter text color for contrast */
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.5);
}

.stApp {
    margin-bottom: 50px;
}

/* Background */
#root > div:nth-child(1) > div.withScreencast > div > div > div {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    background: linear-gradient(#46187091, #461870);            
}

/* Button */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-qcpnpn.e1f1d6gn0 > div > div > div:nth-child(3) > div > button{
    display: flex;
    background: linear-gradient(180deg, #461870, #a31ba582);
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    transition: background 0.3s ease;
    margin: 0 auto;
    width: 400px;
    border-radius: 30px;
}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-qcpnpn.e1f1d6gn0 > div > div > div:nth-child(3) > div > button:hover {
    background: linear-gradient(#a31ba582, #461870);
}

/* Title */
#welcome-to-xti-goals-dashboard {
    color: aliceblue;
    text-align: center;
    font-size: 34px; /* Increase font size */
    font-weight: bold;
    text-shadow: 2px 2px 8px rgb(72 4 88 / 0%), 0px 0px 0px #ffffff;  /*Text shadow for a glowing effect */
    letter-spacing: 1.5px; /* Increase letter spacing for a refined look */
    font-family: 'Poppins', sans-serif; /* Change font to a modern, stylish font */
    background: -webkit-linear-gradient(#ffffff, #000000); /* Gradient effect within the text */
    -webkit-background-clip: text; /* Clip background to text */
    -webkit-text-fill-color: transparent; /* Make background gradient visible */
}

/* Username and password text */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(1) > div > label > div > p {
    color: floralwhite;
}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(2) > div > label > div > p {
    color: floralwhite;
}

/* Div */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-qcpnpn.e1f1d6gn0{
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px) saturate(150%);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    padding: 20px;
    transition: all 0.3s ease;
    margin-top: -40px;
}

/* Alert */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(4) > div > div {
    background: linear-gradient(45deg, #f5a6233d, #ff06062e);
    padding-top: 8px; padding-bottom: 8px;
}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 > div > div > div:nth-child(4) > div > div > div > div > div > div > p {
    color: white;
}

@media only screen and (max-width: 805px) {
    /* Div */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-qcpnpn.e1f1d6gn0{
        margin-top: 50px;
    }

    /* Button */
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-qcpnpn.e1f1d6gn0 > div > div > div:nth-child(3) > div > button {
        width: 300px;
    }

    /* Title */
    #welcome-to-xti-goals-dashboard {
        text-shadow: 2px 2px 2px rgb(72 4 88 / 37%), 0px 0px 2px #ffffff; /* Text shadow for a glowing effect */
    }
}

@media only screen and (max-width: 430px) {
    /* Button */
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-qcpnpn.e1f1d6gn0 > div > div > div:nth-child(3) > div > button{
        width: 100px;
    }
}

@media only screen and (max-width: 480px) {
    /* Div */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.st-emotion-cache-4uzi61.e1f1d6gn0 {
        margin-top: 60px;
        margin-top: 0px;
    }

    /* Title */
    #welcome-to-xti-goals-dashboard {
        font-size: 28px; /* Reduce font size */
        margin-top: -100px;
    }

}
</style>
""", unsafe_allow_html=True)

# Footer HTML
st.markdown("""
<div class="footer">
    <p>© 2024 Xclusive Trading Inc. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

def log_in():
    # Set the authentication status to True
    st.session_state["authentication_status"] = True
    st.session_state["logged_in"] = True
    st.switch_page("pages/app.py") 

def log_out():
    st.session_state["authentication_status"] = False
    st.success("Logged out!")
    sleep(0.5)

st.title("WELCOME TO XTI GOALS DASHBOARD")


with st.container(border=True):

    # st.header("Login Page")

    if not st.session_state.get("authentication_status", False):
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", key="password", type="password")

        if st.button("Login"):
            if username == "test" and password == "test":
                log_in()
            else: 
                st.warning("Username/Password is wrong. Try again!")
    else:
        st.rerun()
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# if st.button("Log in", type="primary"):
#     if username == "test" and password == "test":
#         st.session_state.logged_in = True
#         st.success("Logged in successfully!")
#         sleep(0.5)
#         st.switch_page("pages/app1.py")
#     else:
#         st.error("Incorrect username or password")