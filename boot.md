# installing raspbian

1. download [raspbian.img](https://www.raspberrypi.org/downloads/raspbian/)

1. open / mount the raspbian.img file and add a `wpa_supplicant.conf` file to auto configure
  wifi so you dont have to plug in a keyboard to first test it. You
  can directly ssh at `pi@raspberrypi.local` on the wifi network. This
  website says to put this in the file under `/Volumes/boot`:

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US
    network={
        ssid="YOUR-SSID"
        psk="YOUR-PASSWORD"
        scan_ssid=1
    }
 
  if this is a total failure, though, you can use the serial USB-to-TTL cable
  to directly set it up.

1. follow [this](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md)
  to get it onto a usb or drive of some sort. so, do this

1. eject the device and insert it into the pi and turn it on
  - NOT working for non-usb devices right now though!
    
1. run `dig raspberrypi` to lookup the dns names of all the pis that are on the network

1. ssh into the pi and to find out which one you're in, run

      pi@raspberrypi:/sys/class/leds/led0 $ sudo sh -c "echo timer > trigger"

  to change how the light works. And to change the speed do:

      pi@raspberrypi:/sys/class/leds/led0 $ sudo sh -c "echo 10 > delay_on && echo 10 delay_off"

# after boot
  
- expand root file system to fill whole SD card with `sudo raspi-config` 
