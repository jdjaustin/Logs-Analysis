import psycopg2
conn=psycopg2.connect(dbname="news")
cursor=conn.cursor()
cursor.execute("select authors.name, count(*) as num from articles join authors on articles.author=authors.id join log on log.path=concat('/article/',articles.slug) group by authors.name order by num desc limit 3")
results=cursor.fetchall()
print results
conn.close()