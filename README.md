# Example usage of Celery with FastAPI

## What's this?

This is an example web application showcasing use of FastAPI + Celery + docker-compose.

The exposed API contains endpoint for posting a task (computing square of a positive number), and
obtaining its result. Task for `x` sleeps for `x` seconds to emulate long-running jobs.

If you run the app through docker-compose, it the api will be available at `http://localhost:8004`. Interactive
documentation, automatically generated by FastAPI, is available at `http://localhost:8004/doc` or with
alternative interface at `http://localhost:8004/redoc`.


## Running the web application

1. Run `docker-compose build`
2. Run `docker-compose up`

Or combine both commands with `docker-compose --build up`

## Testing the API

The `call_api.py` script shows basic interaction with API. To run it first install requirements:

```
pip install -r requirements.txt
```
and then run `python call_api.py`. Note that this example assumes Python >= 3.8 because it uses an assignment expression. 

You can also interact with the API via interactive docs
or `curl`, or any other http client.
