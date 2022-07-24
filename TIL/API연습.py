import requests
from pprint import pprint

base_url = 'http://apis.data.go.kr/1051000/MoefOpenAPI/T_OPD_DTLBZ_CSTS'
params = {
    'serviceKey':'nuuu5kzIck8oAbOVyPHu/KFuSkfR32MFJWgByDRn1RA9/fiKsKljk90laL4Uxq9n56q3q/+eWGjD/5EX2wHdNg==',
    'pageNo':1,
    'numOfRows':10,
    'resultType':'json',
    'bsnsyear':2020,
    'dtlbz_nm':'성인전환기 발달장애인 자녀 진로상담 및 코칭 부모교육지원'
}

response = requests.get(base_url, params=params).json()
pprint(response)