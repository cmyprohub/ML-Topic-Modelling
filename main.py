
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:10:17 2018

@author: sumavenugopal
"""
import boto3
import json
from bson import json_util
 
'''comprehend = boto3.client(service_name='comprehend', region_name='region')
                
input_s3_url = "s3://input bucket/input path"
input_doc_format = "ONE_DOC_PER_FILE"
output_s3_url = "s3://output bucket/output path"
data_access_role_arn = "arn:aws:iam::account ID:role/data access role"
number_of_topics = 10
 
input_data_config = {"S3Uri": input_s3_url, "InputFormat": input_doc_format}
output_data_config = {"S3Uri": output_s3_url}'''
 
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
             

input_s3_url = "s3://testcomprehend1234/input/"

input_doc_format = "ONE_DOC_PER_LINE"

output_s3_url = "s3://testcomprehend1234/output/"

data_access_role_arn = "arn:aws:iam::534581738637:role/Comprehend"

number_of_topics = 10


input_data_config = {"S3Uri": input_s3_url, "InputFormat": input_doc_format}

output_data_config = {"S3Uri": output_s3_url}


start_topics_detection_job_result = comprehend.start_topics_detection_job(NumberOfTopics=number_of_topics,

                                                                              InputDataConfig=input_data_config,

                                                                              OutputDataConfig=output_data_config,

                                                                              DataAccessRoleArn=data_access_role_arn)


print('start_topics_detection_job_result: ' + json.dumps(start_topics_detection_job_result))


job_id = start_topics_detection_job_result["JobId"]


print('job_id: ' + job_id)


describe_topics_detection_job_result = comprehend.describe_topics_detection_job(JobId=job_id)


print('describe_topics_detection_job_result: ' + json.dumps(describe_topics_detection_job_result, default=json_util.default))


list_topics_detection_jobs_result = comprehend.list_topics_detection_jobs()


print('list_topics_detection_jobs_result: ' + json.dumps(list_topics_detection_jobs_result, default=json_util.default))

 