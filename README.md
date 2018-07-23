My current pin configuration looks like this:

I have 3 external boards:

Muliplex: TCA9548A
2 Distance Senors: vl6180x
1 Raspberry Pi

The TCA9548A has 4 connections to the Pi:

VIN -> Pin 2
GND -> Pin 6
SDA -> BCM 2
SCL -> BCM 3

The vl6180x have 2 connections each to the Pi:
Board 0:
VIN -> Pin 1
GND -> Pin 9
SDA -> SD0 (multiplex)
SCL -> SC0 (multiplex) 

Board 1:
VIN -> Pin 17
GND -> Pin 25
SDA -> SD1 (multiplex)
SCL -> SC1 (multiplex) 

In addition, I have a hookup to an L298.

Red -> BCM 13 for the PWM 
Grey -> BCM 26
Black -> Pin 39

The motor hookup for right being forward is Black on top and Red on the bottom. 

