import boto3

def verify_email_identity():
    ses_client = boto3.client("ses", region_name="ap-south-1")
    response = ses_client.verify_email_identity(
        EmailAddress="rm584@snu.edu.in"
    )
    print(response)