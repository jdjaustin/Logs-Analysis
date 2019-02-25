import psycopg2
conn=psycopg2.connect(dbname="news")
cursor=conn.cursor()
cursor.execute("select title, count(*) as num from articles,log where log.path like concat('/article/',articles.slug) group by articles.title order by num desc limit 3")
results=cursor.fetchall()
print results
conn.close()