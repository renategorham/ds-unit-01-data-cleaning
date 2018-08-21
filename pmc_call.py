import pandas as pd
import numpy as np
import requests

pmc_data = {1380:3749005,1382:3583273,1338:3381638,1334:3540040,1284:3604800,1482:3635503,1484:3481955,1752:3606973,2335:3707567,1512:3600839,1495:3476336,
        1494:3570213,1184:3547901,420:3676539,422:23426678,805:3793856,982:3627205,980:3525981,578:3529010,576:3479458,574:3670340,572:3704016,570:3511132,
        438:3586675,430:3655688,426:3724995,580:3479523,582:3538261,586:3666720,611:3738233,610:3607403,600:3503170,594:3746881,592:3752214,590:3587277,
        584:3557024,1929:3682634,1923:3524560,1908:3785133,1867:3388079,1863:3712914,1809:3692470,1961:3549237,2084:3613719,1320:3501977,1319:3634199,
        1318:3159156,1316:3692042,1312:3754462,1310:3692041,1309:3673465,1308:3673458,1767:3526116,1488:3496338,1487:3546802,1486:3413389,2104:3749465,
        2266:3853540,2287:3465775,2330:3819359,2146:3638371,1307:3286332,1303:3639724,660:3793867,560:3644702,774:3438445,913:3562439,202:3734580,198:3597819,
        494:3687256,493:3533127,1160:3627817,1159:3770928,1157:3558801,1155:3717178,1241:3465389,1208:3571806,965:3526787,1129:3563216,1018:3763376,1000:3759846,
        970:3694306,969:3664939,968:3651934,967:3542428,1049:3677134,1100:3087623,1073:3715722,1072:3557415,1069:3676342,1046:3689257,1067:3564010,1065:3502006,
        1056:3759789,1053:3644713,1050:3521128,1066:3444764,1893:3679597,1894:3758187,1956:3492749,2041:3627851,2043:3778840,2147:3698701,2331:3773237,
        2332:3815011,1101:3374517,1110:3510731,1749:3612675,1550:3493395,1530:3475639,1505:3673173,1499:3170535,1497:3580272,1481:3819976,2305:3731578,
        612:3549118,613:3606975,614:3612627,615:3491471,616:3529030,1864:3749971,1865:3460945,1207:3717731,1162:3427885,352:3686250}
pmc_list = pd.DataFrame.from_dict(pmc_data, orient='index', columns=['pmc'])

pmc_get = pmc_list.pmc.apply(str)
for i in pmc_get:
    indx = list(pmc_get.loc[pmc_get == i].index)
    pmc = list(pmc_get.loc[pmc_get == i])
    r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='+i+'&retmode=text&rettype=mln-ta&api_key=3ffbbb6bd110815d69e4aa14b7c26d72ab09')
    print(indx, pmc, r.text)

                        
