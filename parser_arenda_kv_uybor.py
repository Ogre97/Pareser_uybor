import requests
import datetime
import csv
import time

print('Программа запустилась')
# Берет телефон из json
def telefon(get_id):
	cookies = {
    '_ym_uid': '1646746645670304867',
    '_ym_d': '1646746645',
    '_gid': 'GA1.2.460190280.1652266732',
    '_ym_visorc': 'w',
    '_ym_isad': '2',
    '_gat_gtag_UA_54967882_1': '1',
    '_ga': 'GA1.1.1366460426.1646746648',
    'XSRF-TOKEN': 'eyJpdiI6Ik9aWnArWGh0RGtDcEQzZzlEdG92M1E9PSIsInZhbHVlIjoiTUdWaDBkUnR6dHQrTGNVVkVYdm5CSG1pT2FiQ1dpakVORGE3eHZ2SDNMY3laSWhLaUNaXC8wSTgra0MwRTJTUUhzcDlLTUVqVlR5UlFTZCtrWHFYcEV3PT0iLCJtYWMiOiI4MWE3NDdlNDFlZGYxYjM0ZWJhYzZmMWRjZTdmNzE0YmM1ZDVhNzQyZGNjM2ZkY2ZiYWEzZTk2MzEwZTU2OTE3In0%3D',
    'laravel_session': 'eyJpdiI6IkNnTEpuT2RTOXN5MDdibXZRWTNcL3l3PT0iLCJ2YWx1ZSI6ImYxalVWTkV2Zm84b2NNdDkrQ1dUbStCam84Q1NnOXJxK1ZWZXM1TGtZUW9pY2V4STZRMzZqbU1CTHdxeTlRdGI0NlE2NmR3N2lOMHMzSlJBREJVdVlBPT0iLCJtYWMiOiJhMDUxNjFiMzZiZjljZTdhZGZjYWU5OWRiOTE3YjQ2ZWQ1OTA4NDkyNWZiNWUwN2RmMGU1ZTc1NDYwM2JhZDc2In0%3D',
    '_ga_B3EV6Z01Q8': 'GS1.1.1652266734.40.1.1652268017.0',
	}

	headers = {
	    'Connection': 'keep-alive',
	    'sec-ch-ua': '"Chromium";v="96", "Opera";v="82", ";Not A Brand";v="99"',
	    'X-CSRF-TOKEN': 'tON1IRYvs0ZXHP7YyANYjF1WXgZxlX12GUeofWnE',
	    'sec-ch-ua-mobile': '?0',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Accept': '*/*',
	    'language-code': 'ru',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua-platform': '"Windows"',
	    'Origin': 'https://uybor.uz',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	    'Referer': 'https://uybor.uz/ru/arenda-kvartir/kvartiry-v-tashkente?user_type=ub_private__ub_dealer&order=created_at-DESC',
	    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
	    # Requests sorts cookies= alphabetically
	    # 'Cookie': '_ym_uid=1646746645670304867; _ym_d=1646746645; _gid=GA1.2.460190280.1652266732; _ym_visorc=w; _ym_isad=2; _gat_gtag_UA_54967882_1=1; _ga=GA1.1.1366460426.1646746648; XSRF-TOKEN=eyJpdiI6Ik9aWnArWGh0RGtDcEQzZzlEdG92M1E9PSIsInZhbHVlIjoiTUdWaDBkUnR6dHQrTGNVVkVYdm5CSG1pT2FiQ1dpakVORGE3eHZ2SDNMY3laSWhLaUNaXC8wSTgra0MwRTJTUUhzcDlLTUVqVlR5UlFTZCtrWHFYcEV3PT0iLCJtYWMiOiI4MWE3NDdlNDFlZGYxYjM0ZWJhYzZmMWRjZTdmNzE0YmM1ZDVhNzQyZGNjM2ZkY2ZiYWEzZTk2MzEwZTU2OTE3In0%3D; laravel_session=eyJpdiI6IkNnTEpuT2RTOXN5MDdibXZRWTNcL3l3PT0iLCJ2YWx1ZSI6ImYxalVWTkV2Zm84b2NNdDkrQ1dUbStCam84Q1NnOXJxK1ZWZXM1TGtZUW9pY2V4STZRMzZqbU1CTHdxeTlRdGI0NlE2NmR3N2lOMHMzSlJBREJVdVlBPT0iLCJtYWMiOiJhMDUxNjFiMzZiZjljZTdhZGZjYWU5OWRiOTE3YjQ2ZWQ1OTA4NDkyNWZiNWUwN2RmMGU1ZTc1NDYwM2JhZDc2In0%3D; _ga_B3EV6Z01Q8=GS1.1.1652266734.40.1.1652268017.0',
	}

	data = {
	    'id': str(get_id)
	}

	url = 'https://uybor.uz/listing/search/get-phones'
	telefon_json = requests.post(url=url, headers=headers, cookies=cookies, data=data)
	time.sleep(8)
	tel = telefon_json.json()
	tel_phone = tel['phones'][0]['phone_original']

	print('Получил телефон')
	return tel_phone

def proverka(get_id):
	with open('ID_ojekt.csv', 'r', newline='', encoding='UTF-8') as file:
		ID_ojekt = csv.reader(file)
		for id_spisok in ID_ojekt:
			if str(get_id) == str(id_spisok[0]):
				print('Новых обьявлений нет')
				return True

# Берет все значения из jsona Этаж кв.м и тд. и записываем в файл
def get_offers(data):
	all_ogjekt = data['data']['listings']
	for i in all_ogjekt:
		get_uId = i['uId']
		if type(get_uId) == int: # Проверяет Вип это обьявление или нет так как вип str а простые int
			get_id = i['uId'] # Айди объявления
			if proverka(get_id) == True:
				break
			# Добавляет айди в базу данных
			with open('ID_ojekt.csv', 'a', newline='', encoding='UTF-8') as file:
				id_x = csv.writer(file, delimiter=',')
				id_x.writerow((str(get_id),))
			get_data = datetime.date.today().strftime('%d.%m.%Y') # Дата записи обьявления в список
			get_data_all = i['upAt'][:-7]  #Дата подачи обьявления
			get_adresfull = i['fullAddress'].split(',') # Адрес полностью 
			get_adres = get_adresfull[1] # Адрес
			get_orentir = get_adresfull[2] # Ориентир 
			get_room = i['roomValue'] # Комнат
			get_flooar = i['floorValue'][:1] # Этаж
			get_flooar_hom = i['floorValue'][2:] # Этажность дома
			get_kv_m = i['squareValue'] # Кв.м
			get_material = '*' # Материал
			get_remont = '*' # Ремонт

			get_description = i['description'].replace('\r\n','') # Описание
			if get_description == '':
				get_description = '*'
			
			get_price = i['price'][:-11] # Цена
			get_tel = f'{telefon(get_id)}' # Телефон ( Принамает айди) работает из функции
			get_url = i['url'] # Сылка
			data_dey = datetime.date.today().strftime('%d.%m.%Y') # Дата сегодня
			print('Все данные получил')
			# Условие если файла с таким названием нет, то создай его и потом запиши значения
			# А если такой файл есть просто добавь в него значения
			try:
				# Создаем файл со значениями
				with open(f'Аренда_{data_dey}.csv', 'x', newline='', encoding='UTF-8') as file:
					writer = csv.writer(file, delimiter=',')
					writer.writerow(
						(
							'Id', 
							'Дата записи', 
							'Дата подачи', 
							'Адрес', 
							'Ориентир', 
							'Комнат', 
							'Этаж',
							'Этажность', 
							'Кв.м',
							'Материал', 
							'Ремонт',
							'Описание',
							'Цена',
							'Телефон',
							'Сылка',
						)
					)
					print('Создал файл')
				# Записываем в файл
				with open(f'Аренда_{data_dey}.csv', 'a', newline='', encoding='UTF-8') as file_1:
					writer = csv.writer(file_1, delimiter=',')
					writer.writerow(
						(
							get_id, 
							get_data, 
							get_data_all, 
							get_adres, 
							get_orentir, 
							get_room, 
							get_flooar,
							get_flooar_hom, 
							get_kv_m,
							get_material, 
							get_remont,
							get_description,
							get_price,
							str(get_tel),
							get_url,
						)
					)
				print('Записал все в файл')
			
			except:
				# Записываем в файл
				with open(f'Аренда_{data_dey}.csv', 'a', newline='', encoding='UTF-8' ) as file_2:
					writer = csv.writer(file_2, delimiter=',')
					writer.writerow(
						(
							get_id, 
							get_data, 
							get_data_all, 
							get_adres, 
							get_orentir, 
							get_room, 
							get_flooar,
							get_flooar_hom, 
							get_kv_m,
							get_material, 
							get_remont,
							get_description,
							get_price,
							get_tel,
							get_url,
						)
					)
				print('Записал все в файл')



# Берет json сайта
def get_json():
	cookies = {
	    '_ym_uid': '1646746645670304867',
	    '_ym_d': '1646746645',
	    '_gid': 'GA1.2.460190280.1652266732',
	    '_ym_visorc': 'w',
	    '_ym_isad': '2',
	    'XSRF-TOKEN': 'eyJpdiI6IllQOXFha0pKbEo2b3dkQjF0eDh6VlE9PSIsInZhbHVlIjoicVZtWlhXdjBQakdNT1lSdDhNUVliQUdja0hUTDI1NUFxQndOQnZCUXpcLzl2cnp0SEVXT3hOZlhPSE9ORnBFWWtTT0J3S1ZBdURia0FZbjRJY0N5WnNRPT0iLCJtYWMiOiJiOGY2ZWFkY2NhMTg1MWRmODA3ZWJhN2IyZDRiMzkyYTkzMTgyZGQ0NTYyNGQ1YWE2N2UxODFmMjc0NThiZDA0In0%3D',
	    'laravel_session': 'eyJpdiI6IkFnS3Z3bklzektqUFJaVFFhVE4zWEE9PSIsInZhbHVlIjoiZ2hZbWNSN0ZYTkRxWFBZdEt0eWpvSzF6NEdXRSszWmNDdjlBdE1QNVk4WUFGblpiMU1cL01US01lb0R3RWJObG8zMU55RDRVT3k2d1ZxQjhGdjNyT1VnPT0iLCJtYWMiOiJkN2FlNmI0NzI1ODZkMTk1ZjA2ZWM5NGU4MjY5OTJmYTc3YjlmN2ZiNDlmOTBkYmU2YWZhNmRiNDAzMDAzODQwIn0%3D',
	    '_gat_gtag_UA_54967882_1': '1',
	    '_ga_B3EV6Z01Q8': 'GS1.1.1652266734.40.1.1652266852.0',
	    '_ga': 'GA1.1.1366460426.1646746648',
	}

	headers = {
	    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="96", "Opera";v="82", ";Not A Brand";v="99"',
    'Content-Encoding': 'gzip',
    'X-CSRF-TOKEN': 'tON1IRYvs0ZXHP7YyANYjF1WXgZxlX12GUeofWnE',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'language-code': 'ru',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://uybor.uz',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://uybor.uz/ru/arenda-kvartir/kvartiry-v-tashkente?user_type=ub_private__ub_dealer&order=created_at-DESC',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ym_uid=1646746645670304867; _ym_d=1646746645; _gid=GA1.2.460190280.1652266732; _ym_visorc=w; _ym_isad=2; XSRF-TOKEN=eyJpdiI6IllQOXFha0pKbEo2b3dkQjF0eDh6VlE9PSIsInZhbHVlIjoicVZtWlhXdjBQakdNT1lSdDhNUVliQUdja0hUTDI1NUFxQndOQnZCUXpcLzl2cnp0SEVXT3hOZlhPSE9ORnBFWWtTT0J3S1ZBdURia0FZbjRJY0N5WnNRPT0iLCJtYWMiOiJiOGY2ZWFkY2NhMTg1MWRmODA3ZWJhN2IyZDRiMzkyYTkzMTgyZGQ0NTYyNGQ1YWE2N2UxODFmMjc0NThiZDA0In0%3D; laravel_session=eyJpdiI6IkFnS3Z3bklzektqUFJaVFFhVE4zWEE9PSIsInZhbHVlIjoiZ2hZbWNSN0ZYTkRxWFBZdEt0eWpvSzF6NEdXRSszWmNDdjlBdE1QNVk4WUFGblpiMU1cL01US01lb0R3RWJObG8zMU55RDRVT3k2d1ZxQjhGdjNyT1VnPT0iLCJtYWMiOiJkN2FlNmI0NzI1ODZkMTk1ZjA2ZWM5NGU4MjY5OTJmYTc3YjlmN2ZiNDlmOTBkYmU2YWZhNmRiNDAzMDAzODQwIn0%3D; _gat_gtag_UA_54967882_1=1; _ga_B3EV6Z01Q8=GS1.1.1652266734.40.1.1652266852.0; _ga=GA1.1.1366460426.1646746648',}
    }

	json_data = {
	    'page': 1,
	    'operation_type_code': 'rent',
	    'category_id': 23,
	    'subcategory_id': [],
	    'region_id': 13,
	    'locality': [],
	    'city_id': '',
	    'md': [],
	    'qt': [],
	    'st': [],
	    'ar': [],
	    'mh': [],
	    'hw': [],
	    'vg': [],
	    'ts': [],
	    'lct': [],
	    'oth': [],
	    'address': '',
	    'lat': '',
	    'lng': '',
	    'quarter_and_area': [],
	    'metro_id': '',
	    'coordinates': '',
	    'verified': '',
	    'owner': '',
	    'price_from': '',
	    'price_to': '',
	    'price_from_rent': '',
	    'price_to_rent': '',
	    'user_type': 'ub_private__ub_dealer',
	    'keyword': '',
	    'with_photo': '',
	    'id': '',
	    'order': 'created_at-DESC',
	    'price_period_unit': '',
	    'square_from': '',
	    'square_to': '',
	    'square_ground_from': '',
	    'square_ground_to': '',
	    'square_ground_unit': 'sot',
	    'room': [],
	    'room_from': '',
	    'room_to': '',
	    'floor_from': '',
	    'floor_to': '',
	    'floor_total_from': '',
	    'floor_total_to': '',
	    'floor_total': '',
	    'residential_complex_id': '',
	    'repair': '',
	    'foundation': [],
	    'unl': '',
	}

	url = 'https://uybor.uz/api/listing/search'
	response = requests.post(url=url, headers=headers, cookies=cookies, json=json_data)
	data = response.json()
	print('Получил json первой страницы')
	return data


def main():
	data = get_json()
	get_offers(data)



if __name__ == '__main__':
	main()
	print('Все')
