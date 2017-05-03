#!/Users/michelnossin/anaconda/bin/python

#We will use $HOME/.aws/credentials and config set by aws cli. (and not boto.client())
#python -m pip install boto3
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('flight_events')

table.put_item( Item= { "day" : "2-may-2107" , "time" : "14:14" , "flight" : "KL1234" , "flt" : { "cdm" : { "eibt" : "2017-05-03T22:39:00.000+02:00" }, "flight" : { "flightArrival" : { "blt" : [ { "belt" : "16A" } ] }, "fltnr" : "CND312" }, "prkStand" : { "prkStatus" : [ { "prk" : [ { "gateType" : "G", "prkValue" : "Z02" }, { "gateType" : "R", "prkValue" : "D02" } ] } ] }, "sdatetime" : "2017-05-03T22:50:00.000+02:00", "arrdep" : "A" } } )

#learning: exact primary and sort key have to be in main level. So as our providers does not give it in this form
#we will add these ourself
