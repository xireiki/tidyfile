#!/bin/python
import os
import argparse
import sys
import platform
import requests
import json

def main():
  parser = argparse.ArgumentParser(description="这是一个用于整理文件夹的python脚本")
  parser.add_argument('-i', '--input', help="需要整理的文件夹", default=None, dest="i")
  parser.add_argument('-o', '--output', help="整理后的文件保存位置", default=None, dest="o")
  parser.add_argument('-v', '--version', help="显示版本信息", action="store_true", dest="v")
  parser.add_argument('-u', '--update', help="更新脚本", action="store_true", dest="update")
  parser.add_argument('-c', '--compulsion', help="强制执行，仅对更新脚本有效", action="store_true", dest="compulsion")
  args = parser.parse_args();
  
  #版本信息
  name="tidyfile";
  author="哔哩哔哩@Gulanguage";
  blog="https://github.com/xireiki/";
  version_number=108;
  version="1.0.8";
  
  if args.i:
    if not args.i.endswith("/"):
      path = args.i + "/";
    else:
      path = args.i;
  elif args.v:
    print("脚本名称："+name);
    print("脚本作者："+author);
    print("我的主页："+blog);
    print("当前版本："+version);
    sys.exit(0);
  elif args.update:
    print("正在检查更新...",end="");
    update = requests.get("https://xireiki.github.io/tidyfile/update.json");
    ujtext = json.loads(update.text);
    def update():
      tidyfile = requests.get(ujtext["version_info"]["update_url"]);
      update_tidyfile = open(sys.argv[0], "w");
      update_tidyfile.write(tidyfile.text);
      update_tidyfile.close();
      print("更新完成！");
    if ujtext["version_info"]["version_number"] > version_number:
      print("发现新版本："+name+" v"+ujtext["version_info"]["version"]);
      print("更新内容：\n"+ujtext["version_info"]["version_text"]);
      tidyfile_update_confirm = input("是否安装 \""+name+" v"+ujtext["version_info"]["version"]+"\"? [Y/n] ");
      if tidyfile_update_confirm != "n" and tidyfile_update_confirm != "N" and tidyfile_update_confirm != "no" and tidyfile_update_confirm != "NO" and tidyfile_update_confirm != "No":
        update();
    elif args.compulsion:
      print("您选择了强制更新\n正在为您安装...",end="");
      update();
    else:
      print("当前已是最新版本！");
    sys.exit(0);
  else:
    if platform.system() == "Linux":
      print("请输入参数，使用 \"" + os.path.basename(__file__) + " --help\" 查看帮助");
      path = None;
      sys.exit(0);
    elif platform.system() == "Windows":
      path = "./";
  
  if args.o:
    if not args.o.endswith("/"):
      outpath = args.o + "/";
    else:
      outpath = args.o;
  else:
    outpath = path;
  
  folders = ["video","audio","document","backup","picture","program","others"];
  program_folder = ["c","cpp","python","java","lua","php","shell"];
  other_folder = ["zippack"];
  for folder in folders:
    if not os.path.exists(outpath + folder):
      os.mkdir(outpath + folder);
  for folder in program_folder:
    if not os.path.exists(outpath + "program/" + folder):
      os.mkdir(outpath + "program/" + folder);
  for folder in other_folder:
    if not os.path.exists(outpath + "others/" + folder):
      os.mkdir(outpath + "others/" + folder);
  
  file_img = ["bmp","png","jpg","jepg","ico","gif"];
  file_doc = ["doc","docx","xls","txt","ppt","pdf","epub"];
  file_audio = ["mp3","wav","flac","ogg","aac","aiff","wma","vqf","ape","amr"];
  file_video = ["mp4","flv","m4a","wmv","asf","asx","3gp","mov","m4v","avi","dat","mkv","vob","amv"];
  file_back = ["bak"];
  file_zip = ["zip","tar.gz","tar.bz2","tar.xz","tar.bz","7z","rar"];
  
  program_c = ["c"];
  program_cpp = ["cpp"];
  program_python = ["py"];
  program_java = ["java","class","jar"];
  program_lua = ["lua"];
  program_php = ["php"];
  program_shell = ["sh"];
  
  #遍历变量path目录下的所有文件并整理
  for file_name in os.listdir(path):
    for type in file_img:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "picture/" + file_name);
        os.rename(path + file_name,outpath + "picture/" + file_name);
    for type in file_doc:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "document/" + file_name);
        os.rename(path + file_name,outpath + "document/" + file_name);
    for type in file_audio:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "audio/" + file_name)
        os.rename(path + file_name,outpath + "audio/" + file_name)
    for type in file_video:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "video/" + file_name)
        os.rename(path + file_name,outpath + "video/" + file_name)
    for type in file_back:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "backup/" + file_name)
        os.rename(path + file_name,outpath + "backup/" + file_name)
  #特殊program目录
    for type in program_c:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/c/" + file_name)
        os.rename(path + file_name,outpath + "program/c/" + file_name)
    for type in program_cpp:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/cpp/" + file_name)
        os.rename(path + file_name,outpath + "program/cpp/" + file_name)
    for type in program_python:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/python/" + file_name)
        os.rename(path + file_name,outpath + "program/python/" + file_name)
    for type in program_java:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/java/" + file_name)
        os.rename(path + file_name,outpath + "program/java/" + file_name)
    for type in program_lua:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/lua/" + file_name)
        os.rename(path + file_name,outpath + "program/lua/" + file_name)
    for type in program_php:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/php/" + file_name)
        os.rename(path + file_name,outpath + "program/php/" + file_name)
    for type in program_shell:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "program/shell/" + file_name)
        os.rename(path + file_name,outpath + "program/shell/" + file_name)
    #特殊others目录
    for type in file_zip:
      if file_name.endswith("."+type):
        print(path + file_name + " >>> " + outpath + "others/zippack/" + file_name)
        os.rename(path + file_name,outpath + "others/zippack/" + file_name)
  #再次遍历目录
  for file_name in os.listdir(path):
    if file_name != "video" and file_name != "audio" and file_name != "document" and file_name != "backup" and file_name != "picture" and file_name != "program" and file_name != "others" :
      print(path + file_name + " >>> " + outpath + "others/" + file_name)
      os.rename(path + file_name,outpath + "others/" + file_name)

def cafmain(path, filename, name):
  main();

if __name__ == "__main__":
  main();
