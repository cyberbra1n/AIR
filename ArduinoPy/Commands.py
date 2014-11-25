import os
import subprocess
import socket

class LinuxShellCmd(object):
    def __init__(self):
        self.PIPE = subprocess.PIPE

    def volume_up_alsa(self):
        print subprocess.Popen(["amixer set 'Master' 3+"], stdout = self.PIPE, shell=True).communicate()[0]

    def volume_down_alsa(self):
        print subprocess.Popen(["amixer set 'Master' 3-"], stdout = self.PIPE, shell=True).communicate()[0]

    def mute_alsa(self):
        print subprocess.Popen(["amixer -D pulse set 'Master' toggle"], stdout = self.PIPE, shell=True).communicate()[0]

class VLCCmd(object):
    def __init__(self):
        self.SOCK = "/home/cyberbrain/.vlcsocket"

    def check_for_socket(self):
        if os.path.exists(self.SOCK) == True:
            return True

    def pause(self):
        if self.check_for_socket() == True:
            command = "pause"
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def next_in_playlist(self):
        if self.check_for_socket() == True:
            command = 'next'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def prev_in_playlist(self):
        if self.check_for_socket() == True:
            command = 'prev'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def show_playlist(self):
        if self.check_for_socket() == True:
            command = 'playlist'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def full_screen(self):
        if self.check_for_socket() == True:
            command = 'key key-toggle-fullscreen'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def forward_medium(self):
        if self.check_for_socket() == True:
            command = 'key key-jump+medium'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def rewind_medium(self):
        if self.check_for_socket() == True:
            command = 'key key-jump-medium'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

    def quit(self):
        if self.check_for_socket() == True:
            command = 'quit'
            self.socket = socket.socket(socket.AF_UNIX)
            self.socket.settimeout(0.01)
            self.socket.connect((self.SOCK))
            self.socket.send("%s\r" % command)
            self.socket.close()

class AudaciousCmd(object):
    def __init__(self):
        self.PIPE = subprocess.PIPE

    def volume_up(self, increment):
        auda_new_vol = 0
        auda_cur_vol = subprocess.Popen(['audtool --get-volume'], stdout = self.PIPE, shell = True).communicate()[0] 
        if int(auda_cur_vol) + increment  > 100:
            auda_new_vol = 100
        else:
            auda_new_vol = int(auda_cur_vol) + increment
        subprocess.Popen(['audtool --set-volume ' + str(auda_new_vol)], stdout = self.PIPE, shell = True).communicate()[0]
        #print auda_new_vol
   
    def volume_down(self, increment):
        auda_new_vol = 0
        auda_cur_vol = subprocess.Popen(['audtool --get-volume'], stdout = self.PIPE, shell = True).communicate()[0] 
        if int(auda_cur_vol) < increment:
            auda_cur_vol = 0
        else:
            auda_new_vol = int(auda_cur_vol) - increment
        subprocess.Popen(['audtool --set-volume ' + str(auda_new_vol)], stdout = self.PIPE, shell = True).communicate()[0]
        #print auda_new_vol

    def next_song(self):
        subprocess.Popen(['audacious -f'], stdout = self.PIPE, shell = True).communicate()[0]

    def prev_song(self):
        subprocess.Popen(['audacious -r'], stdout = self.PIPE, shell = True).communicate()[0]

    def play_pause(self):
        subprocess.Popen(['audacious -t'], stdout = self.PIPE, shell = True).communicate()[0]

    def enqueue(self):
        subprocess.Popen(['audacious -E'], stdout = self.PIPE, shell = True).communicate()[0]


