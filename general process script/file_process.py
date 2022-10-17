import os
import operator



# 文件处理常用程序

# 创建文件夹方法，dir是文件夹或者文件的相对路径或者绝对路径
def makedir(dir):
	if(os.path.exists(dir)):
		print('文件夹已经存在！')
		return True
	else:
		# 创建文件夹(允许跨级创建)
		os.makedirs(dir)
		print('文件夹创建成功！')
		return False

# 获取指定目录文件夹下面的指定类型文件的绝对路径list对象
def get_fpths_from_dir(dir:str,sufffix:str):
	# 存放绝对路径的list对象
	absolutePaths=[]
	pointedPath=dir
	# 注意：listdir()方法返回的并不是按照图片文件编号顺序来的，导致后续操作很不方便
	fileList=os.listdir(pointedPath)
	# 使用lambda表达式和sort()方法排序（根据实际需要取舍）
	fileList.sort(key=lambda x: int(x[6:-4]))
	print(fileList)
	for file in fileList:
		if operator.contains(file,sufffix):
			# 若为指定类型的文件，就装入list
			# 注意，不能使用os.path.abspath(),假的绝对路径
			# 这里使用拼凑出绝对路径
			absolutePaths.append(dir+'\\'+file)

	return absolutePaths

# 在文件操作脚本中中实现get_all_files_pth(dir_pth: str, suffix: str = None)函数
# 该函数返回指定文件夹下（含子目录）以指定后缀结尾的文件路径列表。
# 由于此方法使用递归，所以增加了一个用于存放地址列表的参数
def get_all_files_pth(dir_path: str, paths_list, suffix: str):
	'''

	:param dir_path: 指定目录
	:param paths_list: 用于装地址的空列表
	:param suffix: 指定类型文件
	:return: 装上地址的paths_list
	'''
	# 如果是文件并且符合指定类型，就直接将它的路径加入列表
	if os.path.isfile(dir_path) and operator.contains(dir_path, suffix):

		paths_list.append(dir_path)

	# 如果是目录，就对目录中的文件或子目录递归调用此方法，直到获得所有文件的路径
	elif os.path.isdir(dir_path):

		for s in os.listdir(dir_path):

			newDir = os.path.join(dir_path, s)

			get_all_files_pth(newDir, paths_list, suffix)

	return paths_list

