# AWS CloudFormation SDK Project

This project provides a Python SDK for interacting with AWS CloudFormation using the `boto3` library. It includes functionality to create, update, and delete CloudFormation stacks.

## Project Structure

```
aws-cloudformation-sdk-project
├── src
│   ├── template.py        # Main logic for AWS SDK interactions
│   └── utils
│       └── __init__.py    # Utility functions for the project
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd aws-cloudformation-sdk-project
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the SDK, you can import the functions defined in `template.py` and utilize them to manage your CloudFormation stacks. 

### Example

```python
from src.template import create_stack, update_stack, delete_stack

# Create a CloudFormation stack
create_stack(stack_name='MyStack', template_body='template.yaml')

# Update a CloudFormation stack
update_stack(stack_name='MyStack', template_body='updated_template.yaml')

# Delete a CloudFormation stack
delete_stack(stack_name='MyStack')
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.