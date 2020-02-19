import os
import tkinter
import tkinter.filedialog
import random
import time
import threading
import pygame

folder = ''

def play():
    #預設播放D:\music資料夾的所有mp3檔
    global folder
    musics = [folder+'\\'+music for music in os.listdir(folder) \
            if music.endswith(('.mp3', '.wav', '.ogg'))]
    total = len(musics)
    #初始化混音器設備
    pygame.mixer.init()
    while playing:
        if not pygame.mixer.music.get_busy():
            #隨機播放一首歌曲
            nextMusic = random.choice(musics)
            pygame.mixer.music.load(nextMusic.encode())
            #播放一次
            pygame.mixer.music.play(1)
            musicName.set('playing....'+nextMusic)
        else:
            time.sleep(0.3)
                
root = tkinter.Tk()
root.title('音樂播放機v1.0---董付國')
root.geometry('280x70+400+300')
root.resizable(False, False)

#關閉程式時執行的函數
def closeWindow():
    global playing
    playing = False
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)

pause_resume = tkinter.StringVar(root, value='NotSet')
playing = False

#播放按鈕
def buttonPlayClick():
    global folder
    if not folder:
        folder = tkinter.filedialog.askdirectory()
    if not folder:
        return
    global playing
    playing = True
    #建立一個執行緒，以便播放音樂
    t = threading.Thread(target=play)
    t.start()
    #根據情況禁用和啟用對應的按鈕
    buttonPlay['state'] = 'disabled'
    buttonStop['state'] = 'normal'
    buttonPause['state'] = 'normal'
    buttonNext['state'] = 'normal'
    pause_resume.set('Pause')
buttonPlay = tkinter.Button(root, text='Play', command=buttonPlayClick)
buttonPlay.place(x=20, y=10, width=50, height=20)

#停止按鈕
def buttonStopClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    musicName.set('暫時沒有播放音樂')
    buttonPlay['state'] = 'normal'
    buttonStop['state'] = 'disabled'
    buttonPause['state'] = 'disabled'    
buttonStop = tkinter.Button(root, text='Stop', command=buttonStopClick)
buttonStop.place(x=80, y=10, width=50, height=20)
buttonStop['state'] = 'disabled'

#暫停與恢復，兩個功能共用一個按鈕
def buttonPauseClick():
    global playing
    if pause_resume.get() == 'Pause':
        #playing = False
        pygame.mixer.music.pause()
        pause_resume.set('Resume')
    elif pause_resume.get() == 'Resume':
        #playing = True
        pygame.mixer.music.unpause()
        pause_resume.set('Pause')
buttonPause = tkinter.Button(root, textvariable=pause_resume, \
                 command=buttonPauseClick)
buttonPause.place(x=140, y=10, width=50, height=20)
buttonPause['state'] = 'disabled'

#下一首音樂
def buttonNextClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    buttonPlayClick()
buttonNext = tkinter.Button(root, text='Next', command=buttonNextClick)
buttonNext.place(x=200, y=10, width=50, height=20)
buttonNext['state'] = 'disabled'

musicName = tkinter.StringVar(root, value='暫時沒有播放音樂...')
labelName = tkinter.Label(root, textvariable=musicName)
labelName.place(x=0, y=40, width=270, height=20)

#啟動迴圈
root.mainloop()
