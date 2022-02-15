# Bacar_2021
This will have the code for the BACAR Balloon flite 30 October 2021
Will be flying Africube transponder and Beacon on Bacar Balloon
![Africube](20210927_163502.jpg?raw=true "Africube")<br>
# Creating autostart for africube on startup addinding the following in sudo crontab -e.
    
    @reboot /home/pi/sh/start_africube_transponder.sh > /tmp/africube.log 2>&1

# Creating CW Beacon Wav File using cwwav untility.
    sudo apt-get install libsndfile-dev
    cd /tmp && wget https://github.com/Kerrick/cwwav/archive/master.tar.gz --output-document cwwav.tar.gz
    tar -zxvf cwwav.tar.gz && cd cwwav-master
    make # If this turns out good, continue
    sudo make install
    echo "hello world" | cwwav -f 700 -w 20 -o hello_world.wav
# Creating image from pi Camera for SSTV
    cd /home/pi/pySSTV
    wget https://github.com/antonjan/Bacar_2021/raw/main/take_photo_from_camera.py
    python3 /home/pi/pySSTV/take_photo_from_camera.py && echo " Picture taken"
    
# Creating the SSTV transmition wav file from gif image.
    git clone https://github.com/dnet/pySSTV.git
    cd pySSTV
    python3 /home/pi/pySSTV/camera.py && echo " Picture taken"
    python3 -m pysstv --mode PD180 --fskid ZR6AIC --resize picture.jpg ./sstv-audio.wav

# APRS / AFSK Telemetry transmistion.
manual for direwolf https://raw.githubusercontent.com/wb2osz/direwolf/dev/doc/User-Guide.pdf
raspberry pi direwolf document https://github.com/wb2osz/direwolf/raw/master/doc/Raspberry-Pi-APRS.pdf
    sudo apt get install direwolf
    

# SDR gnuradio transponder.
    cd 
    sd sh
    sudo ./start_gnuradio-companion.sh

# APRS / AFSK transponder Controle.

        git clone https://github.com/casebeer/afsk.git
        cd afsk
        sudo pip install afsk
        sudo pip install --allow-external PyAudio --allow-unverified PyAudio PyAudio
        sudo pip install  PyAudio --allow-unverified PyAudio PyAudio
        sudo pip install  PyAudio PyAudio
        afsk
        aprs

Images
![Africube](20210927_163454.jpg?raw=true "Africube")<br>
![Africube](20210927_163441.jpg?raw=true "Africube")<br>
![Africube](20210927_143742.jpg?raw=true "Africube")<br>
![Africube](20210927_143736.jpg?raw=true "Africube")<br>
![Africube](20210927_143728.jpg?raw=true "Africube")<br>
![Africube](20210927_143717.jpg?raw=true "Africube")<br>
![Africube](20210927_143707.jpg?raw=true "Africube")<br>
![Africube](20210927_143656.jpg?raw=true "Africube")<br>
![Africube](20210927_133130.jpg?raw=true "Africube")<br>
![Africube](20210927_133123.jpg?raw=true "Africube")<br>

