# Nixie Clock Project 🕰️

Un reloj Nixie moderno implementado en Python con soporte para hardware real (Raspberry Pi + NeoPixels) y un simulador gráfico avanzado.

![Wiring diagram](http://i.imgur.com/PyvOyog.png)

## Características Principales ✨

### ⚡ **Funcionalidades Centrales**
- **Doble implementación:** Ejecutable en hardware real y simulador gráfico
- **Soporte NeoPixel:** Control preciso de tiras LED WS2812B
- **Sistema de configuración:** Ajustes persistentes estilo EEPROM

## Estructura del Proyecto 📂

```bash
nixie_clock/
├── base_clock.py       # Clases abstractas y núcleo lógico
├── hardware.py         # Implementación para Raspberry Pi/NeoPixels
├── simulator.py        # Simulador gráfico con Tkinter
├── LED-Nixie6-Sound-Cronios3-Vanessa-1.20.txt  # Código original en BASIC
└── settings.json       # Configuración persistente (ejemplo)
