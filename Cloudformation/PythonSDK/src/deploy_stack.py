import os
from dotenv import load_dotenv
from stack_manager import create_stack

load_dotenv()  # Loads variables from .env

template_path = os.getenv('CF_TEMPLATE_PATH')
stack_name = 'MyVPCStack'

if not template_path:
    raise ValueError("CF_TEMPLATE_PATH not set in .env file.")

with open(template_path, 'r') as f:
    template_body = f.read()

response = create_stack(
    stack_name=stack_name,
    template_body=template_body
)

print(response)