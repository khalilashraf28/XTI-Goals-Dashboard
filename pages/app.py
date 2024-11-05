# app.py:
import pandas as pd
import re
import streamlit as st
import base64
from io import BytesIO
from datetime import datetime
import time
st.markdown('''<style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stSidebar.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-79elbk.eczjsme17 {
        display: none !important;
    }
    </style>''',unsafe_allow_html=True)

# # Check if the user is authenticated
if not st.session_state.get("authentication_status", False):
    st.warning("Please login first. Redirecting in 2 seconds...")
    time.sleep(0.5)
    st.switch_page("./main.py")  # Redirect to the login page

# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#     section.stAppViewMain.main  {
#         background-image: url("data:image/png;base64,%s");
#         background-size: contain;  
#         background-position: center;  
#         background-repeat: no-repeat;
#     }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)
# set_background('111.png')

st.markdown('''<style>
    /*body*/
    #root > div:nth-child(1) > div > div > div > div{
        background-color:pink;/*#4618708a*/
    }
    #root > div:nth-child(1) > div > div > div > header{
        background-color:pink;
    }
    /*body header*/        
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div {
        margin-left: -70px;
        width: 850px;}
            
    /*deploy button*/
    #root > div:nth-child(1) > div > div > div > header > div> div > button{
        background-color: white;
        border: 1px solid;
    }  
    /*: button*/
    #MainMenu > button{
        background-color: white;
        border: 1px solid;
    }              
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div {
        margin-top: -55px;}
    
    /*logo img sidebar*/
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stSidebar.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-sih973.eczjsme12 > div > div > div > div > div:nth-child(1) > div > div > div > img {
        width: 80%;
        margin-top: -25px;
        margin-left: 20px;}
            
    #xti-goals-dashboard {
        background: linear-gradient(45deg, #d1227f, #ff8cb8);
        /*border: 1px solid #ccc;*/
        border-radius: 10px;
        font-family: Arial, sans-serif;
        color: white;
        text-align: center;
        margin-bottom: 20px;
        margin-top:-20px;
        /*border: solid 3px #d1227f;*/
    }
    /*Button*/
        #root > div:nth-child(1) > div > div > div > div > section > div > div > div > div > div > details > div > div > div > div > div:nth-child(3) > div > button{
        Background-color:purple;
        color:white;
    }

   #root > div:nth-child(1) > div > div > div > div > section > div > div > div > div > div > details > div > div > div > div > div:nth-child(3) > div > button:hover{
        Background-color:pink;
        color:white;
    }
    /*logout button*/
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stSidebar.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-sih973.eczjsme12 > div > div > div > div > div:nth-child(9) > div > button{
        background-color: #ff0000;
        border-color: #ffffff;
        color: white;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stSidebar.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-sih973.eczjsme12 > div > div > div > div > div:nth-child(9) > div > button:hover{
        background-color: purple;
        border-color: #ffffff;
        color: white;
    }
    /*Dataframe div*/
    #root > div:nth-child(1) > div > div > div > div > section > div > div > div > div > div > details{
        background: linear-gradient(45deg, #461870e6, #9c4dccab);
        color:white;
        border-style: none;
        border-width: none;
        border-color: none;
    }
    /*Select Market Text*/
    #root > div:nth-child(1) > div > div > div > div > section> div> div > div > div > div > details > div > div > div > div > div:nth-child(1) > div > label{
        color:white;
    }

        @media only screen and (max-width: 500px) {
    /*Title*/
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div{
        width: 320px;
        margin-left: 80px;
    }
    /*Dataframe*/
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stExpander.st-emotion-cache-0.eqpbllx4{
        width: 340px;
        margin-left: 70px;    
    }
    
    /*Button*/
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div:nth-child(7) > div > button{
        margin-left:60px;    
    }

}   
            
    @media only screen and (max-width: 390px) {
    /*Title*/
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div{
        width: 320px;
        margin-left: 40px;
    }
    /*Dataframe*/
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stExpander.st-emotion-cache-0.eqpbllx4{
        width: 340px;
        margin-left: 35px;    
    }
    /*Button*/
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div:nth-child(7) > div > button{
        margin-left:40px;    
    }

}      
    </style>''',unsafe_allow_html=True)
st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] { 
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def read_excel_with_error_handling(file_path, sheet_name=None, **kwargs):
    """Reads an Excel file and handles errors."""
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, **kwargs)
        return df
    except FileNotFoundError:
        st.warning(f"Error: The file '{file_path}' was not found.")
    except ValueError as e:
        st.warning(f"Error: {e}. Check if the sheet name '{sheet_name}' exists in '{file_path}'.")
    except Exception as e:
        st.warning(f"An unexpected error occurred in file : {e}")

# # Read the Shopper Tracker Excel file

df_shopper_track = read_excel_with_error_handling("ShopperTracker.xlsx", sheet_name='Sheet1')
try:
    df_shopper_track.columns = [pd.to_datetime(col).strftime('%b-%y') if re.match(r'\d{4}-\d{2}-\d{2}', str(col)) else str(col) for col in df_shopper_track.columns]
    month_patterns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_columns = [col for col in df_shopper_track.columns if any(month in col for month in month_patterns)]
    last_12_months = month_columns[-12:]  # Get only the last 12 month columns
    columns_to_keep = [col for col in df_shopper_track.columns if col not in month_columns] + last_12_months
    df_shopper_track = df_shopper_track[columns_to_keep]
    df_shopper_track['Store'] = df_shopper_track['Store'].str.upper()   
except ValueError as e:
        st.warning(f"Error: {e}.")
except Exception as e:
        st.warning(f"An unexpected error occurred in file : {e}")
# # Read other Excel files with error handling


try:
    df_metro_target = pd.read_excel("metrotarget.xlsx")
except FileNotFoundError:
        st.warning(f"Error: The file performance by market was not found.")
except ValueError as e:
        st.warning(f"Error: {e}. Check if the sheet name sheet name exists in performance by market remove all extra sheet.")
except Exception as e:
        st.warning(f"An unexpected error occurred in file : {e}")


try:
    df_perf_by_market = pd.read_excel('perfbymarket.xls', engine='xlrd')
except FileNotFoundError:
        st.warning(f"Error: The file performance by market was not found.")
except ValueError as e:
        st.warning(f"Error: {e}. Check if the sheet name sheet name exists in performance by market remove all extra sheet.")
except Exception as e:
        st.warning(f"An unexpected error occurred in file : {e}")
# df_perf_by_market = pd.read_excel('perfbymarket.xls', engine='xlrd')
df_smart_pay = read_excel_with_error_handling("smartpay.xlsx", sheet_name='Sheet1')
df_mapping = read_excel_with_error_handling("mapping.xlsx", sheet_name='Sheet1')

# df_last_month = pd.read_csv('last_month_goals.csv')
df_last_month = pd.read_excel('Copy of XTI Goals October 2024.xlsx')

df_last_month =  df_last_month[['Market','Store','PPD','Accessory']]

try:
    def shopertrack_12month_avg(df):
        df.columns = df.columns.str.strip()
        month_pattern = re.compile(r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s\-]\d{2,4}')
        month_columns = [col for col in df.columns if re.match(month_pattern, col)]

        if len(month_columns) != 12:
            raise ValueError(f"Expected 12 month columns, but found {len(month_columns)}")

        df['AVG'] = df[month_columns].apply(pd.to_numeric, errors='coerce').mean(axis=1)
        return df
    
    if 'ShopperTrak__percentages' not in st.session_state:
        st.session_state.ShopperTrak__percentages = {'ALABAMA': 13.5/100, 'AMARILLO': 11.0/100, 'ARKANSAS': 11/100, 'AUSTIN': 11.5/100, 'COLORADO': 11.5/100, 'CORPUS CHRISTI': 11/100,
                                                 'DALLAS': 11/100, 'HOUSTON': 11.5/100, 'KANSAS': 11.5/100, 'MISSISSIPPI': 10/100, 'OKLAHOMA': 11.5/100, 'OMAHA': 11.5/100, 'ORLANDO': 10.5/100,
                                                 'SAN ANTONIO': 11/100, 'SPRINGFIELD': 12/100, 'ST. LOUIS': 11.5/100, 'TAMPA': 10.5/100, 'CONNECTICUT': 9/100, 'MASSACHUSETTS': 9/100,
                                                 'NEW YORK': 9/100, 'TENNESSEE': 12/100, 'SOUTH FLORIDA 1': 12/100, 'SOUTH FLORIDA 2': 12/100}


    def apply_conversion(goal_data, market_percentages):
        goal_data['ShopperTrak Conv %'] = goal_data.apply(
            lambda row: row['Last 12 Months ShopperTrak'] * market_percentages.get(row['Market'], 0),
            axis=1
        )
        return goal_data

    if 'Accessories__percentages' not in st.session_state:
        st.session_state.Accessories__percentages = {'ALABAMA': 50/100, 'AMARILLO': 37.5/100, 'ARKANSAS': 40/100, 'AUSTIN': 42.5/100, 'COLORADO': 45/100, 'CORPUS CHRISTI': 40/100,
                                                 'DALLAS': 40/100, 'HOUSTON': 40/100, 'KANSAS': 45/100, 'MISSISSIPPI': 35/100, 'OKLAHOMA': 45/100, 'OMAHA': 45/100, 'ORLANDO': 40/100,
                                                 'SAN ANTONIO': 40/100, 'SPRINGFIELD': 50/100, 'ST. LOUIS': 45/100, 'TAMPA': 40/100, 'CONNECTICUT': 55/100, 'MASSACHUSETTS': 55/100,
                                                 'NEW YORK': 55/100, 'TENNESSEE': 50/100, 'SOUTH FLORIDA 1': 50/100, 'SOUTH FLORIDA 2': 50/100}

    def apply_conversion_accessorries(goal_data, market_percentages):
        goal_data['Accessory'] = goal_data.apply(lambda row: row['PPD'] * market_percentages.get(row['Market'], 0),axis=1)
        return goal_data

    if 'Upgrade_value' not in st.session_state:
        st.session_state.Upgrade_value = {'ALABAMA': 35/100, 'AMARILLO': 35/100, 'ARKANSAS': 35/100, 'AUSTIN': 35/100, 'COLORADO': 35/100, 'CORPUS CHRISTI': 35/100,
                                      'DALLAS': 35/100, 'HOUSTON': 35/100, 'KANSAS': 35/100, 'MISSISSIPPI': 35/100, 'OKLAHOMA': 35/100, 'OMAHA': 35/100, 'ORLANDO': 35/100,
                                      'SAN ANTONIO': 35/100, 'SPRINGFIELD': 35/100, 'ST. LOUIS': 35/100, 'TAMPA': 35/100, 'CONNECTICUT': 35/100, 'MASSACHUSETTS': 35/100,
                                      'NEW YORK': 35/100, 'TENNESSEE': 35/100, 'SOUTH FLORIDA 1': 35/100, 'SOUTH FLORIDA 2': 35/100}

    def apply_conversion_upgrade(goal_data, market_percentages):
        goal_data['Upgrade'] = goal_data.apply(lambda row: row['ST Quota'] * market_percentages.get(row['Market'], 0),axis=1)
        return goal_data
    
    if 'Upgrade_value_bts' not in st.session_state:
        st.session_state.Upgrade_value_bts = {'ALABAMA': 35/100, 'AMARILLO': 35/100, 'ARKANSAS': 35/100, 'AUSTIN': 35/100, 'COLORADO': 35/100, 'CORPUS CHRISTI': 35/100,
                                      'DALLAS': 35/100, 'HOUSTON': 35/100, 'KANSAS': 35/100, 'MISSISSIPPI': 35/100, 'OKLAHOMA': 35/100, 'OMAHA': 35/100, 'ORLANDO': 35/100,
                                      'SAN ANTONIO': 35/100, 'SPRINGFIELD': 35/100, 'ST. LOUIS': 35/100, 'TAMPA': 35/100, 'CONNECTICUT': 35/100, 'MASSACHUSETTS': 35/100,
                                      'NEW YORK': 35/100, 'TENNESSEE': 35/100, 'SOUTH FLORIDA 1': 35/100, 'SOUTH FLORIDA 2': 35/100}

    def apply_conversion_upgrade_bts(goal_data, market_percentages):
        goal_data['Upgrade BTS'] = goal_data.apply(lambda row: row['ST BTS'] * market_percentages.get(row['Market'], 0),axis=1)
        return goal_data
    
    if 'Retaintion_target' not in st.session_state:
        st.session_state.Retaintion_target = {'ALABAMA': 60/100, 'AMARILLO': 60/100, 'ARKANSAS': 60/100, 'AUSTIN': 60/100, 'COLORADO': 60/100, 'CORPUS CHRISTI': 60/100,
                                            'DALLAS': 60/100, 'HOUSTON': 60/100, 'KANSAS': 60/100, 'MISSISSIPPI': 60/100, 'OKLAHOMA': 60/100, 'OMAHA': 60/100, 'ORLANDO': 60/100,
                                            'SAN ANTONIO': 60/100, 'SPRINGFIELD': 60/100, 'ST. LOUIS': 60/100, 'TAMPA': 60/100, 'CONNECTICUT': 60/100, 'MASSACHUSETTS': 60/100,
                                            'NEW YORK': 60/100, 'TENNESSEE': 60/100, 'SOUTH FLORIDA 1': 60/100, 'SOUTH FLORIDA 2': 60/100}


    def apply_conversion_retaintion_target(goal_data, market_percentages):
        goal_data['Retention target'] = goal_data.apply(lambda row: row['ST Quota'] * market_percentages.get(row['Market'], 0),axis=1)
        return goal_data
        
    st.sidebar.image("logo.png")
    st.sidebar.title("Please Filter Here:")

    unique_markets = ['ALABAMA','AMARILLO','ARKANSAS','AUSTIN' ,'COLORADO' ,'CONNECTICUT' ,'CORPUS CHRISTI', 'DALLAS' ,'HOUSTON' ,'KANSAS' ,
                    'MASSACHUSETTS' ,'MISSISSIPPI', 'NEW YORK', 'OKLAHOMA' ,'OMAHA','ORLANDO', 'SAN ANTONIO' , 'SOUTH FLORIDA 1' ,
                    'SOUTH FLORIDA 2','ST. LOUIS','TAMPA', 'TENNESSEE']

    markets_list = ['All'] + list(unique_markets)
    selected_market = st.sidebar.selectbox("Select Market:", markets_list)

    # Input fields for new values
    if selected_market == "All":
        st.sidebar.warning("Please Select market to edit values!")
    else:
        new_upgrade_value = st.sidebar.number_input(f"Enter new Upgrade Value for {selected_market}", value=0.0, step=1.0) / 100
        new_upgrade_value_bts = st.sidebar.number_input(f"Enter new BTS Upgrade Value for {selected_market}", value=0.0, step=1.0) / 100
        new_ShopperTrak__percentages_value = st.sidebar.number_input(f"Enter new Expected PPD by ST Clicks Value for {selected_market}", value=0.0, step=1.0) / 100
        new_accessories_value = st.sidebar.number_input(f"Enter new Accessory Value for {selected_market}", value=0.0, step=1.0) / 100
        new_Retaintion_target_value = st.sidebar.number_input(f"Enter new Retention Target Value for {selected_market}", value=0.0, step=1.0) / 100
        
        # Button to save updates
        if st.sidebar.button("Save Updates"):
            if selected_market != 'All':
                st.session_state.Upgrade_value[selected_market] = new_upgrade_value
                st.session_state.ShopperTrak__percentages[selected_market] = new_ShopperTrak__percentages_value
                st.session_state.Accessories__percentages[selected_market] = new_accessories_value
                st.session_state.Retaintion_target[selected_market] = new_Retaintion_target_value
                st.session_state.Upgrade_value_bts[selected_market] = new_upgrade_value_bts
            else:
                for market in st.session_state.Upgrade_value:
                    st.session_state.Upgrade_value[market] = new_upgrade_value
                    st.session_state.ShopperTrak__percentages[market] = new_ShopperTrak__percentages_value
                    st.session_state.Accessories__percentages[market] = new_accessories_value
                    st.session_state.Retaintion_target[market] = new_Retaintion_target_value
                    st.session_state.Upgrade_value_bts[market] = new_upgrade_value_bts

    mapping_df = df_mapping
    goal_df = mapping_df[['Market', 'Store']]
    goal_data = goal_df
    goal_data = goal_data.sort_values(by=['Market', 'Store']).reset_index(drop=True)
    goal_data = goal_data.merge(mapping_df[['Store', 'DM']], on='Store', how='left')
    goal_data = goal_data.merge(mapping_df[['Store', 'RSM']], on='Store', how='left')
    df_metro_target['Metro Quota'] = df_metro_target['Voice Acts'] + df_metro_target['Voice Reacts']
    df_metro_target = df_metro_target.merge(df_mapping[['Dealer Code', 'Store']],left_on='MDealerCode', right_on='Dealer Code', how='left')
    df_metro_target = df_metro_target.drop(columns=['Dealer Code'])
    goal_data = goal_data.merge(df_metro_target[['Store', 'Metro Quota']], on='Store', how='left')
    df_metro_target['Metro BTS'] = df_metro_target['BTS Acts'] + df_metro_target['BTS Reacts']
    goal_data = goal_data.merge(df_metro_target[['Store', 'Metro BTS']], on='Store', how='left')
    df_metro_target['Metro HINT'] = df_metro_target['HSI Activations'] + df_metro_target['HSI Reactivations']
    goal_data = goal_data.merge(df_metro_target[['Store', 'Metro HINT']], on='Store', how='left')
    goal_data = goal_data.merge(df_metro_target[['Store', 'Magenta in Metro']], on='Store', how='left')
    goal_data.rename(columns={'Magenta in Metro': 'Magenta In Metro'}, inplace=True)
    goal_data['Total Quota'] = goal_data['Metro Quota'] + goal_data['Metro BTS'] + goal_data['Metro HINT'] #+ goal_data['Magenta In Metro']
    df_metro_target['Metro HINT'] = df_metro_target['HSI Activations'] + df_metro_target['HSI Reactivations']
    goal_data = goal_data.merge(df_metro_target[['Store', 'Metro HINT']], on='Store', how='left')
    df_shopper_track = shopertrack_12month_avg(df_shopper_track)
    goal_data = goal_data.merge(df_shopper_track[['Store', 'AVG']], on='Store', how='left')
    goal_data.rename(columns={'AVG': 'Last 12 Months ShopperTrak'}, inplace=True)
    apply_conversion(goal_data, st.session_state.ShopperTrak__percentages)
    df_shopper_track = df_shopper_track.merge(df_metro_target[['Store', 'Metro Quota']], on='Store', how='left') 
    UpgradeValue = 35/100
    df_shopper_track['Upg'] = df_shopper_track['Metro Quota'] * UpgradeValue
    df_shopper_track = df_shopper_track.merge(df_metro_target[['Store', 'Metro BTS']], on='Store', how='left') 
    df_shopper_track = df_shopper_track.merge(df_metro_target[['Store', 'Metro HINT']], on='Store', how='left') 
    df_shopper_track = df_shopper_track.merge(df_metro_target[['Store', 'Magenta in Metro']], on='Store', how='left') 
    df_shopper_track.rename(columns={'Magenta in Metro': 'MIM'}, inplace=True) 
    df_shopper_track['Total'] = df_shopper_track['Metro Quota'] + df_shopper_track['Upg'] + df_shopper_track['Metro BTS'] + df_shopper_track['Metro HINT'] #+ df_shopper_track['MIM']
    df_shopper_track['Quota %'] = (df_shopper_track['Metro Quota'] / df_shopper_track['Total'])*100 
    df_shopper_track = df_shopper_track.merge(goal_data[['Store', 'ShopperTrak Conv %']], on='Store', how='left')
    df_shopper_track.rename(columns={'ShopperTrak Conv %': '%'}, inplace=True)
    df_shopper_track['Quota AVG'] = (df_shopper_track['%']*df_shopper_track['Quota %'])/100 
    # Mapping 'Store' values in df_shopper_track with corresponding 'Last 12 Months ShopperTrak' values in goals_data
    # df_shopper_track['AVG'] = df_shopper_track['AVG'].fillna(
    #     df_shopper_track['Store'].map(goal_data.set_index('Store')['Last 12 Months ShopperTrak'])
    # )

    ######
    # st.write(df_shopper_track[(df_shopper_track['Store'] == 'OXFORD') | (df_shopper_track['Store'] == 'LOCKWOOD')| (df_shopper_track['Store'] == '549 GREENS')| (df_shopper_track['Store'] == '7900 NW 27TH')])
    #st.write(df_shopper_track[(df_shopper_track['Metro Quota'].isnull())])
    # st.write(df_shopper_track[(df_shopper_track['AVG'].isnull())])

    if 'Metro Quota' in df_shopper_track.columns and 'Total' in df_shopper_track.columns:
        df_shopper_track['Quota %'] = (df_shopper_track['Metro Quota'] / df_shopper_track['Total']) * 100
        df_shopper_track['Quota AVG'] = (df_shopper_track['%'] * df_shopper_track['Quota %']) / 100
    else:
        print("Required columns ('Metro Quota' and 'Total') are missing from df_shopper_track.")

    if 'ShopperTrak Conv %' in goal_data.columns and 'Store' in goal_data.columns:
        for i in range(len(goal_data)):
            if goal_data['ShopperTrak Conv %'].iloc[i] > 0:
                store = goal_data['Store'].iloc[i]
                if store in df_shopper_track['Store'].values:
                    goal_data.at[i, 'Quota AVG'] = df_shopper_track.loc[df_shopper_track['Store'] == store, 'Quota AVG'].values[0]
                else:
                    goal_data.at[i, 'Quota AVG'] = None  # or set a default value
            else:
                goal_data.at[i, 'Quota AVG'] = goal_data['Metro Quota'].iloc[i]
    else:
        print("Columns 'ShopperTrak Conv %' or 'Store' do not exist in goal_data.")

    goal_data.rename(columns={'Quota AVG': 'ST Quota'}, inplace=True)
    goal_data.rename(columns={'Metro HINT_x': 'Metro HINT'}, inplace=True) 
    goal_data = goal_data.drop(columns=['Metro HINT_y'])
    apply_conversion_upgrade(goal_data, st.session_state.Upgrade_value)

    if 'Metro BTS' in df_shopper_track.columns and 'Total' in df_shopper_track.columns:
        df_shopper_track['BTS %'] = (df_shopper_track['Metro BTS'] / df_shopper_track['Total']) * 100
        df_shopper_track['BTS AVG'] = (df_shopper_track['%'] * df_shopper_track['BTS %']) / 100
    else:
        st.warning("Required columns ('Metro BTS' and 'Total') are missing from df_shopper_track.")    
    if 'ShopperTrak Conv %' in goal_data.columns and 'Store' in goal_data.columns:
        for i in range(len(goal_data)):
            if goal_data['ShopperTrak Conv %'].iloc[i] > 0:
                store = goal_data['Store'].iloc[i]
                if store in df_shopper_track['Store'].values:
                    goal_data.at[i, 'BTS AVG'] = df_shopper_track.loc[df_shopper_track['Store'] == store, 'BTS AVG'].values[0]
                else:
                    goal_data.at[i, 'BTS AVG'] = None
            else:
                goal_data.at[i, 'BTS AVG'] = goal_data['Metro BTS'].iloc[i]
    else:
        print("Column 'ShopperTrak Conv %' or 'Store' does not exist in goal_data.")

    goal_data.rename(columns={'BTS AVG': 'ST BTS'}, inplace=True)
    apply_conversion_upgrade_bts(goal_data, st.session_state.Upgrade_value_bts)
    if 'Metro HINT' in df_shopper_track.columns and 'Total' in df_shopper_track.columns:
        # Calculate 'HINT %' and 'HINT AVG'
        df_shopper_track['HINT %'] = (df_shopper_track['Metro HINT'] / df_shopper_track['Total']) * 100
        df_shopper_track['HINT AVG'] = (df_shopper_track['%'] * df_shopper_track['HINT %']) / 100
    else:
        print("Required columns ('Metro HINT' and 'Total') are missing from df_shopper_track.")

    if 'ShopperTrak Conv %' in goal_data.columns and 'Store' in goal_data.columns:
        for i in range(len(goal_data)):
            if goal_data['ShopperTrak Conv %'].iloc[i] > 0:
                store = goal_data['Store'].iloc[i]
                if store in df_shopper_track['Store'].values:
                    goal_data.at[i, 'HINT AVG'] = df_shopper_track.loc[df_shopper_track['Store'] == store, 'HINT AVG'].values[0]
                else:
                    goal_data.at[i, 'HINT AVG'] = None
            else:
                goal_data.at[i, 'HINT AVG'] = goal_data['Magenta In Metro'].iloc[i]
    else:
        print("Columns 'ShopperTrak Conv %' or 'Store' do not exist in goal_data.")

    goal_data.rename(columns={'HINT AVG': 'ST HINT'}, inplace=True)

    # if 'MIM' in df_shopper_track.columns and 'Total' in df_shopper_track.columns:
    #     df_shopper_track['MIM %'] = (df_shopper_track['MIM'] / df_shopper_track['Total']) * 100
    #     df_shopper_track['MIM AVG'] = (df_shopper_track['%'] * df_shopper_track['MIM %']) / 100
    # else:
    #     print("Required columns ('MIM' and 'Total') are missing from df_shopper_track.")

    # if 'ShopperTrak Conv %' in goal_data.columns and 'Store' in goal_data.columns:
    #     for i in range(len(goal_data)):
    #         if goal_data['ShopperTrak Conv %'].iloc[i] > 0:
    #             store = goal_data['Store'].iloc[i]
    #             if store in df_shopper_track['Store'].values:
    #                 goal_data.at[i, 'MIM AVG'] = df_shopper_track.loc[df_shopper_track['Store'] == store, 'MIM AVG'].values[0]
    #             else:
    #                 goal_data.at[i, 'MIM AVG'] = None  # or set a default value
    #         else:
    #             goal_data.at[i, 'MIM AVG'] = goal_data['Magenta In Metro'].iloc[i]
    # else:
    #     print("Columns 'ShopperTrak Conv %' or 'Store' do not exist in goal_data.")

    # goal_data.rename(columns={'MIM AVG': 'ST MIM'}, inplace=True)
    goal_data['PPD'] = goal_data['ST Quota'] + goal_data['ST BTS'] + goal_data['ST HINT']  + goal_data['Upgrade'] #+ goal_data['ST MIM']
    apply_conversion_accessorries(goal_data, st.session_state.Accessories__percentages)
    goal_data['Accessory'] = goal_data['Accessory'] * 100
    apply_conversion_retaintion_target(goal_data,st.session_state.Retaintion_target)
    df_perf_by_market.rename(columns={'company': 'Store'}, inplace=True)
    goal_data = goal_data.merge(df_perf_by_market[['Store', 'totact']], on='Store', how='left')
    goal_data.rename(columns={'totact': 'Last Month Actual (PPD)'}, inplace=True)
    df_last_month.rename(columns={'PPD': 'Last Month Goal (PPD)'}, inplace=True)
    goal_data = goal_data.merge(df_last_month[['Store', 'Last Month Goal (PPD)']], on='Store', how='left')
    df_perf_by_market.rename(columns={'company': 'Store'}, inplace=True)
    goal_data = goal_data.merge(df_perf_by_market[['Store', 'totaccessory']], on='Store', how='left')
    goal_data.rename(columns={'totaccessory': 'Last Month Actual (Acc)'}, inplace=True)
    df_last_month.rename(columns={'Accessory': 'Last Month Goal (Acc)'}, inplace=True)
    goal_data = goal_data.merge(df_last_month[['Store', 'Last Month Goal (Acc)']], on='Store', how='left')
    goal_data['ACC/BOX'] = goal_data['Last Month Actual (Acc)'] / goal_data['Last Month Actual (PPD)']
    goal_data = goal_data.merge(df_perf_by_market[['Store', 'totpaymentqty']], on='Store', how='left')
    goal_data.rename(columns={'totpaymentqty': 'Last Month BP'}, inplace=True)
    goal_data['Bill Payments Conv%'] = (goal_data['Last Month Actual (PPD)'] / goal_data['Last Month BP'])*100

    def subtotal(data, name_col, quantity_cols):
        if isinstance(data, dict):
            df = pd.DataFrame(data)
        else:
            df = data.copy()

        df.sort_values(by=[name_col], inplace=True)
        totals_df = df.groupby(name_col)[quantity_cols].sum().reset_index()
        result_rows = []

        for name, group in df.groupby(name_col):
            result_rows.append(group)  
            subtotal_row_data = {name_col: f'{name} Total'}
            subtotal_row_data.update({f'{col}': group[col].sum() for col in quantity_cols})
            subtotal_row = pd.DataFrame([subtotal_row_data], columns=[name_col] + [f'{col}' for col in quantity_cols])
            result_rows.append(subtotal_row) 

        grand_total_row_data = {name_col: 'Grand Total'}
        grand_total_row_data.update({f'{col}': totals_df[col].sum() for col in quantity_cols})
        grand_total_row = pd.DataFrame([grand_total_row_data], columns=[name_col] + [f'{col}' for col in quantity_cols])
        result_rows.append(grand_total_row)  
        result_df = pd.concat(result_rows, ignore_index=True)
        return result_df
    result_df = subtotal(goal_data, 'Market', ['Metro Quota', 'Metro BTS','Metro HINT', 'Magenta In Metro', 'ST Quota', 'Upgrade', 
                                            'ST BTS', 'ST HINT', 'PPD', 'Accessory','Total Quota','Last 12 Months ShopperTrak',
                                            'ShopperTrak Conv %','Upgrade BTS','Retention target','Last Month Actual (PPD)',
                                            'Last Month Goal (PPD)','Last Month Actual (Acc)','Last Month Goal (Acc)','ACC/BOX',
                                            'Last Month BP','Bill Payments Conv%']) #,'ST MIM'
    st.header("XTI Goals Dashboard")

    # Initialize filtered dataframe
    filtered_df = result_df
    float_cols = filtered_df.select_dtypes(include=['float']).columns
    filtered_df[float_cols] = filtered_df[float_cols].fillna(0)
    filtered_df[float_cols] = filtered_df[float_cols].apply(lambda col: col.round().astype(int))
    filtered_df.rename(columns={'ST Quota': 'Targeted Quota'}, inplace=True)
    filtered_df.rename(columns={'ShopperTrak Conv %': 'Expected PPD by ST Clicks'}, inplace=True)

# List of columns in the current DataFrame
    cols = list(filtered_df.columns)

    # Remove the columns to be reordered
    cols.remove('Last 12 Months ShopperTrak')
    cols.remove('Expected PPD by ST Clicks')

    # Find the index of 'Retention target' column
    retention_target_idx = cols.index('Retention target')

    # Insert 'Last 12 Months ShopperTrak' after 'Retention target'
    cols.insert(retention_target_idx + 1, 'Last 12 Months ShopperTrak')

    # Find the index of 'Last 12 Months ShopperTrak' to place 'Expected PPD by ST Clicks' after it
    shopper_trak_idx = cols.index('Last 12 Months ShopperTrak')
    cols.insert(shopper_trak_idx + 1, 'Expected PPD by ST Clicks')

    # Reorder the DataFrame with the new column order
    filtered_df = filtered_df[cols]

    def create_complex_style(df):
        # Create empty style DataFrame
        style_df = pd.DataFrame('', index=df.index, columns=df.columns)
        
        # Style for total rows
        total_mask = df['Market'].str.contains('Total', na=False)
        
        # Apply styles to non-total rows
        non_total_mask = ~total_mask
        
        # Apply different column styles
        for col_idx, col_name in enumerate(df.columns):
            base_style = 'border: 1px solid black; '
            
            # Column-specific background colors
            if col_idx < 4:
                bg_color = 'background-color: #ADD8E6;' #blue
            elif 4 <= col_idx <= 7:
                bg_color = 'background-color: #D3D3D3;' #gray
            elif 8 <= col_idx <= 11:
                bg_color = 'background-color:#C4BD97;' #cream
            elif 12 <= col_idx <= 14:
                bg_color = 'background-color: #9cfa84; ' #lightgreen 
            elif col_idx == 15:
                bg_color = 'background-color: #ffff0052;' #lightyellow
            elif col_idx == 16:
                bg_color = 'background-color: #9cfa84; ' #lightgreen
            else:
                bg_color = 'background-color: #D3D3D3;' #gray
                
            # Apply styles to non-total rows
            style_df.loc[non_total_mask, col_name] = base_style + bg_color
            
            # Apply pink background to total rows
            style_df.loc[total_mask, col_name] = 'background-color: #D1227F; border: 1px solid black; color: white;' #pink
        
        return style_df

    def style_header(df):
        header_styles = {
            'selector': 'th',
            'props': [
                ('background-color', '#800000'), #maroon
                ('color', 'white'),
                ('border', '1px solid black'),
                ('font-weight', 'bold'),
                ('text-align', 'center'),
                ('padding', '8px')
            ]
        }
        
        styled_df = df.style.set_table_styles([header_styles])\
                        .apply(lambda _: create_complex_style(df), axis=None)\
                        .set_properties(**{
                            'border': '1px solid black',
                            'text-align': 'center'
                        })
        
        return styled_df

    def to_excel_with_styling(df):
        output = BytesIO()
        
        with pd.ExcelWriter(output, engine='xlsxwriter', engine_kwargs={'options': {'nan_inf_to_errors': True}}) as writer:
            # Write the dataframe without styling first
            df.to_excel(writer, index=False, sheet_name='Filtered Data')
            
            # Get the xlsxwriter workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Filtered Data']
            
            # Define format templates
            formats = {
                'base': workbook.add_format({
                    'border': 1,
                    'text_wrap': True,
                    'align': 'center',
                    'valign': 'vcenter'
                }),
                'header': workbook.add_format({
                    'bg_color': '#800000',  # maroon
                    'font_color': 'white',
                    'bold': True,
                    'border': 1,
                    'align': 'center',
                    'valign': 'vcenter'
                }),
                'total_row': workbook.add_format({
                    'bg_color': '#D1227F',  # pink
                    'border': 1,
                    'color':'white',
                    'align': 'center',
                    'valign': 'vcenter'

                })
            }
            
            # Create column-specific formats
            col_formats = {}
            for col_idx in range(len(df.columns)):
                if col_idx < 4:
                    bg_color = '#ADD8E6'  # lightblue
                elif 4 <= col_idx <= 7:
                    bg_color = '#D3D3D3'  # gray
                elif 8 <= col_idx <= 11:
                    bg_color = '#C4BD97'  # cream
                elif 12 <= col_idx <= 14:
                    bg_color = '#7030A0'  # purple
                    col_formats[col_idx] = workbook.add_format({
                        'bg_color': bg_color,
                        'font_color': 'white',
                        'border': 1,
                        'align': 'center',
                        'valign': 'vcenter'
                    })
                    continue
                elif col_idx == 15:
                    bg_color = '#FFFF00'  # lightyellow
                elif col_idx == 16:
                    bg_color = '#7030A0'  # purple
                    col_formats[col_idx] = workbook.add_format({
                        'bg_color': bg_color,
                        'font_color': 'white',
                        'border': 1,
                        'align': 'center',
                        'valign': 'vcenter'
                    })
                    continue
                else:
                    bg_color = '#D3D3D3'  # lightgray
                
                col_formats[col_idx] = workbook.add_format({
                    'bg_color': bg_color,
                    'border': 1,
                    'align': 'center',
                    'valign': 'vcenter'
                })
            
            # Apply header format
            for col_idx, col_name in enumerate(df.columns):
                worksheet.write(0, col_idx, col_name, formats['header'])
            
            # Apply cell formats based on conditions and column
            total_mask = df['Market'].str.contains('Total', na=False)
            
            for row_idx in range(len(df)):
                for col_idx in range(len(df.columns)):
                    cell_value = df.iloc[row_idx, col_idx]
                    
                    # Handle NaN values
                    if pd.isna(cell_value):
                        cell_value = ''
                    
                    # Determine which format to use
                    if total_mask.iloc[row_idx]:
                        cell_format = formats['total_row']
                    else:
                        cell_format = col_formats[col_idx]
                    
                    try:
                        worksheet.write(row_idx + 1, col_idx, cell_value, cell_format)
                    except:
                        # If writing fails, convert to string
                        worksheet.write(row_idx + 1, col_idx, str(cell_value), cell_format)
            
            # Auto-adjust columns width
            for col_idx, col_name in enumerate(df.columns):
                # Filter out NaN values when calculating max length
                column_values = df.iloc[:, col_idx].dropna()
                if len(column_values) > 0:
                    try:
                        max_length = max(len(str(val)) for val in column_values)
                        max_length = max(max_length, len(col_name)) + 2
                    except:
                        max_length = len(col_name) + 2
                    worksheet.set_column(col_idx, col_idx, max_length)
                else:
                    # If column is empty or all NaN, use header length
                    worksheet.set_column(col_idx, col_idx, len(col_name) + 2)
        
        return output.getvalue()

    # Main display and download section
    with st.expander("Dataframe", expanded=True):
        markets_listt = ['All'] + list(unique_markets)
        selected_markett = st.multiselect("Select Market:", markets_listt, key=1222, default="All")
        
        display_df = filtered_df.copy()
        
        if "All" not in selected_markett:
            # Filter by selected markets and their totals
            market_filter = display_df['Market'].isin(selected_markett) | \
                        display_df['Market'].isin([f"{market} Total" for market in selected_markett])
            display_df = display_df[market_filter]
        
        # Apply styling to the filtered DataFrame
        styled_display_df = style_header(display_df)
        
        # Display the styled DataFrame
        st.dataframe(
            styled_display_df,
            height=400 if "All" in selected_markett else None,
            use_container_width=True,
            hide_index=True
        )
        
        # Add download button
        current_month = datetime.now().strftime("%B")
        file_name = f"{current_month}Goals.xlsx"
        
        xlsx_data = to_excel_with_styling(display_df)  # Use the filtered dataframe
        st.download_button(
            label="Click here to download",
            data=xlsx_data,
            file_name=file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
except KeyError as e:
    st.warning(f"Error during DataFrame manipulation check you upload correct file: {e}")
except Exception as e:
    st.warning(f"Unexpected error check you upload correct file: {e}")

# Collapsible section for file uploads
with st.sidebar.expander("Upload Files for Boxes Goal Automation", expanded=False):
    # Shoppertracker file upload
    shoppertracker = st.file_uploader("Upload Shopper Tracker", key="shoppertracker_file")
    if shoppertracker is not None:
        save_path = "ShopperTracker.xlsx"
        with open(save_path, "wb") as f:
            f.write(shoppertracker.getbuffer())
    
    # Metro target file upload
    metrotarget = st.file_uploader("Upload Metro Target", key="metrotarget_file")
    if metrotarget is not None:
        save_path = "metrotarget.xlsx"
        with open(save_path, "wb") as f:
            f.write(metrotarget.getbuffer())
    
    # Performance by Market file upload
    perfbymarket = st.file_uploader("Upload Performance by Market", key="perfbymarket_file")
    if perfbymarket is not None:
        save_path = "perfbymarket.xls"
        with open(save_path, "wb") as f:
            f.write(perfbymarket.getbuffer())
    
    # Smart Pay file upload
    smartpay = st.file_uploader("Upload Smart Pay", key="smartpay_file")
    if smartpay is not None:
        save_path = "smartpay.xlsx"
        with open(save_path, "wb") as f:
            f.write(smartpay.getbuffer())
    
    # Mapping file upload
    mapping = st.file_uploader("Upload Mapping", key="mapping_file")
    if mapping is not None:
        save_path = "mapping.xlsx"
        with open(save_path, "wb") as f:
            f.write(mapping.getbuffer())

    # last_goals file upload
    last_goals = st.file_uploader("Upload Lasth Month Goals", key="last_month_goals_file")
    if last_goals is not None:
        save_path = "last_month_goals.csv"
        with open(save_path, "wb") as f:
            f.write(last_goals.getbuffer())


# Add the logout button
if st.sidebar.button("Logout"):
    st.session_state["authentication_status"] = False
    st.session_state["logged_in"] = False
    st.rerun()
