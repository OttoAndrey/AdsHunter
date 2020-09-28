# wb = load_workbook('google_regions.xlsx')
# sheet = wb.active
#
# regions = sheet['A']
#
# for index, region in enumerate(regions, start=1):
#     result = 'w+CAIQICI'
#     length = len(region.value)
#     base64_part = base64.b64encode(bytes(region.value, 'utf-8'))
#     key_arr = ["", "", "", "", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "M", "T", "L"]
#     secret = key_arr[length]
#     result += secret
#     result += base64_part.decode('utf-8')
#     sheet['B'+str(index)].value = result
#
#     print(f'{region.value} : {result}')
#
# wb.save('google_regions.xlsx')
# wb.close()