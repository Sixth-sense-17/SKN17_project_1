# pip install pandas openpyxl 해줘야됨
import pandas as pd

def kia_recent():
    excel_path = 'kia2024.xlsx'
    excel2 = 'kia2025.xlsx'
    df = pd.read_excel(excel_path, engine='openpyxl', header=None)
    df2 = pd.read_excel(excel2, engine='openpyxl', header=None)

    car_names = df.loc[4:20, 2].tolist()
    sales = df.loc[4:20, 5].tolist()
    car_names2 = df2.loc[4:20, 2].tolist()
    sales2 = df2.loc[4:20, 5].tolist()

    sale_dict = dict(zip(car_names, sales))
    sale_dict2 = dict(zip(car_names2, sales2))

    for car, sale in sale_dict2.items():
        # print(car, sale)
        if car in sale_dict:
            # print('in')
            # print(sale_dict[car])
            sale_dict[car] += sale
        else:
            # print('out')
            sale_dict[car] = sale
    
    merge_list = list((car, sale) for car, sale in sale_dict.items())

    merge_list.sort(key=lambda x:x[1], reverse=True)
    for i in merge_list:
        print(i)

    return merge_list

def hyundai_recent():
    excel_path = 'hyundai2024.xlsx'
    excel2 = 'hyundai2025.xlsx'
    df = pd.read_excel(excel_path, engine='openpyxl', header=None)
    df2 = pd.read_excel(excel2, engine='openpyxl', header=None)

    car_names = df.loc[7:24, 2].tolist()
    sales = df.loc[7:24, 4].tolist()
    car_names2 = df2.loc[6:24, 2].tolist()
    sales2 = df2.loc[6:24, 4].tolist()

    sale_dict = dict(zip(car_names, sales))
    sale_dict2 = dict(zip(car_names2, sales2))

    for car, sale in sale_dict2.items():
        # print(car, sale)
        if car in sale_dict:
            # print('in')
            # print(sale_dict[car])
            sale_dict[car] += sale
        else:
            # print('out')
            sale_dict[car] = sale
    
    merge_list = list((car, sale) for car, sale in sale_dict.items())

    merge_list.sort(key=lambda x:x[1], reverse=True)
    for i in merge_list:
        print(i)

    return merge_list


if __name__ == "__main__":
    print('kia:')
    kia_recent()
    print('hyundai:')
    hyundai_recent()
