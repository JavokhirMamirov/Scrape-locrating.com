import requests

url = "https://www.locrating.com/LocratingWebService.asmx/GetInfoWindowDetails2_plugin"

payload = "{\r\n    \"id\": \"urn101018\",\r\n    \"GUID\": \"BCB692BD-E5DD-4971-8B1A-E406E494C23F\",\r\n    \"user\": \"\",\r\n    \"userType\": -1\r\n}"
headers = {
  'sticket': 'sAfqi+6XuXfQThU0TbYQvaxnqbhV+H4LWWy4oAPrBpwr79iQZvDFHdNULi1bs0+EtYpHFW7oVSNPMsHg9/Qxj6CohOI4t0SY9YxsOH13fv7cQV8ua254gYGs5UrXMPcAgeAV1/7RD0u8Y34ef2PdVAp/hPic+AnHZ2v9ok3qD5r1GU9GuO/gzWv2VvUPo+G3/UuXdHte27vA/hWnApZCVpoOd3s8P7fTWrLsx+EAPqlCvsJx4hcOzfgR+mk+QO/tQTlkZ0/QuGNIt31qwmVUGB1Sw1F3lMfnHqjGUdALc43p00d1WXzXw5IuZ7Ph2DQpGAgYwO7yAKPbYQo9IYPf+gep56WadUIOKRmY45e3CcFqEuAeRSMEBlW57KsRk6wCMe1drp3bcMgyF6vILYyIkrXuDuR0AzNj34DI2zNN35+/McL5gm3e4QqSIh1qw1XWcPjd4pN2caguxJcT72RSAyNYSq4YzIbe3RhTNF4PPN/2smS/5XqYOSaXOKYj2mtlzmyJfWv9zE6I+m0tGIyUvTHdXKjdMb6XF2/JDLzXwbXiiMWA2vSQFUjbvrZIIb+ML1Fnrd2oiCoaCDO5sJlhAjZBVos03STUPhBdffl8L/3jRxXHwtmdHsvIjmZfp4VjEs0qa/Bsezxu9nyYmRkJE4zDfXFyWBr8Ik3l+hn1ErclNCDKSP0fdw/itWWIbBxV',
  'x-requested-with': 'XMLHttpRequest',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,uz;q=0.7',
  'Content-Type': 'application/json; charset=UTF-8',
  'DNT': '1',
  'Origin': 'https://www.locrating.com',
  'Referer': 'https://www.locrating.com/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'Cookie': 'ASP.NET_SessionId=km5ojrwcxemefn4eqgm5vcgg'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
