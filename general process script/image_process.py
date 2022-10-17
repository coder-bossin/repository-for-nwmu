import os
import operator
import cv2


# 图像处理常用程序

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


# 在图像操作脚本中实现cal_mean_std(images_dir:str)函数
# 该函数返回指定文件夹下（含子目录）返回所有图片整体的均值与标准差字典。即{'mean':mean,'std':std}
# 可对dataset/train/image文件夹进行测试。
# 图像的均值反应了图像的整体亮度
# 标准差反映了图像像素值与均值的离散程度，标准差越大说明图像的质量越好（说明图像边缘清晰）
def cal_mean_std(images_dir: str):
	'''

	:param images_dir: 需要计算的图片所在路径
	:return: 包含均值和标准差的字典{'mean':mean,'std':std}
	'''

	paths_list=get_all_files_pth(images_dir,[],'.jpg')
	mean_total=0
	std_total=0
	for path in paths_list:
		temp=cv2.imread(path,0)
		(mean, std) = cv2.meanStdDev(temp)
		print(mean)
		print(std)
		mean_total=mean_total+mean
		std_total=std_total+std

	mean_total=mean_total/len(paths_list)
	std_total=std_total/len(paths_list)

	mean_std_dict = {'mean': mean_total[0][0], 'std': std_total[0][0]}
	return mean_std_dict


# 实现get_file_name_from_pth(fpth: str)函数，该函数返回其不带后缀的文件名
def get_file_name_from_pth(fpth: str):
	'''

	:param fpth: 指定的文件路径
	:return: 指定路径下的文件名称（不包含后缀）
	'''
	file_Names = []
	# 注意：listdir()方法返回的并不是按照图片文件编号顺序来的，导致后续操作很不方便
	filelist = os.listdir(fpth)
	#print(filelist)
	for file in filelist:
		filename = file.split(".")[0]
		file_Names.append(filename)

	return file_Names

# 测试方法get_file_name_from_pth
print(get_file_name_from_pth(r'F:\TASK\task3-find text area\B3\1'))