import requests
import datetime
from bs4 import BeautifulSoup as bs
from parser.href_groups import all_groups


count = 1


def date(offset_days: int):
    return (datetime.datetime.today() +
            datetime.timedelta(days=offset_days)).strftime('%d.%m.%Y')


def group_par(group: str = '421') -> dict:
    global count
    url = 'http://raspisanie.nnst.ru/public/www/' + all_groups[group]

    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    data = soup.find_all('tr')

    rasp = {}

    begin = 13
    end = 62

    for tr in data[begin:end]:
        two_subgroup_para = []
        for td in tr:
            check_para = td.find('a', class_='z1')
            check_cab = td.find('a', class_='z2')
            para = check_para.text if check_para else ' - '
            cab = check_cab.text if check_cab else ' - '

            if td.get('rowspan') == '6':
                rasp[date := td.text[:-4]] = []

            elif td.get('class') == ['nul']:
                if td.get('colspan') == '2':
                    rasp[date].append([[para, cab], [para, cab]])
                else:
                    if not two_subgroup_para:
                        two_subgroup_para.append([para, cab])
                    else:
                        two_subgroup_para.append([para, cab])
                        rasp[date].append(two_subgroup_para)

            elif td.get('class') == ['ur']:
                if td.get('colspan') == '2':
                    rasp[date].append([[para, cab], [para, cab]])
                else:
                    if not two_subgroup_para:
                        two_subgroup_para.append([para, cab])
                    else:
                        two_subgroup_para.append([para, cab])
                        rasp[date].append(two_subgroup_para)

    return rasp
