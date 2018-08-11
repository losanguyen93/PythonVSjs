import ibm_boto3
import json
import requests
import random
from ibm_botocore.client import Config
from pprint import pprint
import pickle

credentials={
  "apikey": "3jTPzaVye32fSN9YrTfPraZjJ8PfclSQW2fBNkRtVhmX",
  "endpoints": "https://cos-service.bluemix.net/endpoints",
  "iam_apikey_description": "Auto generated apikey during resource-key operation for Instance - crn:v1:bluemix:public:cloud-object-storage:global:a/d31481a8ac43f4d40ea4544424c64881:87dbd1d0-503c-4909-907e-2e29d4ad8c02::",
  "iam_apikey_name": "auto-generated-apikey-b784a23a-3ddd-4df3-8b98-8fc5a170d2bd",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/d31481a8ac43f4d40ea4544424c64881::serviceid:ServiceId-251dcdd2-e7e5-4704-8bd0-3fa3f20ab15a",
  "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/d31481a8ac43f4d40ea4544424c64881:87dbd1d0-503c-4909-907e-2e29d4ad8c02::"

}
auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'
cos = ibm_boto3.client(service_name='s3',
    ibm_api_key_id=credentials['apikey'],
    ibm_service_instance_id=credentials['resource_instance_id'],
    ibm_auth_endpoint='https://iam.bluemix.net/oidc/token',
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3-api.us-geo.objectstorage.softlayer.net')



def download_file_cos(bucket_name,local_file_name,key):  
    try:
        res=cos.download_file(Bucket=bucket_name,Key=key,Filename=local_file_name)
    except Exception as e:
        print(Exception, e)
    else:
        print('File Downloaded')

def download_ds(bucket_name,name_key):
  print "from = ", name_key
  download_file_cos(bucket_name,'/home/pi/losa_linh/all together/losa132.txt',name_key)



