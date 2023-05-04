import os
from dotenv import load_dotenv
load_dotenv()

SECURITY_PROTOCOL = "SASL_SSL"
SSL_MECHANISM = "PLAIN"
API_KEY = os.getenv("API_KEY", None)
BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER", None)

print(BOOTSTRAP_SERVER)
