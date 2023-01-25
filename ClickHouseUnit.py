import clickhouse_connect

client = clickhouse_connect.get_client(host='pxymfzzqvk.eu-central-1.aws.clickhouse.cloud', port=8443,
                                       username='default', password='oHfqUARUFZwf')


def insert():
    test_data1 = [1, 'Süleyman', 'Günel']
    test_data2 = [10, 'Hasan', 'Günel']
    test_data = [test_data1, test_data2]
    ic = client.create_insert_context(table='TableTest', data=test_data)
    client.insert(context=ic)


def delete(firstname, lastname):
    query = "SET allow_experimental_lightweight_delete = true;"
    client.query(query)
    query = "DELETE FROM TableTest WHERE FirstName='{}' AND LastName='{}'".format(firstname, lastname)
    result = client.query(query)
    return result


def search(firstname, lastname):
    query = "SELECT * FROM TableTest WHERE FirstName='{}' AND LastName='{}'".format(firstname, lastname)
    result = client.query(query)
    return result


def main():
    # insert()
    result = search('Süleyman', 'Günel')
    print(result.result_rows)
    print(result.result_rows[0][1])
    # result = delete("Hasan", "Günel")
    # print(result.result_rows)

