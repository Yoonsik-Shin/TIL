import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
serviceKey = os.environ.get('serviceKey')

base_url = 'http://apis.data.go.kr/1051000/MoefOpenAPI/T_OPD_DTLBZ_CSTS'
params = {
    'serviceKey':serviceKey,
    'pageNo':1,
    'numOfRows':10,
    'resultType':'json',
    'bsnsyear':2020,
    'dtlbz_nm':'성인전환기 발달장애인 자녀 진로상담 및 코칭 부모교육지원'
}

response = requests.get(base_url, params=params).json()
pprint(response)