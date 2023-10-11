
# Coinster-API

Developed an API application using Django, Django-
rest-framework, and PostgreSQL that allows users to view market trends with their own schedulers periodically. Implemented user authentication, and WebSocket communication using Django REST framework, and Channels library for sending coin information to user. Utilized Celery and Redis to perform periodic tasks such
as fetching live prices, updating balances, and sending notifications.





## Installation

To run Coinster-Django locally, you will need to have Python 3.6 or higher installed on your machine. You will also need to install the required packages using the following command:

```
pip install -r requirements.txt
```

Then, you can clone this repository and navigate to the project directory:

```
git clone https://github.com/sahil-2118/Coinster-Django.git

```

```
cd Coinster-Django
```

Set env variabeles project:

```
touch .env
```

Bulid Docker compose and run it:

```
docker compose build
```

```
docker compose up
```

You can now access the web application at http://127.0.0.1:8000/swagger
    
## Usage

To use Coinster-Django, you will need to create a regular user account or log in with an existing one. You can then create a scheduler or edit existing one and view list of your schedulers. 

You can periodically view special coin information using the scheduler with a websocket connect request. Additionally, you can access a list of existing coins without logging in.


## License

[MIT](https://choosealicense.com/licenses/mit/)

