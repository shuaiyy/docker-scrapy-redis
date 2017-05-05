# docker-scrapy-redis
ubuntu14.04 with scrapy-redis

这是我测试在docker上部署scrapy-redis爬虫用的，docker小白，很多东西不知其所以然。

安装了Python2.7，scrapy，scrapy-redis， pymongo等库。

我在daocloud上同步了该repository，并build了一个镜像，
使用`docker run -it daocloud.io/blue_whale/scrapy` 进入容器后会自动执行`scrapy crawl moko_spider`

moko_spider是我写的一个基于scrapy-redis的测试小爬虫，redis数据库在腾讯云上，爬到的items也提交到redis上，没有将redis也放到容器中。
爬虫起来后，123.207.253.201:6379(password:mima) `lpush moko_spider:start_urls http://www.moko.cc/moko/post/1.html',喂食爬虫
