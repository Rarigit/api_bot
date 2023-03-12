import requests
import json
import time

api_url = 'http://127.0.0.1:5000/api/market-btc'


while True:
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h")
    data = response.json()
    btc = data[00]
    eth = data[1]
    usdt = data[2]
    bnb = data[3]
    xrp = data[5]
    ada = data[6]
    matic = data[7]
    doge = data[8]
    sol = data[11]
    dot = data[12]

    ath_value = btc.get('ath')
    atl_value = btc.get('atl')
    cur_price_value = btc.get('current_price')
    market_cap_value = btc.get('market_cap')
    market_cap_rank_value = btc.get('market_cap_rank')
    name_value = btc.get('name')
    total_supply_value = btc.get('total_supply')
    total_volume_value = btc.get('total_volume')
    #Eth json data parse
    ath_value_eth = eth.get('ath')
    atl_value_eth = eth.get('atl')
    cur_price_value_eth = eth.get('current_price')
    market_cap_value_eth = eth.get('market_cap')
    market_cap_rank_value_eth = eth.get('market_cap_rank')
    name_value_eth = eth.get('name')
    total_supply_value_eth = eth.get('total_supply')
    total_volume_value_eth = eth.get('total_volume')
    #USDT json data parse
    ath_value_usdt = usdt.get('ath')
    atl_value_usdt= usdt.get('atl')
    cur_price_value_usdt = usdt.get('current_price')
    market_cap_value_usdt = usdt.get('market_cap')
    market_cap_rank_value_usdt = usdt.get('market_cap_rank')
    name_value_usdt = usdt.get('name')
    total_supply_value_usdt = usdt.get('total_supply')
    total_volume_value_usdt = usdt.get('total_volume')
    #BNB json data parse
    ath_value_bnb = bnb.get('ath')
    atl_value_bnb= bnb.get('atl')
    cur_price_value_bnb = bnb.get('current_price')
    market_cap_value_bnb = bnb.get('market_cap')
    market_cap_rank_value_bnb = bnb.get('market_cap_rank')
    name_value_bnb = bnb.get('name')
    total_supply_value_bnb = bnb.get('total_supply')
    total_volume_value_bnb = bnb.get('total_volume')
    #XRP json data parse
    ath_value_xrp = xrp.get('ath')
    atl_value_xrp= xrp.get('atl')
    cur_price_value_xrp = xrp.get('current_price')
    market_cap_value_xrp = xrp.get('market_cap')
    market_cap_rank_value_xrp = xrp.get('market_cap_rank')
    name_value_xrp = xrp.get('name')
    total_supply_value_xrp = xrp.get('total_supply')
    total_volume_value_xrp = xrp.get('total_volume')
    #ADA json parse
    ath_value_ada = ada.get('ath')
    atl_value_ada= ada.get('atl')
    cur_price_value_ada = ada.get('current_price')
    market_cap_value_ada = ada.get('market_cap')
    market_cap_rank_value_ada = ada.get('market_cap_rank')
    name_value_ada = ada.get('name')
    total_supply_value_ada = ada.get('total_supply')
    total_volume_value_ada = ada.get('total_volume')
    #Matic json parse
    ath_value_matic = matic.get('ath')
    atl_value_matic= matic.get('atl')
    cur_price_value_matic = matic.get('current_price')
    market_cap_value_matic = matic.get('market_cap')
    market_cap_rank_value_matic = matic.get('market_cap_rank')
    name_value_matic = matic.get('name')
    total_supply_value_matic = matic.get('total_supply')
    total_volume_value_matic = matic.get('total_volume')
    #Doge json parse
    ath_value_doge = doge.get('ath')
    atl_value_doge= doge.get('atl')
    cur_price_value_doge = doge.get('current_price')
    market_cap_value_doge = doge.get('market_cap')
    market_cap_rank_value_doge = doge.get('market_cap_rank')
    name_value_doge = doge.get('name')
    total_supply_value_doge = doge.get('total_supply')
    total_volume_value_doge = doge.get('total_volume')
    #Sol json parse
    ath_value_sol = sol.get('ath')
    atl_value_sol= sol.get('atl')
    cur_price_value_sol = sol.get('current_price')
    market_cap_value_sol = sol.get('market_cap')
    market_cap_rank_value_sol = sol.get('market_cap_rank')
    name_value_sol = sol.get('name')
    total_supply_value_sol = sol.get('total_supply')
    total_volume_value_sol = sol.get('total_volume')
    #Dot json parse
    ath_value_dot = dot.get('ath')
    atl_value_dot= dot.get('atl')
    cur_price_value_dot = dot.get('current_price')
    market_cap_value_dot = dot.get('market_cap')
    market_cap_rank_value_dot = dot.get('market_cap_rank')
    name_value_dot = dot.get('name')
    total_supply_value_dot = dot.get('total_supply')
    total_volume_value_dot = dot.get('total_volume')

    alpha = {'ath': ath_value, 'atl': atl_value, 'current_price': cur_price_value, 'market_cap': market_cap_value, 'market_cap_rank': market_cap_rank_value, 'name': name_value, 'total_supply': total_supply_value, 'total_volume': total_volume_value,
                'athEth': ath_value_eth, 'atlEth': atl_value_eth, 'current_priceEth': cur_price_value_eth, 'market_capEth': market_cap_value_eth, 'market_cap_rankEth': market_cap_rank_value_eth, 'nameEth': name_value_eth, 'total_supplyEth': total_supply_value_eth, 'total_volumeEth': total_volume_value_eth,
                'athUsdt': ath_value_usdt, 'atlUsdt': atl_value_usdt, 'current_priceUsdt': cur_price_value_usdt, 'market_capUsdt': market_cap_value_usdt, 'market_cap_rankUsdt': market_cap_rank_value_usdt, 'nameUsdt': name_value_usdt, 'total_supplyUsdt': total_supply_value_usdt, 'total_volumeUsdt': total_volume_value_usdt,
                'athBnb': ath_value_bnb, 'atlBnb': atl_value_bnb, 'current_priceBnb': cur_price_value_bnb, 'market_capBnb': market_cap_value_bnb, 'market_cap_rankBnb': market_cap_rank_value_bnb, 'nameBnb': name_value_bnb, 'total_supplyBnb': total_supply_value_bnb, 'total_volumeBnb': total_volume_value_bnb,
                'athXrp': ath_value_xrp, 'atlXrp': atl_value_xrp, 'current_priceXrp': cur_price_value_xrp, 'market_capXrp': market_cap_value_xrp, 'market_cap_rankXrp': market_cap_rank_value_xrp, 'nameXrp': name_value_xrp, 'total_supplyXrp': total_supply_value_xrp, 'total_volumeXrp': total_volume_value_xrp,
                'athAda': ath_value_ada, 'atlAda': atl_value_ada, 'current_priceAda': cur_price_value_ada, 'market_capAda': market_cap_value_ada, 'market_cap_rankAda': market_cap_rank_value_ada, 'nameAda': name_value_ada, 'total_supplyAda': total_supply_value_ada, 'total_volumeAda': total_volume_value_ada,
                'athMatic': ath_value_matic, 'atlMatic': atl_value_matic, 'current_priceMatic': cur_price_value_matic, 'market_capMatic': market_cap_value_matic, 'market_cap_rankMatic': market_cap_rank_value_matic, 'nameMatic': name_value_matic, 'total_supplyMatic': total_supply_value_matic, 'total_volumeMatic': total_volume_value_matic,
                'athDoge': ath_value_doge, 'atlDoge': atl_value_doge, 'current_priceDoge': cur_price_value_doge, 'market_capDoge': market_cap_value_doge, 'market_cap_rankDoge': market_cap_rank_value_doge, 'nameDoge': name_value_doge, 'total_supplyDoge': total_supply_value_doge, 'total_volumeDoge': total_volume_value_doge,
                'athSol': ath_value_sol, 'atlSol': atl_value_sol, 'current_priceSol': cur_price_value_sol, 'market_capSol': market_cap_value_sol, 'market_cap_rankSol': market_cap_rank_value_sol, 'nameSol': name_value_sol, 'total_supplySol': total_supply_value_sol, 'total_volumeSol': total_volume_value_sol,
                'athDot': ath_value_dot, 'atlDot': atl_value_dot, 'current_priceDot': cur_price_value_dot, 'market_capDot': market_cap_value_dot, 'market_cap_rankDot': market_cap_rank_value_dot, 'nameDot': name_value_dot, 'total_supplyDot': total_supply_value_dot, 'total_volumeDot': total_volume_value_dot}                                                                                                     
    
    
    response = requests.post(api_url, json=alpha)
#Make sure to uniquely name the outgoing json data set so that it is able to be extracted properly in my restful api 
#Every minute it should send over the price-data. Keep bot running in own terminal.
    time.sleep(60)