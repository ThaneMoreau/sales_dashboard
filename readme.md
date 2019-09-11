# Sales dashboard


## Description
Microservice, which have a REST interface with two endpoints. The first endpoint  calls by the checkout service whenever a new payment is received and the second endpoint  provides statistics about the total
order amount and average amount per order for the last 60 seconds.

## Set environoment
Python required version: 3.7.*

    cd sales_dashboard
    python -m venv venv
    souce venv/bin/activate
    python -m pip install -U pip
    pip install -r requirements.txt

## Run  application
Run app.py from app directory:

    cd app
    python app.py

Statistics endpoint:

    localhost:8080/statistics

At the client directory there are clients for synchronous and asynchronous requests:

    cd clients
    python client.py
    python async_client.py

Both of them can be configured by calling the run function:
    
    ...
    run(
            requests_amount=10000,
            sales_amount=random.randint(0, 10**6)
        )
    ...


Or use curl for manual queries:

    curl -i -X POST "http://localhost:8080/sales?sales_amount=10.00" -H "Content-Type: application/x-www-form-urlencoded"

