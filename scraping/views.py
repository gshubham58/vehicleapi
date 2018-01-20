from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import json
def index(request):
    return HttpResponse("Welcome to vehicle api")
class list2(APIView):
    def get(self,request,registration):
        url = "http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx"
        br = RoboBrowser(parser='html.parser')
        br.open(url)
        x = br.get_form(id='aspnetForm')
        x['ctl00$ContentPlaceHolder1$txtRegNo'] = registration
        br.submit_form(x)
        a = str(br.parsed())
        soup = BeautifulSoup(a, "html.parser")
        table = soup.find("table", {"border": "1", "id": "ctl00_ContentPlaceHolder1_grvSearchSummary"})
        for row in table.findAll('tr', {'class': 'GridItem'}):
            col = row.findAll('td')
            a = col[2].find('a').string
            b = col[3].string
            c = col[4].string
            d = col[5].string
            e = col[6].string
            f = col[7].string
            g = col[8].string
            h = col[10].string
            i = col[11].string
            j = col[12].string
            k = col[13].string
            l = col[14].string
            data = {
                'registration_num': a,
                'chassis no': b,
                'engine no': c,
                'owner_name': d,
                'rto_name': e,
                'manu year': f,
                'regis_date': g,
                'issued on': h,
                'colour': i,
                'class': j,
                'maker': k,
                'model': l,

            }
        #response = json.dumps(data)
        return JsonResponse(data,safe=False)

