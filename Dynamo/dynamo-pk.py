import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime

dao = BaseDAO('eventos-pizzaria')

dao.put_item({'envet_id':'111', 'name': 'teste1'})