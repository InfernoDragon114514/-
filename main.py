import requests
import os
import json
import wx
from pathlib import Path
class MyFrame(wx.Frame):
    def_init_(self,parent,id);
    wx.Frame._init_(self,parent,id,"下载网易云音乐",size=(500,300))
    #创建面板
    panel=wx.Panel(self)
    
    #创建按钮并绑定事件
    self.bt_confirm=wx.Button(panel,label="确定")
    self.bt_cancel=wx.Button(panel,label="取消")
    
    
    


get_headers = {
    "User-Agent": "Mozilla/5.0 (Windows  NT 10.0; Win64; x64)pyh AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36"}

return_limit = 40
file_path = 'D:/music_output/'

if not os.path.exists(file_path):
    os.makedirs(file_path)
    print(f'当前无匹配路径，已自动创建目录{file_path}')






def music_get(music_name):
    get_url = (f"http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={music_name}&type=1&offset=0&total=true&limit={return_limit}")
    get_return = requests.get(url=get_url, headers=get_headers).text
    json_dic = json.loads(get_return)
    return_lens = len(json_dic['result']['songs'])
    more_music_list(json_dic, return_lens)


def more_music_list(data, lens):
    json_type = 0
    while json_type != lens:
        songs_artist = data["result"]['songs'][json_type]['artists'][0]['name']
        songs_id = data['result']['songs'][json_type]['id']
        songs_name = data['result']['songs'][json_type]['name']
        print(f"序号：{json_type}\n曲名：{songs_name}\n歌曲id：{songs_id}\n曲师（歌手）：{songs_artist}")
        print("")
        json_type += 1
    type(data, input(
        "输入任意字符即可下载所有搜索结果的音乐，输入df即可下载搜索结果第一个，输入dt进入序号选择mode，当前仅为学习demo"),
         lens)


def type(data, type, lens):
    if type == "df":
        songs_artist = data["result"]['songs'][0]['artists'][0]['name']
        songs_id = data['result']['songs'][0]['id']
        songs_name = data['result']['songs'][0]['name']
        music_file_url = requests.get(url=(f"http://music.163.com/song/media/outer/url?id={songs_id}"),
                                      headers=get_headers).content
        with open(file_path + (f"{songs_name}-{songs_artist}") + '.mp3', mode='wb') as f:
            f.write(music_file_url)
            print(f"{songs_name}-{songs_artist}.mp3已经保存到{file_path}啦！！")
            os.startfile(file_path)
    elif type == "dt":
        dttype = int(input("请输入序号"))
        songs_artist = data["result"]['songs'][dttype]['artists'][0]['name']
        songs_id = data['result']['songs'][dttype]['id']
        songs_name = data['result']['songs'][dttype]['name']
        music_file_url = requests.get(url=(f"http://music.163.com/song/media/outer/url?id={songs_id}"),
                                      headers=get_headers).content
        with open(file_path + (f"{songs_name}-{songs_artist}") + '.mp3', mode='wb') as f:
            f.write(music_file_url)
            print(f"{songs_name}-{songs_artist}.mp3已经保存到{file_path}啦！！")
            os.startfile(file_path)
    else:
        jsons_type = 0
        while jsons_type != lens:
            songs_artist = data["result"]['songs'][jsons_type]['artists'][0]['name']
            songs_id = data['result']['songs'][jsons_type]['id']
            songs_name = data['result']['songs'][jsons_type]['name']
            music_file_url = requests.get(url=(f"http://music.163.com/song/media/outer/url?id={songs_id}"),
                                          headers=get_headers).content
            jsons_type += 1
            with open(file_path + (f"{songs_name}-{songs_artist}") + '.mp3', mode='wb') as f:
                f.write(music_file_url)
                print(f"{songs_name}-{songs_artist}.mp3已经保存到{file_path}啦！！")
                os.startfile(file_path)


music_get(input("请输入想要搜索的歌曲"))
