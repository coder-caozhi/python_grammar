"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
  复制方式              	操作对象    	是否复制内容	是否复制权限	是否复制元数据 (时间)	大文件友好	自动处理文件 	推荐场景                
  read() + write()  	字符串 / 字节	✅     	❌     	❌           	❌ 爆内存	手动开 / 关	小文本文件               
  shutil.copyfileobj	文件对象    	✅     	❌     	❌           	✅ 流式 	手动开 / 关	大文件 / 网络流 / 自定义     
  shutil.copyfile   	路径      	✅     	❌     	❌           	✅    	✅ 自动   	只复制内容，最快            
  shutil.copy       	路径      	✅     	✅     	❌           	✅    	✅ 自动   	复制内容 + 权限           
  shutil.copy2      	路径      	✅     	✅     	✅           	✅    	✅ 自动   	复制内容+权限+元数据，最完整备份，推荐
"""
import shutil
# shutil.copy2("1.txt", "1_副本.txt")
shutil.copyfile("documents/1.txt", "documents/1_副本2.txt")
