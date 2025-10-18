def format_template(template):
    # Function to format the CloudFormation template
    return template

def handle_aws_response(response):
    # Function to handle AWS responses
    if 'Error' in response:
        raise Exception(response['Error']['Message'])
    return response