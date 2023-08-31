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

| Name              | ID  |
| ----------------- | --- |
| 7680x4320 30Hz    | 110 |
| 7680x4320 29.97Hz | 111 |
| 7680x4320 25Hz    | 112 |
| 7680x4320 24Hz    | 113 |
| 7680x4320 23.98Hz | 114 |
| 7680x4320 60Hz    | 115 |
| 7680x4320 59.94Hz | 116 |
| 7680x4320 50Hz    | 117 |
| 7680x4320 48Hz    | 118 |
| 7680x4320 47.95Hz | 119 |

#### UHD

| Name               | ID  |
| ------------------ | --- |
| 3840x2160 30Hz     | 28  |
| 3840x2160 29.97Hz  | 29  |
| 3840x2160 25Hz     | 30  |
| 3840x2160 24Hz     | 31  |
| 3840x2160 23.98Hz  | 32  |
| 3840x2160 60Hz     | 34  |
| 3840x2160 59.94Hz  | 35  |
| 3840x2160 50Hz     | 36  |
| 3840x2160 48Hz     | 103 |
| 3840x2160 47.95Hz  | 104 |
| 3840x2160 100Hz    | 107 |
| 3840x2160 120Hz    | 108 |
| 3840x2160 119.88Hz | 109 |

#### 4K-DCI

| Name               | ID  |
| ------------------ | --- |
| 4096x2160 30Hz     | 53  |
| 4096x2160 29.97Hz  | 54  |
| 4096x2160 25Hz     | 55  |
| 4096x2160 24Hz     | 44  |
| 4096x2160 23.976Hz | 56  |
| 4096x2160 60Hz     | 57  |
| 4096x2160 59.94Hz  | 58  |
| 4096x2160 50Hz     | 59  |
| 4096x2160 48Hz     | 105 |
| 4096x2160 47.95Hz  | 106 |

#### 2K-DCI

| Name               | ID  |
| ------------------ | --- |
| 2048x1080 30Hz     | 73  |
| 2048x1080 29.97Hz  | 74  |
| 2048x1080 25Hz     | 75  |
| 2048x1080 24Hz     | 76  |
| 2048x1080 23.976Hz | 77  |
| 2048x1080 60Hz     | 78  |
| 2048x1080 59.94Hz  | 79  |
| 2048x1080 50Hz     | 80  |

#### HD

| Name           | ID  |
| -------------- | --- |
| 720P 60Hz      | 12  |
| 720P 59.94Hz   | 13  |
| 1080i 60Hz     | 14  |
| 1080i 59.94Hz  | 15  |
| 1080p 30Hz     | 16  |
| 1080p 29.97Hz  | 17  |
| 1080p 24Hz     | 18  |
| 1080p 23.976Hz | 19  |
| 1080p 60Hz     | 20  |
| 1080p 59.94Hz  | 21  |
| 720P 50Hz      | 24  |
| 1080i 50Hz     | 25  |
| 1080p 25Hz     | 26  |
| 1080p 50Hz     | 27  |
| 1080p 120Hz    | 81  |
| 1080p 119.88Hz | 82  |
| 1080p 100Hz    | 102 |

#### SD

| Name         | ID  |
| ------------ | --- |
| 480i 59.94Hz | 10  |
| 480p 59.94Hz | 11  |
| 576i 50Hz    | 22  |
| 576p 50Hz    | 23  |

#### VESA

| Name             | ID  |
| ---------------- | --- |
| VGA 640x480      | 0   |
| SVGA 800x600     | 1   |
| XGA 1024x768     | 2   |
| XGA+ 1152x864    | 72  |
| HD 1360x768      | 4   |
| HD 1280x768      | 3   |
| SXGA 1280x960    | 5   |
| SXGA+ 1400x1050  | 7   |
| WXGA+ 1440x900   | 69  |
| HD+ 1600x900     | 70  |
| UXGA 1600x1200   | 8   |
| WUXGA 1920x1200  | 9   |
| XGA+ 1152x900    | 83  |
| WXGA 1280x800    | 84  |
| SXGA 1280x1050   | 85  |
| UN 1920x1280     | 86  |
| UN 1920x1440     | 87  |
| QWXGA 2048x1152  | 88  |
| QXGA 2048x1536   | 89  |
| UN 2160x1440     | 90  |
| UN 2560x1080     | 91  |
| QHD 2560x1440    | 92  |
| WQXGA 2560x1600  | 93  |
| QSXGA 2560x2048  | 94  |
| QWXGA+ 2880x1800 | 95  |
| GAL 2960x1440    | 96  |
| SUR 3000x2000    | 97  |
| WQSXGA 3200x2048 | 98  |
| UWQHD 3440X1440  | 99  |
| UW4K 3840x1600   | 72  |
| WQUXGA 3840x2400 | 101 |

#### 3D

| Name                   | ID  |
| ---------------------- | --- |
| 720P 60Hz (3D-FP)      | 37  |
| 720P 59.94Hz (3D-FP)   | 38  |
| 1080P 24Hz (3D-FP)     | 39  |
| 1080P 23.976Hz (3D-FP) | 40  |
| 720P 50Hz (3D-FP)      | 41  |

#### CUSTOM

| Name    | ID  |
| ------- | --- |
| USER-1  | 43  |
| USER-2  | 44  |
| USER-3  | 45  |
| USER-4  | 46  |
| USER-5  | 47  |
| USER-6  | 48  |
| USER-9  | 49  |
| USER-8  | 50  |
| USER-9  | 51  |
| USER-10 | 52  |

#### AUTO

| Name                                             | ID  |
| ------------------------------------------------ | --- |
| Auto(Output timing based on EDID of sink device) | 43  |

### PATTERN

#### FPGA

| Name              | ID  |
| ----------------- | --- |
| 100% Color Bars   | 0   |
| 75% Color Bars    | 1   |
| 8 Step Gray Bars  | 2   |
| 16 Step Gray Bars | 3   |
| Red Screen        | 4   |
| Green Screen      | 5   |
| Blue Screen       | 6   |
| Cyan Screen       | 7   |
| Magenta Screen    | 8   |
| Yellow Screen     | 9   |
| Black Screen      | 10  |
| White Screen      | 11  |
| Vertical Split    | 12  |
| Horizontal Split  | 13  |
| Multiburst Vert.  | 14  |
| Multiburst Hor.   | 15  |
| Quarter Block 1   | 16  |
| Quarter Block 2   | 17  |
| Alternate W.B     | 18  |
| RGB CMY Ramps     | 19  |
| Black Pluge       | 20  |
| White Pluge       | 21  |
| Still Gray Ramp 1 | 22  |
| Still gray Ramp 2 | 23  |
| Smpte Bars        | 24  |
| Border Lines      | 25  |
| Window            | 26  |
| 3D Boxes          | 27  |
| Line V.Scroll     | 28  |
| Line H.Scroll     | 29  |
| A/V Sync          | 30  |
| Gray Ramp         | 31  |
| Red Ramp          | 32  |
| Green Ramp        | 33  |
| Blue Ramp         | 34  |
| Moving Ball       | 35  |

#### ISF

| Name            | ID  |
| --------------- | --- |
| White Pluge UHD | 36  |
| Black Pluge UHD | 37  |
| Geometry UHD    | 38  |
| White Pluge HD  | 39  |
| Black Pluge HD  | 40  |
| Geometry 178 HD | 41  |
| Geometry 240 HD | 42  |
| ISF Color Girls | 43  |
| PD Family       | 44  |
| Red Blue MTB    | 45  |
| Cone Gradiant   | 46  |
| ISF Dog         | 47  |

#### DVS HDR

##### CLIPPING & COLOR

| Name              | ID  |
| ----------------- | --- |
| Black Level 1     | 48  |
| Black Level 2     | 49  |
| White Level 1     | 50  |
| White Level 2     | 51  |
| White Level 3     | 52  |
| White 80-100      | 53  |
| HDR Mix           | 54  |
| HDR Greyscale     | 55  |
| HDR Red           | 56  |
| HDR Green         | 57  |
| HDR Blue          | 58  |
| HDR Yellow        | 59  |
| HDR Cyan          | 60  |
| HDR Magenta       | 61  |
| Multi-Cube        | 62  |
| 10 Patch Mix      | 63  |
| Greyscale 1000    | 64  |
| Greyscale 2000    | 65  |
| Greyscale 4000    | 66  |
| Greyscale 10000   | 67  |
| Color High        | 68  |
| Color Low         | 69  |
| Decoding 50%      | 70  |
| Decoding 100%     | 71  |
| Blue Filter 100%  | 72  |
| Green Filter 100% | 73  |
| Red Filter 100%   | 74  |
| Blue Filter 50%   | 75  |
| Green Filter 50%  | 76  |
| Red Filter 50%    | 77  |
| Color Flashing    | 78  |
| Dynamic Contrast  | 79  |

##### EVALUATION

| Name            | ID  |
| --------------- | --- |
| Landscape       | 80  |
| Skin Tone       | 81  |
| Skin Tone       | 82  |
| City Sunset     | 83  |
| Oceanside       | 84  |
| Pantone Skin    | 85  |
| Restaurant      | 86  |
| Indian Market   | 87  |
| Ambient 05 Nit  | 88  |
| Ambient 10 Nit  | 89  |
| Ambient 15 Nit  | 90  |
| Chroma Sub 100  | 91  |
| Chroma Sub 500  | 92  |
| Chroma Sub 1000 | 93  |
| Judder 24 FPS   | 94  |
| Judder 60 FPS   | 95  |
| M Judder 24 FPS | 96  |

##### GEOMETRY & CONVERGENCE

| Name              | ID  |
| ----------------- | --- |
| Apsect Ratio 1.78 | 97  |
| Apsect Ratio 1.85 | 98  |
| Apsect Ratio 2.00 | 99  |
| Apsect Ratio 2.35 | 100 |
| Apsect Ratio 2.40 | 101 |
| Apsect Ratio All  | 102 |
| Grid White        | 103 |
| Grid Red          | 104 |
| Grid Green        | 105 |
| Grid Blue         | 106 |
| Grid Yellow       | 107 |
| Grid Cyan         | 108 |
| Grid Magenta      | 109 |
| Dot White         | 110 |
| Dot Red           | 111 |
| Dot Green         | 112 |
| Dot Blue          | 113 |
| Dot Yellow        | 114 |
| Dot Cyan          | 115 |
| Dot Magenta       | 116 |
| Cross White       | 117 |
| Cross Red         | 118 |
| Cross Green       | 119 |
| Cross Blue        | 120 |
| Cross Yellow      | 121 |
| Cross Cyan        | 122 |
| Cross Magenta     | 123 |

##### RAMPS,GRADIENTS,ZONE PLATES

| Name            | ID  |
| --------------- | --- |
| Greyscale Steps | 124 |
| Greyscale Ramp  | 125 |
| Greyscale Mix   | 126 |
| Color Steps     | 127 |
| Color Ramp      | 128 |
| Color Ramp H&V  | 129 |
| Color Ramp Mix  | 130 |
| Color Bar Ramp  | 131 |
| Ramp Red        | 132 |
| Ramp Green      | 133 |
| Ramp Blue       | 134 |
| Ramp Yellow     | 135 |
| Ramp Cyan       | 136 |
| Ramp Magenta    | 137 |
| Zone White      | 138 |
| Zone Red        | 139 |
| Zone Green      | 140 |
| Zone Blue       | 141 |
| Zone Magenta    | 142 |
| Zone Yellow     | 143 |
| Zone Cyan       | 144 |
| Radial Grey     | 145 |
| Radial Red      | 146 |
| Radial Green    | 147 |
| Radial Blue     | 148 |
| Radial Yellow   | 149 |
| Radial Cyan     | 150 |
| Radial Magenta  | 151 |

##### RESOLUTION,ANSI,PLACEMENT

| Name            | ID  |
| --------------- | --- |
| Resolution Mix  | 152 |
| Checkerboard    | 153 |
| Horizontal 1px  | 154 |
| Horizontal 2px  | 155 |
| Horizontal 3px  | 156 |
| Vertical 1px    | 157 |
| Vertical 2px    | 158 |
| Vertical 3px    | 159 |
| Black Pixels    | 160 |
| ANSI Meter 8x8  | 161 |
| ANSI 8x8        | 162 |
| ANSI Meter 5x4  | 163 |
| ANSI M5x4 Black | 164 |
| ANSI M5x4 White | 165 |
| Meter Placement | 166 |
| Sharp & Scan    | 167 |

#### DVS Dolby Vision

##### CLIPPING & COLOR

| Name                | ID  |
| ------------------- | --- |
| Black Level 1       | 472 |
| Black Level 2       | 473 |
| White Level 1       | 474 |
| White Level 2       | 475 |
| White Level 3       | 476 |
| White 80-100        | 477 |
| Blue Filter 50%     | 478 |
| Green Filter 50%    | 479 |
| Red Filter 50%      | 480 |
| Color Clipping High | 481 |
| Color Clipping Low  | 482 |
| Color Decoding      | 483 |
| Color Flashing      | 484 |

##### EVALUATION

| Name          | ID  |
| ------------- | --- |
| Landscape     | 485 |
| Nature        | 486 |
| Skin Tone     | 487 |
| City Sunset   | 488 |
| Oceanside     | 489 |
| Pantone Skin  | 490 |
| Restaurant    | 491 |
| Indian Market | 492 |

##### RAMPS,GRADIENTS,ZONE PLATES

| Name                    | ID  |
| ----------------------- | --- |
| Greyscale Steps         | 493 |
| Greyscale Ramp          | 494 |
| Greyscale Mix           | 495 |
| Color Steps             | 496 |
| Red Radial Gradient     | 497 |
| Green Radial Gradient   | 498 |
| Blue Radial Gradient    | 499 |
| Yellow Radial Gradient  | 500 |
| Cyan Radial Gradient    | 501 |
| Magenta Radial Gradient | 502 |

##### RESOLUTION,ANSI,PLACEMENT

| Name            | ID  |
| --------------- | --- |
| ANSI Meter 8x8  | 503 |
| ANSI 8x8 Black  | 504 |
| ANSI 8x8 White  | 505 |
| ANSI Meter 5x4  | 506 |
| ANSI M5x4 Black | 507 |
| ANSI M5x4 White | 508 |
| Meter Placement | 509 |
| Sharp & Scan    | 510 |

#### DVS HLG

##### CLIPPING & COLOR

| Name                | ID  |
| ------------------- | --- |
| Black Level 1       | 511 |
| Black Level 2       | 512 |
| White Level 1       | 513 |
| White Level 2       | 514 |
| White Level 3       | 515 |
| HDR Mix             | 517 |
| HDR Greyscale       | 518 |
| HDR Red             | 519 |
| HDR Green           | 520 |
| HDR Blue            | 521 |
| HDR Yellow          | 522 |
| HDR Cyan            | 523 |
| HDR Magenta         | 524 |
| Multi-Cube          | 525 |
| 10 Patch Mix        | 526 |
| Blue Filter 100%    | 529 |
| Green Filter 100%   | 530 |
| Red Filter 100%     | 531 |
| Color Clipping High | 527 |
| Color Clipping Low  | 528 |
| Color Decoding 50%  | 532 |
| Color Decoding 100% | 533 |
| Color Flashing      | 516 |

##### EVALUATION

| Name          | ID  |
| ------------- | --- |
| Landscape     | 534 |
| Nature        | 535 |
| Skin Tone     | 536 |
| City Sunset   | 537 |
| Oceanside     | 538 |
| Pantone Skin  | 539 |
| Restaurant    | 540 |
| Indian Market | 541 |

##### RAMPS,GRADIENTS,ZONE PLATES

| Name            | ID  |
| --------------- | --- |
| Greyscale Steps | 542 |
| Greyscale Ramp  | 543 |
| Greyscale Mix   | 544 |
| Color Steps     | 545 |
| Color Ramp      | 546 |
| Color Ramp H&V  | 547 |
| Color Ramp Mix  | 548 |
| Color Bar Ramp  | 549 |
| Ramp Red        | 550 |
| Ramp Green      | 551 |
| Ramp Blue       | 552 |
| Ramp Yellow     | 553 |
| Ramp Cyan       | 554 |
| Ramp Magenta    | 555 |
| Zone White      | 556 |
| Zone Red        | 557 |
| Zone Green      | 558 |
| Zone Blue       | 559 |
| Zone Magenta    | 560 |
| Zone Yellow     | 561 |
| Zone Cyan       | 562 |
| Radial Grey     | 563 |
| Radial Red      | 564 |
| Radial Green    | 565 |
| Radial Blue     | 566 |
| Radial Yellow   | 567 |
| Radial Cyan     | 568 |
| Radial Magenta  | 569 |

##### RESOLUTION,ANSI,PLACEMENT

| Name            | ID  |
| --------------- | --- |
| ANSI Meter 8x8  | 570 |
| ANSI 8x8 Black  | 571 |
| ANSI 8x8 White  | 572 |
| ANSI Meter 5x4  | 573 |
| ANSI M5x4 Black | 574 |
| ANSI M5x4 White | 575 |
| Meter Placement | 576 |
| Sharp & Scan    | 577 |
| Resolution Mix  | 578 |

#### UHD SDR

##### CLIPPING & GAMMA

| Name              | ID  |
| ----------------- | --- |
| Target Limited    | 168 |
| Target Full       | 169 |
| Contrast Check    | 170 |
| Contrast Lines    | 171 |
| Gamma Check       | 172 |
| Gamma Lines       | 173 |
| High Clipping     | 174 |
| High Clip Red     | 175 |
| High Clip Green   | 176 |
| High Clip Blue    | 177 |
| Low Clipping      | 178 |
| Low Clip Red      | 179 |
| Low Clip Green    | 180 |
| Low Clip Blue     | 181 |
| Composite Grey    | 182 |
| Composite Red     | 183 |
| Composite Green   | 184 |
| Composite Blue    | 185 |
| Lin Step Grey     | 186 |
| Lin Step Red      | 187 |
| Lin Step Green    | 188 |
| Lin Step Blue     | 189 |
| Lin Step Magent   | 190 |
| Lin Step Yellow   | 191 |
| Lin Step Cyan     | 192 |
| Log Step Grey     | 193 |
| Log Step Red      | 194 |
| Log Step Green    | 195 |
| Log Step Blue     | 196 |
| Log Step Magent   | 197 |
| Log Step Yellow   | 198 |
| Log Step Cyan     | 199 |
| Gamma Grey        | 200 |
| Gamma Red         | 201 |
| Gamma Green       | 202 |
| Gamma Blue        | 203 |
| Gamma Lines Grey  | 204 |
| Gamma Lines Red   | 205 |
| Gamma Lines Green | 206 |
| Gamma Lines Blue  | 207 |

##### COLOR BARS & NOISE

| Name            | ID  |
| --------------- | --- |
| Color Wipe Full | 208 |
| Color Wipe Half | 209 |
| Quick Check     | 210 |
| H Bars RGB      | 211 |
| H Bars RGBCMY   | 212 |
| H Bars Shade    | 214 |
| V Bars RGB      | 215 |
| V Bars RGBCMY   | 216 |
| V Bars Layover  | 217 |
| V Bars Shade    | 218 |
| Color Noise 01  | 219 |
| Color Noise 02  | 220 |
| Color Noise 04  | 221 |
| Color Noise 08  | 222 |
| Color Noise 16  | 223 |
| Color Noise 01  | 224 |
| Color Noise 02  | 225 |
| Color Noise 04  | 226 |
| Color Noise 08  | 227 |
| Color Noise 16  | 228 |

##### COLOR CHECKER

| Name             | ID  |
| ---------------- | --- |
| HSL BlueMagenta  | 229 |
| HSL Blue         | 230 |
| HSL Cyan Blue    | 231 |
| HSL Cyan         | 232 |
| HSL Green Cyan   | 233 |
| HSL Green        | 234 |
| HSL Magenta Red  | 235 |
| HSL Magenta      | 236 |
| HSL Red          | 237 |
| HSL Yellow Green | 238 |
| HSL Yellow Red   | 239 |
| HSL Yellow       | 240 |
| HSV BlueMagenta  | 241 |
| HSV Cyan Blue    | 243 |
| HSV Cyan         | 244 |
| HSV Green Cyan   | 245 |
| HSV Green        | 246 |
| HSV Magenta Red  | 247 |
| HSV Magenta      | 248 |
| HSV Red          | 249 |
| HSV Yellow Green | 250 |
| HSV Yellow Red   | 251 |
| HSV Yellow       | 252 |
| RGB Blue 064     | 253 |
| RGB Blue 127     | 254 |
| RGB Blue 191     | 255 |
| RGB Blue 255     | 256 |
| RGB Green 064    | 257 |
| RGB Green 127    | 258 |
| RGB Green 191    | 259 |
| RGB Green 255    | 260 |
| RGB Red 064      | 261 |
| RGB Red 127      | 262 |
| RGB Red 191      | 263 |
| RGB Red 255      | 264 |

##### GEOMETRY AND RESOLUTION

| Name            | ID  |
| --------------- | --- |
| H Convergence   | 265 |
| V Convergence   | 266 |
| H Length        | 267 |
| V Length        | 268 |
| Overscan        | 269 |
| BW Evaluation   | 270 |
| BW Evaluation 2 | 271 |
| H Wedge         | 272 |
| Star Burst      | 273 |
| V Wedge         | 274 |
| H Multiburst    | 275 |
| V Multiburst    | 276 |
| Checkers 02     | 277 |
| Checkers 04     | 278 |
| Checkers 08     | 279 |
| Checkers 16     | 280 |
| Checkers 32     | 281 |
| Checkers Log    | 282 |
| Many Circles    | 283 |
| Center Circle   | 284 |
| Many Squares    | 285 |
| Grid            | 286 |
| H Lines 02      | 287 |
| H Lines 04      | 288 |
| H Lines 08      | 289 |
| H Lines Log     | 290 |
| V Lines 02      | 291 |
| V Lines 04      | 292 |
| V Lines 08      | 293 |
| V Lines Log     | 294 |
| Points 02       | 295 |
| Points 04       | 296 |
| Points 08       | 297 |
| Points 16       | 298 |
| Points 32       | 299 |
| Squares 02      | 300 |
| Squares 04      | 301 |
| Squares 08      | 302 |
| Squares 16      | 303 |
| Squares 32      | 304 |

##### RAMPS

| Name          | ID  |
| ------------- | --- |
| Color Patch   | 305 |
| Triangle      | 306 |
| Wireframe     | 307 |
| Full Red      | 308 |
| Full Green    | 309 |
| Full Blue     | 310 |
| Full Magenta  | 311 |
| Full Yellow   | 312 |
| Full Cyan     | 313 |
| Full Grey     | 314 |
| Half Red      | 315 |
| Half Green    | 316 |
| Half Blue     | 317 |
| Half Magenta  | 318 |
| Half Yellow   | 319 |
| Half Cyan     | 320 |
| HSL Sat 0.00  | 321 |
| HSL Hue 0.00  | 322 |
| HSL Hue 0.33  | 323 |
| HSL Hue 0.66  | 324 |
| HSL Lev 0.25  | 325 |
| HSL Lev 0.50  | 326 |
| HSL Lev 0.75  | 327 |
| HSV Sat 0.00  | 328 |
| HSV Sat 0.50  | 329 |
| HSV Sat 1.00  | 330 |
| HSV Hue 0.00  | 331 |
| HSV Hue 0.33  | 332 |
| HSV Hue 0.66  | 333 |
| HSV Sat 0.50  | 334 |
| HSV Sat 1.00  | 335 |
| HSV Sat 0.00  | 336 |
| HSV Sat 0.50  | 337 |
| HSV Sat 1.00  | 338 |
| RGB Green 000 | 339 |
| RGB Green 127 | 340 |
| RGB Green 255 | 341 |
| RGB Blue 000  | 342 |
| RGB Blue 127  | 343 |
| RGB Blue 255  | 344 |
| RGB Red 000   | 345 |
| RGB Red 127   | 346 |
| RGB Red 255   | 347 |

#### Dolby Vision

| Name              | ID  |
| ----------------- | --- |
| Dolby Vision UHD  | 425 |
| CornerBox_UHD     | 426 |
| Checker_UHD       | 427 |
| Steps_UHD_L255rm1 | 428 |
| Steps_UHD_L255rm2 | 429 |
| Steps_UHD_noL255  | 430 |
| Ramp_UHD_L255rm1  | 431 |
| Ramp_UHD_L255rm2  | 432 |
| Ramp_UHD_noL255   | 433 |
| Dolby Vision FHD  | 434 |
| CornerBox_FHD     | 435 |
| Checker_FHD       | 436 |
| Steps_FHD_L255rm1 | 437 |
| Steps_FHD_L255rm2 | 438 |
| Steps_FHD_noL255  | 439 |
| Ramp_FHD_L255rm1  | 440 |
| Ramp_FHD_L255rm2  | 441 |
| Ramp_FHD_noL255   | 442 |

#### HD

| Name                | ID  |
| ------------------- | --- |
| High Clipping       | 350 |
| Low Clipping        | 351 |
| Color Noise 01      | 352 |
| Color Noise 02      | 353 |
| Color Noise 04      | 354 |
| Color Noise 08      | 355 |
| Triangle            | 356 |
| Color Wipe Full     | 357 |
| Color Wipe Half     | 358 |
| Composite           | 359 |
| H Multiburst        | 360 |
| V Multiburst        | 361 |
| Checkers 02         | 362 |
| Checkers 04         | 363 |
| Checkers 08         | 364 |
| Checkers 16         | 365 |
| Checkers 32         | 366 |
| Checkers Log        | 367 |
| Many Circles        | 368 |
| Center Circle       | 369 |
| Many Squares        | 370 |
| Grid                | 371 |
| H Lines 02          | 372 |
| H Lines 04          | 373 |
| H Lines 08          | 374 |
| H Lines Log         | 375 |
| V Lines 02          | 376 |
| V Lines 04          | 377 |
| V Lines 08          | 378 |
| Geometry Points 02  | 380 |
| Geometry Points 04  | 381 |
| Geometry Points 08  | 382 |
| Geometry Points 16  | 383 |
| Geometry Points 32  | 384 |
| Geometry Squares 04 | 385 |
| Geometry Squares 08 | 386 |
| Geometry Squares 16 | 387 |
| Geometry Squares 32 | 388 |
| H Length            | 389 |
| V Length            | 390 |
| Overscan            | 391 |
| BW Evaluation 2     | 392 |
| BW Evaluation       | 393 |
| H Wedge             | 394 |
| Star Burst          | 395 |
| V Wedge             | 396 |
| RGB Text            | 397 |

#### PVA

| Name                        | ID  |
| --------------------------- | --- |
| (BT709) White_Clipping      | 443 |
| (BT709) Black_Clipping      | 444 |
| (BT709) APL_W_B_Clipping    | 445 |
| (BT709) Color_Clipping      | 446 |
| (BT709) Sharpness_Overscan  | 447 |
| (BT709) Alignment           | 448 |
| (BT709) Multi_Skin_Tone     | 449 |
| (BT709) Restaurant_Scene    | 450 |
| (BT709) Skin_Tone           | 451 |
| (BT2020) White_Clipping     | 579 |
| (BT2020) Black_Clipping     | 580 |
| (BT2020) APL_W_B_Clipping   | 581 |
| (BT2020) Color_Clipping     | 582 |
| (BT2020) Sharpness_Overscan | 583 |
| (BT2020) Alignment          | 584 |
| (BT2020) Multi_Skin_Tone    | 585 |
| (BT2020) Restaurant_Scene   | 586 |
| (BT2020) Skin_Tone          | 587 |

#### SPE

| Name                         | ID  |
| ---------------------------- | --- |
| (4:2:0) Girl                 | 452 |
| (4:2:0) Women                | 453 |
| (4:2:0) Girl HDR & SDR       | 454 |
| (4:4:4 Full) Girl            | 455 |
| (4:4:4 Full) Women           | 588 |
| (4:4:4 Full) Girl HDR & SDR  | 589 |
| (4:4:4 Limit) Girl           | 590 |
| (4:4:4 Limit) Women          | 591 |
| (4:4:4 Limit) Girl HDR & SDR | 590 |

#### SPEARS & MUNSIL

| Name               | ID  |
| ------------------ | --- |
| Bias_Light_10%     | 456 |
| Bias_Light_15%     | 457 |
| Framing            | 458 |
| Hammock_24p        | 459 |
| Hammock_30p        | 460 |
| Hammock_260i       | 461 |
| Mixed_video_H_60i  | 462 |
| Mixed_Video_V_60i  | 463 |
| ColorTint_01_Red   | 464 |
| ColorTint_01_Green | 465 |
| ColorTint_01_Blue  | 466 |
| Jaggies_Full_60i   | 467 |
| Ship1_60i          | 468 |
| Ship2_60i          | 469 |
| Ship3_60i          | 470 |

#### USER (STILLS)

| Name             | ID  |
| ---------------- | --- |
| User Pattern1 () | 398 |
| User Pattern2 () | 399 |
| User Pattern3 () | 400 |
| User Pattern4 () | 401 |
| User Pattern5 () | 402 |
| User Pattern6 () | 403 |

#### SHORTCUTS

| Name         | ID  |
| ------------ | --- |
| SHORTCUTS 1  | 471 |
| SHORTCUTS 2  | 472 |
| SHORTCUTS 3  | 473 |
| SHORTCUTS 4  | 474 |
| SHORTCUTS 5  | 475 |
| SHORTCUTS 6  | 476 |
| SHORTCUTS 7  | 477 |
| SHORTCUTS 8  | 478 |
| SHORTCUTS 9  | 495 |
| SHORTCUTS 10 | 480 |
| SHORTCUTS 11 | 481 |
| SHORTCUTS 12 | 482 |
| SHORTCUTS 13 | 483 |
| SHORTCUTS 14 | 484 |

### COLOR SPACE

| Name             | ID  |
| ---------------- | --- |
| RGB(0-255)       | 0   |
| RGB(16-235)      | 1   |
| YC 4:4:4(16-235) | 2   |
| YC 4:2:2(16-235) | 3   |
| YC 4:2:0(16-235) | 4   |

### BT 2020

| Name    | ID  |
| ------- | --- |
| ENABLE  | 1   |
| DISABLE | 0   |

### COLOR DEPTH

| Name  | ID  |
| ----- | --- |
| 8Bit  | 0   |
| 10Bit | 1   |
| 12Bit | 2   |
| 16Bit | 3   |

### HDCP

| Name      | ID  |
| --------- | --- |
| HDCP OFF  | 0   |
| HDCP 1.4  | 1   |
| HDCP 2.2  | 2   |
| HDCP AUTO | 3   |

### HDMI/DVI

| Name | ID  |
| ---- | --- |
| DVI  | 0   |
| HDMI | 1   |
| AUTO | 2   |

### HDR

| Name         | ID  |
| ------------ | --- |
| HDR OFF(SDR) | 0   |
| HDR-10       | 1   |
| HLG          | 2   |
| HDR CUSTOM 1 | 3   |
| HDR CUSTOM 2 | 4   |
| HDR CUSTOM 3 | 5   |
| HDR CUSTOM 4 | 6   |
| HDR CUSTOM 5 | 7   |
| HDR CUSTOM 6 | 8   |
| HDR CUSTOM 7 | 9   |
| HDR CUSTOM 8 | 10  |

## Video Tests

| Name                               | ID  |
| ---------------------------------- | --- |
| Spicey Pixels Chongqing Day        | 404 |
| Spicey Pixels Chongqing Night      | 405 |
| Spicey Pixels Chongqing Lights     | 406 |
| Spicey Pixels Chongqing Cars       | 407 |
| Spicey Pixels Chongqing Cars2      | 408 |
| Spicey Pixels London Yogurt        | 411 |
| Spicey Pixels London River         | 412 |
| Spicey Pixels London Sidewalk      | 413 |
| Spicey Pixels London Busses        | 414 |
| Spicey Pixels London cafe          | 415 |
| Spicey Pixels Mukilteo Street      | 416 |
| Spicey Pixels Mukilteo Loading     | 417 |
| Spicey Pixels Carnival Wheel       | 418 |
| Spicey Pixels Carnival Ride        | 419 |
| Spicey Pixels Carnival night       | 420 |
| Spicey Pixels Carnival Balloon Pop | 421 |
| Spicey Pixels Tiger Mountain 120   | 422 |
| Spicey Pixels Biker 120            | 423 |
| SPE Test Video                     | 424 |
| User Video Clip 1                  | 409 |
| User Video Clip 2                  | 410 |
| Automation Testing Clip            | 471 |

## Audio Generator

### PCM AUDIO

#### Audio Sampling Rate

| Name  | ID  |
| ----- | --- |
| 32K   | 0   |
| 44.1K | 1   |
| 48K   | 2   |
| 88K   | 3   |
| 96K   | 4   |
| 176k  | 5   |
| 192k  | 6   |

#### Audio Bit Depth

| Name  | ID  |
| ----- | --- |
| 16Bit | 0   |
| 20Bit | 1   |
| 24Bit | 2   |

#### Sinewave Tone

| Name                 | ID  |
| -------------------- | --- |
| SINEWAVE TONE(100Hz) | 0   |
| SINEWAVE TONE(200Hz) | 1   |
| SINEWAVE TONE(300Hz) | 2   |
| SINEWAVE TONE(400Hz) | 3   |
| SINEWAVE TONE(500Hz) | 4   |
| SINEWAVE TONE(600Hz) | 5   |
| SINEWAVE TONE(700Hz) | 6   |
| SINEWAVE TONE(800Hz) | 7   |
| SINEWAVE TONE(900Hz) | 8   |
| SINEWAVE TONE(1KHz)  | 9   |
| SINEWAVE TONE(2KHz)  | 10  |
| SINEWAVE TONE(3KHz)  | 11  |
| SINEWAVE TONE(4KHz)  | 12  |
| SINEWAVE TONE(5KHz)  | 13  |

#### Audio Volume

| Name  | ID  |
| ----- | --- |
| -60db | 0   |
| -54db | 1   |
| -48db | 2   |
| -42db | 3   |
| -36db | 4   |
| -30db | 5   |
| -24db | 6   |
| -18db | 7   |
| -12   | 8   |
| -6db  | 9   |
| 0db   | 10  |

#### Audio Channel Config

| Name                               | ID  |
| ---------------------------------- | --- |
| 2CH (FR_FL)                        | 0   |
| 2.1CH (LFE_FR_FL)                  | 1   |
| 3CH (FC_FR_FL)                     | 2   |
| 3.1CH (FC_LFE_FR_FL)               | 3   |
| 3CH (RC_FR_FL)                     | 4   |
| 3.1CH (RC_LFE_FR_FL)               | 5   |
| 4CH (RC_LFE_FR_FL)                 | 6   |
| 4.1CH (RC_FC_LFE_FR_FL)            | 7   |
| 4CH (RR_RL_FR_FL)                  | 8   |
| 4.1CH (RR_RL_LFE_FR_FL)            | 9   |
| 5CH (RR_RS_FC_FR_FL)               | 10  |
| 5.1CH (RR_RL_FC_LFE_FR_FL)         | 11  |
| 5CH (RC_RR_RL_FR_FL)               | 12  |
| 5.1CH (RC_RR_RL_LFE_FR_FL)         | 13  |
| 6CH (RC_RR_RL_FC_FR_FL)            | 14  |
| 6.1CH (RC_RR_RL_FC_LFE_FR_FL)      | 15  |
| 6CH (RRC_RLC_RR_RL_FR_FL)          | 16  |
| 6.1CH (RRC_RLC_RR_RL_LFE_FR_FL)    | 17  |
| 7CH (RRC_RLC_RR_RL_FC_FR_FL)       | 18  |
| 7.1CH (RRC_RLC_RR_RL_FC_LFE_FR_FL) | 19  |
| 4CH (FRC_FLC_FR_FL)                | 20  |
| 4.1CH (FRC_FLC_LFE_FR_FL)          | 21  |
| 5CH (FRC_FLC_FC_FR_FL)             | 22  |
| 5.1CH (FRC_FLC_FC_LFE_FR_FL)       | 23  |
| 5CH (FRC_FLC_RC_FR_FL)             | 24  |
| 5.1CH (FRC_FLC_RC_FC_FR_FL)        | 25  |
| 6CH (FRC_FLC_RC_FC_FR_FL)          | 26  |
| 6.1CH (FRC_FLC_RC_FC_LFE_FR_FL)    | 27  |
| 6CH (FRC_FLC_RR_RL_FR_FL)          | 28  |
| 6.1CH (FRC_FLC_RR_RL_LFE_FR_FL)    | 29  |
| 7CH (FRC_FLC_RR_RL_FC_FR_FL)       | 30  |
| 7.1CH (FRC_FLC_RR_RL_FC_LFE_FR_FL) | 31  |

### DOLBY AUDIO GENERATOR

#### DOLBY Digital

| Name                        | ID  |
| --------------------------- | --- |
| Dolby Digital-32KHz-2.0Ch   | 2   |
| Dolby Digital-32KHz-5.1Ch   | 3   |
| Dolby Digital-44.1KHz-2.0Ch | 4   |
| Dolby Digital-44.1KHz-5.1Ch | 5   |
| Dolby Digital-48KHz-2.0Ch   | 6   |
| Dolby Digital-48KHz-5.1Ch   | 7   |

#### DOLBY Digital Plus

| Name                           | ID  |
| ------------------------------ | --- |
| Dolby Digital Plus-48KHz-2.0Ch | 8   |
| Dolby Digital Plus-48KHz-5.1Ch | 9   |
| Dolby Digital Plus-48KHz-7.1Ch | 10  |
| Dolby Digital Plus-48KHz-Atmos | 11  |

#### DOLBY MAT

| Name                                            | ID  |
| ----------------------------------------------- | --- |
| Dolby MAT(PCM)-44.1KHz-2.0Ch                    | 12  |
| Dolby MAT(PCM)-44.1KHz-5.1Ch                    | 13  |
| Dolby MAT(PCM)-44.1KHz-7.1Ch                    | 14  |
| Dolby MAT(PCM)-48KHz-2.0Ch                      | 15  |
| Dolby MAT(PCM)-48KHz-5.1Ch                      | 16  |
| Dolby MAT(PCM)-48KHz-7.1Ch                      | 17  |
| Dolby MAT(PCM object audio)-44.1KHz-Dolby Atmos | 18  |
| Dolby MAT(PCM object audio)-48KHz-Dolby Atmos   | 19  |

#### DOLBY MAT (DOLBY TrueHD)

| Name                                                  | ID  |
| ----------------------------------------------------- | --- |
| Dolby MAT(Dolby TrueHD)-48KHz-2.0Ch                   | 20  |
| Dolby MAT(Dolby TrueHD)-48KHz-5.1Ch                   | 21  |
| Dolby MAT(Dolby TrueHD)-48KHz-7.1Ch                   | 22  |
| Dolby MAT(Dolby TrueHD)-96KHz-2.0Ch                   | 23  |
| Dolby MAT(Dolby TrueHD)-96KHz-5.1Ch                   | 24  |
| Dolby MAT(Dolby TrueHD)-96KHz-7.1Ch                   | 25  |
| Dolby MAT(Dolby TrueHD)-192KHz-2.0Ch                  | 26  |
| Dolby MAT(Dolby TrueHD)-192KHz-5.1Ch                  | 27  |
| Dolby MAT(Dolby TrueHD)Object Based 48KHz-Dolby Atmos | 28  |

#### My Streams

| Name          | ID  |
| ------------- | --- |
| MY STREAM1 () | 288 |
| MY STREAM2 () | 308 |
| MY STREAM3 () | 328 |
| MY STREAM4 () | 348 |
| MY STREAM5 () | 368 |
| MY STREAM6 () | 388 |

### EXT.ANALOG L/R INPUT

| Name   | ID  |
| ------ | --- |
| ENABLE | 0   |

### DTS AUDIO GENERATOR

#### DTS Digital Surround

| Name                               | ID  |
| ---------------------------------- | --- |
| DTS Digital Surround-48KHz-2.0Ch   | 562 |
| DTS Digital Surround-48KHz-5.1Ch   | 563 |
| DTS Digital Surround-48.1KHz-6.1Ch | 564 |
| DTS Digital Surround-44.1KHz-5.1Ch | 565 |
| DTS Digital Surround-96KHz-5.1Ch   | 566 |

#### DTS-HD Higher Resolution

| Name                                 | ID  |
| ------------------------------------ | --- |
| DTS-HD High Resolution-48KHz-5.1Ch   | 567 |
| DTS-HD High Resolution-48KHz-7.1Ch   | 568 |
| DTS-HD High Resolution-96KHz-7.1Ch   | 569 |
| DTS-HD High Resolution-88.2KHz-7.1Ch | 570 |

#### DTS-HD Master Audio

| Name                             | ID  |
| -------------------------------- | --- |
| DTS-HD Master Audio-48KHz-5.1Ch  | 571 |
| DTS-HD Master Audio-48KHz-7.1Ch  | 572 |
| DTS-HD Master Audio-192KHz-2.0Ch | 573 |
| DTS-HD Master Audio-192KHz-7.1Ch | 574 |

#### DTS: X

| Name                             | ID  |
| -------------------------------- | --- |
| DTS:X-48KHz-7.1.4Ch              | 575 |
| DTS:X-48KHz-5.1.4Ch              | 576 |
| DTS:X Master Audio-48KHz-7.1.4Ch | 577 |
| DTS:X Master Audio-96KHz-7.1.4Ch | 578 |
| DTS:X(32 Objects)                | 579 |

#### DTS Express

| Name                         | ID  |
| ---------------------------- | --- |
| DTS Low Bit Rate-48KHz-5.1Ch | 580 |

#### MY STREAMS

| Name          | ID  |
| ------------- | --- |
| MY STREAM1 () | 581 |
| MY STREAM2 () | 601 |
| MY STREAM3 () | 621 |
| MY STREAM4 () | 641 |
| MY STREAM5 () | 661 |
| MY STREAM6 () | 681 |

## Audio Tests

### SYNC-LATENCY TEST

#### VIDEO SETTINGS

| Name              | ID  |
| ----------------- | --- |
| 3840X2160 30HZ    | 0   |
| 3840X2160 29.97HZ | 1   |
| 3840X2160 25HZ    | 2   |
| 3840X2160 24HZ    | 3   |
| 3840X2160 60HZ    | 4   |
| 3840X2160 59.94HZ | 5   |
| 3840X2160 50HZ    | 6   |
| 1080P 30HZ        | 7   |
| 1080P 29.97HZ     | 8   |
| 1080P 25HZ        | 9   |
| 1080P 24HZ        | 10  |
| 1080P 60HZ        | 11  |
| 1080P 59.94HZ     | 12  |
| 1080P 50HZ        | 13  |
| 1080P 120HZ       | 14  |
| 1080P 119.88HZ    | 15  |

#### DOLBY VISION SETTINGS

| Name                    | ID  |
| ----------------------- | --- |
| DOLBY VISION OFF        | 0   |
| DOLBY VISION SINK-LED   | 1   |
| DOLBY VISION SOURCE-LED | 2   |

#### AUDIO STREAM ADJUST

| Name                          | ID   |
| ----------------------------- | ---- |
| Adjust audio -500ms to +500ms | None |

#### AV SENSORS FUNCTIONAL TEST

| Name                              | ID  |
| --------------------------------- | --- |
| Mic Functional Test - READ STATUS | 0   |
| Visual Sensor Test - READ STATUS  | 1   |

#### ARM AV LATENCY

#### ARM ARC LATENCY

#### ARM eARC LATENCY

### SOURCE-SPEAKER TEST

| Name               | ID  |
| ------------------ | --- |
| SPEAKER ALLOCATION | 528 |
| WHITE NOISE        | 538 |
| SWEEP AUDIO        | 548 |

## EDID eARC CDS

### SINK DEVICE EDID INFO

| Name      | ID   |
| --------- | ---- |
| READ EDID | 1    |
| SAVE EDID | None |
| OPEN EDID | None |

### eARC/ARC AUDIO INFO

### ARC HPD CTL

| Name              | ID  |
| ----------------- | --- |
| ASSERT HPD(HIGH)  | 1   |
| DEASSERT HPD(LOW) | 0   |

### ARC PHYSICAL HPD CTL

| Name              | ID  |
| ----------------- | --- |
| ASSERT HPD(HIGH)  | 1   |
| DEASSERT HPD(LOW) | 0   |

### eARC HPD bit CTL

| Name                   | ID  |
| ---------------------- | --- |
| SET HDMI_HPD bit(=1)   | 1   |
| CLERA HDMI_HPD bit(=0) | 0   |

### HDMI +5V POWER CTL

| Name                | ID  |
| ------------------- | --- |
| SET HDMI TX +5V ON  | 1   |
| SET HDMI TX +5V OFF | 0   |

### eARC TX LATENCY

| Name                              | ID   |
| --------------------------------- | ---- |
| ERX_LATENCY_REQ(To eARC RX) id=ms | None |

### eARC RX LATENCY

| Name                              | ID   |
| --------------------------------- | ---- |
| ERX_LATENCY_REQ(To eARC TX) id=ms | None |

### Send CEC Command

## System Setup

### IP MANAGEMENT

### ARC/eARC OUT SETUP

| Name             | ID  |
| ---------------- | --- |
| DISABLE ARC/eARC | 0   |
| ENABLE eARC      | 1   |
| ENABLE ARC       | 2   |

| Name   | ID  |
| ------ | --- |
| VITALS | 1   |

### FAN CONTROL

| Name         | ID  |
| ------------ | --- |
| OFF          | 0   |
| LOW SPEED    | 1   |
| MIDDLE SPEED | 2   |
| HIGH SPEED   | 3   |

### RESET ALL SETTINGS

| Tools | None |

### UPDATE FIRMWARE

#### Update Firmware

#### reboot
