patient_name = input('nhập tên bệnh nhân: ')
birth_year = int(input('nhập năm sinh: '))
sick_days = int(input("nhập số ngày bị bệnh: "))
temperature = float(input("nhập nhiệt độ cơ thể: "))
medical_fee = float(input("nhập chi phí khám bệnh: "))

if patient_name == "" or (birth_year < 1900 or birth_year > 2026) or (temperature < 30 or temperature > 45) or medical_fee <= 0 or sick_days < 0:
    print('nhập sai dữ liệu')
else:
    age = 2026 - birth_year
    print('tuổi bệnh nhân là: ', age)
    print('phụ phí: ', medical_fee * 0.1)
    print('tổng chi phí: ', medical_fee + medical_fee * 0.1)
    
    if temperature > 38 and sick_days > 3 :
        print('nguy hiểm')
        if age > 60 :
            print('cấp cứu')
        else :
            print('ưu tiên cao')
    elif temperature > 38 :
        print('sốt cao')
    elif temperature > 37.5 :
        print('sốt nhẹ')
    else :
        print('bình thường')

    rate_fee = 'cao' if (medical_fee + medical_fee * 0.1) > 500000 else 'thấp'