from ArduinoPy.Device import Device
from ArduinoPy.Commands import LinuxShellCmd, VLCCmd, AudaciousCmd

class Daemon(object): 
    def __init__(self):
        self.device_object = Device() 
        self.device_path = self.device_object.findDevice("linux")
        self.device = self.device_object.getDevice(self.device_path[0])

        self.linux_cmds = LinuxShellCmd()
        self.vlc_cmds = VLCCmd()
        self.auda_cmds = AudaciousCmd()

    def set_last_command(self, last_command):
        self.last_command = last_command

    def get_last_command(self):
        return self.last_command

    def indicator_led_on(self):
        pass

    def indicator_led_off(self):
        pass

    def indicator_led_blink(self):
        pass

    def relay_on(self):
        self.set_last_command(self.no_command)
        print "rely on"

    def relay_off(self):
        self.set_last_command(self.no_command)
        print "rely off"

    def volume_up(self):
        self.set_last_command(self.volume_up)
        self.linux_cmds.volume_up_alsa()
        print "volume up"

    def volume_down(self):
        self.linux_cmds.volume_down_alsa()
        self.set_last_command(self.volume_down)
        print "volume_down"

    def mute(self):
        self.linux_cmds.mute_alsa()
        self.set_last_command(self.no_command)
        print "mute"


    def vlc_pause(self):
        self.vlc_cmds.pause()
        self.set_last_command(self.no_command)
        print "vlc pause"

    def vlc_next(self):
        self.vlc_cmds.next_in_playlist()
        self.set_last_command(self.no_command)
        print "vlc next"

    def vlc_prev(self):
        self.vlc_cmds.prev_in_playlist()
        self.set_last_command(self.no_command)
        print "vlc previous"

    def vlc_full_screen(self): #bug!
        self.vlc_cmds.full_screen()
        self.set_last_command(self.no_command)
        print "vlc full screen"

    def vlc_forward_medium(self):
        self.vlc_cmds.forward_medium()
        self.set_last_command(self.vlc_forward_medium)
        print "vlc forward medium"

    def vlc_rewind_medium(self):
        self.vlc_cmds.rewind_medium()
        self.set_last_command(self.vlc_rewind_medium)
        print "vlc rewind medium"

    def vlc_quit(self):
        self.vlc_cmds.quit()
        self.set_last_command(self.no_command)
        print "vlc quit"


    def auda_play_pause(self):
        self.auda_cmds.play_pause()
        self.set_last_command(self.no_command)
        print "audacious play/pause"

    def auda_volume_up(self):
        self.auda_cmds.volume_up(4)
        self.set_last_command(self.auda_volume_up)
        print "audacious volume up"

    def auda_volume_down(self):
        self.auda_cmds.volume_down(4)
        self.set_last_command(self.auda_volume_down)
        print "audacious volume down"

    def auda_next_song(self):
        self.auda_cmds.next_song()
        self.set_last_command(self.no_command)
        print "audacious next song"

    def auda_prev_song(self):
        self.auda_cmds.prev_song()
        self.set_last_command(self.no_command)
        print "audacious previous song"

    def auda_play_pause(self):
        self.auda_cmds.play_pause()
        self.set_last_command(self.no_command)
        print "audacious play/pause"

    def no_command(self):
        pass

    def run(self):
        while True:
            try:
                serial_data = self.device_object.readSerialOnce(self.device)
                serial_data = serial_data.strip()

            except IOError as e:
                print "Serial data value error", e
                continue

            if serial_data == "4294967295":
                #break signal
                last_cmd = self.get_last_command()
                try:
                    last_cmd()
                except ValueError:
                    print "Function is required.\
                            Probably None received."
                    continue

            # codes check and connect to functions
            elif serial_data == "16210087":
                self.volume_up()
                continue
            elif serial_data == "16218247":
                self.volume_down()
                continue
            elif serial_data == "16216207":
                self.mute()
                continue
            elif serial_data == "16242727":
                self.relay_on()
                continue
            elif serial_data == "16250887":
                self.relay_off()
                continue


            elif serial_data=="16193767":
                self.vlc_pause()
                continue
            elif serial_data == "16189687":
                self.vlc_full_screen()
                continue
            elif serial_data == "16248847":
                self.vlc_next()
                continue
            elif serial_data == "16201927":
                self.vlc_prev()
                continue
            elif serial_data == "16199887":
                self.vlc_forward_medium()
                continue
            elif serial_data == "16230487":
                self.vlc_rewind_medium()
                continue
            elif serial_data == "16206007":
                self.vlc_quit()
                continue


            elif serial_data == "16203967":
                self.auda_volume_up()
                continue
            elif serial_data == "16191727":
                self.auda_volume_down()
                continue
            elif serial_data == "16212127":
                self.auda_next_song()
                continue
            elif serial_data == "16195807":
                self.auda_prev_song()
                continue
            elif serial_data == "16228447":
                self.auda_play_pause()
                continue


            else:
                self.set_last_command(self.no_command)
                #control print for new remote codes
                print serial_data
                continue


if __name__ == "__main__":
    daemon = Daemon()
    daemon.run()
