import pymysql


###################### top5_girl_names ################################
def top5_girl_names(date_text):
    Connection = pymysql.connect(host='localhost', user='bot', password='telebot', db='bot',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor )
    cur = Connection.cursor()

    if '/' in date_text:
        date_text_separ = date_text.split('/')
    if '-' in date_text:
        date_text_separ = date_text.split('-')

    year = date_text_separ[0]
    month = date_text_separ[1]

    cur.execute("SELECT concat(name, '(', NumberOfPersons, ') ' ) as name_num FROM bot.girl_names where year={} and month={} order by NumberOfPersons desc limit 5".format(year, month))

    answer = ''
    for response in cur:
        print(response['name_num'])
        answer += response['name_num'] 
        cur.close()
    Connection.close()
    print (answer)
    return answer

###################### MAIN ################################

def main():
    top5_girl_names('2016-01')


if __name__ == '__main__':
    main()