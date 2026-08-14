<div align="center">

<img src="./assets/profile-banner.svg" width="100%" alt="Embedded Systems Engineer"/>

# ⚡ Embedded Systems • Hardware • Software • Cloud

### Building systems from **PCB → Firmware → FPGA → Kernel → UI → IoT → Cloud**

**Embedded Systems Engineer · Hardware Designer · Systems Programmer · Researcher**

<br>

[![C](https://img.shields.io/badge/C-111827?style=for-the-badge\&logo=c\&logoColor=A8B9CC)](https://en.wikipedia.org/wiki/C_%28programming_language%29)
[![C++](https://img.shields.io/badge/C%2B%2B-111827?style=for-the-badge\&logo=cplusplus\&logoColor=00599C)](https://isocpp.org/)
[![ESP32](https://img.shields.io/badge/ESP32-111827?style=for-the-badge\&logo=espressif\&logoColor=E7352C)](https://www.espressif.com/)
[![STM32](https://img.shields.io/badge/STM32-111827?style=for-the-badge\&logo=stmicroelectronics\&logoColor=03234B)](https://www.st.com/)
[![Linux](https://img.shields.io/badge/Linux-111827?style=for-the-badge\&logo=linux\&logoColor=FCC624)](https://www.linux.org/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-111827?style=for-the-badge\&logo=googlecloud\&logoColor=4285F4)](https://cloud.google.com/)

</div>

---

## 👨‍💻 About Me

I'm an engineer focused on **building complete systems from the hardware level upward**.

With **8+ years of experience in embedded systems**, I work across electronics, PCB design, microcontrollers, FPGA, firmware, device drivers, operating systems, graphical interfaces, web applications, IoT, robotics, and cloud-connected systems.

I enjoy working close to the hardware — understanding the architecture, designing the electronics, writing the firmware, developing the software stack, and connecting the finished system to the outside world.

```text
                    ┌─────────────────┐
                    │    CLOUD / WEB  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   IoT / ROBOTICS│
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   GUI / TUI     │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   OS / KERNEL   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ FIRMWARE / RTOS │
                    └────────┬────────┘
                             │
                 ┌───────────▼───────────┐
                 │      MCU / FPGA       │
                 └───────────┬───────────┘
                             │
                    ┌────────▼────────┐
                    │   PCB / HARDWARE│
                    └─────────────────┘
```

---

# 🧩 What I Build

<table>
<tr>
<td width="50%" valign="top">

### 🔩 Hardware

* PCB design
* Schematic design
* Digital electronics
* MCU-based hardware
* Sensor interfaces
* Communication interfaces
* Hardware/software co-design
* Prototyping

</td>
<td width="50%" valign="top">

### ⚙️ Embedded

* Firmware
* Embedded C/C++
* Bare-metal systems
* Device drivers
* RTOS
* Peripheral programming
* Interrupts & timers
* Hardware abstraction

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🧠 Systems

* Operating systems
* Kernel development
* Embedded OS
* Memory management
* Scheduling
* Low-level programming
* System architecture
* Linux

</td>
<td width="50%" valign="top">

### 🔬 FPGA

* FPGA programming
* Digital logic
* Programmable hardware
* Digital system architecture
* Hardware/software co-design
* FPGA-based embedded systems

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🖥️ Interfaces

* Embedded GUI
* Desktop GUI
* TUI
* Display systems
* Web interfaces
* Dashboards
* Device configuration tools

</td>
<td width="50%" valign="top">

### ☁️ Connected Systems

* IoT
* Smart devices
* Robotics
* Cloud-connected hardware
* Google Cloud
* Web applications
* Backend systems
* Device telemetry

</td>
</tr>
</table>

---

# 🛠️ Technology Stack

### Languages

<p>
<img src="https://skillicons.dev/icons?i=c,cpp,python,java,js" />
</p>

**C · C++ · Embedded C · Python · Java · JavaScript**

### Embedded & Hardware

<p>
<img src="https://skillicons.dev/icons?i=arduino,esp32,stm32,raspberrypi" />
</p>

**ESP8266 · ESP32 · ESP32-S3 · ESP32-C3 · ESP32-C6 · STM32 · Renesas · AVR · Arduino · Raspberry Pi**

### Systems

**Bare Metal · Firmware · Device Drivers · RTOS · Operating Systems · Kernel Development · Linux**

### Hardware & Communication

**PCB Design · Electronics · FPGA · Digital Logic · UART · SPI · I²C · CAN · GPIO · PWM · ADC**

### Software & Cloud

<p>
<img src="https://skillicons.dev/icons?i=linux,git,github,cmake,gcp" />
</p>

**Linux · Git · GitHub · CMake · Google Cloud · Web Development · IoT**

---

# 🚀 Featured Project

## 🖥️ Zeno OS

<div align="center">

### **A Native C-Kernel Embedded Operating System for ESP32-S3**

`C` · `ESP32-S3` · `Kernel` · `Embedded OS` · `GUI` · `Research`

</div>

**Zeno OS** is my research-oriented embedded operating system built from the ground up for the **ESP32-S3**.

The project explores how operating-system concepts can be implemented directly on resource-constrained microcontroller hardware.

### Core areas

* Native C kernel
* Hardware initialization
* Memory management
* Scheduling
* Device drivers
* Peripheral management
* Embedded graphics
* GUI development
* Application execution
* Low-level hardware integration

### Architecture

```text
                     ZENO OS
                        │
          ┌─────────────┴─────────────┐
          │                           │
       KERNEL                      DRIVERS
          │                           │
     ┌────┴────┐               ┌──────┴──────┐
     │         │               │             │
 Scheduler  Memory         Peripherals    Hardware
            Manager                         I/O
     │         │               │             │
     └─────────┴───────────────┴─────────────┘
                        │
                   GUI / DISPLAY
                        │
                   APPLICATIONS
                        │
                    ESP32-S3
```

📄 **Research Paper:**
[Zeno OS — ResearchGate](https://www.researchgate.net/publication/409852826_Zeno_OS_-_A_Native_C-Kernel_Embedded_Operating_System_with_a_Graphical_Interface_for_the_ESP32-S3)

---

# 🤖 IoT & Robotics

I build **smart devices and robotic systems** that combine electronics, embedded software, sensors, connectivity, control logic, and cloud services.

Typical architecture:

```text
Sensors / Actuators
        │
        ▼
   MCU / Raspberry Pi
        │
        ▼
 Firmware / Control
        │
        ▼
 Connectivity
        │
        ├──────────────► Local GUI / TUI
        │
        ▼
      IoT Backend
        │
        ▼
   Google Cloud
        │
        ▼
 Web / Dashboard / Data
```

This lets me work across the entire lifecycle of a connected device — **from the circuit board to the cloud**.

---

# 🌐 Web & Application Development

Although my core background is embedded and systems engineering, I also develop software beyond the device.

### I build:

* Websites
* Web applications
* APIs
* IoT dashboards
* Device management interfaces
* Monitoring systems
* Configuration tools
* GUI applications
* Terminal applications
* Cloud-connected applications

I particularly enjoy building software that interacts directly with **real hardware and physical systems**.

---

# 🔌 Hardware Interfaces

<p align="center">

`UART` · `SPI` · `I²C` · `CAN` · `GPIO` · `PWM` · `ADC` · `Timers` · `Interrupts`

</p>

---

# 🔬 Engineering Focus

My interests sit at the intersection of several engineering disciplines:

```text
 ELECTRONICS
      │
      ▼
  PCB DESIGN
      │
      ▼
  MCU / FPGA
      │
      ▼
   FIRMWARE
      │
      ▼
 DRIVERS / RTOS
      │
      ▼
 OS / KERNEL
      │
      ▼
 GUI / TUI / WEB
      │
      ▼
    IoT
      │
      ▼
 ROBOTICS
      │
      ▼
 GOOGLE CLOUD
```

---

# 🧪 Things I Like Building

```text
┌──────────────────────────────────────────┐
│                                          │
│   🔩 Custom PCB Hardware                 │
│   ⚡ FPGA Systems                         │
│   🔧 Embedded Firmware                   │
│   🧠 Operating Systems                   │
│   ⚙️ Device Drivers                      │
│   🖥️ Embedded GUIs                       │
│   ⌨️ TUIs                                │
│   🌐 Websites & Applications             │
│   📡 IoT Devices                         │
│   🏠 Smart Devices                       │
│   🤖 Robots                              │
│   🍓 Raspberry Pi Systems                │
│   ☁️ Cloud-Connected Hardware            │
│   🔬 Experimental Systems                │
│                                          │
└──────────────────────────────────────────┘
```

---

# 📊 Technical Overview

| Domain         | Technologies                                                      |
| -------------- | ----------------------------------------------------------------- |
| **Languages**  | C, C++, Embedded C, Python, Java, JavaScript                      |
| **MCUs**       | ESP8266, ESP32, ESP32-S3, ESP32-C3, ESP32-C6, STM32, Renesas, AVR |
| **Platforms**  | Arduino, ESP-IDF, Raspberry Pi                                    |
| **Hardware**   | PCB Design, Electronics, Schematics, Prototyping                  |
| **FPGA**       | FPGA Programming, Digital Logic, Hardware/Software Co-design      |
| **Firmware**   | Bare Metal, Drivers, Peripheral Programming                       |
| **Systems**    | RTOS, Operating Systems, Kernel Development                       |
| **Interfaces** | UART, SPI, I²C, CAN, GPIO, PWM, ADC                               |
| **Graphics**   | Embedded GUI, GUI, TUI, Display Systems                           |
| **Web**        | Websites, Web Applications, APIs, Dashboards                      |
| **IoT**        | Smart Devices, Telemetry, Connected Systems                       |
| **Robotics**   | Sensors, Actuators, Control, Embedded Robotics                    |
| **Cloud**      | Google Cloud, Cloud-connected Systems                             |
| **Tools**      | Linux, Git, GitHub, CMake                                         |

---

# ⚡ Engineering Philosophy

> **Build close to the hardware. Understand every layer.**

I don't want to only use systems — I want to understand how they work.

From **PCB traces and microcontroller registers** to **firmware, drivers, kernels, graphical interfaces, robots, websites, and cloud infrastructure**, I enjoy exploring the complete technology stack.

<div align="center">

### **Hardware → Software → Systems → Cloud**

**Building things from the ground up. ⚙️**

</div>
