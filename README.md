<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0a0e1a,60:111827,100:0d1117&height=220&section=header&text=Embedded%20Systems%20Engineer&fontSize=42&fontColor=e2e8f0&animation=fadeIn&fontAlignY=38&desc=Hardware%20%C2%B7%20Firmware%20%C2%B7%20Kernels%20%C2%B7%20Operating%20Systems%20%C2%B7%20IoT%20%C2%B7%20Cloud&descAlignY=58&descSize=16&descAlign=50"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?lines=Building+systems+from+silicon+to+software;Understanding+what+happens+below+the+abstraction+layer;Kernel+Development+%C2%B7+RTOS+%C2%B7+Drivers+%C2%B7+GUI+%C2%B7+Cloud&font=Fira%20Code&center=true&width=700&height=45&color=94a3b8&vCenter=true&size=18&pause=1800&background=00000000"/>

<br/><br/>

[![GitHub Followers](https://img.shields.io/github/followers/FerrariForever95?style=for-the-badge&color=0f172a&labelColor=0d1117&logo=github)](https://github.com/FerrariForever95)
[![Profile Views](https://komarev.com/ghpvc/?username=FerrariForever95&style=for-the-badge&color=0f172a&labelColor=0d1117)](https://github.com/FerrariForever95)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0f172a?style=for-the-badge&logo=linkedin&logoColor=0A66C2&labelColor=0d1117)](https://www.linkedin.com/in/shanmukha-marthi-aa78043b1/)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-0f172a?style=for-the-badge&logo=researchgate&logoColor=00CCBB&labelColor=0d1117)](https://www.researchgate.net/profile/Marthi-Viswanadh)
[![Email](https://img.shields.io/badge/Email-0f172a?style=for-the-badge&logo=gmail&logoColor=EA4335&labelColor=0d1117)](mailto:shanmukhamarthi@gmail.com)

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

## `03` Flagship Project — Zeno OS / Zeno Micro PC

<div align="center">

### **Zeno OS**
#### A Sandboxed, Edge-Computing Operating System for Constrained Microcontroller Platforms

![Status](https://img.shields.io/badge/STATUS-ACTIVE-0f172a?style=for-the-badge&labelColor=0d1117&color=22c55e)
![Language](https://img.shields.io/badge/LANGUAGE-MicroPython%20%2F%20C-0f172a?style=for-the-badge&labelColor=0d1117&color=3776AB)
![Target](https://img.shields.io/badge/TARGET-ESP32--S3--N16R8-0f172a?style=for-the-badge&labelColor=0d1117&color=E7352E)
![License](https://img.shields.io/badge/LICENSE-EPL--2.0-0f172a?style=for-the-badge&labelColor=0d1117&color=94a3b8)

</div>

Zeno OS (shipped as **Zeno Micro PC**) is a solo research and engineering project exploring how far a general-purpose, multi-application OS experience — process-like isolation, a hierarchical filesystem, a POSIX-flavored shell, a graphical desktop, package management, and networked services — can be pushed onto a single SoC with kilobytes, not gigabytes, of usable RAM. It runs a MicroPython execution core on ESP-IDF, driving an ILI9488/ILI9341-class parallel LCD with touch, and was presented publicly at the SCSVMV engineering symposium.

```text
L6 — Applications        (Home/APPS/*)
L5 — Shell                ZenCMD — POSIX-flavored interpreter
L4 — OS Services           Storage · Networking · Process · Package Mgmt
L3 — Kernel & Capability   Multi-path fail-safe boot, capability-gated auth
L2 — MicroPython VM       moclcd (native display driver) · zfs (private FS)
L1 — ESP-IDF / FreeRTOS   Partitioning, drivers, RTOS scheduler
L0 — Hardware              ESP32-S3-N16R8 · ILI9488 LCD · SD · Radio
```

**Engineering highlights:** capability-gated multi-path boot (`kernel.c` / `kernel.py` / `safe.py` / `recovery.py`) · cooperative task scheduler with EWMA execution-time estimation · dual-tier storage (user VFS + mutex-guarded private `zfs`/LittleFS2 kernel partition) · disposable, sandboxed application execution with guaranteed namespace cleanup · ~30-widget native-backed GUI toolkit · roadmap toward a dual-domain **SCPU/GCPU** architecture separating system logic from rendering.

**Domains:** `Kernel & Boot Design` `Cooperative Scheduling` `Filesystem Architecture` `Native C Extensions` `GUI Toolkit` `Fault Isolation`

📦 **[View the repository →](https://github.com/FerrariForever95/Zeno-Micro-PC)**

<br/>

## `04` Project & Status Matrix

<div align="center">

| Project | Problem Statement | Stack | Status |
|:---|:---|:---|:---:|
| **[Zeno Micro PC](https://github.com/FerrariForever95/Zeno-Micro-PC)** | Turns an ESP32-S3 into a sandboxed, touchscreen microcomputer with a full OS stack | `MicroPython` `ESP-IDF` `ESP32-S3` `C` | ![](https://img.shields.io/badge/Active-22c55e?style=flat-square&labelColor=0d1117) |
| **YOUR_PROJECT_NAME** | One-sentence problem this project solves | `Tech` `Tags` `Here` | ![](https://img.shields.io/badge/Active-22c55e?style=flat-square&labelColor=0d1117) |
| **YOUR_PROJECT_NAME** | One-sentence problem this project solves | `Tech` `Tags` `Here` | ![](https://img.shields.io/badge/v1.0-3b82f6?style=flat-square&labelColor=0d1117) |

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

<img height="165" src="https://github-readme-stats.vercel.app/api?username=FerrariForever95&show_icons=true&theme=transparent&hide_border=true&bg_color=0d1117&title_color=94a3b8&icon_color=64748b&text_color=e2e8f0&ring_color=334155"/>
<img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=FerrariForever95&theme=dark&hide_border=true&background=0d1117&ring=334155&fire=94a3b8&currStreakLabel=e2e8f0&sideLabels=94a3b8&currStreakNum=e2e8f0&sideNums=e2e8f0&dates=64748b"/>

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=FerrariForever95&layout=compact&theme=transparent&hide_border=true&bg_color=0d1117&title_color=94a3b8&text_color=e2e8f0&langs_count=10"/>

<br/><br/>

<img src="https://github-profile-trophy.vercel.app/?username=FerrariForever95&theme=darkhub&no-frame=true&no-bg=true&margin-w=8&column=7"/>

</div>

<br/>

## `07` Contribution Graph

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/FerrariForever95/FerrariForever95/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/FerrariForever95/FerrariForever95/output/github-contribution-grid-snake.svg"/>
  <img alt="contribution snake" src="https://raw.githubusercontent.com/FerrariForever95/FerrariForever95/output/github-contribution-grid-snake-dark.svg"/>
</picture>

<sub>Generated via <a href="https://github.com/Platane/snk">Platane/snk</a> — requires a scheduled GitHub Action on your profile repo.</sub>

</div>

<br/>

<div align="center">

### Embedded Systems · Operating Systems · Hardware · IoT

**Building systems from silicon to software.**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0a0e1a,60:111827,100:0d1117&height=120&section=footer"/>

</div>
