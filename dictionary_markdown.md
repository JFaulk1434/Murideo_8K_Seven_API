# Dictionary Markdown

- [Dictionary Markdown](#dictionary-markdown)
  - [Video Generator](#video-generator)
    - [TIMING](#timing)
      - [8K](#8k)
      - [UHD](#uhd)
      - [4K-DCI](#4k-dci)
      - [2K-DCI](#2k-dci)
      - [HD](#hd)
      - [SD](#sd)
      - [VESA](#vesa)
      - [3D](#3d)
      - [CUSTOM](#custom)
      - [AUTO](#auto)
    - [PATTERN](#pattern)
      - [FPGA](#fpga)
      - [ISF](#isf)
      - [DVS HDR](#dvs-hdr)
        - [CLIPPING \& COLOR](#clipping--color)
        - [EVALUATION](#evaluation)
        - [GEOMETRY \& CONVERGENCE](#geometry--convergence)
        - [RAMPS,GRADIENTS,ZONE PLATES](#rampsgradientszone-plates)
        - [RESOLUTION,ANSI,PLACEMENT](#resolutionansiplacement)
      - [DVS Dolby Vision](#dvs-dolby-vision)
        - [CLIPPING \& COLOR](#clipping--color-1)
        - [EVALUATION](#evaluation-1)
        - [RAMPS,GRADIENTS,ZONE PLATES](#rampsgradientszone-plates-1)
        - [RESOLUTION,ANSI,PLACEMENT](#resolutionansiplacement-1)
      - [DVS HLG](#dvs-hlg)
        - [CLIPPING \& COLOR](#clipping--color-2)
        - [EVALUATION](#evaluation-2)
        - [RAMPS,GRADIENTS,ZONE PLATES](#rampsgradientszone-plates-2)
        - [RESOLUTION,ANSI,PLACEMENT](#resolutionansiplacement-2)
      - [UHD SDR](#uhd-sdr)
        - [CLIPPING \& GAMMA](#clipping--gamma)
        - [COLOR BARS \& NOISE](#color-bars--noise)
        - [COLOR CHECKER](#color-checker)
        - [GEOMETRY AND RESOLUTION](#geometry-and-resolution)
        - [RAMPS](#ramps)
      - [Dolby Vision](#dolby-vision)
      - [HD](#hd-1)
      - [PVA](#pva)
      - [SPE](#spe)
      - [SPEARS \& MUNSIL](#spears--munsil)
      - [USER (STILLS)](#user-stills)
      - [SHORTCUTS](#shortcuts)
    - [COLOR SPACE](#color-space)
    - [BT 2020](#bt-2020)
    - [COLOR DEPTH](#color-depth)
    - [HDCP](#hdcp)
    - [HDMI/DVI](#hdmidvi)
    - [HDR](#hdr)
  - [Video Tests](#video-tests)
  - [Audio Generator](#audio-generator)
    - [PCM AUDIO](#pcm-audio)
      - [Audio Sampling Rate](#audio-sampling-rate)
      - [Audio Bit Depth](#audio-bit-depth)
      - [Sinewave Tone](#sinewave-tone)
      - [Audio Volume](#audio-volume)
      - [Audio Channel Config](#audio-channel-config)
    - [DOLBY AUDIO GENERATOR](#dolby-audio-generator)
      - [DOLBY Digital](#dolby-digital)
      - [DOLBY Digital Plus](#dolby-digital-plus)
      - [DOLBY MAT](#dolby-mat)
      - [DOLBY MAT (DOLBY TrueHD)](#dolby-mat-dolby-truehd)
      - [My Streams](#my-streams)
    - [EXT.ANALOG L/R INPUT](#extanalog-lr-input)
    - [DTS AUDIO GENERATOR](#dts-audio-generator)
      - [DTS Digital Surround](#dts-digital-surround)
      - [DTS-HD Higher Resolution](#dts-hd-higher-resolution)
      - [DTS-HD Master Audio](#dts-hd-master-audio)
      - [DTS: X](#dts-x)
      - [DTS Express](#dts-express)
      - [MY STREAMS](#my-streams-1)
  - [Audio Tests](#audio-tests)
    - [SYNC-LATENCY TEST](#sync-latency-test)
      - [VIDEO SETTINGS](#video-settings)
      - [DOLBY VISION SETTINGS](#dolby-vision-settings)
      - [AUDIO STREAM ADJUST](#audio-stream-adjust)
      - [AV SENSORS FUNCTIONAL TEST](#av-sensors-functional-test)
      - [ARM AV LATENCY](#arm-av-latency)
      - [ARM ARC LATENCY](#arm-arc-latency)
      - [ARM eARC LATENCY](#arm-earc-latency)
    - [SOURCE-SPEAKER TEST](#source-speaker-test)
  - [EDID eARC CDS](#edid-earc-cds)
    - [SINK DEVICE EDID INFO](#sink-device-edid-info)
    - [eARC/ARC AUDIO INFO](#earcarc-audio-info)
    - [ARC HPD CTL](#arc-hpd-ctl)
    - [ARC PHYSICAL HPD CTL](#arc-physical-hpd-ctl)
    - [eARC HPD bit CTL](#earc-hpd-bit-ctl)
    - [HDMI +5V POWER CTL](#hdmi-5v-power-ctl)
    - [eARC TX LATENCY](#earc-tx-latency)
    - [eARC RX LATENCY](#earc-rx-latency)
    - [Send CEC Command](#send-cec-command)
  - [System Setup](#system-setup)
    - [IP MANAGEMENT](#ip-management)
    - [ARC/eARC OUT SETUP](#arcearc-out-setup)
    - [FAN CONTROL](#fan-control)
    - [RESET ALL SETTINGS](#reset-all-settings)
    - [UPDATE FIRMWARE](#update-firmware)
      - [Update Firmware](#update-firmware-1)
      - [reboot](#reboot)

## Video Generator

### TIMING

#### 8K

- 7680x4320 30Hz
  - id=110
- 7680x4320 29.97Hz
  - id=111
- 7680x4320 25Hz
  - id=112
- 7680x4320 24Hz
  - id=113
- 7680x4320 23.98Hz
  - id=114
- 7680x4320 60Hz
  - id=115
- 7680x4320 59.94Hz
  - id=116
- 7680x4320 50Hz
  - id=117
- 7680x4320 48Hz
  - id=118
- 7680x4320 47.95Hz
  - id=119

#### UHD

- 3840x2160 30Hz
  - id=28
- 3840x2160 29.97Hz
  - id=29
- 3840x2160 25Hz
  - id=30
- 3840x2160 24Hz
  - id=31
- 3840x2160 23.98Hz
  - id=32
- 3840x2160 60Hz
  - id=34
- 3840x2160 59.94Hz
  - id=35
- 3840x2160 50Hz
  - id=36
- 3840x2160 48Hz
  - id=103
- 3840x2160 47.95Hz
  - id=104
- 3840x2160 100Hz
  - id=107
- 3840x2160 120Hz
  - id=108
- 3840x2160 119.88Hz
  - id=109

#### 4K-DCI

- 4096x2160 30Hz
  - id=53
- 4096x2160 29.97Hz
  - id=54
- 4096x2160 25Hz
  - id=55
- 4096x2160 24Hz
  - id=44
- 4096x2160 23.976Hz
  - id=56
- 4096x2160 60Hz
  - id=57
- 4096x2160 59.94Hz
  - id=58
- 4096x2160 50Hz
  - id=59
- 4096x2160 48Hz
  - id=105
- 4096x2160 47.95Hz
  - id=106

#### 2K-DCI

- 2048x1080 30Hz
  - id=73
- 2048x1080 29.97Hz
  - id=74
- 2048x1080 25Hz
  - id=75
- 2048x1080 24Hz
  - id=76
- 2048x1080 23.976Hz
  - id=77
- 2048x1080 60Hz
  - id=78
- 2048x1080 59.94Hz
  - id=79
- 2048x1080 50Hz
  - id=80

#### HD

- 720P 60Hz
  - id=12
- 720P 59.94Hz
  - id=13
- 1080i 60Hz
  - id=14
- 1080i 59.94Hz
  - id=15
- 1080p 30Hz
  - id=16
- 1080p 29.97Hz
  - id=17
- 1080p 24Hz
  - id=18
- 1080p 23.976Hz
  - id=19
- 1080p 60Hz
  - id=20
- 1080p 59.94Hz
  - id=21
- 720P 50Hz
  - id=24
- 1080i 50Hz
  - id=25
- 1080p 25Hz
  - id=26
- 1080p 50Hz
  - id=27
- 1080p 120Hz
  - id=81
- 1080p 119.88Hz
  - id=82
- 1080p 100Hz
  - id=102

#### SD

- 480i 59.94Hz
  - id=10
- 480p 59.94Hz
  - id=11
- 576i 50Hz
  - id=22
- 576p 50Hz
  - id=23

#### VESA

- VGA 640x480
  - id=0
- SVGA 800x600
  - id=1
- XGA 1024x768
  - id=2
- XGA+ 1152x864
  - id=72
- HD 1360x768
  - id=4
- HD 1280x768
  - id=3
- SXGA 1280x960
  - id=5
- SXGA+ 1400x1050
  - id=7
- WXGA+ 1440x900
  - id=69
- HD+ 1600x900
  - id=70
- UXGA 1600x1200
  - id=8
- WUXGA 1920x1200
  - id=9
- XGA+ 1152x900
  - id=83
- WXGA 1280x800
  - id=84
- SXGA 1280x1050
  - id=85
- UN 1920x1280
  - id=86
- UN 1920x1440
  - id=87
- QWXGA 2048x1152
  - id=88
- QXGA 2048x1536
  - id=89
- UN 2160x1440
  - id=90
- UN 2560x1080
  - id=91
- QHD 2560x1440
  - id=92
- WQXGA 2560x1600
  - id=93
- QSXGA 2560x2048
  - id=94
- QWXGA+ 2880x1800
  - id=95
- GAL 2960x1440
  - id=96
- SUR 3000x2000
  - id=97
- WQSXGA 3200x2048
  - id=98
- UWQHD 3440X1440
  - id=99
- UW4K 3840x1600
  - id=72
- WQUXGA 3840x2400
  - id=101

#### 3D

- 720P 60Hz (3D-FP)
  - id=37
- 720P 59.94Hz (3D-FP)
  - id=38
- 1080P 24Hz (3D-FP)
  - id=39
- 1080P 23.976Hz (3D-FP)
  - id=40
- 720P 50Hz (3D-FP)
  - id=41

#### CUSTOM

- USER-1
  - id=43
- USER-2
  - id=44
- USER-3
  - id=45
- USER-4
  - id=46
- USER-5
  - id=47
- USER-6
  - id=48
- USER-9
  - id=49
- USER-8
  - id=50
- USER-9
  - id=51
- USER-10
  - id=52

#### AUTO

- Auto(Output timing based on EDID of sink device)
  - id=43

### PATTERN

#### FPGA

- 100% Color Bars
  - id=0
- 75% Color Bars
  - id=1
- 8 Step Gray Bars
  - id=2
- 16 Step Gray Bars
  - id=3
- Red Screen
  - id=4
- Green Screen
  - id=5
- Blue Screen
  - id=6
- Cyan Screen
  - id=7
- Magenta Screen
  - id=8
- Yellow Screen
  - id=9
- Black Screen
  - id=10
- White Screen
  - id=11
- Vertical Split
  - id=12
- Horizontal Split
  - id=13
- Multiburst Vert.
  - id=14
- Multiburst Hor.
  - id=15
- Quarter Block 1
  - id=16
- Quarter Block 2
  - id=17
- Alternate W.B
  - id=18
- RGB CMY Ramps
  - id=19
- Black Pluge
  - id=20
- White Pluge
  - id=21
- Still Gray Ramp 1
  - id=22
- Still gray Ramp 2
  - id=23
- Smpte Bars
  - id=24
- Border Lines
  - id=25
- Window
  - id=26
- 3D Boxes
  - id=27
- Line V.Scroll
  - id=28
- Line H.Scroll
  - id=29
- A/V Sync
  - id=30
- Gray Ramp
  - id=31
- Red Ramp
  - id=32
- Green Ramp
  - id=33
- Blue Ramp
  - id=34
- Moving Ball
  - id=35

#### ISF

- White Pluge UHD
  - id=36
- Black Pluge UHD
  - id=37
- Geometry UHD
  - id=38
- White Pluge HD
  - id=39
- Black Pluge HD
  - id=40
- Geometry 178 HD
  - id=41
- Geometry 240 HD
  - id=42
- ISF Color Girls
  - id=43
- PD Family
  - id=44
- Red Blue MTB
  - id=45
- Cone Gradiant
  - id=46
- ISF Dog
  - id=47

#### DVS HDR

##### CLIPPING & COLOR

- Black Level 1
  - id=48
- Black Level 2
  - id=49
- White Level 1
  - id=50
- White Level 2
  - id=51
- White Level 3
  - id=52
- White 80-100
  - id=53
- HDR Mix
  - id=54
- HDR Greyscale
  - id=55
- HDR Red
  - id=56
- HDR Green
  - id=57
- HDR Blue
  - id=58
- HDR Yellow
  - id=59
- HDR Cyan
  - id=60
- HDR Magenta
  - id=61
- Multi-Cube
  - id=62
- 10 Patch Mix
  - id=63
- Greyscale 1000
  - id=64
- Greyscale 2000
  - id=65
- Greyscale 4000
  - id=66
- Greyscale 10000
  - id=67
- Color High
  - id=68
- Color Low
  - id=69
- Decoding 50%
  - id=70
- Decoding 100%
  - id=71
- Blue Filter 100%
  - id=72
- Green Filter 100%
  - id=73
- Red Filter 100%
  - id=74
- Blue Filter 50%
  - id=75
- Green Filter 50%
  - id=76
- Red Filter 50%
  - id=77
- Color Flashing
  - id=78
- Dynamic Contrast
  - id=79

##### EVALUATION

- Landscape
  - id=80
- Skin Tone
  - id=81
- Skin Tone
  - id=82
- City Sunset
  - id=83
- Oceanside
  - id=84
- Pantone Skin
  - id=85
- Restaurant
  - id=86
- Indian Market
  - id=87
- Ambient 05 Nit
  - id=88
- Ambient 10 Nit
  - id=89
- Ambient 15 Nit
  - id=90
- Chroma Sub 100
  - id=91
- Chroma Sub 500
  - id=92
- Chroma Sub 1000
  - id=93
- Judder 24 FPS
  - id=94
- Judder 60 FPS
  - id=95
- M Judder 24 FPS
  - id=96

##### GEOMETRY & CONVERGENCE

- Apsect Ratio 1.78
  - id=97
- Apsect Ratio 1.85
  - id=98
- Apsect Ratio 2.00
  - id=99
- Apsect Ratio 2.35
  - id=100
- Apsect Ratio 2.40
  - id=101
- Apsect Ratio All
  - id=102
- Grid White
  - id=103
- Grid Red
  - id=104
- Grid Green
  - id=105
- Grid Blue
  - id=106
- Grid Yellow
  - id=107
- Grid Cyan
  - id=108
- Grid Magenta
  - id=109
- Dot White
  - id=110
- Dot Red
  - id=111
- Dot Green
  - id=112
- Dot Blue
  - id=113
- Dot Yellow
  - id=114
- Dot Cyan
  - id=115
- Dot Magenta
  - id=116
- Cross White
  - id=117
- Cross Red
  - id=118
- Cross Green
  - id=119
- Cross Blue
  - id=120
- Cross Yellow
  - id=121
- Cross Cyan
  - id=122
- Cross Magenta
  - id=123

##### RAMPS,GRADIENTS,ZONE PLATES

- Greyscale Steps
  - id=124
- Greyscale Ramp
  - id=125
- Greyscale Mix
  - id=126
- Color Steps
  - id=127
- Color Ramp
  - id=128
- Color Ramp H&V
  - id=129
- Color Ramp Mix
  - id=130
- Color Bar Ramp
  - id=131
- Ramp Red
  - id=132
- Ramp Green
  - id=133
- Ramp Blue
  - id=134
- Ramp Yellow
  - id=135
- Ramp Cyan
  - id=136
- Ramp Magenta
  - id=137
- Zone White
  - id=138
- Zone Red
  - id=139
- Zone Green
  - id=140
- Zone Blue
  - id=141
- Zone Magenta
  - id=142
- Zone Yellow
  - id=143
- Zone Cyan
  - id=144
- Radial Grey
  - id=145
- Radial Red
  - id=146
- Radial Green
  - id=147
- Radial Blue
  - id=148
- Radial Yellow
  - id=149
- Radial Cyan
  - id=150
- Radial Magenta
  - id=151

##### RESOLUTION,ANSI,PLACEMENT

- Resolution Mix
  - id=152
- Checkerboard
  - id=153
- Horizontal 1px
  - id=154
- Horizontal 2px
  - id=155
- Horizontal 3px
  - id=156
- Vertical 1px
  - id=157
- Vertical 2px
  - id=158
- Vertical 3px
  - id=159
- Black Pixels
  - id=160
- ANSI Meter 8x8
  - id=161
- ANSI 8x8
  - id=162
- ANSI Meter 5x4
  - id=163
- ANSI M5x4 Black
  - id=164
- ANSI M5x4 White
  - id=165
- Meter Placement
  - id=166
- Sharp & Scan
  - id=167

#### DVS Dolby Vision

##### CLIPPING & COLOR

- Black Level 1
  - id=472
- Black Level 2
  - id=473
- White Level 1
  - id=474
- White Level 2
  - id=475
- White Level 3
  - id=476
- White 80-100
  - id=477
- Blue Filter 50%
  - id=478
- Green Filter 50%
  - id=479
- Red Filter 50%
  - id=480
- Color Clipping High
  - id=481
- Color Clipping Low
  - id=482
- Color Decoding
  - id=483
- Color Flashing
  - id=484

##### EVALUATION

- Landscape
  - id=485
- Nature
  - id=486
- Skin Tone
  - id=487
- City Sunset
  - id=488
- Oceanside
  - id=489
- Pantone Skin
  - id=490
- Restaurant
  - id=491
- Indian Market
  - id=492

##### RAMPS,GRADIENTS,ZONE PLATES

- Greyscale Steps
  - id=493
- Greyscale Ramp
  - id=494
- Greyscale Mix
  - id=495
- Color Steps
  - id=496
- Red Radial Gradient
  - id=497
- Green Radial Gradient
  - id=498
- Blue Radial Gradient
  - id=499
- Yellow Radial Gradient
  - id=500
- Cyan Radial Gradient
  - id=501
- Magenta Radial Gradient
  - id=502

##### RESOLUTION,ANSI,PLACEMENT

- ANSI Meter 8x8
  - id=503
- ANSI 8x8 Black
  - id=504
- ANSI 8x8 White
  - id=505
- ANSI Meter 5x4
  - id=506
- ANSI M5x4 Black
  - id=507
- ANSI M5x4 White
  - id=508
- Meter Placement
  - id=509
- Sharp & Scan
  - id=510

#### DVS HLG

##### CLIPPING & COLOR

- Black Level 1
  - id=511
- Black Level 2
  - id=512
- White Level 1
  - id=513
- White Level 2
  - id=514
- White Level 3
  - id=515
- HDR Mix
  - id=517
- HDR Greyscale
  - id=518
- HDR Red
  - id=519
- HDR Green
  - id=520
- HDR Blue
  - id=521
- HDR Yellow
  - id=522
- HDR Cyan
  - id=523
- HDR Magenta
  - id=524
- Multi-Cube
  - id=525
- 10 Patch Mix
  - id=526
- Blue Filter 100%
  - id=529
- Green Filter 100%
  - id=530
- Red Filter 100%
  - id=531
- Color Clipping High
  - id=527
- Color Clipping Low
  - id=528
- Color Decoding 50%
  - id=532
- Color Decoding 100%
  - id=533
- Color Flashing
  - id=516

##### EVALUATION

- Landscape
  - id=534
- Nature
  - id=535
- Skin Tone
  - id=536
- City Sunset
  - id=537
- Oceanside
  - id=538
- Pantone Skin
  - id=539
- Restaurant
  - id=540
- Indian Market
  - id=541

##### RAMPS,GRADIENTS,ZONE PLATES

- Greyscale Steps
  - id=542
- Greyscale Ramp
  - id=543
- Greyscale Mix
  - id=544
- Color Steps
  - id=545
- Color Ramp
  - id=546
- Color Ramp H&V
  - id=547
- Color Ramp Mix
  - id=548
- Color Bar Ramp
  - id=549
- Ramp Red
  - id=550
- Ramp Green
  - id=551
- Ramp Blue
  - id=552
- Ramp Yellow
  - id=553
- Ramp Cyan
  - id=554
- Ramp Magenta
  - id=555
- Zone White
  - id=556
- Zone Red
  - id=557
- Zone Green
  - id=558
- Zone Blue
  - id=559
- Zone Magenta
  - id=560
- Zone Yellow
  - id=561
- Zone Cyan
  - id=562
- Radial Grey
  - id=563
- Radial Red
  - id=564
- Radial Green
  - id=565
- Radial Blue
  - id=566
- Radial Yellow
  - id=567
- Radial Cyan
  - id=568
- Radial Magenta
  - id=569

##### RESOLUTION,ANSI,PLACEMENT

- ANSI Meter 8x8
  - id=570
- ANSI 8x8 Black
  - id=571
- ANSI 8x8 White
  - id=572
- ANSI Meter 5x4
  - id=573
- ANSI M5x4 Black
  - id=574
- ANSI M5x4 White
  - id=575
- Meter Placement
  - id=576
- Sharp & Scan
  - id=577
- Resolution Mix
  - id=578

#### UHD SDR

##### CLIPPING & GAMMA

- Target Limited
  - id=168
- Target Full
  - id=169
- Contrast Check
  - id=170
- Contrast Lines
  - id=171
- Gamma Check
  - id=172
- Gamma Lines
  - id=173
- High Clipping
  - id=174
- High Clip Red
  - id=175
- High Clip Green
  - id=176
- High Clip Blue
  - id=177
- Low Clipping
  - id=178
- Low Clip Red
  - id=179
- Low Clip Green
  - id=180
- Low Clip Blue
  - id=181
- Composite Grey
  - id=182
- Composite Red
  - id=183
- Composite Green
  - id=184
- Composite Blue
  - id=185
- Lin Step Grey
  - id=186
- Lin Step Red
  - id=187
- Lin Step Green
  - id=188
- Lin Step Blue
  - id=189
- Lin Step Magent
  - id=190
- Lin Step Yellow
  - id=191
- Lin Step Cyan
  - id=192
- Log Step Grey
  - id=193
- Log Step Red
  - id=194
- Log Step Green
  - id=195
- Log Step Blue
  - id=196
- Log Step Magent
  - id=197
- Log Step Yellow
  - id=198
- Log Step Cyan
  - id=199
- Gamma Grey
  - id=200
- Gamma Red
  - id=201
- Gamma Green
  - id=202
- Gamma Blue
  - id=203
- Gamma Lines Grey
  - id=204
- Gamma Lines Red
  - id=205
- Gamma Lines Green
  - id=206
- Gamma Lines Blue
  - id=207

##### COLOR BARS & NOISE

- Color Wipe Full
  - id=208
- Color Wipe Half
  - id=209
- Quick Check
  - id=210
- H Bars RGB
  - id=211
- H Bars RGBCMY
  - id=212
- H Bars Shade
  - id=214
- V Bars RGB
  - id=215
- V Bars RGBCMY
  - id=216
- V Bars Layover
  - id=217
- V Bars Shade
  - id=218
- Color Noise 01
  - id=219
- Color Noise 02
  - id=220
- Color Noise 04
  - id=221
- Color Noise 08
  - id=222
- Color Noise 16
  - id=223
- Color Noise 01
  - id=224
- Color Noise 02
  - id=225
- Color Noise 04
  - id=226
- Color Noise 08
  - id=227
- Color Noise 16
  - id=228

##### COLOR CHECKER

- HSL BlueMagenta
  - id=229
- HSL Blue
  - id=230
- HSL Cyan Blue
  - id=231
- HSL Cyan
  - id=232
- HSL Green Cyan
  - id=233
- HSL Green
  - id=234
- HSL Magenta Red
  - id=235
- HSL Magenta
  - id=236
- HSL Red
  - id=237
- HSL Yellow Green
  - id=238
- HSL Yellow Red
  - id=239
- HSL Yellow
  - id=240
- HSV BlueMagenta
  - id=241
- HSV Cyan Blue
  - id=243
- HSV Cyan
  - id=244
- HSV Green Cyan
  - id=245
- HSV Green
  - id=246
- HSV Magenta Red
  - id=247
- HSV Magenta
  - id=248
- HSV Red
  - id=249
- HSV Yellow Green
  - id=250
- HSV Yellow Red
  - id=251
- HSV Yellow
  - id=252
- RGB Blue 064
  - id=253
- RGB Blue 127
  - id=254
- RGB Blue 191
  - id=255
- RGB Blue 255
  - id=256
- RGB Green 064
  - id=257
- RGB Green 127
  - id=258
- RGB Green 191
  - id=259
- RGB Green 255
  - id=260
- RGB Red 064
  - id=261
- RGB Red 127
  - id=262
- RGB Red 191
  - id=263
- RGB Red 255
  - id=264

##### GEOMETRY AND RESOLUTION

- H Convergence
  - id=265
- V Convergence
  - id=266
- H Length
  - id=267
- V Length
  - id=268
- Overscan
  - id=269
- BW Evaluation
  - id=270
- BW Evaluation 2
  - id=271
- H Wedge
  - id=272
- Star Burst
  - id=273
- V Wedge
  - id=274
- H Multiburst
  - id=275
- V Multiburst
  - id=276
- Checkers 02
  - id=277
- Checkers 04
  - id=278
- Checkers 08
  - id=279
- Checkers 16
  - id=280
- Checkers 32
  - id=281
- Checkers Log
  - id=282
- Many Circles
  - id=283
- Center Circle
  - id=284
- Many Squares
  - id=285
- Grid
  - id=286
- H Lines 02
  - id=287
- H Lines 04
  - id=288
- H Lines 08
  - id=289
- H Lines Log
  - id=290
- V Lines 02
  - id=291
- V Lines 04
  - id=292
- V Lines 08
  - id=293
- V Lines Log
  - id=294
- Points 02
  - id=295
- Points 04
  - id=296
- Points 08
  - id=297
- Points 16
  - id=298
- Points 32
  - id=299
- Squares 02
  - id=300
- Squares 04
  - id=301
- Squares 08
  - id=302
- Squares 16
  - id=303
- Squares 32
  - id=304

##### RAMPS

- Color Patch
  - id=305
- Triangle
  - id=306
- Wireframe
  - id=307
- Full Red
  - id=308
- Full Green
  - id=309
- Full Blue
  - id=310
- Full Magenta
  - id=311
- Full Yellow
  - id=312
- Full Cyan
  - id=313
- Full Grey
  - id=314
- Half Red
  - id=315
- Half Green
  - id=316
- Half Blue
  - id=317
- Half Magenta
  - id=318
- Half Yellow
  - id=319
- Half Cyan
  - id=320
- HSL Sat 0.00
  - id=321
- HSL Hue 0.00
  - id=322
- HSL Hue 0.33
  - id=323
- HSL Hue 0.66
  - id=324
- HSL Lev 0.25
  - id=325
- HSL Lev 0.50
  - id=326
- HSL Lev 0.75
  - id=327
- HSV Sat 0.00
  - id=328
- HSV Sat 0.50
  - id=329
- HSV Sat 1.00
  - id=330
- HSV Hue 0.00
  - id=331
- HSV Hue 0.33
  - id=332
- HSV Hue 0.66
  - id=333
- HSV Sat 0.50
  - id=334
- HSV Sat 1.00
  - id=335
- HSV Sat 0.00
  - id=336
- HSV Sat 0.50
  - id=337
- HSV Sat 1.00
  - id=338
- RGB Green 000
  - id=339
- RGB Green 127
  - id=340
- RGB Green 255
  - id=341
- RGB Blue 000
  - id=342
- RGB Blue 127
  - id=343
- RGB Blue 255
  - id=344
- RGB Red 000
  - id=345
- RGB Red 127
  - id=346
- RGB Red 255
  - id=347

#### Dolby Vision

- Dolby Vision UHD
  - id=425
- CornerBox_UHD
  - id=426
- Checker_UHD
  - id=427
- Steps_UHD_L255rm1
  - id=428
- Steps_UHD_L255rm2
  - id=429
- Steps_UHD_noL255
  - id=430
- Ramp_UHD_L255rm1
  - id=431
- Ramp_UHD_L255rm2
  - id=432
- Ramp_UHD_noL255
  - id=433
- Dolby Vision FHD
  - id=434
- CornerBox_FHD
  - id=435
- Checker_FHD
  - id=436
- Steps_FHD_L255rm1
  - id=437
- Steps_FHD_L255rm2
  - id=438
- Steps_FHD_noL255
  - id=439
- Ramp_FHD_L255rm1
  - id=440
- Ramp_FHD_L255rm2
  - id=441
- Ramp_FHD_noL255
  - id=442

#### HD

- High Clipping
  - id=350
- Low Clipping
  - id=351
- Color Noise 01
  - id=352
- Color Noise 02
  - id=353
- Color Noise 04
  - id=354
- Color Noise 08
  - id=355
- Triangle
  - id=356
- Color Wipe Full
  - id=357
- Color Wipe Half
  - id=358
- Composite
  - id=359
- H Multiburst
  - id=360
- V Multiburst
  - id=361
- Checkers 02
  - id=362
- Checkers 04
  - id=363
- Checkers 08
  - id=364
- Checkers 16
  - id=365
- Checkers 32
  - id=366
- Checkers Log
  - id=367
- Many Circles
  - id=368
- Center Circle
  - id=369
- Many Squares
  - id=370
- Grid
  - id=371
- H Lines 02
  - id=372
- H Lines 04
  - id=373
- H Lines 08
  - id=374
- H Lines Log
  - id=375
- V Lines 02
  - id=376
- V Lines 04
  - id=377
- V Lines 08
  - id=378
- Geometry Points 02
  - id=380
- Geometry Points 04
  - id=381
- Geometry Points 08
  - id=382
- Geometry Points 16
  - id=383
- Geometry Points 32
  - id=384
- Geometry Squares 04
  - id=385
- Geometry Squares 08
  - id=386
- Geometry Squares 16
  - id=387
- Geometry Squares 32
  - id=388
- H Length
  - id=389
- V Length
  - id=390
- Overscan
  - id=391
- BW Evaluation 2
  - id=392
- BW Evaluation
  - id=393
- H Wedge
  - id=394
- Star Burst
  - id=395
- V Wedge
  - id=396
- RGB Text
  - id=397

#### PVA

- (BT709) White_Clipping
  - id=443
- (BT709) Black_Clipping
  - id=444
- (BT709) APL_W_B_Clipping
  - id=445
- (BT709) Color_Clipping
  - id=446
- (BT709) Sharpness_Overscan
  - id=447
- (BT709) Alignment
  - id=448
- (BT709) Multi_Skin_Tone
  - id=449
- (BT709) Restaurant_Scene
  - id=450
- (BT709) Skin_Tone
  - id=451
- (BT2020) White_Clipping
  - id=579
- (BT2020) Black_Clipping
  - id=580
- (BT2020) APL_W_B_Clipping
  - id=581
- (BT2020) Color_Clipping
  - id=582
- (BT2020) Sharpness_Overscan
  - id=583
- (BT2020) Alignment
  - id=584
- (BT2020) Multi_Skin_Tone
  - id=585
- (BT2020) Restaurant_Scene
  - id=586
- (BT2020) Skin_Tone
  - id=587

#### SPE

- (4:2:0) Girl
  - id=452
- (4:2:0) Women
  - id=453
- (4:2:0) Girl HDR & SDR
  - id=454
- (4:4:4 Full) Girl
  - id=455
- (4:4:4 Full) Women
  - id=588
- (4:4:4 Full) Girl HDR & SDR
  - id=589
- (4:4:4 Limit) Girl
  - id=590
- (4:4:4 Limit) Women
  - id=591
- (4:4:4 Limit) Girl HDR & SDR
  - id=590

#### SPEARS & MUNSIL

- Bias_Light_10%
  - id=456
- Bias_Light_15%
  - id=457
- Framing
  - id=458
- Hammock_24p
  - id=459
- Hammock_30p
  - id=460
- Hammock_260i
  - id=461
- Mixed_video_H_60i
  - id=462
- Mixed_Video_V_60i
  - id=463
- ColorTint_01_Red
  - id=464
- ColorTint_01_Green
  - id=465
- ColorTint_01_Blue
  - id=466
- Jaggies_Full_60i
  - id=467
- Ship1_60i
  - id=468
- Ship2_60i
  - id=469
- Ship3_60i
  - id=470

#### USER (STILLS)

- User Pattern1 ()
  - id=398
- User Pattern2 ()
  - id=399
- User Pattern3 ()
  - id=400
- User Pattern4 ()
  - id=401
- User Pattern5 ()
  - id=402
- User Pattern6 ()
  - id=403

#### SHORTCUTS

- SHORTCUTS 1
  - id=471
- SHORTCUTS 2
  - id=472
- SHORTCUTS 3
  - id=473
- SHORTCUTS 4
  - id=474
- SHORTCUTS 5
  - id=475
- SHORTCUTS 6
  - id=476
- SHORTCUTS 7
  - id=477
- SHORTCUTS 8
  - id=478
- SHORTCUTS 9
  - id=495
- SHORTCUTS 10
  - id=480
- SHORTCUTS 11
  - id=481
- SHORTCUTS 12
  - id=482
- SHORTCUTS 13
  - id=483
- SHORTCUTS 14
  - id=484

### COLOR SPACE

- RGB(0-255)
  - id=0
- RGB(16-235)
  - id=1
- YC 4:4:4(16-235)
  - id=2
- YC 4:2:2(16-235)
  - id=3
- YC 4:2:0(16-235)
  - id=4

### BT 2020

- ENABLE
  - id=1
- DISABLE
  - id=0

### COLOR DEPTH

- 8Bit
  - id=0
- 10Bit
  - id=1
- 12Bit
  - id=2
- 16Bit
  - id=3

### HDCP

- HDCP OFF
  - id=0
- HDCP 1.4
  - id=1
- HDCP 2.2
  - id=2
- HDCP AUTO
  - id=3

### HDMI/DVI

- DVI
  - id=0
- HDMI
  - id=1
- AUTO
  - id=2

### HDR

- HDR OFF(SDR)
  - id=0
- HDR-10
  - id=1
- HLG
  - id=2
- HDR CUSTOM 1
  - id=3
- HDR CUSTOM 2
  - id=4
- HDR CUSTOM 3
  - id=5
- HDR CUSTOM 4
  - id=6
- HDR CUSTOM 5
  - id=7
- HDR CUSTOM 6
  - id=8
- HDR CUSTOM 7
  - id=9
- HDR CUSTOM 8
  - id=10

## Video Tests

- Spicey Pixels Chongqing Day
  - id=404
- Spicey Pixels Chongqing Night
  - id=405
- Spicey Pixels Chongqing Lights
  - id=406
- Spicey Pixels Chongqing Cars
  - id=407
- Spicey Pixels Chongqing Cars2
  - id=408
- Spicey Pixels London Yogurt
  - id=411
- Spicey Pixels London River
  - id=412
- Spicey Pixels London Sidewalk
  - id=413
- Spicey Pixels London Busses
  - id=414
- Spicey Pixels London cafe
  - id=415
- Spicey Pixels Mukilteo Street
  - id=416
- Spicey Pixels Mukilteo Loading
  - id=417
- Spicey Pixels Carnival Wheel
  - id=418
- Spicey Pixels Carnival Ride
  - id=419
- Spicey Pixels Carnival night
  - id=420
- Spicey Pixels Carnival Balloon Pop
  - id=421
- Spicey Pixels Tiger Mountain 120
  - id=422
- Spicey Pixels Biker 120
  - id=423
- SPE Test Video
  - id=424
- User Video Clip 1
  - id=409
- User Video Clip 2
  - id=410
- Automation Testing Clip
  - id=471

## Audio Generator

### PCM AUDIO

#### Audio Sampling Rate

- 32K
  - id=0
- 44.1K
  - id=1
- 48K
  - id=2
- 88K
  - id=3
- 96K
  - id=4
- 176k
  - id=5
- 192k
  - id=6

#### Audio Bit Depth

- 16Bit
  - id=0
- 20Bit
  - id=1
- 24Bit
  - id=2

#### Sinewave Tone

- SINEWAVE TONE(100Hz)
  - id=0
- SINEWAVE TONE(200Hz)
  - id=1
- SINEWAVE TONE(300Hz)
  - id=2
- SINEWAVE TONE(400Hz)
  - id=3
- SINEWAVE TONE(500Hz)
  - id=4
- SINEWAVE TONE(600Hz)
  - id=5
- SINEWAVE TONE(700Hz)
  - id=6
- SINEWAVE TONE(800Hz)
  - id=7
- SINEWAVE TONE(900Hz)
  - id=8
- SINEWAVE TONE(1KHz)
  - id=9
- SINEWAVE TONE(2KHz)
  - id=10
- SINEWAVE TONE(3KHz)
  - id=11
- SINEWAVE TONE(4KHz)
  - id=12
- SINEWAVE TONE(5KHz)
  - id=13

#### Audio Volume

- -60db
  - id=0
- -54db
  - id=1
- -48db
  - id=2
- -42db
  - id=3
- -36db
  - id=4
- -30db
  - id=5
- -24db
  - id=6
- -18db
  - id=7
- -12
  - id=8
- -6db
  - id=9
- 0db
  - id=10

#### Audio Channel Config

- 2CH (FR_FL)
  - id=0
- 2.1CH (LFE_FR_FL)
  - id=1
- 3CH (FC_FR_FL)
  - id=2
- 3.1CH (FC_LFE_FR_FL)
  - id=3
- 3CH (RC_FR_FL)
  - id=4
- 3.1CH (RC_LFE_FR_FL)
  - id=5
- 4CH (RC_LFE_FR_FL)
  - id=6
- 4.1CH (RC_FC_LFE_FR_FL)
  - id=7
- 4CH (RR_RL_FR_FL)
  - id=8
- 4.1CH (RR_RL_LFE_FR_FL)
  - id=9
- 5CH (RR_RS_FC_FR_FL)
  - id=10
- 5.1CH (RR_RL_FC_LFE_FR_FL)
  - id=11
- 5CH (RC_RR_RL_FR_FL)
  - id=12
- 5.1CH (RC_RR_RL_LFE_FR_FL)
  - id=13
- 6CH (RC_RR_RL_FC_FR_FL)
  - id=14
- 6.1CH (RC_RR_RL_FC_LFE_FR_FL)
  - id=15
- 6CH (RRC_RLC_RR_RL_FR_FL)
  - id=16
- 6.1CH (RRC_RLC_RR_RL_LFE_FR_FL)
  - id=17
- 7CH (RRC_RLC_RR_RL_FC_FR_FL)
  - id=18
- 7.1CH (RRC_RLC_RR_RL_FC_LFE_FR_FL)
  - id=19
- 4CH (FRC_FLC_FR_FL)
  - id=20
- 4.1CH (FRC_FLC_LFE_FR_FL)
  - id=21
- 5CH (FRC_FLC_FC_FR_FL)
  - id=22
- 5.1CH (FRC_FLC_FC_LFE_FR_FL)
  - id=23
- 5CH (FRC_FLC_RC_FR_FL)
  - id=24
- 5.1CH (FRC_FLC_RC_FC_FR_FL)
  - id=25
- 6CH (FRC_FLC_RC_FC_FR_FL)
  - id=26
- 6.1CH (FRC_FLC_RC_FC_LFE_FR_FL)
  - id=27
- 6CH (FRC_FLC_RR_RL_FR_FL)
  - id=28
- 6.1CH (FRC_FLC_RR_RL_LFE_FR_FL)
  - id=29
- 7CH (FRC_FLC_RR_RL_FC_FR_FL)
  - id=30
- 7.1CH (FRC_FLC_RR_RL_FC_LFE_FR_FL)
  - id=31

### DOLBY AUDIO GENERATOR

#### DOLBY Digital

- Dolby Digital-32KHz-2.0Ch
  - id=2
- Dolby Digital-32KHz-5.1Ch
  - id=3
- Dolby Digital-44.1KHz-2.0Ch
  - id=4
- Dolby Digital-44.1KHz-5.1Ch
  - id=5
- Dolby Digital-48KHz-2.0Ch
  - id=6
- Dolby Digital-48KHz-5.1Ch
  - id=7

#### DOLBY Digital Plus

- Dolby Digital Plus-48KHz-2.0Ch
  - id=8
- Dolby Digital Plus-48KHz-5.1Ch
  - id=9
- Dolby Digital Plus-48KHz-7.1Ch
  - id=10
- Dolby Digital Plus-48KHz-Atmos
  - id=11

#### DOLBY MAT

- Dolby MAT(PCM)-44.1KHz-2.0Ch
  - id=12
- Dolby MAT(PCM)-44.1KHz-5.1Ch
  - id=13
- Dolby MAT(PCM)-44.1KHz-7.1Ch
  - id=14
- Dolby MAT(PCM)-48KHz-2.0Ch
  - id=15
- Dolby MAT(PCM)-48KHz-5.1Ch
  - id=16
- Dolby MAT(PCM)-48KHz-7.1Ch
  - id=17
- Dolby MAT(PCM object audio)-44.1KHz-Dolby Atmos
  - id=18
- Dolby MAT(PCM object audio)-48KHz-Dolby Atmos
  - id=19

#### DOLBY MAT (DOLBY TrueHD)

- Dolby MAT(Dolby TrueHD)-48KHz-2.0Ch
  - id=20
- Dolby MAT(Dolby TrueHD)-48KHz-5.1Ch
  - id=21
- Dolby MAT(Dolby TrueHD)-48KHz-7.1Ch
  - id=22
- Dolby MAT(Dolby TrueHD)-96KHz-2.0Ch
  - id=23
- Dolby MAT(Dolby TrueHD)-96KHz-5.1Ch
  - id=24
- Dolby MAT(Dolby TrueHD)-96KHz-7.1Ch
  - id=25
- Dolby MAT(Dolby TrueHD)-192KHz-2.0Ch
  - id=26
- Dolby MAT(Dolby TrueHD)-192KHz-5.1Ch
  - id=27
- Dolby MAT(Dolby TrueHD)Object Based 48KHz-Dolby Atmos
  - id=28

#### My Streams

- MY STREAM1 ()
  - id=288
- MY STREAM2 ()
  - id=308
- MY STREAM3 ()
  - id=328
- MY STREAM4 ()
  - id=348
- MY STREAM5 ()
  - id=368
- MY STREAM6 ()
  - id=388

### EXT.ANALOG L/R INPUT

- ENABLE
  - id=0

### DTS AUDIO GENERATOR

#### DTS Digital Surround

- DTS Digital Surround-48KHz-2.0Ch
  - id=562
- DTS Digital Surround-48KHz-5.1Ch
  - id=563
- DTS Digital Surround-48.1KHz-6.1Ch
  - id=564
- DTS Digital Surround-44.1KHz-5.1Ch
  - id=565
- DTS Digital Surround-96KHz-5.1Ch
  - id=566

#### DTS-HD Higher Resolution

- DTS-HD High Resolution-48KHz-5.1Ch
  - id=567
- DTS-HD High Resolution-48KHz-7.1Ch
  - id=568
- DTS-HD High Resolution-96KHz-7.1Ch
  - id=569
- DTS-HD High Resolution-88.2KHz-7.1Ch
  - id=570

#### DTS-HD Master Audio

- DTS-HD Master Audio-48KHz-5.1Ch
  - id=571
- DTS-HD Master Audio-48KHz-7.1Ch
  - id=572
- DTS-HD Master Audio-192KHz-2.0Ch
  - id=573
- DTS-HD Master Audio-192KHz-7.1Ch
  - id=574

#### DTS: X

- DTS:X-48KHz-7.1.4Ch
  - id=575
- DTS:X-48KHz-5.1.4Ch
  - id=576
- DTS:X Master Audio-48KHz-7.1.4Ch
  - id=577
- DTS:X Master Audio-96KHz-7.1.4Ch
  - id=578
- DTS:X(32 Objects)
  - id=579

#### DTS Express

- DTS Low Bit Rate-48KHz-5.1Ch
  - id=580

#### MY STREAMS

- MY STREAM1 ()
  - id=581
- MY STREAM2 ()
  - id=601
- MY STREAM3 ()
  - id=621
- MY STREAM4 ()
  - id=641
- MY STREAM5 ()
  - id=661
- MY STREAM6 ()
  - id=681

## Audio Tests

### SYNC-LATENCY TEST

#### VIDEO SETTINGS

- 3840X2160 30HZ
  - id=0
- 3840X2160 29.97HZ
  - id=1
- 3840X2160 25HZ
  - id=2
- 3840X2160 24HZ
  - id=3
- 3840X2160 60HZ
  - id=4
- 3840X2160 59.94HZ
  - id=5
- 3840X2160 50HZ
  - id=6
- 1080P 30HZ
  - id=7
- 1080P 29.97HZ
  - id=8
- 1080P 25HZ
  - id=9
- 1080P 24HZ
  - id=10
- 1080P 60HZ
  - id=11
- 1080P 59.94HZ
  - id=12
- 1080P 50HZ
  - id=13
- 1080P 120HZ
  - id=14
- 1080P 119.88HZ
  - id=15

#### DOLBY VISION SETTINGS

- DOLBY VISION OFF
  - id=0
- DOLBY VISION SINK-LED
  - id=1
- DOLBY VISION SOURCE-LED
  - id=2

#### AUDIO STREAM ADJUST

- Adjust audio -500ms to +500ms
  - id=None

#### AV SENSORS FUNCTIONAL TEST

- Mic Functional Test - READ STATUS
  - id=0
- Visual Sensor Test - READ STATUS
  - id=1

#### ARM AV LATENCY

#### ARM ARC LATENCY

#### ARM eARC LATENCY

### SOURCE-SPEAKER TEST

- SPEAKER ALLOCATION
  - id=528
- WHITE NOISE
  - id=538
- SWEEP AUDIO
  - id=548

## EDID eARC CDS

### SINK DEVICE EDID INFO

- READ EDID
  - id=1
- SAVE EDID
  - id=None
- OPEN EDID
  - id=None

### eARC/ARC AUDIO INFO

### ARC HPD CTL

- ASSERT HPD(HIGH)
  - id=1
- DEASSERT HPD(LOW)
  - id=0

### ARC PHYSICAL HPD CTL

- ASSERT HPD(HIGH)
  - id=1
- DEASSERT HPD(LOW)
  - id=0

### eARC HPD bit CTL

- SET HDMI_HPD bit(=1)
  - id=1
- CLERA HDMI_HPD bit(=0)
  - id=0

### HDMI +5V POWER CTL

- SET HDMI TX +5V ON
  - id=1
- SET HDMI TX +5V OFF
  - id=0

### eARC TX LATENCY

- ERX_LATENCY_REQ(To eARC RX) id=ms
  - id=None

### eARC RX LATENCY

- ERX_LATENCY_REQ(To eARC TX) id=ms
  - id=None

### Send CEC Command

## System Setup

### IP MANAGEMENT

### ARC/eARC OUT SETUP

- DISABLE ARC/eARC
  - id=0
- ENABLE eARC
  - id=1
- ENABLE ARC
  - id=2

### FAN CONTROL

- OFF
  - id=0
- LOW SPEED
  - id=1
- MIDDLE SPEED
  - id=2
- HIGH SPEED
  - id=3

### RESET ALL SETTINGS

### UPDATE FIRMWARE

#### Update Firmware

#### reboot

- VITALS
  - id=1
- Tools
  - id=None
