'''This configuration might be different for your account. 
You can find the values by inspecting the network requests in your browser.
The values are in the request body. for cookies '''

cookies = {
    'c3a98dd0f1': 'd6d199fbec1f7a3837eb15c2de47bd3c',
    'zccpn': 'c548f375-509d-40b6-af5e-80077ec37aa5',
    '_zcsr_tmp': 'c548f375-509d-40b6-af5e-80077ec37aa5',
    'JSESSIONID': '33F384C9E152EA99EB4B658F151D61DA',
}
private_key = 'z34R7s1N5Y6evpFgjePs1b10Ut3JAQ0uxZZrN8BZup9h9ZHrtXAsXsQu8YqjfBBam9gvJOqUYJpAd9BBZDQMfnpnkgnRf9wk9R0f'
total_records = 77260
start_index = 1
total_value = 300
total_size = 300
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'c3a98dd0f1=d6d199fbec1f7a3837eb15c2de47bd3c; zccpn=c548f375-509d-40b6-af5e-80077ec37aa5; _zcsr_tmp=c548f375-509d-40b6-af5e-80077ec37aa5; JSESSIONID=33F384C9E152EA99EB4B658F151D61DA',
    'Origin': 'https://creatorapp.zohopublic.com',
    'Referer': f'https://creatorapp.zohopublic.com/francisco.roda/roho-inventory/report-embed/CATALOGO/{private_key}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

product_list_file = 'product_list.txt'
params = {
'privatelink': private_key,
'parentViewType': '9',
}

product_output_file = 'product.csv'