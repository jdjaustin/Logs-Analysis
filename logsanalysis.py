#!/usr/bin/env python2

import psycopg2

#define question titles and SQL queries

articleQueryTitle=("What are the most popular three articles of all time?")
articleQuery=("select title, count(*) as num from articles,log where log.path like concat('/article/',articles.slug) group by articles.title order by num desc limit 3")

authorQueryTitle=("Who are the most popular article authors of all time?")
authorQuery=("select authors.name, count(*) as num from articles join authors on articles.author=authors.id join log on log.path=concat('/article/',articles.slug) group by authors.name order by num desc limit 3")

errorQueryTitle=("On which days did more than 1% of requests lead to errors?")
errorQuery=("select * from (select hittable.day, round(cast((100*errortable.errors) as numeric)/cast(hittable.hits as numeric),2) as percentage from (select date(time) as day, count(*) as hits from log group by day) as hittable join (select date(time) as day, count(*) as errors from log where status like '%404%' group by day) as errortable on hittable.day=errortable.day) as y where percentage>=1")

#define functions to fetch data and print results

def queryLogs(query):
	conn=psycopg2.connect(dbname="news")
	cursor=conn.cursor()
	cursor.execute(query)
	results=cursor.fetchall()
	conn.close()
	return results

def printQueries(title,logResults):
	print title
	for i in range(len(logResults)):
		print '\t',i + 1,'.',logResults[i][0],'-',logResults[i][1]," views"
	print ""

def printErrors(title,logResults):
	print title
	for i in range(len(logResults)):
		print '\t',i + 1,'.',logResults[i][0],'-',logResults[i][1],"%"

#get data

articlesResults=queryLogs(articleQuery)
authorsResults=queryLogs(authorQuery)
errorsResults=queryLogs(errorQuery)

#print results

printQueries(articleQueryTitle,articlesResults)
printQueries(authorQueryTitle,authorsResults)
printErrors(errorQueryTitle,errorsResults)
