# AWS CloudFormation PythonSDK Project

This project demonstrates how to use the AWS Python SDK (`boto3`) to deploy AWS infrastructure using CloudFormation templates.

## Features

- Create, update, and delete CloudFormation stacks using Python
- Example CloudFormation template for:
  - VPC
  - Internet Gateway
  - Security Group (SSH access)
  - Private Subnet
  - EC2 Instance (t3.micro, Amazon Linux 2)

## Project Structure

```
Cloudformation/
└── PythonSDK/
    ├── src/
    │   ├── stack_manager.py
    │   ├── deploy_stack.py
    │   └── utils/
    │       └── __init__.py
    ├── templates/
    │   └── vpc_stack.yaml
    ├── .env
    ├── requirements.txt
    └── README.md
```

## Getting Started

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Configure AWS credentials:**
    ```bash
    aws configure
    ```

3. **Set the template path in `.env`:**
    ```
    CF_TEMPLATE_PATH=path/to/templates/vpc_stack.yaml
    ```

4. **Deploy the stack:**
    ```bash
    cd src
    python deploy_stack.py
    ```

## Notes

- Make sure your AWS account is within the Free Tier limits.
- Update the `ImageId` in the CloudFormation template for your AWS region.
- The `.env` file is used to store environment variables and should not be committed to version control.

## License

MIT License