import html2text as ht
import os
import re


def changeHtmlToMd(filePath, rootPath):
	text_maker = ht.HTML2Text()

	with open(filePath, 'r', encoding='UTF-8') as f:
		htmlpage = f.read()

	text = text_maker.handle(htmlpage)

	# outPath = '临时MD路径' + filePath[len(rootPath):-11] + '.md'

	# 图片替换成本地图片地址
	with open(outPath, 'w') as f:
		# subtext = re.sub(r'github图片目录', 'file://本地图片目录', text)
		f.write(subtext)


def readTitle(path):
	with open(path, 'r', encoding='UTF-8') as f:
		out = f.readlines()
		titleString = out[20].split("\n")[0].split("## ")[1]
		dateString = out[22].split("\n")[0]
		tagsDict = {'computertheory001':'计算机原理','数据加密':'计算机原理',
					'DesignPatterns_':'设计模式',
					'internet':'网络',
					'ios13Fit':'iOS','Xcode-libstdc++Error':'iOS',
					'javascript':'javascript',
					'MacDeleteLaunchPadIcon':'MacOS',
					'MakeMoneyGame_':'理财','Primary_':'理财',
					'python-':'Python',
					'spirit':'心情'}
		tag = ''
		for k in tagsDict.keys():
			if k in path:
				tag = tagsDict[k]
		mdTitle = "---\ntitle: '"+titleString+"'\ndate: " + dateString + " 12:00:00\ntags: [" + tag + "]\npublished: true\nhideInList: true\nfeature: \nisTop: false\n---\n"
		deadLine = 0
		index = 0
		for lineContent in out:
			if "下一篇" in lineContent:
				deadLine = index
			index=index+1
		resultContent = ''.join(out[24:deadLine if deadLine != 0 else (len(out)-1)])
		resultContent = mdTitle + resultContent
		fout=open(path+'.bak','w')
		fout.write(resultContent)
		f.close()
		fout.close()
		os.rename(path,path+'.temp')
		os.rename(path+'.bak',path)
		os.rename(path+'.temp',path+'.bak')


def changeContent():
	# defaultPath = 'MD地址 + /MD/'
	for root, dirs, files in os.walk(defaultPath):
		for name in files:
			if  'md' in name:
				filePath = os.path.join(root + name)
				print(filePath)
				readTitle(filePath)

if __name__ == "__main__":
	# defaultPath = 'github地址 + /post/'
	for root,dirs,files in os.walk(defaultPath):
		for name in files:
			if  'html' in name:
				print(os.path.join(root+name))
				changeHtmlToMd(os.path.join(root + '/' + name), defaultPath)

	changeContent()



