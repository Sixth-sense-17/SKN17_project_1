import mysql.connector

# DB 연결
def insert_to_db(sedan_dict):
    connection = mysql.connector.connect(
        host='localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )
    cursor = connection.cursor()

    sql = """
    INSERT INTO car_info (MANUFACTURE, CAR_NAME, REGISTED_COUNT)
    VALUES (%s, %s, %s)
    """

    car_list = [(car.manufacture, car.car_name, car.purchase)
                for car in sedan_dict.value()]

# INSERT
    cursor.executemany(sql, car_list)

# 커밋 및 종료
    connection.commit()

    cursor.close()
    connection.close()
    print('저장완료')
