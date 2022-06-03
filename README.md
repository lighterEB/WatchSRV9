# WatchSRV9 (问道端口扫描)
PortScanner for asktao

# Description
#						                                         
#		            Date ：2018-12-26		                 
#	             Author: Hu Shangpengcheng	            
#         Environment: Win7(10) + Python3.7 + PyQt5   
#      Brief description of how to package into exe   
#						                                          
#				      

# 1.安装 'pyinstaller' of version 3.4

## pip install pyinstaller

# 2.切换到含有主文件的文件夹下

# 3.按住shift右键打开命令窗口

# 4.对主文件PortScanner.py进行打包

## pyintaller -F -w -p (当前目录路径) PortScanner.py -i asktao.ico --version-file (资源文件，非必须)

# 注：-F（打包单文件） -w（去除命令提示窗口） -p（引入主文件相关的其他文件资源） -i（图标目录） -n （文件生成名称）
