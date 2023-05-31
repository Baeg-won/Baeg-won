import feedparser, time

URL = "https://daegwonkim.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
<div align="center"> 

![header](https://capsule-render.vercel.app/api?type=waving&color=000000&height=150&section=header&text=Baeg-won&fontColor=ffffff&fontSize=70&animation=fadeIn&fontAlignY=55&desc=%20&descAlignY=62&descAlign=62)
  
####  :wave: Welcome my github profile !
  
<br/>
<br/>
  
####  :clipboard: Once I've Used

<img src="https://img.shields.io/badge/JAVA-007396?style=for-the-badge&logo=Java&logoColor=white">
<img src="https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=Spring&logoColor=white">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
<img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=Oracle&logoColor=white"> 

<br/>
<br/>

#### :pencil2: Study log

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Baeg-won&layout=compact&theme=highcontrast)](https://github.com/anuraghazra/github-readme-stats)

</div>

## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
