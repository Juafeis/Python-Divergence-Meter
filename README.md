# Nixie Clock Project 🕰️

Un reloj Nixie moderno implementado en Python con soporte para hardware real (Raspberry Pi + NeoPixels) y un simulador gráfico avanzado.

![Wiring diagram](http://i.imgur.com/PyvOyog.png)

## Características Principales ✨

### ⚡ **Funcionalidades Centrales**
- **Doble implementación:** Ejecutable en hardware real y simulador gráfico
- **Soporte NeoPixel:** Control preciso de tiras LED WS2812B
- **Animaciones fluidas:** Transiciones de fade/flip configurables
- **Multiplataforma:** Funciona en Windows/Linux/Raspberry Pi
- **Sistema de configuración:** Ajustes persistentes estilo EEPROM

### 🎨 **Características Visuales**
- Simulación fiel de tubos Nixie clásicos
- 6 dígitos con posicionamiento flexible
- Control individual de color por dígito
- Efectos de brillo realistas (incandescencia, fade)
- Soporte para múltiples esquemas de color

### ⚙️ **Características Técnicas**
- Arquitectura basada en clases abstractas
- Sistema de actualización por eventos
- Threading seguro para operaciones en tiempo real
- Optimización de rendimiento (60 FPS estables)
- Logging detallado para diagnóstico

## Estructura del Proyecto 📂

```bash
nixie_clock/
├── base_clock.py       # Clases abstractas y núcleo lógico
├── hardware.py         # Implementación para Raspberry Pi/NeoPixels
├── simulator.py        # Simulador gráfico con Tkinter
├── LED-Nixie6-Sound-Cronios3-Vanessa-1.20.txt  # Código original en BASIC
└── settings.json       # Configuración persistente (ejemplo)
