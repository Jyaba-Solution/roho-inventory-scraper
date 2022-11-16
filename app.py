import requests
import pandas as pd
import re
from datetime import datetime
from config import cookies, headers, private_key, total_records, total_value, product_list_file,product_output_file, params

def crawl_product_id():
    start_index = 1
    total_size = total_value
    product_list = []

    data = {
    'isPermaOrEmbed': 'true',
    'printFooterClassName': '',
    'zc_ColMenu': 'true',
    'zc_Export': 'false',
    'pageSize': '10', # This is changing
    'allowAdd': 'true',
    'zc_SecHeader': 'false',
    'tableName': 't_3816014000000995386',
    'viewLinkName': 'CATALOGO',
    'zc_MoreAction': 'false',
    'zc_DelRec': 'false',
    'aggrColSize': '0',
    'zc_AddRec': 'false',
    'zc_HeaderColor': 'background-color:#ffffff',
    'zc_Search': 'true',
    'zc_EditBulkRec': 'false',
    'previousfromIDX': '-1',
    'formDisplayName': 'ARTICULO',
    'fromIDX': str(start_index), # This is changing 1
    'zc_ScrollTop': '0',
    'allowDelete': 'true',
    'isPerma': 'false',
    'zc_Add': 'false',
    'isSharedAnalyticsReport': 'false',
    'parentViewID': '3816014000004149049',
    'isRecSummaryUrl': 'false',
    'zc_ScrollLeft': '0',
    'isLastPage': 'false',
    'viewFormName': 'ARTICULO',
    'viewType': '9',
    'baseViewType': '9',
    'zc_Header': 'false',
    'zc_RecPrint': 'false',
    'zc_ReportName': 'false',
    'zc_LoadIn': '',
    'isGroup': 'true',
    'searchCrit': '',
    'zc_BoderColor': 'border:',
    'totalRecords': str(total_records),
    'zc_SaveRec': 'false',
    'zc_EditRec': 'false',
    'showReportWarning': 'false',
    'zc_GroupHeaderColor': 'background-color:',
    'isDetailedView': 'false',
    'baseViewLinkName': 'CATALOGO',
    'viewDispName': 'CATALOGO',
    'viewID': '3816014000004149049',
    'toIDX': str(total_value), # This is changing 50
    'allowEdit': 'true',
    'nViewName': '3816014000000995386',
    'reportPrintClassName': '',
    'zc_RecordScroll': 'true',
    'zc_Filter': 'true',
    'zc_SumRow': 'true',
    'allowDuplicate': 'true',
    'isCreatorFive': 'true',
    'isEmbed': 'true',
    'zc_Print': 'false',
    'showPage': '',
    'viewFormID': '3816014000000995386',
    'urlParams': '{}',
    'previoustoIDX': '-1',
    'dataSize': str(total_size), # THis is changing 45
    'isPrint': 'false',
    'SUMMARY_LAYOUTTYPE': '1',
    'zc_BulkDelete': 'true',
    'footerClass': 'zc-summary-details-action',
    'privatelink': private_key ,
    'allowBulkEdit': 'true',
    'zc_Footer': 'true',
    'isHTML': 'false',
    'zc_Import': 'false',
    'zc_RecSelect': 'false',
    'zc_DuplRec': 'false',
    'isFirstPage': 'false',
    'isThirdpartyReport': 'false',
    'openSearch': 'false',
    'filterVal': 'All',
    'parentViewType': '',
    'isUpdateRecords': 'true',
    }
    while start_index < total_records:
        new_data = data.copy()
        new_data['fromIDX'] = str(start_index)
        new_data['toIDX'] = str(total_value)
        new_data['dataSize'] = str(total_size)

        response = requests.post('https://creatorapp.zohopublic.com/francisco.roda/roho-inventory/report-embed-json/CATALOGO', cookies=cookies, headers=headers, data=new_data)

        try:
            response_files = response.json()['MODEL']['DATAJSONARRAY'][0]['data']
        except:
            print(response.text)
            break
        print(len(response_files))
        print("Running from {} to {}".format(start_index, total_value))

        # write all Ids
        for product in response_files:
            product_list.append(product['ID'])
        start_index += total_value
        total_size = start_index - 1
        
    with open(product_list_file, 'w') as f:
        f.write(','.join(product_list) + ',')
    


def crawl_product():
    product_list = []
    product_ids = open(product_list_file).read().split(',') 
    product_ids = list(set(product_ids))
    id_list = [id for id in product_ids if id]
    for id in id_list:
        response = requests.get(f'https://creatorapp.zohopublic.com/francisco.roda/roho-inventory/summary-embed/CATALOGO/{id}', params=params, cookies=cookies, headers=headers)
        data = response.json()['MODEL']['DATAJSONARRAY'][0]
        product_details = {}
        product_details['Date'] = datetime.now().strftime('%Y-%m-%d')
        product_details['Canal'] = 'Roho HomeCenter'
        product_details['Category'] = data.get('CATEGORIA_OBJ')
        product_details['Subcategory2'] = ''
        product_details['Subcategory3'] = ''
        product_details['Marca'] = ''
        product_details['Modelo'] = ''
        product_details['SKU'] = data.get('SKU', '')
        product_details['UPC'] = data.get('UPC', '')
        product_details['Item'] = data.get('Descripcion', '')
        product_details['item_characteristics'] = data.get('DESCRIPCION_DE_CATALOGO', '')
        product_details['URL SKU'] = f'https://creatorapp.zohopublic.com/francisco.roda/roho-inventory/summary/CATALOGO/{id}'
        # product_details['profile_link']= re.findall('downqual="(.*?)"',images) 
        images = data['FOTO_DE_CATALOGO'] if data.get('FOTO_DE_CATALOGO') else ''
        product_details['Image'] =  re.findall('downqual="(.*?)"',images)
        product_details['Price'] = data['PRECIO_DE_LISTA']
        product_details['Sale Price'] = data['DESCUENTO']
        product_details['Shipment Cost'] = ''
        product_details['Sales Flag'] = ''
        product_details['Store ID'] = ''
        product_details['Store Name'] = ''
        product_details['Store Address'] = ''
        product_details['Stock'] = ''
        product_details['UPC WM'] = ''
        product_details['Final Price'] = data['PRECIO_FINAL']




        product_list.append(product_details)
        df = pd.DataFrame(product_list)
        df.to_csv(product_output_file, index=False)


if __name__ == '__main__':
    print("Starting to crawl product id ...")
    crawl_product_id()
    print("Finished crawling product id ...")
    print("Starting to crawl product details ...")
    crawl_product()
    print("Finished crawling product details ...")
