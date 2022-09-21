import os

# dir是文件夹或者文件的相对路径或者绝对路径
def makedir(dir):
	if(os.path.exists(dir)):
		print('文件夹已经存在！')
		return True
	else:
		#创建文件夹(允许跨级创建)
		os.makedirs(dir)
		print('文件夹创建成功！')
		return False

#python中\是转义字符，Windows 路径如果只有一个\，会被识别为转义字符
dir=r'F:\my local repository\repository-for-nwmu\general process script\hello\test'
makedir(dir)