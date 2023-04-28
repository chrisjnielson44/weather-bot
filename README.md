# Weather Bot Project

This is a weather bot project that utilizes weatherAPI.com for real-time updates on current weather and daily forecast. The project is written in Python and includes Twitter functionality and SMS functionality for users to receive updates on the weather.

## Requirements

Before running this project, you will need to sign up for an account at weatherAPI.com to obtain an API key. Additionally, you will need to have the following packages installed:

requests
tweepy
twilio
These can be installed using pip:
```bash 
pip install requests tweepy twilio
```
## Setup

1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Create a new file called .env in the root directory.
4. Add your weatherAPI.com API key, Twitter API key, Twitter API secret key, Twitter access token, Twitter access token secret, Twilio account SID, Twilio auth token, and Twilio phone number to the .env file using the following format:

```bash 
WEATHER_API_KEY=your_api_key_here
WEATHER_LOCATION=your_location
TWITTER_API_KEY=your_api_key_here
TWITTER_API_SECRET_KEY=your_secret_key_here
TWITTER_ACCESS_TOKEN=your_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_phone_number_here
```

Replace your_api_key_here, your_secret_key_here, etc. with your own API keys and access tokens. For the location visit https://rapidapi.com/weatherapi/api/weatherapi-com for acceptable location parameters.

## Usage
### Twitter Weather Bot
1. First, you need to create a developer account on Twitter Developer Portal.
2. Then, create a new Project and generate Consumer Keys, Access Tokens and Keys, and Secrets. These keys are necessary for authenticating requests to the Twitter API.
3. Add these keys and secrets to the .env file.
4. Install Tweepy with the command pip install tweepy.
5. Run the twitterBot.py file to get a tweet about the current weather in your location.

## Twilio SMS Weather Bot
1. You need to have a Twilio account to use the SMS bot.
2. After creating an account, go to the Twilio Console and get your Account SID and Auth Token.
3. Add these credentials and other details, such as the 'From' and 'To' phone numbers, to the .env file.
4. Install the Twilio package with the command pip install twilio.
5. Run the smsBot.py file to get an SMS message about the current weather in your location.


## Credits

This project was created by Christopher Nielson, CS undergrad student at Florida State University. Special thanks to weatherAPI.com, Tweepy, and Twilio for their APIs and libraries.

[Github Profile](https://github.com/chrisjnielson44)
[Website](https://cjnielson.com)
