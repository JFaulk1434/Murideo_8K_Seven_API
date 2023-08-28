"""Decoder ring for the WebUI on the murideo"""

Murideo_WebUI = {  # Master Dictionary for WebUI of Murideo 8K Seven Genderator
    "video_generator": {
        "timing": {
            "function": "sendsingle",  # Function needed to send the command ex: SENDSINGLE||97,110
            "category_type": 97,  # ID For the category in this case it's 97=Timing
            "8k": {
                "7680x4320@30": {
                    "id": 110,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "7680x4320 30Hz",  # The actual Button text
                },
                "7680x4320@29.97": {
                    "id": 111,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "7680x4320 29.97Hz",  # The actual Button text
                },
                "7680x4320@25": {
                    "id": 112,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "7680x4320 25Hz",  # The actual Button text
                },
                "7680x4320@24": {
                    "id": 113,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "7680x4320 24Hz",  # The actual Button text
                },
                "7680x4320@23.98": {
                    "id": 114,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 23.98,  # Refresh Rate
                    "tag": "7680x4320 23.98Hz",  # The actual Button text
                },
                "7680x4320@60": {
                    "id": 115,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "7680x4320 60Hz",  # The actual Button text
                },
                "7680x4320@59.94": {
                    "id": 116,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "7680x4320 59.94Hz",  # The actual Button text
                },
                "7680x4320@50": {
                    "id": 117,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "7680x4320 50Hz",  # The actual Button text
                },
                "7680x4320@48": {
                    "id": 118,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 48,  # Refresh Rate
                    "tag": "7680x4320 48Hz",  # The actual Button text
                },
                "7680x4320@47.95": {
                    "id": 119,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 47.95,  # Refresh Rate
                    "tag": "7680x4320 47.95Hz",  # The actual Button text
                },
            },
            "uhd": {
                "3840x2160@30": {
                    "id": 28,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "3840x2160 30Hz",  # The actual Button text
                },
                "3840x2160@29.97": {
                    "id": 29,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "3840x2160 29.97Hz",  # The actual Button text
                },
                "3840x2160@25": {
                    "id": 30,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "3840x2160 25Hz",  # The actual Button text
                },
                "3840x2160@24": {
                    "id": 31,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "3840x2160 24Hz",  # The actual Button text
                },
                "3840x2160@23.98": {
                    "id": 32,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 23.98,  # Refresh Rate
                    "tag": "3840x2160 23.98Hz",  # The actual Button text
                },
                "3840x2160@60": {
                    "id": 34,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "3840x2160 60Hz",  # The actual Button text
                },
                "3840x2160@59.94": {
                    "id": 35,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "3840x2160 59.94Hz",  # The actual Button text
                },
                "3840x2160@50": {
                    "id": 36,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "3840x2160 50Hz",  # The actual Button text
                },
                "3840x2160@48": {
                    "id": 103,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 48,  # Refresh Rate
                    "tag": "3840x2160 48Hz",  # The actual Button text
                },
                "3840x2160@47.95": {
                    "id": 104,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 47.95,  # Refresh Rate
                    "tag": "3840x2160 47.95Hz",  # The actual Button text
                },
                "3840x2160@100": {
                    "id": 107,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 100,  # Refresh Rate
                    "tag": "3840x2160 100Hz",  # The actual Button text
                },
                "3840x2160@120": {
                    "id": 108,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 120,  # Refresh Rate
                    "tag": "3840x2160 120Hz",  # The actual Button text
                },
                "3840x2160@119.88": {
                    "id": 109,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 119.88,  # Refresh Rate
                    "tag": "3840x2160 119.88Hz",  # The actual Button text
                },
            },
            "4k-dci": {
                "4096x2160@30": {
                    "id": 53,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "4096x2160 30Hz",  # The actual Button text
                },
                "4096x2160@29.97": {
                    "id": 54,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "4096x2160 29.97Hz",  # The actual Button text
                },
                "4096x2160@25": {
                    "id": 55,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "4096x2160 25Hz",  # The actual Button text
                },
                "4096x2160@24": {
                    "id": 44,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "4096x2160 24Hz",  # The actual Button text
                },
                "4096x2160@23.976": {
                    "id": 56,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "4096x2160 23.976Hz",  # The actual Button text
                },
                "4096x2160@60": {
                    "id": 57,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "4096x2160 60Hz",  # The actual Button text
                },
                "4096x2160@59.94": {
                    "id": 58,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "4096x2160 59.94Hz",  # The actual Button text
                },
                "4096x2160@50": {
                    "id": 59,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "4096x2160 50Hz",  # The actual Button text
                },
                "4096x2160@48": {
                    "id": 105,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 48,  # Refresh Rate
                    "tag": "4096x2160 48Hz",  # The actual Button text
                },
                "4096x2160@47.95": {
                    "id": 106,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 47.95,  # Refresh Rate
                    "tag": "4096x2160 47.95Hz",  # The actual Button text
                },
            },
            "2k-dci": {
                "2048x1080@30": {
                    "id": 73,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "2048x1080 30Hz",  # The actual Button text
                },
                "2048x1080@29.97": {
                    "id": 74,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "2048x1080 29.97Hz",  # The actual Button text
                },
                "2048x1080@25": {
                    "id": 75,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "2048x1080 25Hz",  # The actual Button text
                },
                "2048x1080@24": {
                    "id": 76,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "2048x1080 24Hz",  # The actual Button text
                },
                "2048x1080@23.976": {
                    "id": 77,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "2048x1080 23.976Hz",  # The actual Button text
                },
                "2048x1080@60": {
                    "id": 78,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "2048x1080 60Hz",  # The actual Button text
                },
                "2048x1080@59.94": {
                    "id": 79,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "2048x1080 59.94Hz",  # The actual Button text
                },
                "2048x1080@50": {
                    "id": 80,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "2048x1080 50Hz",  # The actual Button text
                },
            },
            "hd": {
                "1280x720p@60": {
                    "id": 12,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "720P 60Hz",  # The actual Button text
                },
                "1280x720p@59.94": {
                    "id": 13,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "720P 59.94Hz",  # The actual Button text
                },
                "1920x1080i@60": {
                    "id": 14,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "1080i 60Hz",  # The actual Button text
                },
                "1920x1080i@59.94": {
                    "id": 15,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "1080i 59.94Hz",  # The actual Button text
                },
                "1920x1080p@30": {
                    "id": 16,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "1080p 30Hz",  # The actual Button text
                },
                "1920x1080p@29.97": {
                    "id": 17,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "1080p 29.97Hz",  # The actual Button text
                },
                "1920x1080p@24": {
                    "id": 18,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "1080p 24Hz",  # The actual Button text
                },
                "1920x1080p@23.976": {
                    "id": 19,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "1080p 23.976Hz",  # The actual Button text
                },
                "1920x1080p@60": {
                    "id": 20,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "1080p 60Hz",  # The actual Button text
                },
                "1920x1080p@59.94": {
                    "id": 21,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "1080p 59.94Hz",  # The actual Button text
                },
                "1280x720p@50": {
                    "id": 24,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "720P 50Hz",  # The actual Button text
                },
                "1920x1080i@50": {
                    "id": 25,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "1080i 50Hz",  # The actual Button text
                },
                "1920x1080p@25": {
                    "id": 26,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "1080p 25Hz",  # The actual Button text
                },
                "1920x1080p@50": {
                    "id": 27,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "1080p 50Hz",  # The actual Button text
                },
                "1920x1080p@120": {
                    "id": 81,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 120,  # Refresh Rate
                    "tag": "1080p 120Hz",  # The actual Button text
                },
                "1920x1080p@119.88": {
                    "id": 82,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 119.88,  # Refresh Rate
                    "tag": "1080p 119.88Hz",  # The actual Button text
                },
                "1920x1080p@100": {
                    "id": 102,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 100,  # Refresh Rate
                    "tag": "1080p 100Hz",  # The actual Button text
                },
            },
            "sd": {
                "720x480i@59.94": {
                    "id": 10,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 480,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "480i 59.94Hz",  # The actual Button text
                },
                "720x480p@59.94": {
                    "id": 11,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 480,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "480p 59.94Hz",  # The actual Button text
                },
                "720x576i@50": {
                    "id": 22,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 576,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "576i 50Hz",  # The actual Button text
                },
                "720x576p@50": {
                    "id": 23,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 576,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "576p 50Hz",  # The actual Button text
                },
            },
            "vesa": {
                "640x480@60": {
                    "id": 0,  # command to be called for this resolution
                    "h_rez": 640,  # Horizontal Pixels
                    "v_rez": 480,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "VGA 640x480",  # The actual Button text
                },
                "800x600@60": {
                    "id": 1,  # command to be called for this resolution
                    "h_rez": 800,  # Horizontal Pixels
                    "v_rez": 600,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SVGA 800x600",  # The actual Button text
                },
                "1024x768@60": {
                    "id": 2,  # command to be called for this resolution
                    "h_rez": 1024,  # Horizontal Pixels
                    "v_rez": 768,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "XGA 1024x768",  # The actual Button text
                },
                "1152x864@60": {
                    "id": 72,  # command to be called for this resolution
                    "h_rez": 1152,  # Horizontal Pixels
                    "v_rez": 864,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "XGA+ 1152x864",  # The actual Button text
                },
                "1360x768@60": {
                    "id": 4,  # command to be called for this resolution
                    "h_rez": 1360,  # Horizontal Pixels
                    "v_rez": 768,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "HD 1360x768",  # The actual Button text
                },
                "1280x768@60": {
                    "id": 3,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 768,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "HD 1280x768",  # The actual Button text
                },
                "1280x960@60": {
                    "id": 5,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 896064,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SXGA 1280x960",  # The actual Button text
                },
                "1400x1050@60": {
                    "id": 7,  # command to be called for this resolution
                    "h_rez": 1400,  # Horizontal Pixels
                    "v_rez": 1050,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SXGA+ 1400x1050",  # The actual Button text
                },
                "1440x900@60": {
                    "id": 69,  # command to be called for this resolution
                    "h_rez": 1440,  # Horizontal Pixels
                    "v_rez": 60,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WXGA+ 1440x900",  # The actual Button text
                },
                "1600x900@60": {
                    "id": 70,  # command to be called for this resolution
                    "h_rez": 1600,  # Horizontal Pixels
                    "v_rez": 900,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "HD+ 1600x900",  # The actual Button text
                },
                "1600x1200@60": {
                    "id": 8,  # command to be called for this resolution
                    "h_rez": 1600,  # Horizontal Pixels
                    "v_rez": 1200,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UXGA 1600x1200",  # The actual Button text
                },
                "1920x1200@60": {
                    "id": 9,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1200,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WUXGA 1920x1200",  # The actual Button text
                },
                "1152x900@60": {
                    "id": 83,  # command to be called for this resolution
                    "h_rez": 1152,  # Horizontal Pixels
                    "v_rez": 900,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "XGA+ 1152x900",  # The actual Button text
                },
                "1280x800@60": {
                    "id": 84,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 800,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WXGA 1280x800",  # The actual Button text
                },
                "1280x1050@60": {
                    "id": 85,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 1050,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SXGA 1280x1050",  # The actual Button text
                },
                "1920x1280@60": {
                    "id": 86,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1280,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 1920x1280",  # The actual Button text
                },
                "1920x1440@60": {
                    "id": 87,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 1920x1440",  # The actual Button text
                },
                "2048x1152@60": {
                    "id": 88,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1152,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QWXGA 2048x1152",  # The actual Button text
                },
                "2048x1536@60": {
                    "id": 89,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1536,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QXGA 2048x1536",  # The actual Button text
                },
                "2160x1440@60": {
                    "id": 90,  # command to be called for this resolution
                    "h_rez": 2160,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 2160x1440",  # The actual Button text
                },
                "2560x1080@60": {
                    "id": 91,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 2560x1080",  # The actual Button text
                },
                "2560x1440@60": {
                    "id": 92,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QHD 2560x1440",  # The actual Button text
                },
                "2560x1600@60": {
                    "id": 93,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 1600,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WQXGA 2560x1600",  # The actual Button text
                },
                "2560x2048@60": {
                    "id": 94,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 2048,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QSXGA 2560x2048",  # The actual Button text
                },
                "2880x1800@60": {
                    "id": 95,  # command to be called for this resolution
                    "h_rez": 2880,  # Horizontal Pixels
                    "v_rez": 1800,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QWXGA+ 2880x1800",  # The actual Button text
                },
                "2960x1440@60": {
                    "id": 96,  # command to be called for this resolution
                    "h_rez": 2960,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "GAL 2960x1440",  # The actual Button text
                },
                "3000x2000@60": {
                    "id": 97,  # command to be called for this resolution
                    "h_rez": 3000,  # Horizontal Pixels
                    "v_rez": 2000,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SUR 3000x2000",  # The actual Button text
                },
                "3200x2048@60": {
                    "id": 98,  # command to be called for this resolution
                    "h_rez": 3200,  # Horizontal Pixels
                    "v_rez": 2048,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WQSXGA 3200x2048",  # The actual Button text
                },
                "3440x1440@60": {
                    "id": 99,  # command to be called for this resolution
                    "h_rez": 3440,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UWQHD 3440X1440",  # The actual Button text
                },
                "3840x1600@60": {
                    "id": 72,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 1600,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UW4K 3840x1600",  # The actual Button text
                },
                "3840x2400@60": {
                    "id": 101,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2400,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WQUXGA 3840x2400",  # The actual Button text
                },
            },
            "3d": {
                "1280x720p@60": {
                    "id": 37,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "720P 60Hz (3D-FP)",  # The actual Button text
                },
                "1280x720p@59.94": {
                    "id": 38,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "720P 59.94Hz (3D-FP)",  # The actual Button text
                },
                "1920x1080p@24": {
                    "id": 39,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "1080P 24Hz (3D-FP)",  # The actual Button text
                },
                "1920x1080P@23.976": {
                    "id": 40,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "1080P 23.976Hz (3D-FP)",  # The actual Button text
                },
                "1280x720p@50": {
                    "id": 41,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "720P 50Hz (3D-FP)",  # The actual Button text
                },
            },
            "custom": {
                "USER-1": {
                    "id": 43,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-1",  # The actual Button text
                },
                "USER-2": {
                    "id": 44,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-2",  # The actual Button text
                },
                "USER-3": {
                    "id": 45,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-3",  # The actual Button text
                },
                "USER-4": {
                    "id": 46,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-4",  # The actual Button text
                },
                "USER-5": {
                    "id": 47,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-5",  # The actual Button text
                },
                "USER-6": {
                    "id": 48,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-6",  # The actual Button text
                },
                "USER-7": {
                    "id": 49,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-9",  # The actual Button text
                },
                "USER-8": {
                    "id": 50,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-8",  # The actual Button text
                },
                "USER-9": {
                    "id": 51,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-9",  # The actual Button text
                },
                "USER-10": {
                    "id": 52,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-10",  # The actual Button text
                },
            },
            "auto": {
                "AUTO": {
                    "id": 43,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "Auto(Output timing based on EDID of sink device)",  # The actual Button text
                    "note": "This needs to send 2 commands, 1. SENDSINGLE||97,42 2. SENDSINGLE||47160,1",  # TODO Figure out how to send 2 commands
                },
            },
        },
        "pattern": {
            "function": "senddouble",  # Function needed to send the command ex: SENDDOUBLE||98,458
            "category_type": 98,  # ID for the category in this case it's 98=Pattern
            "fpga": {
                "100% Color Bars": {
                    "id": 0,
                    "tag": "100% Color Bars",
                },
                "75% Color Bars": {
                    "id": 1,
                    "tag": "75% Color Bars",
                },
                "8 Step Gray Bars": {
                    "id": 2,
                    "tag": "8 Step Gray Bars",
                },
                "16 Step Gray Bars": {
                    "id": 3,
                    "tag": "16 Step Gray Bars",
                },
                "Red Screen": {
                    "id": 4,
                    "tag": "Red Screen",
                },
                "Green Screen": {
                    "id": 5,
                    "tag": "Green Screen",
                },
                "Blue Screen": {
                    "id": 6,
                    "tag": "Blue Screen",
                },
                "Cyan Screen": {
                    "id": 7,
                    "tag": "Cyan Screen",
                },
                "Magenta Screen": {
                    "id": 8,
                    "tag": "Magenta Screen",
                },
                "Yellow Screen": {
                    "id": 9,
                    "tag": "Yellow Screen",
                },
                "Black Screen": {
                    "id": 10,
                    "tag": "Black Screen",
                },
                "White Screen": {
                    "id": 11,
                    "tag": "White Screen",
                },
                "Vertical Split": {
                    "id": 12,
                    "tag": "Vertical Split",
                },
                "Horizontal Split": {
                    "id": 13,
                    "tag": "Horizontal Split",
                },
                "Multiburst Vert.": {
                    "id": 14,
                    "tag": "Multiburst Vert.",
                },
                "Multiburst Hor.": {
                    "id": 15,
                    "tag": "Multiburst Hor.",
                },
                "Quarter Block 1": {
                    "id": 16,
                    "tag": "Quarter Block 1",
                },
                "Quarter Block 2": {
                    "id": 17,
                    "tag": "Quarter Block 2",
                },
                "Alternate W.B": {
                    "id": 18,
                    "tag": "Alternate W.B",
                },
                "RGB CMY Ramps": {
                    "id": 19,
                    "tag": "RGB CMY Ramps",
                },
                "Black Pluge": {
                    "id": 20,
                    "tag": "Black Pluge",
                },
                "White Pluge": {
                    "id": 21,
                    "tag": "White Pluge",
                },
                "Still Gray Ramp 1": {
                    "id": 22,
                    "tag": "Still Gray Ramp 1",
                },
                "Still Gray Ramp 2": {
                    "id": 23,
                    "tag": "Still gray Ramp 2",
                },
                "Smpte Bars": {
                    "id": 24,
                    "tag": "Smpte Bars",
                },
                "Border Lines": {
                    "id": 25,
                    "tag": "Border Lines",
                },
                "Window": {
                    "id": 26,
                    "tag": "Window",
                },
                "3D Boxes": {
                    "id": 27,
                    "tag": "3D Boxes",
                },
                "Line V.Scroll": {
                    "id": 28,
                    "tag": "Line V.Scroll",
                },
                "Line H.Scroll": {
                    "id": 29,
                    "tag": "Line H.Scroll",
                },
                "A/V Sync": {
                    "id": 30,
                    "tag": "A/V Sync",
                },
                "Gray Ramp": {
                    "id": 31,
                    "tag": "Gray Ramp",
                },
                "Red Ramp": {
                    "id": 32,
                    "tag": "Red Ramp",
                },
                "Green Ramp": {
                    "id": 33,
                    "tag": "Green Ramp",
                },
                "Blue Ramp": {
                    "id": 34,
                    "tag": "Blue Ramp",
                },
                "Moving Ball": {
                    "id": 35,
                    "tag": "Moving Ball",
                },
            },
            "isf": {
                "White Pluge UHD": {
                    "id": 36,
                    "tag": "White Pluge UHD",
                },
                "Black Pluge UHD": {
                    "id": 37,
                    "tag": "Black Pluge UHD",
                },
                "Geometry UHD": {
                    "id": 38,
                    "tag": "Geometry UHD",
                },
                "White Pluge HD": {
                    "id": 39,
                    "tag": "White Pluge HD",
                },
                "Black Pluge HD": {
                    "id": 40,
                    "tag": "Black Pluge HD",
                },
                "Geometry 178 HD": {
                    "id": 41,
                    "tag": "Geometry 178 HD",
                },
                "Geometry 240 HD": {
                    "id": 42,
                    "tag": "Geometry 240 HD",
                },
                "ISF Color Girls": {
                    "id": 43,
                    "tag": "ISF Color Girls",
                },
                "PD Family": {
                    "id": 44,
                    "tag": "PD Family",
                },
                "Red Blue MTB": {
                    "id": 45,
                    "tag": "Red Blue MTB",
                },
                "Cone Gradiant": {
                    "id": 46,
                    "tag": "Cone Gradiant",
                },
                "ISF Dog": {
                    "id": 47,
                    "tag": "ISF Dog",
                },
            },
            "dvs hdr": {
                "clipping & color": {
                    "Black Level 1": {
                        "id": 48,
                        "tag": "Black Level 1",
                    },
                    "Black Level 2": {
                        "id": 49,
                        "tag": "Black Level 2",
                    },
                    "White Level 1": {
                        "id": 50,
                        "tag": "White Level 1",
                    },
                    "White Level 2": {
                        "id": 51,
                        "tag": "White Level 2",
                    },
                    "White Level 3": {
                        "id": 52,
                        "tag": "White Level 3",
                    },
                    "White 80-100": {
                        "id": 53,
                        "tag": "White 80-100",
                    },
                    "HDR Mix": {
                        "id": 54,
                        "tag": "HDR Mix",
                    },
                    "HDR Greyscale": {
                        "id": 55,
                        "tag": "HDR Greyscale",
                    },
                    "HDR Red": {
                        "id": 56,
                        "tag": "HDR Red",
                    },
                    "HDR Green": {
                        "id": 57,
                        "tag": "HDR Green",
                    },
                    "HDR Blue": {
                        "id": 58,
                        "tag": "HDR Blue",
                    },
                    "HDR Yellow": {
                        "id": 59,
                        "tag": "HDR Yellow",
                    },
                    "HDR Cyan": {
                        "id": 60,
                        "tag": "HDR Cyan",
                    },
                    "HDR Magenta": {
                        "id": 61,
                        "tag": "HDR Magenta",
                    },
                    "Multi-Cube": {
                        "id": 62,
                        "tag": "Multi-Cube",
                    },
                    "10 Patch Mix": {
                        "id": 63,
                        "tag": "10 Patch Mix",
                    },
                    "Greyscale 1000": {
                        "id": 64,
                        "tag": "Greyscale 1000",
                    },
                    "Greyscale 2000": {
                        "id": 65,
                        "tag": "Greyscale 2000",
                    },
                    "Greyscale 4000": {
                        "id": 66,
                        "tag": "Greyscale 4000",
                    },
                    "Greyscale 10000": {
                        "id": 67,
                        "tag": "Greyscale 10000",
                    },
                    "Color High": {
                        "id": 68,
                        "tag": "Color High",
                    },
                    "Color Low": {
                        "id": 69,
                        "tag": "Color Low",
                    },
                    "Decoding 50%": {
                        "id": 70,
                        "tag": "Decoding 50%",
                    },
                    "Decoding 100%": {
                        "id": 71,
                        "tag": "Decoding 100%",
                    },
                    "Blue Filter 100%": {
                        "id": 72,
                        "tag": "Blue Filter 100%",
                    },
                    "Green Filter 100%": {
                        "id": 73,
                        "tag": "Green Filter 100%",
                    },
                    "Red Filter 100%": {
                        "id": 74,
                        "tag": "Red Filter 100%",
                    },
                    "Blue Filter 50%": {
                        "id": 75,
                        "tag": "Blue Filter 50%",
                    },
                    "Green Filter 50%": {
                        "id": 76,
                        "tag": "Green Filter 50%",
                    },
                    "Red Filter 50%": {
                        "id": 77,
                        "tag": "Red Filter 50%",
                    },
                    "Color Flashing": {
                        "id": 78,
                        "tag": "Color Flashing",
                    },
                    "Dynamic Contrast": {
                        "id": 79,
                        "tag": "Dynamic Contrast",
                    },
                },
                "evaluation": {
                    "Landscape": {
                        "id": 80,
                        "tag": "Landscape",
                    },
                    "Nature": {
                        "id": 81,
                        "tag": "Skin Tone",
                    },
                    "Skin Tone": {
                        "id": 82,
                        "tag": "Skin Tone",
                    },
                    "City Sunset": {
                        "id": 83,
                        "tag": "City Sunset",
                    },
                    "Oceanside": {
                        "id": 84,
                        "tag": "Oceanside",
                    },
                    "Pantone Skin": {
                        "id": 85,
                        "tag": "Pantone Skin",
                    },
                    "Restaurant": {
                        "id": 86,
                        "tag": "Restaurant",
                    },
                    "Indian Market": {
                        "id": 87,
                        "tag": "Indian Market",
                    },
                    "Ambient 05 Nit": {
                        "id": 88,
                        "tag": "Ambient 05 Nit",
                    },
                    "Ambient 10 Nit": {
                        "id": 89,
                        "tag": "Ambient 10 Nit",
                    },
                    "Ambient 15 Nit": {
                        "id": 90,
                        "tag": "Ambient 15 Nit",
                    },
                    "Chroma Sub 100": {
                        "id": 91,
                        "tag": "Chroma Sub 100",
                    },
                    "Chroma Sub 500": {
                        "id": 92,
                        "tag": "Chroma Sub 500",
                    },
                    "Chroma Sub 1000": {
                        "id": 93,
                        "tag": "Chroma Sub 1000",
                    },
                    "Judder 24 FPS": {
                        "id": 94,
                        "tag": "Judder 24 FPS",
                    },
                    "Judder 60 FPS": {
                        "id": 95,
                        "tag": "Judder 60 FPS",
                    },
                    "M Judder 24 FPS": {
                        "id": 96,
                        "tag": "M Judder 24 FPS",
                    },
                },
                "geometry & convergence": {
                    "Apsect Ratio 1.78": {
                        "id": 97,
                        "tag": "Apsect Ratio 1.78",
                    },
                    "Apsect Ratio 1.85": {
                        "id": 98,
                        "tag": "Apsect Ratio 1.85",
                    },
                    "Apsect Ratio 2.00": {
                        "id": 99,
                        "tag": "Apsect Ratio 2.00",
                    },
                    "Apsect Ratio 2.35": {
                        "id": 100,
                        "tag": "Apsect Ratio 2.35",
                    },
                    "Apsect Ratio 2.40": {
                        "id": 101,
                        "tag": "Apsect Ratio 2.40",
                    },
                    "Apsect Ratio All": {
                        "id": 102,
                        "tag": "Apsect Ratio All",
                    },
                    "Grid White": {
                        "id": 103,
                        "tag": "Grid White",
                    },
                    "Grid Red": {
                        "id": 104,
                        "tag": "Grid Red",
                    },
                    "Grid Green": {
                        "id": 105,
                        "tag": "Grid Green",
                    },
                    "Grid Blue": {
                        "id": 106,
                        "tag": "Grid Blue",
                    },
                    "Grid Yellow": {
                        "id": 107,
                        "tag": "Grid Yellow",
                    },
                    "Grid Cyan": {
                        "id": 108,
                        "tag": "Grid Cyan",
                    },
                    "Grid Magenta": {
                        "id": 109,
                        "tag": "Grid Magenta",
                    },
                    "Dot White": {
                        "id": 110,
                        "tag": "Dot White",
                    },
                    "Dot Red": {
                        "id": 111,
                        "tag": "Dot Red",
                    },
                    "Dot Green": {
                        "id": 112,
                        "tag": "Dot Green",
                    },
                    "Dot Blue": {
                        "id": 113,
                        "tag": "Dot Blue",
                    },
                    "Dot Yellow": {
                        "id": 114,
                        "tag": "Dot Yellow",
                    },
                    "Dot Cyan": {
                        "id": 115,
                        "tag": "Dot Cyan",
                    },
                    "Dot Magenta": {
                        "id": 116,
                        "tag": "Dot Magenta",
                    },
                    "Cross White": {
                        "id": 117,
                        "tag": "Cross White",
                    },
                    "Cross Red": {
                        "id": 118,
                        "tag": "Cross Red",
                    },
                    "Cross Green": {
                        "id": 119,
                        "tag": "Cross Green",
                    },
                    "Cross Blue": {
                        "id": 120,
                        "tag": "Cross Blue",
                    },
                    "Cross Yellow": {
                        "id": 121,
                        "tag": "Cross Yellow",
                    },
                    "Cross Cyan": {
                        "id": 122,
                        "tag": "Cross Cyan",
                    },
                    "Cross Magenta": {
                        "id": 123,
                        "tag": "Cross Magenta",
                    },
                },
                "ramps, gradients, zone plates": {
                    "Greyscale Steps": {
                        "id": 124,
                        "tag": "Greyscale Steps",
                    },
                    "Greyscale Ramp": {
                        "id": 125,
                        "tag": "Greyscale Ramp",
                    },
                    "Greyscale Mix": {
                        "id": 126,
                        "tag": "Greyscale Mix",
                    },
                    "Color Steps": {
                        "id": 127,
                        "tag": "Color Steps",
                    },
                    "Color Ramp": {
                        "id": 128,
                        "tag": "Color Ramp",
                    },
                    "Color Ramp H&V": {
                        "id": 129,
                        "tag": "Color Ramp H&V",
                    },
                    "Color Ramp Mix": {
                        "id": 130,
                        "tag": "Color Ramp Mix",
                    },
                    "Color Bar Ramp": {
                        "id": 131,
                        "tag": "Color Bar Ramp",
                    },
                    "Ramp Red": {
                        "id": 132,
                        "tag": "Ramp Red",
                    },
                    "Ramp Green": {
                        "id": 133,
                        "tag": "Ramp Green",
                    },
                    "Ramp Blue": {
                        "id": 134,
                        "tag": "Ramp Blue",
                    },
                    "Ramp Yellow": {
                        "id": 135,
                        "tag": "Ramp Yellow",
                    },
                    "Ramp Cyan": {
                        "id": 136,
                        "tag": "Ramp Cyan",
                    },
                    "Ramp Magenta": {
                        "id": 137,
                        "tag": "Ramp Magenta",
                    },
                    "Zone White": {
                        "id": 138,
                        "tag": "Zone White",
                    },
                    "Zone Red": {
                        "id": 139,
                        "tag": "Zone Red",
                    },
                    "Zone Green": {
                        "id": 140,
                        "tag": "Zone Green",
                    },
                    "Zone Blue": {
                        "id": 141,
                        "tag": "Zone Blue",
                    },
                    "Zone Magenta": {
                        "id": 142,
                        "tag": "Zone Magenta",
                    },
                    "Zone Yellow": {
                        "id": 143,
                        "tag": "Zone Yellow",
                    },
                    "Zone Cyan": {
                        "id": 144,
                        "tag": "Zone Cyan",
                    },
                    "Radial Grey": {
                        "id": 145,
                        "tag": "Radial Grey",
                    },
                    "Radial Red": {
                        "id": 146,
                        "tag": "Radial Red",
                    },
                    "Radial Green": {
                        "id": 147,
                        "tag": "Radial Green",
                    },
                    "Radial Blue": {
                        "id": 148,
                        "tag": "Radial Blue",
                    },
                    "Radial Yellow": {
                        "id": 149,
                        "tag": "Radial Yellow",
                    },
                    "Radial Cyan": {
                        "id": 150,
                        "tag": "Radial Cyan",
                    },
                    "Radial Magenta": {
                        "id": 151,
                        "tag": "Radial Magenta",
                    },
                },
                "resolution, ansi, placement": {
                    "Resolution Mix": {
                        "id": 152,
                        "tag": "Resoltuion Mix",
                    },
                    "Checkerboard": {
                        "id": 153,
                        "tag": "Checkerboard",
                    },
                    "Horizontal 1px": {
                        "id": 154,
                        "tag": "Horizontal 1px",
                    },
                    "Horizontal 2px": {
                        "id": 155,
                        "tag": "Horizontal 2px",
                    },
                    "Horizontal 3px": {
                        "id": 156,
                        "tag": "Horizontal 3px",
                    },
                    "Vertical 1px": {
                        "id": 157,
                        "tag": "Vertical 1px",
                    },
                    "Vertical 2px": {
                        "id": 158,
                        "tag": "Vertical 2px",
                    },
                    "Vertical 3px": {
                        "id": 159,
                        "tag": "Vertical 3px",
                    },
                    "Black Pixels": {
                        "id": 160,
                        "tag": "Black Pixels",
                    },
                    "ANSI Meter 8x8": {
                        "id": 161,
                        "tag": "ANSI Meter 8x8",
                    },
                    "ANSI 8x8": {
                        "id": 162,
                        "tag": "ANSI 8x8",
                    },
                    "ANSI Meter 5x4": {
                        "id": 163,
                        "tag": "ANSI Meter 5x4",
                    },
                    "ANSI 5x4 Black": {
                        "id": 164,
                        "tag": "ANSI M5x4 Black",
                    },
                    "ANSI 5x4 White": {
                        "id": 165,
                        "tag": "ANSI M5x4 White",
                    },
                    "Meter Placement": {
                        "id": 166,
                        "tag": "Meter Placement",
                    },
                    "Sharp & Scan": {
                        "id": 167,
                        "tag": "Sharp & Scan",
                    },
                },
            },
            "dvs dolby vision": {
                "clipping & color": {
                    "Black Level 1": {
                        "id": 472,
                        "tag": "Black Level 1",
                    },
                    "Black Level 2": {
                        "id": 473,
                        "tag": "Black Level 2",
                    },
                    "White Level 1": {
                        "id": 474,
                        "tag": "White Level 1",
                    },
                    "White Level 2": {
                        "id": 475,
                        "tag": "White Level 2",
                    },
                    "White Level 3": {
                        "id": 476,
                        "tag": "White Level 3",
                    },
                    "White 80-100": {
                        "id": 477,
                        "tag": "White 80-100",
                    },
                    "Blue Filter 50%": {
                        "id": 478,
                        "tag": "Blue Filter 50%",
                    },
                    "Green Filter 50%": {
                        "id": 479,
                        "tag": "Green Filter 50%",
                    },
                    "Red Filter 50%": {
                        "id": 480,
                        "tag": "Red Filter 50%",
                    },
                    "Color Clipping High": {
                        "id": 481,
                        "tag": "Color Clipping High",
                    },
                    "Color Clipping Low": {
                        "id": 482,
                        "tag": "Color Clipping Low",
                    },
                    "Color Decoding": {
                        "id": 483,
                        "tag": "Color Decoding",
                    },
                    "Color Flashing": {
                        "id": 484,
                        "tag": "Color Flashing",
                    },
                },
                "evaluation": {
                    "Landscape": {
                        "id": 485,
                        "tag": "Landscape",
                    },
                    "Nature": {
                        "id": 486,
                        "tag": "Nature",
                    },
                    "Skin Tone": {
                        "id": 487,
                        "tag": "Skin Tone",
                    },
                    "City Sunset": {
                        "id": 488,
                        "tag": "City Sunset",
                    },
                    "Oceanside": {
                        "id": 489,
                        "tag": "Oceanside",
                    },
                    "Pantone Skin": {
                        "id": 490,
                        "tag": "Pantone Skin",
                    },
                    "Restaurant": {
                        "id": 491,
                        "tag": "Restaurant",
                    },
                    "Indian Market": {
                        "id": 492,
                        "tag": "Indian Market",
                    },
                },
                "ramps, gradients, zone plates": {
                    "Greyscale Steps": {
                        "id": 493,
                        "tag": "Greyscale Steps",
                    },
                    "Greyscale Ramp": {
                        "id": 494,
                        "tag": "Greyscale Ramp",
                    },
                    "Greyscale Mix": {
                        "id": 495,
                        "tag": "Greyscale Mix",
                    },
                    "Color Steps": {
                        "id": 496,
                        "tag": "Color Steps",
                    },
                    "Red Radial Gradient": {
                        "id": 497,
                        "tag": "Red Radial Gradient",
                    },
                    "Green Radial Gradient": {
                        "id": 498,
                        "tag": "Green Radial Gradient",
                    },
                    "Blue Radial Gradient": {
                        "id": 499,
                        "tag": "Blue Radial Gradient",
                    },
                    "Yellow Radial Gradient": {
                        "id": 500,
                        "tag": "Yellow Radial Gradient",
                    },
                    "Cyan Radial Gradient": {
                        "id": 501,
                        "tag": "Cyan Radial Gradient",
                    },
                    "Magenta Radial Gradient": {
                        "id": 502,
                        "tag": "Magenta Radial Gradient",
                    },
                },
                "resolution, ansi, placement": {
                    "ANSI Meter 8x8": {
                        "id": 503,
                        "tag": "ANSI Meter 8x8",
                    },
                    "ANSI 8x8 Black": {
                        "id": 504,
                        "tag": "ANSI 8x8 Black",
                    },
                    "ANSI 8x8 White": {
                        "id": 505,
                        "tag": "ANSI 8x8 White",
                    },
                    "ANSI Meter 5x4": {
                        "id": 506,
                        "tag": "ANSI Meter 5x4",
                    },
                    "ANSI 5x4 Black": {
                        "id": 507,
                        "tag": "ANSI M5x4 Black",
                    },
                    "ANSI 5x4 White": {
                        "id": 508,
                        "tag": "ANSI M5x4 White",
                    },
                    "Meter Placement": {
                        "id": 509,
                        "tag": "Meter Placement",
                    },
                    "Sharp & Scan": {
                        "id": 510,
                        "tag": "Sharp & Scan",
                    },
                },
            },
            "dvs hlg": {
                "clipping & color": {
                    "Black Level 1": {
                        "id": 511,
                        "tag": "Black Level 1",
                    },
                    "Black Level 2": {
                        "id": 512,
                        "tag": "Black Level 2",
                    },
                    "White Level 1": {
                        "id": 513,
                        "tag": "White Level 1",
                    },
                    "White Level 2": {
                        "id": 514,
                        "tag": "White Level 2",
                    },
                    "White Level 3": {
                        "id": 515,
                        "tag": "White Level 3",
                    },
                    "HDR Mix": {
                        "id": 517,
                        "tag": "HDR Mix",
                    },
                    "HDR Greyscale": {
                        "id": 518,
                        "tag": "HDR Greyscale",
                    },
                    "HDR Red": {
                        "id": 519,
                        "tag": "HDR Red",
                    },
                    "HDR Green": {
                        "id": 520,
                        "tag": "HDR Green",
                    },
                    "HDR Blue": {
                        "id": 521,
                        "tag": "HDR Blue",
                    },
                    "HDR Yellow": {
                        "id": 522,
                        "tag": "HDR Yellow",
                    },
                    "HDR Cyan": {
                        "id": 523,
                        "tag": "HDR Cyan",
                    },
                    "HDR Magenta": {
                        "id": 524,
                        "tag": "HDR Magenta",
                    },
                    "Multi-Cube": {
                        "id": 525,
                        "tag": "Multi-Cube",
                    },
                    "10 Patch Mix": {
                        "id": 526,
                        "tag": "10 Patch Mix",
                    },
                    "Blue Filter 100%": {
                        "id": 529,
                        "tag": "Blue Filter 100%",
                    },
                    "Green Filter 100%": {
                        "id": 530,
                        "tag": "Green Filter 100%",
                    },
                    "Red Filter 100%": {
                        "id": 531,
                        "tag": "Red Filter 100%",
                    },
                    "Color Clipping High": {
                        "id": 527,
                        "tag": "Color Clipping High",
                    },
                    "Color Clipping Low": {
                        "id": 528,
                        "tag": "Color Clipping Low",
                    },
                    "Color Decoding 50%": {
                        "id": 532,
                        "tag": "Color Decoding 50%",
                    },
                    "Color Decoding 100%": {
                        "id": 533,
                        "tag": "Color Decoding 100%",
                    },
                    "Color Flashing": {
                        "id": 516,
                        "tag": "Color Flashing",
                    },
                },
                "evaluation": {
                    "Landscape": {
                        "id": 534,
                        "tag": "Landscape",
                    },
                    "Nature": {
                        "id": 535,
                        "tag": "Nature",
                    },
                    "Skin Tone": {
                        "id": 536,
                        "tag": "Skin Tone",
                    },
                    "City Sunset": {
                        "id": 537,
                        "tag": "City Sunset",
                    },
                    "Oceanside": {
                        "id": 538,
                        "tag": "Oceanside",
                    },
                    "Pantone Skin": {
                        "id": 539,
                        "tag": "Pantone Skin",
                    },
                    "Restaurant": {
                        "id": 540,
                        "tag": "Restaurant",
                    },
                    "Indian Market": {
                        "id": 541,
                        "tag": "Indian Market",
                    },
                },
                "ramps, gradients, zone plates": {
                    "Greyscale Steps": {
                        "id": 542,
                        "tag": "Greyscale Steps",
                    },
                    "Greyscale Ramp": {
                        "id": 543,
                        "tag": "Greyscale Ramp",
                    },
                    "Greyscale Mix": {
                        "id": 544,
                        "tag": "Greyscale Mix",
                    },
                    "Color Steps": {
                        "id": 545,
                        "tag": "Color Steps",
                    },
                    "Color Ramp": {
                        "id": 546,
                        "tag": "Color Ramp",
                    },
                    "Color Ramp H&V": {
                        "id": 547,
                        "tag": "Color Ramp H&V",
                    },
                    "Color Ramp Mix": {
                        "id": 548,
                        "tag": "Color Ramp Mix",
                    },
                    "Color Bar Ramp": {
                        "id": 549,
                        "tag": "Color Bar Ramp",
                    },
                    "Ramp Red": {
                        "id": 550,
                        "tag": "Ramp Red",
                    },
                    "Ramp Green": {
                        "id": 551,
                        "tag": "Ramp Green",
                    },
                    "Ramp Blue": {
                        "id": 552,
                        "tag": "Ramp Blue",
                    },
                    "Ramp Yellow": {
                        "id": 553,
                        "tag": "Ramp Yellow",
                    },
                    "Ramp Cyan": {
                        "id": 554,
                        "tag": "Ramp Cyan",
                    },
                    "Ramp Magenta": {
                        "id": 555,
                        "tag": "Ramp Magenta",
                    },
                    "Zone White": {
                        "id": 556,
                        "tag": "Zone White",
                    },
                    "Zone Red": {
                        "id": 557,
                        "tag": "Zone Red",
                    },
                    "Zone Green": {
                        "id": 558,
                        "tag": "Zone Green",
                    },
                    "Zone Blue": {
                        "id": 559,
                        "tag": "Zone Blue",
                    },
                    "Zone Magenta": {
                        "id": 560,
                        "tag": "Zone Magenta",
                    },
                    "Zone Yellow": {
                        "id": 561,
                        "tag": "Zone Yellow",
                    },
                    "Zone Cyan": {
                        "id": 562,
                        "tag": "Zone Cyan",
                    },
                    "Radial Grey": {
                        "id": 563,
                        "tag": "Radial Grey",
                    },
                    "Radial Red": {
                        "id": 564,
                        "tag": "Radial Red",
                    },
                    "Radial Green": {
                        "id": 565,
                        "tag": "Radial Green",
                    },
                    "Radial Blue": {
                        "id": 566,
                        "tag": "Radial Blue",
                    },
                    "Radial Yellow": {
                        "id": 567,
                        "tag": "Radial Yellow",
                    },
                    "Radial Cyan": {
                        "id": 568,
                        "tag": "Radial Cyan",
                    },
                    "Radial Magenta": {
                        "id": 569,
                        "tag": "Radial Magenta",
                    },
                },
                "resolution, ansi, placement": {
                    "ANSI Meter 8x8": {
                        "id": 570,
                        "tag": "ANSI Meter 8x8",
                    },
                    "ANSI 8x8 Black": {
                        "id": 571,
                        "tag": "ANSI 8x8 Black",
                    },
                    "ANSI 8x8 White": {
                        "id": 572,
                        "tag": "ANSI 8x8 White",
                    },
                    "ANSI Meter 5x4": {
                        "id": 573,
                        "tag": "ANSI Meter 5x4",
                    },
                    "ANSI 5x4 Black": {
                        "id": 574,
                        "tag": "ANSI M5x4 Black",
                    },
                    "ANSI 5x4 White": {
                        "id": 575,
                        "tag": "ANSI M5x4 White",
                    },
                    "Meter Placement": {
                        "id": 576,
                        "tag": "Meter Placement",
                    },
                    "Sharp & Scan": {
                        "id": 577,
                        "tag": "Sharp & Scan",
                    },
                    "Resolution Mix": {
                        "id": 578,
                        "tag": "Resolution Mix",
                    },
                },
            },
            "uhd sdr": {
                "clipping & gamma": {
                    "Target Limited": {
                        "id": 168,
                        "tag": "Target Limited",
                    },
                    "Target Full": {
                        "id": 169,
                        "tag": "Target Full",
                    },
                    "Contrast Check": {
                        "id": 170,
                        "tag": "Contrast Check",
                    },
                    "Contrast Lines": {
                        "id": 171,
                        "tag": "Contrast Lines",
                    },
                    "Gamma Check": {
                        "id": 172,
                        "tag": "Gamma Check",
                    },
                    "Gamma Lines": {
                        "id": 173,
                        "tag": "Gamma Lines",
                    },
                    "High Clipping": {
                        "id": 174,
                        "tag": "High Clipping",
                    },
                    "High Clip Red": {
                        "id": 175,
                        "tag": "High Clip Red",
                    },
                    "High Clip Green": {
                        "id": 176,
                        "tag": "High Clip Green",
                    },
                    "High Clip Blue": {
                        "id": 177,
                        "tag": "High Clip Blue",
                    },
                    "Low Clipping": {
                        "id": 178,
                        "tag": "Low Clipping",
                    },
                    "Low Clip Red": {
                        "id": 179,
                        "tag": "Low Clip Red",
                    },
                    "Low Clip Green": {
                        "id": 180,
                        "tag": "Low Clip Green",
                    },
                    "Low Clip Blue": {
                        "id": 181,
                        "tag": "Low Clip Blue",
                    },
                    "Composite Grey": {
                        "id": 182,
                        "tag": "Composite Grey",
                    },
                    "Composite Red": {
                        "id": 183,
                        "tag": "Composite Red",
                    },
                    "Composite Green": {
                        "id": 184,
                        "tag": "Composite Green",
                    },
                    "Composite Blue": {
                        "id": 185,
                        "tag": "Composite Blue",
                    },
                    "Lin Step Grey": {
                        "id": 186,
                        "tag": "Lin Step Grey",
                    },
                    "Lin Step Red": {
                        "id": 187,
                        "tag": "Lin Step Red",
                    },
                    "Lin Step Green": {
                        "id": 188,
                        "tag": "Lin Step Green",
                    },
                    "Lin Step Blue": {
                        "id": 189,
                        "tag": "Lin Step Blue",
                    },
                    "Lin Step Magent": {
                        "id": 190,
                        "tag": "Lin Step Magent",
                    },
                    "Lin Step Yellow": {
                        "id": 191,
                        "tag": "Lin Step Yellow",
                    },
                    "Lin Step Cyan": {
                        "id": 192,
                        "tag": "Lin Step Cyan",
                    },
                    "Log Step Grey": {
                        "id": 193,
                        "tag": "Log Step Grey",
                    },
                    "Log Step Red": {
                        "id": 194,
                        "tag": "Log Step Red",
                    },
                    "Log Step Green": {
                        "id": 195,
                        "tag": "Log Step Green",
                    },
                    "Log Step Blue": {
                        "id": 196,
                        "tag": "Log Step Blue",
                    },
                    "Log Step Magent": {
                        "id": 197,
                        "tag": "Log Step Magent",
                    },
                    "Log Step Yellow": {
                        "id": 198,
                        "tag": "Log Step Yellow",
                    },
                    "Log Step Cyan": {
                        "id": 199,
                        "tag": "Log Step Cyan",
                    },
                    "Gamma Grey": {
                        "id": 200,
                        "tag": "Gamma Grey",
                    },
                    "Gamma Red": {
                        "id": 201,
                        "tag": "Gamma Red",
                    },
                    "Gamma Green": {
                        "id": 202,
                        "tag": "Gamma Green",
                    },
                    "Gamma Blue": {
                        "id": 203,
                        "tag": "Gamma Blue",
                    },
                    "Gamma Lines Grey": {
                        "id": 204,
                        "tag": "Gamma Lines Grey",
                    },
                    "Gamma Lines Red": {
                        "id": 205,
                        "tag": "Gamma Lines Red",
                    },
                    "Gamma Lines Green": {
                        "id": 206,
                        "tag": "Gamma Lines Green",
                    },
                    "Gamma Lines Blue": {
                        "id": 207,
                        "tag": "Gamma Lines Blue",
                    },
                },
                "color bars & noise": {
                    "Color Wipe Full": {
                        "id": 208,
                        "tag": "Color Wipe Full",
                    },
                    "Color Wipe Half": {
                        "id": 209,
                        "tag": "Color Wipe Half",
                    },
                    "Quick Check": {
                        "id": 210,
                        "tag": "Quick Check",
                    },
                    "H Bars RGB": {
                        "id": 211,
                        "tag": "H Bars RGB",
                    },
                    "H Bars RGBCMY": {
                        "id": 212,
                        "tag": "H Bars RGBCMY",
                    },
                    "H Bars Shade": {
                        "id": 214,
                        "tag": "H Bars Shade",
                    },
                    "V Bars RGB": {
                        "id": 215,
                        "tag": "V Bars RGB",
                    },
                    "V Bars RGBCMY": {
                        "id": 216,
                        "tag": "V Bars RGBCMY",
                    },
                    "V Bars Layover": {
                        "id": 217,
                        "tag": "V Bars Layover",
                    },
                    "V Bars Shade": {
                        "id": 218,
                        "tag": "V Bars Shade",
                    },
                    "Color Noise 01": {
                        "id": 219,
                        "tag": "Color Noise 01",
                    },
                    "Color Noise 02": {
                        "id": 220,
                        "tag": "Color Noise 02",
                    },
                    "Color Noise 04": {
                        "id": 221,
                        "tag": "Color Noise 04",
                    },
                    "Color Noise 08": {
                        "id": 222,
                        "tag": "Color Noise 08",
                    },
                    "Color Noise 16": {
                        "id": 223,
                        "tag": "Color Noise 16",
                    },
                    "Grey Moise 01": {
                        "id": 224,
                        "tag": "Color Noise 01",
                    },
                    "Grey Moise 02": {
                        "id": 225,
                        "tag": "Color Noise 02",
                    },
                    "Grey Moise 04": {
                        "id": 226,
                        "tag": "Color Noise 04",
                    },
                    "Grey Moise 08": {
                        "id": 227,
                        "tag": "Color Noise 08",
                    },
                    "Grey Moise 16": {
                        "id": 228,
                        "tag": "Color Noise 16",
                    },
                },
                "color checker": {
                    "HSL BlueMagenta": {
                        "id": 229,
                        "tag": "HSL BlueMagenta",
                    },
                    "HSL Blue": {
                        "id": 230,
                        "tag": "HSL Blue",
                    },
                    "HSL Cyan Blue": {
                        "id": 231,
                        "tag": "HSL Cyan Blue",
                    },
                    "HSL Cyan": {
                        "id": 232,
                        "tag": "HSL Cyan",
                    },
                    "HSL Green Cyan": {
                        "id": 233,
                        "tag": "HSL Green Cyan",
                    },
                    "HSL Green": {
                        "id": 234,
                        "tag": "HSL Green",
                    },
                    "HSL Magenta Red": {
                        "id": 235,
                        "tag": "HSL Magenta Red",
                    },
                    "HSL Magenta": {
                        "id": 236,
                        "tag": "HSL Magenta",
                    },
                    "HSL Red": {
                        "id": 237,
                        "tag": "HSL Red",
                    },
                    "HSL Yellow Green": {
                        "id": 238,
                        "tag": "HSL Yellow Green",
                    },
                    "HSL Yellow Red": {
                        "id": 239,
                        "tag": "HSL Yellow Red",
                    },
                    "HSL Yellow": {
                        "id": 240,
                        "tag": "HSL Yellow",
                    },
                    "HSV BlueMagenta": {
                        "id": 241,
                        "tag": "HSV BlueMagenta",
                    },
                    "HSV Cyan Blue": {
                        "id": 243,
                        "tag": "HSV Cyan Blue",
                    },
                    "HSV Cyan": {
                        "id": 244,
                        "tag": "HSV Cyan",
                    },
                    "HSV Green Cyan": {
                        "id": 245,
                        "tag": "HSV Green Cyan",
                    },
                    "HSV Green": {
                        "id": 246,
                        "tag": "HSV Green",
                    },
                    "HSV Magenta Red": {
                        "id": 247,
                        "tag": "HSV Magenta Red",
                    },
                    "HSV Magenta": {
                        "id": 248,
                        "tag": "HSV Magenta",
                    },
                    "HSV Red": {
                        "id": 249,
                        "tag": "HSV Red",
                    },
                    "HSV Yellow Green": {
                        "id": 250,
                        "tag": "HSV Yellow Green",
                    },
                    "HSV Yellow Red": {
                        "id": 251,
                        "tag": "HSV Yellow Red",
                    },
                    "HSV Yellow": {
                        "id": 252,
                        "tag": "HSV Yellow",
                    },
                    "RGB Blue 064": {
                        "id": 253,
                        "tag": "RGB Blue 064",
                    },
                    "RGB Blue 127": {
                        "id": 254,
                        "tag": "RGB Blue 127",
                    },
                    "RGB Blue 191": {
                        "id": 255,
                        "tag": "RGB Blue 191",
                    },
                    "RGB Blue 255": {
                        "id": 256,
                        "tag": "RGB Blue 255",
                    },
                    "RGB Green 064": {
                        "id": 257,
                        "tag": "RGB Green 064",
                    },
                    "RGB Green 127": {
                        "id": 258,
                        "tag": "RGB Green 127",
                    },
                    "RGB Green 191": {
                        "id": 259,
                        "tag": "RGB Green 191",
                    },
                    "RGB Green 255": {
                        "id": 260,
                        "tag": "RGB Green 255",
                    },
                    "RGB Red 064": {
                        "id": 261,
                        "tag": "RGB Red 064",
                    },
                    "RGB Red 127": {
                        "id": 262,
                        "tag": "RGB Red 127",
                    },
                    "RGB Red 191": {
                        "id": 263,
                        "tag": "RGB Red 191",
                    },
                    "RGB Red 255": {
                        "id": 264,
                        "tag": "RGB Red 255",
                    },
                },
                "geometry and resolution": {
                    "H Convergence": {
                        "id": 265,
                        "tag": "H Convergence",
                    },
                    "V Convergence": {
                        "id": 266,
                        "tag": "V Convergence",
                    },
                    "H Length": {
                        "id": 267,
                        "tag": "H Length",
                    },
                    "V Length": {
                        "id": 268,
                        "tag": "V Length",
                    },
                    "Overscan": {
                        "id": 269,
                        "tag": "Overscan",
                    },
                    "BW Evaluation": {
                        "id": 270,
                        "tag": "BW Evaluation",
                    },
                    "BW Evaluation 2": {
                        "id": 271,
                        "tag": "BW Evaluation 2",
                    },
                    "H Wedge": {
                        "id": 272,
                        "tag": "H Wedge",
                    },
                    "Star Burst": {
                        "id": 273,
                        "tag": "Star Burst",
                    },
                    "V Wedge": {
                        "id": 274,
                        "tag": "V Wedge",
                    },
                    "H Multiburst": {
                        "id": 275,
                        "tag": "H Multiburst",
                    },
                    "V Multiburst": {
                        "id": 276,
                        "tag": "V Multiburst",
                    },
                    "Checkers 02": {
                        "id": 277,
                        "tag": "Checkers 02",
                    },
                    "Checkers 04": {
                        "id": 278,
                        "tag": "Checkers 04",
                    },
                    "Checkers 08": {
                        "id": 279,
                        "tag": "Checkers 08",
                    },
                    "Checkers 16": {
                        "id": 280,
                        "tag": "Checkers 16",
                    },
                    "Checkers 32": {
                        "id": 281,
                        "tag": "Checkers 32",
                    },
                    "Checkers Log": {
                        "id": 282,
                        "tag": "Checkers Log",
                    },
                    "Many Circles": {
                        "id": 283,
                        "tag": "Many Circles",
                    },
                    "Center Circle": {
                        "id": 284,
                        "tag": "Center Circle",
                    },
                    "Many Squares": {
                        "id": 285,
                        "tag": "Many Squares",
                    },
                    "Grid": {
                        "id": 286,
                        "tag": "Grid",
                    },
                    "H Lines 02": {
                        "id": 287,
                        "tag": "H Lines 02",
                    },
                    "H Lines 04": {
                        "id": 288,
                        "tag": "H Lines 04",
                    },
                    "H Lines 08": {
                        "id": 289,
                        "tag": "H Lines 08",
                    },
                    "H Lines Log": {
                        "id": 290,
                        "tag": "H Lines Log",
                    },
                    "V Lines 02": {
                        "id": 291,
                        "tag": "V Lines 02",
                    },
                    "V Lines 04": {
                        "id": 292,
                        "tag": "V Lines 04",
                    },
                    "V Lines 08": {
                        "id": 293,
                        "tag": "V Lines 08",
                    },
                    "V Lines Log": {
                        "id": 294,
                        "tag": "V Lines Log",
                    },
                    "Points 02": {
                        "id": 295,
                        "tag": "Points 02",
                    },
                    "Points 04": {
                        "id": 296,
                        "tag": "Points 04",
                    },
                    "Points 08": {
                        "id": 297,
                        "tag": "Points 08",
                    },
                    "Points 16": {
                        "id": 298,
                        "tag": "Points 16",
                    },
                    "Points 32": {
                        "id": 299,
                        "tag": "Points 32",
                    },
                    "Squares 02": {
                        "id": 300,
                        "tag": "Squares 02",
                    },
                    "Squares 04": {
                        "id": 301,
                        "tag": "Squares 04",
                    },
                    "Squares 08": {
                        "id": 302,
                        "tag": "Squares 08",
                    },
                    "Squares 16": {
                        "id": 303,
                        "tag": "Squares 16",
                    },
                    "Squares 32": {
                        "id": 304,
                        "tag": "Squares 32",
                    },
                },
                "ramps": {
                    "Color Patch": {
                        "id": 305,
                        "tag": "Color Patch",
                    },
                    "Triangle ": {
                        "id": 306,
                        "tag": "Triangle",
                    },
                    "Wireframe": {
                        "id": 307,
                        "tag": "Wireframe",
                    },
                    "Full Red": {
                        "id": 308,
                        "tag": "Full Red",
                    },
                    "Full Green": {
                        "id": 309,
                        "tag": "Full Green",
                    },
                    "Full Blue": {
                        "id": 310,
                        "tag": "Full Blue",
                    },
                    "Full Magenta": {
                        "id": 311,
                        "tag": "Full Magenta",
                    },
                    "Full Yellow": {
                        "id": 312,
                        "tag": "Full Yellow",
                    },
                    "Full Cyan": {
                        "id": 313,
                        "tag": "Full Cyan",
                    },
                    "Full Grey": {
                        "id": 314,
                        "tag": "Full Grey",
                    },
                    "Half Red": {
                        "id": 315,
                        "tag": "Half Red",
                    },
                    "Half Green": {
                        "id": 316,
                        "tag": "Half Green",
                    },
                    "Half Blue": {
                        "id": 317,
                        "tag": "Half Blue",
                    },
                    "Half Magenta": {
                        "id": 318,
                        "tag": "Half Magenta",
                    },
                    "Half Yellow": {
                        "id": 319,
                        "tag": "Half Yellow",
                    },
                    "Half Cyan": {
                        "id": 320,
                        "tag": "Half Cyan",
                    },
                    "HSL Sat 0.00": {
                        "id": 321,
                        "tag": "HSL Sat 0.00",
                    },
                    "HSL Hue 0.00": {
                        "id": 322,
                        "tag": "HSL Hue 0.00",
                    },
                    "HSL Hue 0.33": {
                        "id": 323,
                        "tag": "HSL Hue 0.33",
                    },
                    "HSL Hue 0.66": {
                        "id": 324,
                        "tag": "HSL Hue 0.66",
                    },
                    "HSL Lev 0.25": {
                        "id": 325,
                        "tag": "HSL Lev 0.25",
                    },
                    "HSL Lev 0.50": {
                        "id": 326,
                        "tag": "HSL Lev 0.50",
                    },
                    "HSL Lev 0.75": {
                        "id": 327,
                        "tag": "HSL Lev 0.75",
                    },
                    "HSV Sat 0.00": {
                        "id": 328,
                        "tag": "HSV Sat 0.00",
                    },
                    "HSV Sat 0.50": {
                        "id": 329,
                        "tag": "HSV Sat 0.50",
                    },
                    "HSV Sat 1.00": {
                        "id": 330,
                        "tag": "HSV Sat 1.00",
                    },
                    "HSV Hue 0.00": {
                        "id": 331,
                        "tag": "HSV Hue 0.00",
                    },
                    "HSV Hue 0.33": {
                        "id": 332,
                        "tag": "HSV Hue 0.33",
                    },
                    "HSV Hue 0.66": {
                        "id": 333,
                        "tag": "HSV Hue 0.66",
                    },
                    "HSV Sat 0.50": {
                        "id": 334,
                        "tag": "HSV Sat 0.50",
                    },
                    "HSV Sat 1.00": {
                        "id": 335,
                        "tag": "HSV Sat 1.00",
                    },
                    "HSV Val 0.00": {
                        "id": 336,
                        "tag": "HSV Sat 0.00",
                    },
                    "HSV Val 0.50": {
                        "id": 337,
                        "tag": "HSV Sat 0.50",
                    },
                    "HSV Val 1.00": {
                        "id": 338,
                        "tag": "HSV Sat 1.00",
                    },
                    "RGB Green 000": {
                        "id": 339,
                        "tag": "RGB Green 000",
                    },
                    "RGB Green 127": {
                        "id": 340,
                        "tag": "RGB Green 127",
                    },
                    "RGB Green 255": {
                        "id": 341,
                        "tag": "RGB Green 255",
                    },
                    "RGB Blue 000": {
                        "id": 342,
                        "tag": "RGB Blue 000",
                    },
                    "RGB Blue 127": {
                        "id": 343,
                        "tag": "RGB Blue 127",
                    },
                    "RGB Blue 255": {
                        "id": 344,
                        "tag": "RGB Blue 255",
                    },
                    "RGB Red 000": {
                        "id": 345,
                        "tag": "RGB Red 000",
                    },
                    "RGB Red 127": {
                        "id": 346,
                        "tag": "RGB Red 127",
                    },
                    "RGB Red 255": {
                        "id": 347,
                        "tag": "RGB Red 255",
                    },
                },
            },
        },
    }
}
