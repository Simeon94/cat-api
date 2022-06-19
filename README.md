# cat-api
This app has been created with Falsk solely for extracting data from https://thecatapi.com/. The data is then transformed to a pandas DataFrame, then written to an html file and finally rendered to a webpage at http://127.0.0.1:5000/.

The extracted data has been transformed into a pandas Dataframe to make the data more presentatble (easy to read) and ready to be uploaded to a database.

Two sets of data; cat categories and breeds have been extracted and rendered to a webpage at http://127.0.0.1:5000/.

Users can run the scripts on their local machine and it will automatically display the data on port 5000.

Screenshots of the rendered data are in the root folder.

NB: Users to make sure to kill the port 5000 after running the script. Else, another attempt to run either of the script will return an error message saying port is already in use.

To kill port 5000 after running either of the script:
ss -lptn 'sport = :5000'
kill -9 <pid>
