"""Class for Murideo 8K Seven Generator"""


class Murideo:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.Video = self._Video(self)
        self.Audio = self._Audio(self)
        self.Commands = self._Commands(self)

    class _Video:
        def __init__(self, parent):
            self.parent = parent

        def Timing(self, value):
            print(f"Setting Video Timing to {value} on IP: {self.parent.ip_address}")

        # ... more methods

    class _Audio:
        def __init__(self, parent):
            self.parent = parent
            self.PCM = self._PCM(self)

        class _PCM:
            def __init__(self, parent):
                self.parent = parent

            def sample(self, value):
                print(
                    f"Setting Audio PCM Sample to {value} on IP: {self.parent.parent.ip_address}"
                )

        # ... more methods

    class _Commands:
        def __init__(self, parent):
            self.parent = parent

        def get_EDID(self):
            print(f"Getting EDID on IP: {self.parent.ip_address}")

        # ... more methods


# Usage
m1 = Murideo("192.168.4.100")
m1.Video.Timing(38)
m1.Audio.PCM.sample(3)
m1.Commands.get_EDID()

# Structure I want to use

# Murideo.Video.Timing(38)
# Murideo.Video.Pattern(74)
# Murideo.Video.ColorSpace(0)
# Murideo.Video.BT("Enable")
# Murideo.Video.ColorDepth(1)
# Murideo.Video.HDCP(2)
# Murideo.Video.Output("HDMI")
# Murideo.Video.HDR(4)
# Murideo.Video.VideoTest(18)
# Murideo.Audio.PCM.sample(3)
# Murideo.Audio.PCM.bit(0)
# Murideo.Audio.PCM.SineWave(3)
# Murideo.Audio.PCM.Volume(4)
# Murideo.Audio.PCM.Channels(13)
# Murideo.Audio.Dolby(18)
# Murideo.Audio.DTS(27)
# Murideo.Commands.get_EDID()
# Murideo.Commands.send_CEC("05.0E.3A.63")
# Murideo.Commands.hdmi_5v("on")
# Murideo.Commands.fan_control("low")
# Murideo.Commands.reset_default()
# Murideo.Commands.reboot()
# Murideo.Commands.get_vitals()
