import pymysql
import datetime
import math

fopen = open('/usr/share/nginx/html/sitemap.xml', 'w')
fopen.write('<?xml version="1.0" encoding="UTF-8"?>\n')
fopen.write('<urlset\n')
fopen.write('      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n')
fopen.write('      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
fopen.write('      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n')
fopen.write('http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n')
fopen.write('  <url>\n')
fopen.write('    <loc>http://www.bbgo.xyz/</loc>\n')
fopen.write('    <lastmod>%s</lastmod>\n' % datetime.date.today())
fopen.write('    <priority>1.00</priority>\n')
fopen.write('  </url>\n')

conn = pymysql.connect('localhost', 'root', 'MyNewPass4!', 'mysite', charset='utf8mb4', )
cur = conn.cursor()

sql_game = "select distinct game_name from polls_gameinfo"
game_num = cur.execute(sql_game)
game_res = cur.fetchall()
for re in game_res:
    fopen.write('  <url>\n')
    fopen.write('    <loc>http://www.bbgo.xyz/accounts/%s/</loc>\n' % re[0])
    fopen.write('    <lastmod>%s</lastmod>\n' % datetime.date.today())
    fopen.write('    <priority>0.80</priority>\n')
    fopen.write('  </url>\n')
fopen.write('</urlset>\n')
fopen.close()

# detail_sql="select id,game_name from polls_postdetail where length(post_detail) >5000 order by create_time desc "
detail_sql = "select id,game_name from polls_postdetail where  game_name not like '%&%' order by create_time desc "
num = cur.execute(detail_sql)
detail_res = cur.fetchall()

for i in range(1, math.ceil(num / 20000)):
    fopen = open('/usr/share/nginx/html/sitemap{index}.xml'.format(index=i), 'w')
    for re in detail_res[(i - 1) * 20000:i * 20000]:
        fopen.write('  <url>\n')
        fopen.write('    <loc>http://www.bbgo.xyz/accounts/%s/%s/site_index</loc>\n' % (re[1], re[0]))
        fopen.write('    <lastmod>%s</lastmod>\n' % datetime.date.today())
        fopen.write('    <priority>0.80</priority>\n')
        fopen.write('  </url>\n')
    fopen.write('</urlset>\n')
    fopen.close()
