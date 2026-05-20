patient_name = input('nhập tên bệnh nhân: ').strip()
if patient_name == "" :
    print('Tên bệnh nhân không được để trống')
    exit()
    
birth_year = int(input('nhập năm sinh: '))
if birth_year < 1900 or birth_year > 2026:
    print('Năm sinh không hợp lệ')
    exit()

sick_days = int(input("nhập số ngày bị bệnh: "))
if sick_days < 0:
    print('Số ngày bị bệnh không hợp lệ')
    exit()
    
temperature = float(input("nhập nhiệt độ cơ thể: "))
if temperature < 30 or temperature > 45:
    print('Nhiệt độ không hợp lệ')
    exit()
    
medical_fee = float(input("nhập chi phí khám bệnh: "))
if medical_fee <= 0:
    print('Chi phí khám bệnh không hợp lệ')
    exit()
    

age = 2026 - birth_year

extra_fee = medical_fee * 0.1
total_fee = medical_fee + extra_fee

if temperature > 38 and sick_days > 3 :
    status = 'nguy hiểm'
elif temperature > 38 :
    status = 'sốt cao'
elif temperature > 37.5 :
    status = 'sốt nhẹ'
else :
    status = 'bình thường'

if status == 'nguy hiểm':
    if age > 60:
        priority = 'cấp cứu'
    else:
        priority = 'ưu tiên cao'
else :
    priority = 'bình thường'

level_fee = 'cao' if total_fee > 500000 else 'thấp'

print(f'Tên: {patient_name}')
print(f'Tuổi: {age}')
print(f'Nhiệt độ: {temperature} °C')
print(f'Số ngày bị bệnh: {sick_days}')
print(f'Tình trạng: {status}')
print(f'Mức độ ưu tiên: {priority}')
print(f'Tổng chi phí: {total_fee}')
print(f'Mức chi phí: {level_fee}')