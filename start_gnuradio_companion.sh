sudo modprobe snd-aloop
sleep 3
export XDG_RUNTIME_DIR=/run/user/0
#usbreset 1df7:2500
sleep 10
#export XAUTHORITY=/home/pi/.Xauthority 
#export DISPLAY=localhost:11.0
export PATH=/usr/local/bin:/root/.local/bin:$PATH
export PYTHONPATH=/usr/local/lib/python3/dist-packages:/usr/local/lib/python2.7/dist-packages/construct
:$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib/python2.7/dist-packages/construct:$LD_LIBRARY_CONFIG
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/home/pi/.local/lib/python3.7/site-packages/construct:$PKG_CONFIG_PATH
/usr/local/bin/gnuradio-companion
