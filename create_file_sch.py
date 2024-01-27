import os
import uuid
import random
from translate import Translator
import datetime
from datetime import timedelta
import string
import json

def files_dir(path):
  for root, dirs, files in os.walk(path):
    for dir in dirs:
      for i in range(0,2):
        uuid_val = uuid.uuid4()
        file_name = f'file_{uuid_val}.json'
        file_path = os.path.join(path,dir,file_name)
        dataGen(file_path, num_dict=1)

def dataGen(file_path,num_dict):
  
  translator= Translator(to_lang="Arabic")

  start_date = datetime.datetime.now()
  end_date = start_date + timedelta(days=15)

  another_startdate = datetime.date.today()
  another_enddate = another_startdate + timedelta(days=5)

  for dictionary in range(1,num_dict+1):

    dummy = {}
    dummy['Request'] = {}
    dummy['Request']['OperatingAirlines'] = "SaudiAirlines"
    dummy['Request']['OrderId']= random.randint(pow(10,5),pow(10,6)-1)
    dummy['Request']['EncryptOrderId'] = str(str(dummy['Request']['OrderId']).encode())
    dummy['Request']['OrderNumber'] = str(random.randint(pow(10,9),pow(10,10)-1))
    dummy['Request']['AccountNo'] = None
    dummy['Request']['ClassTicketEn'] ="ECONOMY"
    dummy['Request']['ClassTicketAr'] = str(translator.translate("ECONOMY"))
    dummy['Request']['NumberPassengers'] = 1
    dummy['Request']['TicketTypeName'] = str(translator.translate("ECONOMY"))
    dummy['Request']['UserOwnerMail'] = None
    dummy['Request']['TicketTypeId'] = 1
    dummy['Request']['Adults'] = 1
    dummy['Request']['Childern'] = 0
    dummy['Request']['Infant'] = 0
    dummy['Request']['Youth'] = 0
    dummy['Request']['FlexibleDays'] = 0
    dummy['Request']['Currency'] = "SAR"
    dummy['Request']['IncludeAirlines'] = None
    dummy['Request']['ExcludeAirlines'] = None
    dummy['Request']['OrderCreationDate'] = str(start_date + (end_date - start_date) * random.random())
    dummy['Request']['nonStop'] = random.choices([True,False])
    dummy['Request']['max'] = 0
    dummy['Request']['AgencyCode'] = random.randint(pow(10,5),pow(10,6)-1)

    order_details = {}
    order_details['CountrycodeFrom'] = "SAU"
    order_details['CountrycodeTo'] = "SAU"
    order_details['FromDate'] = str(another_startdate + (another_enddate-another_startdate) * random.random())
    order_details['ToDate'] = str(another_startdate + (another_enddate-another_startdate) * random.random())
    order_details['FlightFrom'] = "GIZ"
    order_details['FlightTo'] = "DMM"
    order_details['FromCountry'] = str(translator.translate("United Arabic Emirates"))
    order_details['ToCountry'] = "King Fhad International Airpot"
    order_details['FromCityNameAr'] = None
    order_details['ToCityNameAr'] = None
    order_details['FromAirportName'] = None
    order_details['ToAirpotName'] = None
    dummy['Request']['Order_Details'] = order_details
    dummy['Request']['FromDateWhenNoTicket'] =  str(start_date + (end_date - start_date) * random.random())
    dummy['Request']['ToDateWhenNoTicket'] =  str(start_date + (end_date - start_date) * random.random())
    dummy['Request']['TicketClassWhenNoTicket'] = "ECONOMY"
    dummy['Request']['TripTypeId'] = 1
    dummy['Request']['TripTypeName'] = None
    dummy['Request']['AfterDays'] = None
    dummy['Request']['IsInBoundReuest'] =random.choices([True,False])
    dummy['Request']['SelectedGoFlightDuration'] = "295"
    dummy['Request']['SelctedFlighFareFamily'] = "EGOV"
    dummy['Request']['SelectedFlightFareFamilyHierarchy'] = "6500"
    dummy['Request']['UserLoginId'] = random.randint(pow(10,6),pow(10,7)-1)
    dummy['Request']['FromDate'] = str(start_date + (end_date - start_date) * random.random())
    dummy['Request']['ToDate'] = str(start_date + (end_date - start_date) * random.random())
    dummy['Request']['SelectedFlightId'] = ''.join(random.choices(string.ascii_uppercase +
                                string.digits + string.punctuation, k=50))
    dummy['Request']['OfficeCode'] =''.join(random.choices(string.ascii_uppercase +
                                string.digits,k=10))
    dummy['Request']['MultiTripCode'] = None
    dummy['Request']['FlightSegmentList'] = None
    dummy['Request']['FlightIndex'] = None

    # dummy_data.append(dummy)
    with open(file_path, mode='a', encoding='utf-8') as feedsjson:
      feedsjson.write(json.dumps(dummy,indent=4))
    
   
path = r'C:\Soft Mania\Usecase 3\mkdir'
files_dir(path)