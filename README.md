# Embedded Systems · Firmware · Digital Hardware

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:111827,70:0f172a,100:020617&height=220&section=header&text=Embedded%20Systems%20Engineer&fontSize=42&fontColor=e2e8f0&animation=fadeIn&fontAlignY=38&desc=Hardware%20%C2%B7%20Firmware%20%C2%B7%20FPGA%20%C2%B7%20Systems&descAlignY=58&descSize=17&descAlign=50"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?lines=Hardware+to+firmware;Registers+to+drivers;Microcontrollers+to+systems;Building+close+to+the+silicon&font=Fira%20Code&center=true&width=700&height=45&color=94a3b8&vCenter=true&size=18&pause=1800&background=00000000"/>

<br/><br/>

[![GitHub Followers](https://img.shields.io/github/followers/FerrariForever95?style=for-the-badge\&color=0f172a\&labelColor=0d1117\&logo=github)](https://github.com/FerrariForever95)
[![Profile Views](https://komarev.com/ghpvc/?username=FerrariForever95\&style=for-the-badge\&color=0f172a\&labelColor=0d1117)](https://github.com/FerrariForever95)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0f172a?style=for-the-badge\&logo=linkedin\&logoColor=0A66C2\&labelColor=0d1117)](https://www.linkedin.com/in/shanmukha-marthi-aa78043b1/)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-0f172a?style=for-the-badge\&logo=researchgate\&logoColor=00CCBB\&labelColor=0d1117)](https://www.researchgate.net/profile/Marthi-Viswanadh)
[![Email](https://img.shields.io/badge/Email-0f172a?style=for-the-badge\&logo=gmail\&logoColor=EA4335\&labelColor=0d1117)](mailto:shanmukhamarthi@gmail.com)

</div>

<br/>

## `01` About

I work primarily at the boundary between **hardware and software**.

My projects usually start close to the hardware — registers, buses, peripherals, interrupts, memory and timing — and build upward into firmware, drivers and complete embedded systems.

```text
Hardware
   ↓
Registers / Peripherals
   ↓
Firmware
   ↓
Drivers / RTOS
   ↓
System Software
   ↓
Applications
```

### What I Build

* Bare-metal firmware
* Register-level microcontroller software
* Interrupt-driven systems
* Embedded drivers
* FreeRTOS applications
* MicroPython systems
* FPGA logic and Verilog
* Embedded graphical interfaces
* Custom embedded operating-system components
* PCB-based hardware prototypes

### Engineering Approach

```text
Understand
    ↓
Design
    ↓
Build
    ↓
Measure
    ↓
Debug
    ↓
Improve
```

I prefer understanding what happens underneath an abstraction before depending on it.

---

## `02` Featured Projects

### 🖥️ Zeno

**Embedded system environment for ESP32-S3**

[View Repository →](https://github.com/FerrariForever95/Zeno-Micro-PC)

Zeno is an experimental embedded system built around the ESP32-S3, combining MicroPython, ESP-IDF, custom system services, storage, a graphical interface and application execution.

```text
ESP32-S3
   │
   ├── ESP-IDF / FreeRTOS
   │
   ├── MicroPython
   │
   ├── System Services
   │      ├── Storage
   │      ├── Applications
   │      ├── Process Management
   │      └── Package Management
   │
   └── GUI
          ├── Display
          └── Touch
```

#### Engineering Work

* Custom boot and recovery paths
* ESP32-S3 system integration
* Filesystem architecture
* Application execution environment
* Cooperative scheduling
* Native C extensions
* Display-driver integration
* Touch-enabled GUI
* SD-card storage
* MicroPython runtime integration

```text
ESP32-S3
   ↓
Boot
   ↓
Kernel / System Services
   ↓
Runtime
   ↓
Applications
   ↓
Display + Input
```

---

### 🤖 Robot MkII

**Embedded robotics platform**

A hardware-focused robotics platform built around an MCU, inertial sensing, environmental sensing and motor control.

```text
Sensors
   ↓
MCU
   ↓
Control Logic
   ↓
Motor Driver
   ↓
DC Motors
```

Hardware includes:

* MPU6050
* DHT11
* TB6612FNG
* N20 gear motors
* Arduino Nano
* Wireless interfaces
* Li-ion power system

Focus areas:

`Sensor Interfaces` · `Motor Control` · `Embedded Control` · `Power`

---

### ⚡ Shrike FPGA Experiments

**FPGA + microcontroller development**

Exploring digital logic design and hardware acceleration using the Shrike FPGA platform.

```text
Verilog
   ↓
RTL
   ↓
Synthesis
   ↓
FPGA Logic
   ↓
Hardware
```

Areas of interest:

* Verilog
* RTL design
* Digital logic
* FPGA peripherals
* MCU ↔ FPGA interfaces
* Hardware-level experimentation

---

### 🔬 AVR Register-Level Experiments

**Understanding microcontrollers below the Arduino abstraction**

Working directly with MCU registers and peripherals to understand how embedded systems operate underneath higher-level frameworks.

```text
Register
   ↓
Peripheral
   ↓
Interrupt
   ↓
Firmware
   ↓
Application
```

Focus:

`GPIO` · `Timers` · `PWM` · `ADC` · `UART` · `SPI` · `I²C` · `Interrupts`

---

## `03` Hardware

```text
                    DIGITAL HARDWARE
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
        MCU              FPGA            PCB
          │               │               │
      ESP32 / AVR       Verilog       Prototyping
          │               │               │
          └───────────────┼───────────────┘
                          ↓
                       SYSTEM
```

### Microcontrollers

`ESP32` · `ESP32-S3` · `ESP32-C3` · `ESP32-C6` · `ESP8266` · `AVR`

### FPGA

`Renesas FPGA` · `Verilog` · `RTL`

### Hardware Design

`PCB Design` · `Digital Electronics` · `SMD` · `Through-Hole` · `Power Electronics`

### Interfaces

`GPIO` · `UART` · `SPI` · `I²C` · `PWM` · `ADC`

---

## `04` Software & Systems

### Languages

![C](https://img.shields.io/badge/C-111827?style=for-the-badge\&logo=c\&logoColor=A8B9CC)
![C++](https://img.shields.io/badge/C%2B%2B-111827?style=for-the-badge\&logo=cplusplus\&logoColor=00599C)
![Python](https://img.shields.io/badge/Python-111827?style=for-the-badge\&logo=python\&logoColor=3776AB)
![Verilog](https://img.shields.io/badge/Verilog-111827?style=for-the-badge\&logoColor=e2e8f0)
![Assembly](https://img.shields.io/badge/Assembly-111827?style=for-the-badge\&logoColor=e2e8f0)

### Embedded

![ESP32](https://img.shields.io/badge/ESP32-111827?style=for-the-badge\&logo=espressif\&logoColor=E7352E)
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-111827?style=for-the-badge\&logo=freertos\&logoColor=00979D)
![MicroPython](https://img.shields.io/badge/MicroPython-111827?style=for-the-badge\&logo=micropython\&logoColor=2B2728)

### Systems

![Linux](https://img.shields.io/badge/Linux-111827?style=for-the-badge\&logo=linux\&logoColor=FCC624)
![Git](https://img.shields.io/badge/Git-111827?style=for-the-badge\&logo=git\&logoColor=F05032)
![CMake](https://img.shields.io/badge/CMake-111827?style=for-the-badge\&logo=cmake\&logoColor=064F8C)

```text
C / C++
    ↓
Firmware
    ↓
Drivers
    ↓
RTOS / System Software
    ↓
Applications
```

---

## `05` Current Areas of Exploration

```text
FPGA
 ↓
Verilog / RTL
 ↓
Digital System Design
```

```text
ESP32-S3
 ↓
ESP-IDF
 ↓
FreeRTOS
 ↓
MicroPython
 ↓
Embedded Systems
```

```text
AVR
 ↓
Registers
 ↓
Peripherals
 ↓
Bare Metal
```

```text
Hardware
 ↓
PCB
 ↓
Firmware
 ↓
System
```

---

## `06` GitHub Activity

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=FerrariForever95&show_icons=true&theme=transparent&hide_border=true&bg_color=0d1117&title_color=94a3b8&icon_color=64748b&text_color=e2e8f0&ring_color=334155"/>

<img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=FerrariForever95&theme=dark&hide_border=true&background=0d1117&ring=334155&fire=94a3b8&currStreakLabel=e2e8f0&sideLabels=94a3b8&currStreakNum=e2e8f0&sideNums=e2e8f0&dates=64748b"/>

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=FerrariForever95&layout=compact&theme=transparent&hide_border=true&bg_color=0d1117&title_color=94a3b8&text_color=e2e8f0&langs_count=10"/>

</div>

---

## `07` Contribution Graph

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg"/>
  <img alt="GitHub contribution graph" src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg"/>
</picture>

</div>

---

<div align="center">

### Hardware → Firmware → Systems

**Building close to the silicon.**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:111827,70:0f172a,100:020617&height=120&section=footer"/>

</div>
