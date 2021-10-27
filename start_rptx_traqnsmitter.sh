sudo modprobe snd-aloop
sleep 3
/usr/local/bin/SoapySDRUtil --find
sleep 3
#export XAUTHORITY=/home/pi/.Xauthority 
#export DISPLAY=localhost:11.0
export PATH=/usr/local/bin:$PATH
export PYTHONPATH=/usr/local/lib/python3/dist-packages:$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_CONFIG
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
#/usr/local/bin/gnuradio-companion
#/home/pi/gnuradio_radios/rptx_traqnsmitter.py
#/home/pi/gnuradio_radios/SDRPlay.py
/home/pi/gnuradio_radios/working_africube_transponder_and_beacon.py
