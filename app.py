import streamlit as st
import requests
import pandas as pd
import base64
import uuid
import requests

st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title('JotForm API Form Explorer')
st.markdown('This app allows you to view and download your JotForm forms using the JotForm API.')

st.sidebar.markdown('<img src="https://www.jotform.com/resources/assets/logo-nb/jotform-logo-transparent-800x200.png" alt="JotForm logo" width="200">', unsafe_allow_html=True)

st.sidebar.header('JotForm API Options')

api_url = st.sidebar.selectbox('API URL', ['api.jotform.com', 'custom'])
if api_url == 'custom':
    custom_api_url = st.sidebar.text_input('Custom API URL', 'yourdomain.com/API/')
    api_url = custom_api_url.rstrip('/')
api_key = st.sidebar.text_input('Enter API Key', placeholder="API Key", value="")
limit = st.sidebar.slider('Form Limit', 100, 4000, 100, step=100)
orderby = st.sidebar.selectbox('Order By', ['id', 'username', 'title', 'status', 'created_at', 'updated_at', 'new', 'count', 'slug'])
status_filter = st.sidebar.selectbox('Status', ['All', 'ENABLED', 'DISABLED', 'DELETED'])
submit_button = st.sidebar.button('Submit')
if not submit_button:
    st.write("Please Enter your API and select the criteria and click on the Submit Button.")
else:
    st.empty()

st.sidebar.markdown("""Parameter | Description
--- | ---
apikey | Jotform User API Key. Get a new API Key [here](https://www.jotform.com/myaccount/api). If you have an Enterprise account, select 'custom' and enter your Enterprise JotForm API URL.
limit | Number of results in each result set for form list. Default is 100. Maximum is 4000.
orderby | Order results by a form field name: id, username, title, status(ENABLED, DISABLED, DELETED), created_at, updated_at, new (unread submissions count), count (all submissions count), slug (used in form URL).""")


if submit_button:
    forms = []
    for i in range(0, limit, 1000):
        url = f'https://{api_url}/user/forms?apikey={api_key}&offset={i}&limit=1000&orderby={orderby}'

        response = requests.get(url)
        data = response.json()

        if 'content' in data:
            forms += data['content']
    
    if forms:
        df = pd.DataFrame(forms)
        if status_filter != 'All':
            df = df[df['status'] == status_filter]
        st.table(df)
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        button_label = 'Download CSV file'
        button_uuid = str(uuid.uuid4()).replace('-', '')
        button_id = f'{button_label}-{button_uuid}'
        button_html = f'<a download="forms.csv" href="data:file/csv;base64,{b64}" id="{button_id}" class="css-1p3ovfs e17oygji0"><button type="button" class="css-lc06hr e17oygji2"><span class="css-1ljozgh e17oygji1">{button_label}</span></button></a><style>.css-1p3ovfs.e17oygji0{{display: inline-block;}}.css-lc06hr.e17oygji2{{background-color: #f63366; color: white; border: none; cursor: pointer; padding: 8px 12px;}}.css-lc06hr.e17oygji2:hover{{background-color: #d80e41;}}</style>'
        st.markdown(button_html, unsafe_allow_html=True)
    else:
        st.write('No forms found')

st.markdown("", unsafe_allow_html=True)
st.markdown("<hr style='text-align: center;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)   
