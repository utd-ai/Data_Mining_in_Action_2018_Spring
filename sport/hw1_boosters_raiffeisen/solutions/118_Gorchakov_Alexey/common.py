# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import datetime

SPB = "SPB"
SAMARA = "SAMARA"
S_POSAD = "S_POSAD"
MSK = "MSK"
NN = "NN"
NCH = "NCH"
NF = "NF"
EKB = "EKB"
KZN = "KZN"
KHMK = "KHMK"
KHMS = "KHMS"
HBR = "HBR"
ORZ = "ORZ"
RND = "RND"
VOR = "VOR"
VOLZ = "VOLZH" # Рядом с волгоградом
KRYSK = "KRYSK"
CITY_MAPPER = {
    "st petersburg": SPB,
    "sankt-peterbu": SPB,
'sank-peterbur': SPB,
 'sanket peterb': SPB,
 'sankpeterburg': SPB,
 'sankt - peter': SPB,
 'sankt pererbu': SPB,
 'sankt peterbu': SPB,
 'sankt petersb': SPB,
 'sankt-pekterb': SPB,
 'sankt-pererbu': SPB,
 'sankt-petebur': SPB,
 'sankt-peter': SPB,
 'sankt-peterbo': SPB,
 'sankt-peters': SPB,
 'sankt-petersb': SPB,
 'sankt-peterub': SPB,
 'sankt-prtrrbu': SPB,
 'sankt-pterbur': SPB,
 'sanqt peterbu': SPB,
 'sant peterbur': SPB,
'san peterburg': SPB,
 'san-peterburg': SPB,    
'speterburg': SPB,
 'spetersburg': SPB,
 'spetersrurg': SPB,    
 'stpete': SPB,
 'stpeterburg': SPB,
 'stpetersburg': SPB,    
 'st.-peterburg': SPB,
 'st.-petersbur': SPB,
 'st.peresburg': SPB,
 'st.peterburg': SPB,
 'st.petersburg': SPB,
 'st.petesburg': SPB,
 'st.petresburg': SPB,
 'st.petrsburg': SPB,
 'st/petersburg': SPB,    
 'st-peter': SPB,
 'st-peter.': SPB,
 'st-peterb.': SPB,
 'st-peterbur': SPB,
 'st-peterburg': SPB,
 'st-petersburg': SPB,
 'st-peterurg': SPB,    
 'st peterburg': SPB,
 'st petersbur': SPB,
 'snpeterburg': SPB,  
 'spb': SPB,
 'saint peterbu': SPB,
 'saint petersb': SPB,
 'saint-peterbu': SPB,
 'saint-petersb': SPB,    
 's.peterburg': SPB,
 's.peterburg,': SPB,
 's.petersburg': SPB,    
's.-peterburg': SPB ,    
 's-peter': SPB,
 's-peterburg': SPB,
 's-petersburg': SPB,    
 's. peterburg': SPB,    
's peterburg': SPB,    
    'c-peterburg': SPB,
    
 'serg posad': S_POSAD,
 'sergev posad': S_POSAD,
 'sergie posad': S_POSAD,
 'sergiev pasad': S_POSAD,
 'sergiev posa': S_POSAD,
 'sergiev posad': S_POSAD,
 'sergiev-posad': S_POSAD,
 'sergievo posa': S_POSAD,
 'sergievo-posa': S_POSAD,
 'sergievposad': S_POSAD,   
    
    
'samara': SAMARA,
 'samara g': SAMARA,
 'samara mkrn k': SAMARA,
 'samara p.bere': SAMARA,
 'samara pos.up': SAMARA,
 'samara*': SAMARA,
 'samara,mkr kr': SAMARA,
 'samara,mkr. k': SAMARA,    
    
    'mockva': MSK,    
    'moscow': MSK,
    'moskow': MSK,
    'moskva': MSK,
'moskva.': MSK,
 'moskvaa': MSK,
 'moskve': MSK,
 'moskvy': MSK,
 'moskwa': MSK,
 'mosocw': MSK,    
 'mosva': MSK,
    '*moscow': MSK,

    'n novgorod': NN,
    'n-novgorod': NN,
    'n. novgorod': NN,
    'n.-novgorod': NN,
    'n.novgorod': NN,
    'nighniy novgo': NN,
'nigniy novgor': NN,
 'nijiy novgoro': NN,
 'nijnii novgor': NN,
 'nijniy novgor': NN,
'nizgniy novgo': NN,
 'nizh novgorod': NN,
 'nizh.novgorod': NN,
'nizhhiy novgo': NN,
 'nizhn.novgord': NN,
'nizhnii novg': NN,
 'nizhnii novgo': NN,
 'nizhniiy novg': NN,
 'nizhnij novgo': NN,
 'nizhniy novg': NN,
 'nizhniy novgo': NN,
 'nizhniy-novgo': NN,
 'nizhniyj novg': NN,
 'nizhny novgor': NN,
 'nizhnyi novgo': NN,
 'nizjniy novgo': NN,    
'nizniy novgor': NN,
 'niznov': NN,    
'nnovgorod': NN,    
'nyzhny novgor': NN,    
    
    'nab chelny': NCH, 
'nab. chelny': NCH,
 'nab.chelny': NCH,
 'nabche': NCH,
 'naber. chelny': NCH,
 'naber.chelny': NCH,
 'naberezh.chel': NCH,
 'naberezhnie c': NCH,
 'naberezhniye': NCH,
 'naberezhnue c': NCH,
 'naberezhnye c': NCH,
 'naberezhnyie': NCH,
 'naberezhnyye': NCH,
 'nabereznie ch': NCH,
 'n.chelny': NCH,
    
'naro fominsk': NF,
    'naor-fominsk': NF,
    'n-fominsk': NF,
'naro-fominsk': NF,
 'naro-fominski': NF,
 'narofominsk': NF,
    
'eka-burg': EKB,
 'ekaterinb': EKB,
 'ekaterinbourg': EKB,
 'ekaterinburg': EKB,
 'ekaterinburg,': EKB,
 'ekaterinburtg': EKB,
 'ekaterinbyrg': EKB,
 'ekaterindurg': EKB,
 'ekaterniburg': EKB,
 'ekaterubbyrg': EKB,
 'ekatirinburg': EKB,
 'ekatr': EKB,
 'eketerinburg': EKB,
 'ekt': EKB,    

'kazan': KZN,
 'kazan g': KZN,
 "kazan'": KZN,
 'kazan, scherb':KZN,
 'kazan`':KZN,
    
    "khimki": KHMK,
    'khimki': KHMK,
    'khimki g': KHMK,
    'khimki ikea': KHMK,
    'khimki levobe': KHMK,
    'khimki mkr. p': KHMK,
    'khimki region': KHMK,
    'khimki, kvart': KHMK,
    'khimki, mkr.': KHMK,
    'khimki, mkr.l': KHMK,
    'khimki, mkr.s': KHMK,
    'khimki,mkr.po': KHMK,
    'khimki,mkr.sk': KHMK,
    'khimki-skhodn': KHMK,
    'khimkinskiy': KHMK,
    'khimkinskiy r': KHMK,
    'khimkm': KHMK,
    'khimky': KHMK,
    'himki': KHMK,
    'himky': KHMK,
    
    'hante-mansiis': KHMS,
    'hanty mansiys': KHMS,
    'hanty-mansijs': KHMS,
    'kh-mansiysk': KHMS,
    'khanty-mansiy': KHMS,
    
    'khabarovsk':HBR,
    'khabarovsk g':HBR,
    'khabrv':HBR,
    'habarovsk':HBR,

'orehkovo zuev' : ORZ,
'orehovo zuevo' : ORZ,
'orehovo-zueva' : ORZ,
'orehovo-zuevo' : ORZ,
'orehovo-zuyev' : ORZ,
'orehovo-zyevs' : ORZ,
'orekhovo - zu' : ORZ,
'orekhovo zuev' : ORZ,
'orekhovo-zu' : ORZ,
'orekhovo-zuev' : ORZ,
'orekhz' : ORZ,    
    
    'ros-na-donu': RND,
    'rostdn': RND,
    'roston': RND,
    'rostov na don': RND,
    'rostov nd': RND,
    'rostov on don': RND,
'rostov-don': RND,
'rostov-n': RND,
'rostov-na -do': RND,
'rostov-na-d': RND,
'rostov-na-do': RND,
'rostov-na-don': RND,
'rostov-on-don': RND,
'rostov.na.don': RND,
'rostov/donu': RND,
    'rostovnadonu': RND,
    
    'voronazh': VOR,
'voroneg': VOR,
'voronegh': VOR,
'voronej': VOR,
'voronezh': VOR,
'voronezh g': VOR,
    
'volzhskiiy':VOLZ,
'volzhskij':VOLZ,
'volzhskiy':VOLZ,
'volzhskiy ute':VOLZ,
'volzhskiy,p.':VOLZ,
'volzhsky':VOLZ,
'volzhsqii':VOLZ,
'volzshskiy':VOLZ,

'krasn-nsk':KRYSK,
    'krasnoryask':KRYSK,
'krasnoyarsk':KRYSK,
'krasnoyarsk g':KRYSK,
'krasnoyask':KRYSK,
'krasnoyasrk':KRYSK,
'krasnoyasrsk':KRYSK,
}

def map_city(name):
    if name in CITY_MAPPER:
        return CITY_MAPPER[name]
    else:
        return name

def get_unite_df_mk1():
    train_df = load_train_mk2()
    test_df = load_test_mk2()
    
    df = pd.concat([train_df, test_df])
    print len(df)
    df['is_atm'] = (~df['atm_address_lat'].isnull()).astype(np.int32)
    df['is_pos'] = (~df['pos_address_lat'].isnull()).astype(np.int32)

    df['address_lat'] = df['atm_address_lat'].fillna(0) + df['pos_address_lat'].fillna(0)
    df['address_lon'] = df['atm_address_lon'].fillna(0) + df['pos_address_lon'].fillna(0)

    df.drop(['atm_address_lat','atm_address_lon','pos_address_lat','pos_address_lon'], axis = 1, inplace = True)

    # удалим транзакции без адреса
    df.drop(df[((df['address_lon'] == 0) & (df['address_lat'] == 0))].index, axis = 0, inplace = True)
    print len(df)
    
    # Генерируем признаки is_home, is_work
    lat = df['home_add_lat'] - df['address_lat']
    lon = df['home_add_lon'] - df['address_lon']
    df['is_home'] = (np.sqrt((lat ** 2) + (lon ** 2)) <= 0.02).astype(np.int32)
    df['has_home'] = (~df['home_add_lon'].isnull()).astype(np.int32)

    lat = df['work_add_lat'] - df['address_lat']
    lon = df['work_add_lon'] - df['address_lon']
    df['is_work'] = (np.sqrt((lat ** 2) + (lon ** 2)) <= 0.02).astype(np.int32)
    df['has_work'] = (~df['work_add_lon'].isnull()).astype(np.int32)    
    
    # Генерируем категориальный признак для адреса
    df['address'] = df['address_lat'].apply(lambda x: "%.02f" % x) + ';' + df['address_lon'].apply(lambda x: "%.02f" % x)    
    
    df['address_f'] = df['address'].factorize()[0].astype(np.int32)
    
    # количество транзакций каждого клиента
    df = df.merge(df.groupby('customer_id')['amount'].count().reset_index(name = 'tx'), how = 'left')
    df['tx'] = df['tx'].astype(np.int32)

    df = df.merge(df.groupby(['customer_id','address'])['amount'].count().reset_index(name = 'tx_cust_addr'), how = 'left')
    df['tx_cust_addr'] = df['tx_cust_addr'].astype(np.int32)

    # какая часть транзакций клиента приходится на данный адрес
    df['ratio1'] = df['tx_cust_addr'] / df['tx']    
    
    df['weekday'] = df['transaction_date'].dt.weekday.astype(np.int32)
    
    df['city_f'] = df['city'].str.strip().str.lower().str.replace("`", "").str.replace("'", "").str.replace("g. ", "").str.replace("g ", "").str.replace(" g", "").apply(map_city).factorize()[0].astype(np.int32)
    
    return df

def get_rus_country_mask(df):
    rus_country_mask = (df.country == "RUS") | (df.country == "RU")
    return rus_country_mask

def load_train():
    train_df_raw = pd.read_csv("./data/train_set.csv", encoding="utf-8")
    train_df_raw.rename(columns = {u"pos_adress_lat": u"pos_address_lat", u"pos_adress_lon": u"pos_address_lon"}, inplace=True)
    train_df_raw["train"] = True
    train_df_raw["row_n"] =  pd.RangeIndex(start=0,stop=train_df_raw.shape[0])
    rus_country_mask = get_rus_country_mask(train_df_raw)
    return train_df_raw[rus_country_mask]

def load_train_mk2():
    dtypes = {
        'amount': np.float32,
        'atm_address': str,
        'atm_address_lat': np.float32,
        'atm_address_lon': np.float32,
        'city': str,
        'country': str,
        'currency': np.float32,
        'customer_id': str,
        'home_add_lat': np.float32,
        'home_add_lon': np.float32,
        'mcc': np.int32,
        'pos_address': str,
        'pos_address_lat': np.float32,'pos_adress_lat': np.float32,
        'pos_address_lon': np.float32,'pos_adress_lon': np.float32,
        'terminal_id': str,
        'transaction_date': str,
        'work_add_lat': np.float32,
        'work_add_lon': np.float32,
    }
    train_df_raw = pd.read_csv("./data/train_set.csv", encoding="utf-8", dtype = dtypes)
    print len(train_df_raw)
    train_df_raw.rename(columns = {u"pos_adress_lat": u"pos_address_lat", u"pos_adress_lon": u"pos_address_lon"}, inplace=True)
    train_df_raw['is_train'] = np.int32(1)
    train_df_raw["row_n"] =  pd.RangeIndex(start=0,stop=train_df_raw.shape[0])
    rus_country_mask = get_rus_country_mask(train_df_raw)
    train_df_raw.drop(train_df_raw[~rus_country_mask].index, axis = 0, inplace = True)
    del train_df_raw["country"]
    print len(train_df_raw)

    train_df_raw['currency'] = train_df_raw['currency'].fillna(-1).astype(np.int32)
    
    # удаляем транзакции без даты
    no_transaction_date_mask = train_df_raw['transaction_date'].isnull()
    train_df_raw.drop(train_df_raw[no_transaction_date_mask].index, axis = 0, inplace = True)
    print len(train_df_raw)
    
    train_df_raw['transaction_date'] = train_df_raw['transaction_date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))    
    return train_df_raw

def factorize_city(df):
    return df['city'].factorize()

def load_test():
    dtypes={
        "amount": "float64",
        "mcc": "str",
        "atm_address": "str",
        "pos_address": "str",
    }    
   
    df_raw = pd.read_csv("./data/test_set.csv", encoding="utf-8", dtype = dtypes)
    
    df_raw["train"] = False
    mcc = df_raw.pop("mcc")
    mcc = mcc.apply(lambda x: int(x.replace(",", ""))) 
    df_raw["mcc"] = mcc
    rus_country_mask = get_rus_country_mask(df_raw)
    return df_raw[rus_country_mask]

def load_test_mk2():
    dtypes = {
        'amount': np.float32,
        'atm_address': str,
        'atm_address_lat': np.float32,
        'atm_address_lon': np.float32,
        'city': str,
        'country': str,
        'currency': np.float32,
        'customer_id': str,
        'home_add_lat': np.float32,
        'home_add_lon': np.float32,
        'mcc': str,
        'pos_address': str,
        'pos_address_lat': np.float32,'pos_adress_lat': np.float32,
        'pos_address_lon': np.float32,'pos_adress_lon': np.float32,
        'terminal_id': str,
        'transaction_date': str,
        'work_add_lat': np.float32,
        'work_add_lon': np.float32,
    }  
    df_raw = pd.read_csv("./data/test_set.csv", encoding="utf-8", dtype = dtypes)
    print len(df_raw)
    df_raw['is_train'] = np.int32(0)
    shift = 700000000
    df_raw["row_n"] =  pd.RangeIndex(start=0 + shift,stop=df_raw.shape[0]  + shift)

    mcc = df_raw.pop("mcc")
    mcc = mcc.apply(lambda x: int(x.replace(",", ""))) 
    df_raw["mcc"] = mcc.astype(np.int32)
    rus_country_mask = get_rus_country_mask(df_raw)

    df_raw.drop(df_raw[~rus_country_mask].index, axis = 0, inplace = True)
    del df_raw["country"]
    print len(df_raw)
    
    df_raw['currency'] = df_raw['currency'].fillna(-1).astype(np.int32)
    
    # удаляем транзакции без даты
    no_transaction_date_mask = df_raw['transaction_date'].isnull()
    df_raw.drop(df_raw[no_transaction_date_mask].index, axis = 0, inplace = True)
    print len(df_raw)
    
    df_raw['transaction_date'] = df_raw['transaction_date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))    
    
    return df_raw




def get_columns_and_dtypes(df):
    return zip(df.columns, range(len(df.columns) + 1), [df[name].dtype for name in df.columns])

def print_columns_and_dtypes(df):
    for item in get_columns_and_dtypes(df):
        print item    

def get_cid_by_atm_adress(atm_addr, df):
    _mask = df[df.atm_address.notna()].apply(lambda x: atm_addr in x.atm_address, axis = 1)
    return df[df.atm_address.notna()][_mask].customer_id.value_counts().index    

def get_cid_data(cid, df):
    _mask = df.customer_id == cid
    return df[_mask]

def get_work_lat_lon_by_cid(cid, df):
    cid_data = get_cid_data(cid, df)
    return (set(cid_data[cid_data.work_add_lat.notna()].work_add_lat), 
            set(cid_data[cid_data.work_add_lon.notna()].work_add_lon))


def get_lat_lon_home(df):
    lat = sorted(set(df.home_add_lat))[0]
    lon = sorted(set(df.home_add_lon))[0]
    return lat, lon


def get_submission_tempalte():
    submission = pd.read_csv(
    "./data/sample.csv", 
    encoding="utf-8", 
    index_col="customer_id", 
    dtype={"work_add_lat":"double",
    "work_add_lon":"double",
    "home_add_lat":"double",
    "home_add_lon":"double",}
    )
    return submission

def check_columns_for_complete_nan(df):
    for factor in df.columns:
        print factor, not np.any(df[factor].notna())

MOSCOW = u"Москва"
ODINTSOVO = u'ODINTSOVO'
KRASNODAR = u"Краснодар"
SPB = u"Санкт-Петербург"
EKATERINBURG = u"Екатеринбург"
NOVOSIBIRSK = u"Новосибирск"
N_NOVGOROD = u"Нижний Новгород"
CHEREPOVETS = u"CHEREPOVETS"
KRASNOYARSK = u"KRASNOYARSK"
SAMARA = u"SAMARA"
KAZAN= u"KAZAN"
SOCHI = u"SOCHI"
PETROZAVODSK = u"PETROZAVODSK"
KHIMKI = "KHIMKI"
CITY_MAPPING = {
    u'MOSCOW': MOSCOW, 
    u'MOSKVA': MOSCOW, 
    u'MOSKOW': MOSCOW, 
    u'Moskva': MOSCOW, 
    u'ODINTSOVO': ODINTSOVO,
    u'NOVAYA ADYGEY': KRASNODAR,
    u"KRASNODAR": KRASNODAR,
    u'SANKT-PETERBU': SPB,
    u"EKATERINBURG": EKATERINBURG,
    u"NOVOSIBIRSK": NOVOSIBIRSK,
    u"St Petersburg": SPB,
    u"N.NOVGOROD": N_NOVGOROD,
    u"CHEREPOVETS": CHEREPOVETS,
    u"KRASNOYARSK": KRASNOYARSK,
    u"SAMARA": SAMARA,
    u"KAZAN": KAZAN,
    u"SOCHI": SOCHI,
    u"PETROZAVODSK": PETROZAVODSK,
    u"KHIMKI": KHIMKI, # MOSCOW?
}

def add_projected_city(df):
    cp = df["city_pr"] = df.apply(lambda x: CITY_MAPPING[x.city] if x.city in CITY_MAPPING else x.city , axis = 1)
    re
