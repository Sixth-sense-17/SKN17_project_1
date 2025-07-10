from crawling import crawl_car_sedan as c
import mysql.connector

# 브랜드코드 매핑 
def get_brand_code():
    connection = mysql.connector.connect(
        host = 'localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT BRAND_NAME, BRAND_CODE FROM BRAND_INFO")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return {brand_name:brand_code for brand_name,brand_code in rows}

# DB 연결
def insert_to_db(sedan_dict):
    brand_map = get_brand_code()

    connection = mysql.connector.connect(
        host='localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )
    cursor = connection.cursor()

    sql = """
    INSERT INTO REGISTED_info (YEAR, BRAND_CODE, CAR_NAME, REGISTED_COUNT)
    VALUES (%s, %s, %s, %s)
    """

    car_dict = c(sedan_dict)
    print(type(car_dict))
    print(len(car_dict))
    car_list = [("2020", brand_map.get(car_dict[car].manufacture), car_dict[car].car_name, car_dict[car].purchase)
                for car in car_dict
                if brand_map.get(car_dict[car].manufacture) is not None]

    print(len(car_list))

# INSERT
    cursor.executemany(sql, car_list)

# 커밋 및 종료
    connection.commit()

    cursor.close()
    connection.close()
    print('저장완료')


insert_to_db(1)

