import boto3
from botocore.exceptions import ClientError

def create_stack(stack_name, template_body, parameters=None, capabilities=None):
    client = boto3.client('cloudformation')
    try:
        response = client.create_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters or [],
            Capabilities=capabilities or []
        )
        return response
    except ClientError as e:
        print(f"Error creating stack: {e}")
        return None

def update_stack(stack_name, template_body, parameters=None, capabilities=None):
    client = boto3.client('cloudformation')
    try:
        response = client.update_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters or [],
            Capabilities=capabilities or []
        )
        return response
    except ClientError as e:
        print(f"Error updating stack: {e}")
        return None

def delete_stack(stack_name):
    client = boto3.client('cloudformation')
    try:
        response = client.delete_stack(StackName=stack_name)
        return response
    except ClientError as e:
        print(f"Error deleting stack: {e}")
        return None