#convert pdf to txt using xpdf
import subprocess
import  os
	
def formart_converter(path=path, pdf_dir=in_dir, txt_dir=out_dir):
	path = path #xpdf所在路径
	in_dir = in_dir  #初始pdf文件夹
	out_dir = out_dir     #存放txt的文件夹
	files = os.listdir(in_dir)
	exit_files = os.listdir(out_dir)

	for j  in files:
	    if j.replace('pdf', 'txt') not in exit_files: #检查文件是否已被转换过
			in_file = os.path.join(in_dir,j)
			out_file = os.path.join(out_dir,j).replace('.pdf', '.txt')
			cmd = ["pdftotext","-layout","-enc", "UTF-8",in_file, out_file]  #命令行终端命令
			sub = subprocess.Popen(args=cmd,cwd=path,shell=True)  #不要忘记cwd
			sub.wait()   #最好加上，否则可能由于多个进程同时执行带来机器瘫痪

	pass