import youtube_dl


# refer to YoutubeDL.py
yt_flags = {
        'source_address': '0.0.0.0',
        'format': 'bestaudio/best',

        # 'extractaudio': True,           # commandline args
        # 'audioformat': "mp3",

        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192',
        # }],

        # 'outtmpl': '%(id)s',            # output template
        # 'noplaylist': True,           # Download single video instead of a playlist if in doubt.
        # 'nocheckcertificate': True,
        # 'ignoreerrors': True,
        # 'quiet': True,
        # 'no_warnings': True,



        'default_search': 'auto',

        'invalidflag': 'undefinedbehaviour'

    }

with youtube_dl.YoutubeDL(yt_flags) as ytdl:
    ytdl.download(['https://www.youtube.com/watch?v=fTlLMsblceg'])
