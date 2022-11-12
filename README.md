# HubspotOauth2

OAuth2 authentication method implemented by using [hubspot](hhttps://www.hubspot.com/) 

1. Clone this project

    `git clone git@github.com:esmejia277/HubspotOauth2.git`

2. Create a virtualenv

   `python3 -m venv env`

3. Activate your virtual environment

   Linux ad MacOs systems:

   `source env/bin/activate`

   Windows systems: 
    
   `.\env\Scripts/activate`

4. Install dependencies

   `pip install -r requirements.txt`

5. Get your hubspost credentials in [hubspot](hhttps://www.hubspot.com/) and export them as env vars
    
    For Linux ad MacOs systems
    ```
    export CLIENT_ID="***"
    export SCOPE="***"
    export REDIRECT_URI="***"
    ```

    For windows
    ```
    set CLIENT_ID="***"
    set SCOPE="***"
    set REDIRECT_URI="***"
    ```

6. Provide an instance of mongo database and export the environment variables in order to get access into the database
    
    For Linux ad MacOs systems
    ```
    export MONGO_HOST="***"
    export MONGO_PORT="***"
    export MONGO_DATABASE_NAME="***"
    ```
    For windows
   ```
    set MONGO_HOST="***"
    set MONGO_PORT="***"
    set MONGO_DATABASE_NAME="***"
    ```

5. Start the server and visit `/`, if you are not authenticated you will be redirected to `/install` in order to log into hubspot

   `python wsgi.py`