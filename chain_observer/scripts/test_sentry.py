import sentry_sdk
from dotenv import load_dotenv
import os
load_dotenv()

SENTRY_DSN = os.getenv('SENTRY_DSN')
sentry_sdk.init(
    dsn=SENTRY_DSN,
)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return "Error: Division by zero!"

if __name__ == "__main__":
    divide(10, 2)  # This will work
    divide(10, 0)  # This will trigger an error
