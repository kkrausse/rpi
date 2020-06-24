# Notes on the meat project

basically ripping off [this guys project](https://kyleflan.wordpress.com/2017/10/20/tempiture-a-raspberry-pi-powered-wireless-grilling-thermometer-system/)

the goal is to do the same thing as him, except:
- make it battery powered
- use the rpi zero w
- set up a dhcp server on the pi so you can connect from phone
  - basically, I'm thinking of this project in terms of being able to take it to
    someone else's house / wifi and have it work just as well.
    Need to think of a way to switch between the two "modes" (i.e. internet and LAN)
- wont be able to run docker images, so will have different UI maybe
- analytics / data saving so I can crunch the numbers and predict when to remove something

## supplies

TODO: price it out first

| thing             | cost |
|-------------------|------|
| rpi               | $10  |
| thermometer probe | $$$  |
| mcp3008           | $$$  |
| breadboard + wire | cost |
| soiderin iron     | cost |

## Resources

- in that above things are these useful ones
  - [analog to digital](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008)
  - [using thermistor](https://learn.adafruit.com/thermistor/using-a-thermistor)
