
# ~ 2022-01-24
# ~ не работает

# ~ # this will load Libdiscid
# ~ import discid

# ~ disc = discid.read()  # use default device
# ~ print "id: %s" % disc.id  # Python 2
# ~ print("id: %s" % disc.id) # Python 3

import os
from pprint import pp

# ~ pp(dict(os.environ))

# ~ {'LESSOPEN': '| /usr/bin/lesspipe %s',
 # ~ 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG',
 # ~ 'USER': 'myke',
 # ~ 'LANGUAGE': 'ru',
 # ~ 'XDG_SEAT': 'seat0',
 # ~ 'XDG_SESSION_TYPE': 'x11',
 # ~ 'SSH_AGENT_PID': '2331',
 # ~ 'SHLVL': '0',
 # ~ 'HOME': '/home/myke',
 # ~ 'CONDA_SHLVL': '0',
 # ~ 'OLDPWD': '/home/myke/pro/asap-kab/tables/dirstudy',
 # ~ 'DESKTOP_SESSION': 'cinnamon',
 # ~ 'GTK_MODULES': 'gail:atk-bridge',
 # ~ 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0',
 # ~ 'PS1': '(venv) \\[\\e]0;\\u@\\h: '
        # ~ '\\w\\a\\]${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ ',
 # ~ 'CINNAMON_VERSION': '5.2.7',
 # ~ 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus',
 # ~ '_CE_M': '',
 # ~ 'LIBVIRT_DEFAULT_URI': 'qemu:///system',
 # ~ 'COLORTERM': 'truecolor',
 # ~ 'QT_QPA_PLATFORMTHEME': 'qt5ct',
 # ~ 'LOGNAME': 'myke',
 # ~ '_': '/usr/bin/geany',
 # ~ 'XDG_SESSION_CLASS': 'user',
 # ~ 'XDG_SESSION_ID': 'c2',
 # ~ 'GTK_OVERLAY_SCROLLING': '1',
 # ~ 'MC_SID': '285598',
 # ~ 'TERM': 'xterm-256color',
 # ~ 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated',
 # ~ '_CE_CONDA': '',
 # ~ 'HISTCONTROL': 'ignoreboth',
 # ~ 'PATH': '/home/myke/pro/asap-kab/tables/dirstudy/venv/bin:/home/myke/anaconda3/condabin:/home/myke/.local/bin:/home/myke/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/myke/tex/2021/bin/x86_64-linux',
 # ~ 'GTK3_MODULES': 'xapp-gtk3-module',
 # ~ 'SESSION_MANAGER': 'local/mykex:@/tmp/.ICE-unix/2262,unix/mykex:/tmp/.ICE-unix/2262',
 # ~ 'GDM_LANG': 'ru',
 # ~ 'XDG_RUNTIME_DIR': '/run/user/1000',
 # ~ 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0',
 # ~ 'GNOME_TERMINAL_SCREEN': '/org/gnome/Terminal/screen/e1f03cd3_e37c_49c3_8ac6_4e4a9bf6569a',
 # ~ 'DISPLAY': ':0',
 # ~ 'LANG': 'ru_RU.UTF-8',
 # ~ 'XDG_CURRENT_DESKTOP': 'X-Cinnamon',
 # ~ 'MC_TMPDIR': '/tmp/mc-myke',
 # ~ 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:',
 # ~ 'XAUTHORITY': '/home/myke/.Xauthority',
 # ~ 'XDG_SESSION_DESKTOP': 'cinnamon',
 # ~ 'GNOME_TERMINAL_SERVICE': ':1.577',
 # ~ 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/myke',
 # ~ 'CONDA_PYTHON_EXE': '/home/myke/anaconda3/bin/python',
 # ~ 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh',
 # ~ 'SHELL': '/bin/bash',
 # ~ 'GDMSESSION': 'cinnamon',
 # ~ 'QT_ACCESSIBILITY': '1',
 # ~ 'LESSCLOSE': '/usr/bin/lesspipe %s %s',
 # ~ 'GJS_DEBUG_OUTPUT': 'stderr',
 # ~ 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1',
 # ~ 'VIRTUAL_ENV': '/home/myke/pro/asap-kab/tables/dirstudy/venv',
 # ~ 'XDG_VTNR': '7',
 # ~ 'PWD': '/home/myke/pro/asap-kab/tables/dirstudy',
 # ~ 'CONDA_EXE': '/home/myke/anaconda3/bin/conda',
 # ~ 'XDG_DATA_DIRS': '/usr/share/cinnamon:/usr/share/gnome:/home/myke/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share:/var/lib/snapd/desktop',
 # ~ 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-cinnamon:/etc/xdg',
 # ~ 'VTE_VERSION': '6003'}

# ~ print(os.getenv())

print(os.uname())
# ~ posix.uname_result(sysname='Linux', nodename='mykex', release='5.13.0-27-generic', version='#29~20.04.1-Ubuntu SMP Fri Jan 14 00:32:30 UTC 2022', machine='x86_64')

