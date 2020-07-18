# TohoMusicPy
# 成果展示：https://www.bilibili.com/video/BV1Cp4y1S7U4/

该项目为数据后端（爬虫端），数据前端我使用的是Jannchie的开源可视化项目，在github上也能找到

拉到Pycharm下即可，需要把pyvenv.cfg中的home改为你自己本机的python目录

由于搜索结果是嵌套在iframe中，所以用到了selenium，项目使用的浏览器为Chrome，如果需要Firefox请自行更改配置并使用相关驱动

运行结果最终会生成result.xls文件，里面的排布是专门针对Jannchie的前端项目，导入时需要用Excel软件将date转换为日期类型
