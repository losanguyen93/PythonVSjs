import ibm_boto3
import json
import requests
import random
from ibm_botocore.client import Config
from pprint import pprint
import os
import string
import database


def Up_to_storage(lname, file_name):

  with open('./credentials.json') as data_file:
      credentials = json.load(data_file)

  print("Service credential:")
  print(json.dumps(credentials, indent=2))
  print("")
  print("Connecting to COS...")

  # Rquest detailed enpoint list
  endpoints = requests.get(credentials.get('endpoints')).json()
  #import pdb; pdb.set_trace()

  # Obtain iam and cos host from the the detailed endpoints
  iam_host = (endpoints['identity-endpoints']['iam-token'])
  cos_host = (endpoints['service-endpoints']['cross-region']['us']['public']['us-geo'])

  api_key = credentials.get('apikey')
  service_instance_id = credentials.get('resource_instance_id')

  # Constrict auth and cos endpoint
  auth_endpoint = "https://" + iam_host + "/oidc/token"
  service_endpoint = "https://" + cos_host

  print("Creating client...")
  # Get bucket list
  cos = ibm_boto3.client('s3',
                      ibm_api_key_id=api_key,
                      ibm_service_instance_id=service_instance_id,
                      ibm_auth_endpoint=auth_endpoint,
                      config=Config(signature_version='oauth'),
                      endpoint_url=service_endpoint)


  # Call COS to list current buckets
  response = cos.list_buckets()

  # Get a list of all bucket names from the response
  buckets = [bucket['Name'] for bucket in response['Buckets']]

  # Print out the bucket list
  print("Current Bucket List:")
  print(json.dumps(buckets, indent=2))
  print("---")

  result = database.get_bucket_name(lname)
  print "result = ", result
  
  print("Creating a new bucket and uploading an object...")
  print file_name
  if len(result) == 0 :
     bucket_name = 'bucket' + str(random.randint(100,99999999));
     # Create a bucket
     cos.create_bucket(Bucket=bucket_name)
     # Upload a file
     cos.upload_file('./' + file_name, bucket_name, file_name)

     # Call COS to list current buckets
     response = cos.list_buckets()

     # Get a list of all bucket names from the response
     buckets = [bucket['Name'] for bucket in response['Buckets']]

     # Print out the bucket list
     print("New Bucket List:")
     print(json.dumps(buckets, indent=2))
     print("---")
  else :
     bucket_name = result
     cos.upload_file('./' + file_name, bucket_name, file_name)
  os.remove('./' + file_name)

  # Call COS to list current objects
  response = cos.list_objects(Bucket=bucket_name)



  # Get a list of all object names from the response
  objects = [object['Key'] for object in response['Contents']]

  # Print out the object list
  print("Objects in %s:" % bucket_name)
  print(json.dumps(objects, indent=2))
  return bucket_name
