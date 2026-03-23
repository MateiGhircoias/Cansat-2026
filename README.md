# Cansat 2026 Project – Team "Catastronauts"

## Overview
This project focuses on building a CanSat system capable of collecting and transmitting environmental telemetry in real time using a low-power embedded setup.

## Primary Mission
- Transmit telemetry data using LoRa (RFM9X module) at 433 MHz between two Raspberry Pi Picos  
- Measure temperature and pressure in real time  
- Estimate altitude based on pressure readings  
- Achieve reliable long-range communication (target: 100m+ using UFL antenna)  
- Visualize collected data using Matplotlib  

## Hardware
- Raspberry Pi Pico (x2)  
- LoRa RFM9X module (433 MHz)  
- Pressure & temperature sensor (BMP280)  
- External antenna (UFL connector)  

## Software
- Data acquisition in Python (MicroPython/CircuitPython)  
- LoRa communication protocol implementation  
- Telemetry logging and parsing  
- Data visualization using Matplotlib  

## Output
- Real-time telemetry stream  
- Logged dataset (temperature, pressure, altitude)  
- Graphs showing variation with altitude  
