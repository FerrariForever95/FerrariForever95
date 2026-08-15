<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0a0e1a,60:111827,100:0d1117&height=220&section=header&text=Embedded%20Systems%20Engineer&fontSize=42&fontColor=e2e8f0&animation=fadeIn&fontAlignY=38&desc=Hardware%20%C2%B7%20Firmware%20%C2%B7%20Kernels%20%C2%B7%20Operating%20Systems%20%C2%B7%20IoT%20%C2%B7%20Cloud&descAlignY=58&descSize=16&descAlign=50"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?lines=Building+systems+from+silicon+to+software;Understanding+what+happens+below+the+abstraction+layer;Kernel+Development+%C2%B7+RTOS+%C2%B7+Drivers+%C2%B7+GUI+%C2%B7+Cloud&font=Fira%20Code&center=true&width=700&height=45&color=94a3b8&vCenter=true&size=18&pause=1800&background=00000000"/>

<br/><br/>

[![GitHub Followers](https://img.shields.io/github/followers/YOUR_GITHUB_USERNAME?style=for-the-badge&color=0f172a&labelColor=0d1117&logo=github)](https://github.com/YOUR_GITHUB_USERNAME)
[![Profile Views](https://komarev.com/ghpvc/?username=YOUR_GITHUB_USERNAME&style=for-the-badge&color=0f172a&labelColor=0d1117)](https://github.com/YOUR_GITHUB_USERNAME)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0f172a?style=for-the-badge&logo=linkedin&logoColor=0A66C2&labelColor=0d1117)](https://linkedin.com/in/YOUR_LINKEDIN_USERNAME)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-0f172a?style=for-the-badge&logo=researchgate&logoColor=00CCBB&labelColor=0d1117)](https://www.researchgate.net/profile/YOUR_RESEARCHGATE_PROFILE)
[![Email](https://img.shields.io/badge/Email-0f172a?style=for-the-badge&logo=gmail&logoColor=EA4335&labelColor=0d1117)](mailto:YOUR_EMAIL@example.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-0f172a?style=for-the-badge&logo=vercel&logoColor=ffffff&labelColor=0d1117)](https://YOUR_PORTFOLIO_URL.com)

</div>

<br/>

## `01` About

<table>
<tr>
<td width="50%" valign="top">

### 🔧 What I Build

- Native kernels & schedulers for constrained MCUs
- Bare-metal firmware & interrupt-driven drivers
- RTOS-based embedded applications (FreeRTOS)
- Graphical interfaces for embedded displays
- PCB-to-cloud IoT device pipelines
- Custom toolchains & build systems (CMake)

</td>
<td width="50%" valign="top">

### 🧭 Core Engineering Philosophy

- Understand every layer — never treat hardware as a black box
- Build close to silicon; abstract only when it earns its cost
- Measure before optimizing, debug before assuming
- Prefer deterministic, resource-aware system design
- Systems should be traceable from register to UI

</td>
</tr>
</table>

<div align="center">

```text
Understand  →  Build  →  Measure  →  Debug  →  Improve
```

</div>

<br/>

## `02` System Stack

```text
┌─────────────────────────────────────────────┐
│                   SILICON                    │   PCB · MCU · FPGA
├─────────────────────────────────────────────┤
│                  FIRMWARE                    │   Bare Metal · RTOS · Interrupts
├─────────────────────────────────────────────┤
│                   KERNEL                     │   Scheduler · Memory · Drivers
├─────────────────────────────────────────────┤
│                 GUI / APPS                   │   Display · Applications
├─────────────────────────────────────────────┤
│              IoT / ROBOTICS                  │   Sensors · Connectivity · Control
├─────────────────────────────────────────────┤
│                   CLOUD                      │   APIs · Dashboards · Backends
└─────────────────────────────────────────────┘
```

<br/>

## `03` Flagship Research — Zeno OS

<div align="center">

### **Zeno OS**
#### A Native C-Kernel Embedded Operating System with a Graphical Interface for the ESP32-S3

![Status](https://img.shields.io/badge/STATUS-RESEARCH-0f172a?style=for-the-badge&labelColor=0d1117&color=fbbf24)
![Language](https://img.shields.io/badge/LANGUAGE-C-0f172a?style=for-the-badge&labelColor=0d1117&color=00599C)
![Target](https://img.shields.io/badge/TARGET-ESP32--S3-0f172a?style=for-the-badge&labelColor=0d1117&color=E7352E)
![Type](https://img.shields.io/badge/TYPE-KERNEL-0f172a?style=for-the-badge&labelColor=0d1117&color=94a3b8)

</div>

Zeno OS is a research-oriented embedded operating system built from the ground up for the **ESP32-S3**, exploring kernel architecture, task scheduling, memory management, driver design, and graphics on resource-constrained hardware.

```text
                              ZENO OS
                                 │
                  ┌──────────────┴──────────────┐
                  │                              │
               KERNEL                         DRIVERS
                  │                              │
         ┌────────┴────────┐            ┌────────┴────────┐
         │                 │            │                 │
     Scheduler      Memory Manager   Peripherals     Hardware I/O
         │                 │            │                 │
         └─────────────────┴────────────┴─────────────────┘
                                 │
                                 ▼
                         GUI / Display Subsystem
                                 │
                                 ▼
                             Applications
                                 │
                                 ▼
                              ESP32-S3
```

**Research domains:** `Kernel Development` `Preemptive & Cooperative Scheduling` `Dynamic Memory Management` `Peripheral Drivers` `Graphics Subsystem`

📖 **[Read the Research Paper on ResearchGate →](https://www.researchgate.net/publication/409852826_Zeno_OS_-_A_Native_C-Kernel_Embedded_Operating_System_with_a_Graphical_Interface_for_the_ESP32-S3)**

<br/>

## `04` Project & Status Matrix

<div align="center">

| Project | Problem Statement | Stack | Status |
|:---|:---|:---|:---:|
| **Zeno OS** | Native kernel + GUI for ESP32-S3 from first principles | `C` `ESP32-S3` `Kernel` | ![](https://img.shields.io/badge/Research-fbbf24?style=flat-square&labelColor=0d1117) |
| **YOUR_PROJECT_NAME** | One-sentence problem this project solves | `Tech` `Tags` `Here` | ![](https://img.shields.io/badge/Active-22c55e?style=flat-square&labelColor=0d1117) |
| **YOUR_PROJECT_NAME** | One-sentence problem this project solves | `Tech` `Tags` `Here` | ![](https://img.shields.io/badge/v1.0-3b82f6?style=flat-square&labelColor=0d1117) |
| **YOUR_PROJECT_NAME** | One-sentence problem this project solves | `Tech` `Tags` `Here` | ![](https://img.shields.io/badge/Archived-64748b?style=flat-square&labelColor=0d1117) |

</div>

<br/>

## `05` Technology Stack

<div align="center">

**Languages**

![C](https://img.shields.io/badge/C-111827?style=for-the-badge&logo=c&logoColor=A8B9CC)
![C++](https://img.shields.io/badge/C%2B%2B-111827?style=for-the-badge&logo=cplusplus&logoColor=00599C)
![Python](https://img.shields.io/badge/Python-111827?style=for-the-badge&logo=python&logoColor=3776AB)
![Assembly](https://img.shields.io/badge/Assembly-111827?style=for-the-badge&logo=assemblyscript&logoColor=6E4C13)
![Java](https://img.shields.io/badge/Java-111827?style=for-the-badge&logo=openjdk&logoColor=ED8B00)
![JavaScript](https://img.shields.io/badge/JavaScript-111827?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Dart](https://img.shields.io/badge/Dart-111827?style=for-the-badge&logo=dart&logoColor=0175C2)

**Silicon · MCUs · FPGA**

![ESP32](https://img.shields.io/badge/ESP32%20S3%20C3%20C6-111827?style=for-the-badge&logo=espressif&logoColor=E7352E)
![STM32](https://img.shields.io/badge/STM32-111827?style=for-the-badge&logo=stmicroelectronics&logoColor=03234B)
![AVR](https://img.shields.io/badge/AVR-111827?style=for-the-badge&logo=arduino&logoColor=00979D)
![Renesas](https://img.shields.io/badge/Renesas-111827?style=for-the-badge&logoColor=ffffff)
![FPGA](https://img.shields.io/badge/FPGA%20Logic-111827?style=for-the-badge&logoColor=ffffff)

**Systems & Low-Level**

![Linux](https://img.shields.io/badge/Linux-111827?style=for-the-badge&logo=linux&logoColor=FCC624)
![Bare Metal](https://img.shields.io/badge/Bare%20Metal-111827?style=for-the-badge&logoColor=ffffff)
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-111827?style=for-the-badge&logoColor=00979D)
![Custom Kernels](https://img.shields.io/badge/Custom%20Kernels-111827?style=for-the-badge&logoColor=ffffff)
![Drivers](https://img.shields.io/badge/Drivers-111827?style=for-the-badge&logoColor=ffffff)
![Interrupts](https://img.shields.io/badge/Interrupt%20Subsystems-111827?style=for-the-badge&logoColor=ffffff)

**Hardware & Protocols**

![PCB](https://img.shields.io/badge/PCB%20Design-111827?style=for-the-badge&logoColor=ffffff)
![Digital Electronics](https://img.shields.io/badge/Digital%20Electronics-111827?style=for-the-badge&logoColor=ffffff)
![UART](https://img.shields.io/badge/UART-111827?style=for-the-badge&logoColor=ffffff)
![SPI](https://img.shields.io/badge/SPI-111827?style=for-the-badge&logoColor=ffffff)
![I2C](https://img.shields.io/badge/I2C-111827?style=for-the-badge&logoColor=ffffff)
![CAN](https://img.shields.io/badge/CAN-111827?style=for-the-badge&logoColor=ffffff)
![GPIO](https://img.shields.io/badge/GPIO-111827?style=for-the-badge&logoColor=ffffff)
![PWM](https://img.shields.io/badge/PWM-111827?style=for-the-badge&logoColor=ffffff)
![ADC](https://img.shields.io/badge/ADC-111827?style=for-the-badge&logoColor=ffffff)

**Tooling & Cloud**

![CMake](https://img.shields.io/badge/CMake-111827?style=for-the-badge&logo=cmake&logoColor=064F8C)
![Git](https://img.shields.io/badge/Git-111827?style=for-the-badge&logo=git&logoColor=F05032)
![Docker](https://img.shields.io/badge/Docker-111827?style=for-the-badge&logo=docker&logoColor=2496ED)
![GCP](https://img.shields.io/badge/Google%20Cloud-111827?style=for-the-badge&logo=googlecloud&logoColor=4285F4)
![MicroPython](https://img.shields.io/badge/MicroPython-111827?style=for-the-badge&logo=micropython&logoColor=2B2728)
![scrcpy](https://img.shields.io/badge/scrcpy-111827?style=for-the-badge&logoColor=ffffff)

</div>

<br/>

## `06` Telemetry

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=YOUR_GITHUB_USERNAME&show_icons=true&theme=transparent&hide_border=true&bg_color=0d1117&title_color=94a3b8&icon_color=64748b&text_color=e2e8f0&ring_color=334155"/>
<img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=YOUR_GITHUB_USERNAME&theme=dark&hide_border=true&background=0d1117&ring=334155&fire=94a3b8&currStreakLabel=e2e8f0&sideLabels=94a3b8&currStreakNum=e2e8f0&sideNums=e2e8f0&dates=64748b"/>

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_GITHUB_USERNAME&layout=compact&theme=transparent&hide_border=true&bg_color=0d1117&title_color=94a3b8&text_color=e2e8f0&langs_count=10"/>

<br/><br/>

<img src="https://github-profile-trophy.vercel.app/?username=YOUR_GITHUB_USERNAME&theme=darkhub&no-frame=true&no-bg=true&margin-w=8&column=7"/>

</div>

<br/>

## `07` Contribution Graph

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME/output/github-contribution-grid-snake.svg"/>
  <img alt="contribution snake" src="https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME/output/github-contribution-grid-snake-dark.svg"/>
</picture>

<sub>Generated via <a href="https://github.com/Platane/snk">Platane/snk</a> — requires a scheduled GitHub Action on your profile repo.</sub>

</div>

<br/>

<div align="center">

### Embedded Systems · Operating Systems · Hardware · IoT

**Building systems from silicon to software.**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0a0e1a,60:111827,100:0d1117&height=120&section=footer"/>

</div>
