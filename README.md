# JotForm API Form Explorer

This is a simple web app built using the python library [Streamlit](https://streamlit.io/) to explore and download JotForm forms using the JotForm API. If you have an enterprise plan with a custom domain, you can click on the API URL dropdown, select "*custom*", and enter your own custom jotform API URL. This app enhances the current JotForm maximum form limit of 1000 by automatically correcting the offset and increasing the limit to 4000. This number can be increased to whichever maximum number is needed by changing '4000' to a higher number in the code.

The app displays the form data in a table based on the selected criteria. If any forms match the criteria, a "Download CSV file" button will appear, allowing you to download a CSV file containing the form data.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/JotForm-API-Form-Explorer_App "Here") To View This App Online!

![image](https://user-images.githubusercontent.com/63890666/221301910-e42e5285-57c9-4074-93cb-717f4dc81daa.png)

## Usage

1.  Enter your JotForm API key in the text box in the sidebar.
2.  Select the API URL, limit, order by and status filter options in the sidebar.
3.  Click on the "Submit" button.
4.  The app will display a table of your JotForm forms based on your selected criteria.
5.  If there are any forms that match your criteria, a "Download CSV file" button will appear. Click on the button to download a CSV file containing the form data.

## Prerequisites

-   Python 3.7 or higher
-   JotForm API key
-   Streamlit

## Installation

1.  Clone the repository:

`git clone https://github.com/Kaludii/JotForm-API-Form-Explorer.git` 

2.  Change directory:

`cd jotform-api-explorer` 

3.  Install the required packages:

`pip install -r requirements.txt` 

4.  Run the app:

`streamlit run app.py` 
