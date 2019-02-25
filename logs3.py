import psycopg2
conn=psycopg2.connect(dbname="news")
cursor=conn.cursor()
cursor.execute("select * from (select hittable.day, round(cast((100*errortable.errors) as numeric)/cast(hittable.hits as numeric),2) as percentage from (select date(time) as day, count(*) as hits from log group by day) as hittable join (select date(time) as day, count(*) as errors from log where status like '%404%' group by day) as errortable on hittable.day=errortable.day) as y where percentage>=1")
results=cursor.fetchall()
print results
conn.close()