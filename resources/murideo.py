"""Class for Murideo 8K Seven Generator"""

import asyncio
import websockets
from map_key import find_tag_by_id


class Murideo:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.uri = f"ws://{ip_address}/ws/uart"
        self.websocket = None
        self.Video = self._Video(self)
        self.Audio = self._Audio(self)
        self.Commands = self._Commands(self)
        # TODO init other sub-classes

    async def connect(self):
        self.websocket = await websockets.connect(self.uri)
        asyncio.create_task(self.handle_message())

    async def handle_message(self):
        async for message in self.websocket:
            print("Received:", message)

    async def send_single_command(self, category, *ids):
        id_str = ",".join(map(str, ids))
        command = f"\r\nSENDSINGLE||{category},{id_str}\r\n"
        # print(f"Sending command: {command.strip()}")
        await self.websocket.send(command)

    async def send_double_command(self, category, *ids):
        id_str = ",".join(map(str, ids))
        command = f"\r\nSENDDOUBLE||{category},{id_str}\r\n"
        # print(f"Sending command: {command.strip()}")
        await self.websocket.send(command)

    async def send_other_command(self, category, *ids):
        id_str = ",".join(map(str, ids))
        command = f"\r\nSENDOTHER||{category},{id_str}\r\n"
        # print(f"Sending command: {command.strip()}")
        await self.websocket.send(command)

    class _Video:
        def __init__(self, parent):
            self.parent = parent

        async def Timing(self, id):
            category = 97  # TODO Replace
            await self.parent.send_single_command(category, id)
            print(
                f"Setting Video Timing to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def Pattern(self, id):
            category = 98
            await self.parent.send_double_command(category, id)
            print(
                f"Setting Pattern to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def Color(self, id):
            category = 99
            await self.parent.send_single_command(category, id)
            print(
                f"Setting Color to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def BT_2020(self, id):
            category = 112
            await self.parent.send_single_command(category, id)
            print(
                f"Setting BT 2020 to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def Color_Depth(self, id):
            category = 100
            await self.parent.send_single_command(category, id)
            print(
                f"Setting Color Depth to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def HDCP(self, id):
            category = 101
            await self.parent.send_single_command(category, id)
            print(
                f"Setting HDCP to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def Output(self, id):
            """Sets Output to HDMI or DVI or Auto"""
            category = 102
            await self.parent.send_single_command(category, id)
            print(
                f"Setting Output to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def HDR(self, id):
            category = 111
            await self.parent.send_single_command(category, id)
            print(
                f"Setting HDR to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def Video_Selection(self, id):
            category = 98
            await self.parent.send_double_command(category, id)
            print(
                f"Setting Video to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

    class _Audio:
        def __init__(self, parent):
            self.parent = parent
            self.PCM = self._PCM(self.parent)

        async def Dolby(self, id):
            category = 105
            await self.parent.send_double_command(category, id)
            print(
                f"Setting Audio to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def DTS(self, id):
            category = 105
            await self.parent.send_double_command(category, id)
            print(
                f"Setting Audio to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        class _PCM:
            def __init__(self, parent):
                self.parent = parent

            async def Sample(self, id):
                category = 103
                await self.parent.send_single_command(category, id)
                print(
                    f"Setting Sample Rate to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
                )

            async def Bit(self, id):
                category = 104
                await self.parent.send_single_command(category, id)
                print(
                    f"Setting Bit Depth to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
                )

            async def Sinewave(self, id):
                category = 115
                await self.parent.send_single_command(category, id)
                print(
                    f"Setting Sinewave Tone to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
                )

            async def Volume(self, id):
                category = 109
                await self.parent.send_single_command(category, id)
                print(
                    f"Setting Volume to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
                )

            async def Channel(self, id):
                category = 107
                await self.parent.send_single_command(category, id)
                print(
                    f"Setting Channel to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
                )

    class _Commands:
        def __init__(self, parent):
            self.parent = parent

        async def send_CEC(self, cec_string):
            category = 122
            await self.parent.send_single_command(category, cec_string)
            print(f"Sending CEC {cec_string} on IP: {self.parent.ip_address}\n")

        async def get_EDID(self):
            pass

        async def hdmi_5v(self, id):
            category = 179
            await self.parent.send_single_command(category, id)
            print(f"{find_tag_by_id(id)} on IP: {self.parent.ip_address}\n")

        async def fan_control(self, id):
            category = 30723
            await self.parent.send_single_command(category, id)
            print(
                f"Setting Fan to {find_tag_by_id(id)} on IP: {self.parent.ip_address}\n"
            )

        async def factory_reset(self):
            category = 30722
            await self.parent.send_other_command(category)
            print(f"Resetting all settings on IP: {self.parent.ip_address}\n")

        async def get_vitals(self):
            pass

        async def arc_earc(self, id):
            category = 131
            await self.parent.send_single_command(category, id)
            print(f"{find_tag_by_id(id)} on IP: {self.parent.ip_address}\n")

        async def earc_rx_latency(self, id):
            """id=ms use to add delay to eArc Latency"""
            category = 122
            await self.parent.send_single_command(category, id)
            print(f"eArc RX delay set {id}ms on IP: {self.parent.ip_address}\n")

        async def earc_tx_latency(self, id):
            """id=ms use to add delay to eArc Latency"""
            category = 121
            await self.parent.send_single_command(category, id)
            print(f"eArc TX delay set {id}ms on IP: {self.parent.ip_address}\n")

        async def earc_hpd_bit(self, id):
            category = 178
            await self.parent.send_single_command(category, id)
            print(f"{find_tag_by_id(id)} on IP: {self.parent.ip_address}\n")

        async def arc_physical_hdp(self, id):
            category = 177
            await self.parent.send_single_command(category, id)
            print(f"{find_tag_by_id(id)} on IP: {self.parent.ip_address}\n")

        async def arc_hpd(self, id):
            pass  # Dictionary is incorrect matches physical_hpd

        async def arc_audio_info(self, id):
            pass


async def main():
    m1 = Murideo("10.0.50.18")
    await m1.connect()

    for x in range(5):
        await m1.Video.Timing(34)
        await asyncio.sleep(15)  # Use asyncio's sleep for non-blocking delay
        await m1.Video.Timing(28)
        await asyncio.sleep(15)  # Use asyncio's sleep for non-blocking delay


asyncio.get_event_loop().run_until_complete(main())

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
# Murideo.Commands.hdmi_5v(1)
# Murideo.Commands.fan_control("low")
# Murideo.Commands.reset_default()
# Murideo.Commands.reboot()
# Murideo.Commands.get_vitals()
