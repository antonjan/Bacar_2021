# Bacar_2021
This will have the code for the BACAR Balloon flite 30 October 2021
Will be flying Africube transponder and Beacon on Bacar Balloon

# Creating CW Beacon Wav File using cwwav untility.
    sudo apt-get install libsndfile-dev
    cd /tmp && wget https://github.com/Kerrick/cwwav/archive/master.tar.gz --output-document cwwav.tar.gz
    tar -zxvf cwwav.tar.gz && cd cwwav-master
    make # If this turns out good, continue
    sudo make install
    echo "hello world" | cwwav -f 700 -w 20 -o hello_world.wav
# Creating image from Camera for SSTV
    
# Creating the SSTV transmition from gif.
    git clone https://github.com/dnet/pySSTV.git
    cd pySSTV
    python3 /home/pi/pySSTV/camera.py && echo " Picture taken"
    python3 -m pysstv --mode PD180 --fskid ZR6AIC --resize picture.jpg ./sstv-audio.wav


# APRS / AFSK Telemetry transmistion.


# SDR gnuradio transponder.

# APRS / AFSK transponder Controle.



