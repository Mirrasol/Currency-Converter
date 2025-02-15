[![Maintainability](https://api.codeclimate.com/v1/badges/ed619f783e5a0091eff0/maintainability)](https://codeclimate.com/github/Mirrasol/curr-api/maintainability)


Currency Converter - a simple and easy to use REST API to check the latest global currency rates. It provides registered users with an access to the list of world currencies and allows them to convert from one currency to another. The project includes JWT authentication and integration with an external API for a real-time exchange.

## Features

  - register and login to check the list of all available currencies
  - quickly convert one currency to another using the most recent exchange rate data

## Installation

This project is built using FastAPI as the main framework. Please refer to the pyproject.toml file for the full list of required dependencies.

1) Download the package from GitHub:

`git clone git@github.com:Mirrasol/Currency-Converter.git`

2) Install using uv from your console:

`make install`

or set your own virtual environment using pip and other package managers.

3) Don't for get to create the .env file that contains your secret keys and database settings:

>DB_HOST = localhost
>
>DB_PORT = 5432
>
>DB_USER = username
>
>DB_PASS = my_pass
>
>DB_NAME = db_name
> SECRET_KEY = enter_your_key 
>
> ALGORITHM = choose_algorithm 
>
> API_KEY = exchange_api_key 
>
> MODE=DEV

You can get the API_Key from the external forex API: ["Currency Data API"](https://apilayer.com/marketplace/currency_data-api`).

4) Run the project using Uvicorn:

`uvicorn main:app`

and check Makefile for the list of the available commands.

## Swagger Demo Screens

- Registering new user:

![](/img/5_add_new_user.png)

-  Login request:

![](/img/1_login_data.png)

- Login response:

![](/img/2_login_response.png)

- Getting the list of currencies:

![](/img/3_currency_list.png)

- Checking available exchange responses:

![](/img/4_exchange_responses.png)