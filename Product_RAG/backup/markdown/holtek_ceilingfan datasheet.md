# HT32F65532G


# Datasheet


**32-Bit Arm**
**®**
** Cortex**
**®**
**-M0+ BLDC Microcontroller**


**with 3-channel 48 V Half-bridge Gate-Driver,**


**up to 32 KB Flash and 4 KB SRAM with 2 MSPS ADC,**


**CMP, OPA, USART, UART, SPI, I**
**2**
**C, MCTM, GPTM,**


**SCTM,  BFTM, CRC, LSTM, WDT, DIV and PDMA**


Revision: V1.00    Date: April 29, 2022


Rev. 1.00	
2 of 55
April 29, 2022


**Table of Contents**


## Table of Contents


**1  General Description................................................................................................. 7**


**2  Features.................................................................................................................... 8**


Core........................................................................................................................................8


On-Chip Memory....................................................................................................................8


Flash Memory Controller – FMC............................................................................................. 8


Reset Control Unit – RSTCU.................................................................................................. 9


Clock Control Unit – CKCU.....................................................................................................9


Power Management Control Unit – PWRCU.......................................................................... 9


Gate-Driver...........................................................................................................................10


External Interrupt/Event Controller – EXTI........................................................................... 10


Analog to Digital Converter – ADC....................................................................................... 10


Operational Amplifier – OPA................................................................................................. 11


Comparator – CMP............................................................................................................... 11


I/O Ports – GPIO................................................................................................................... 11


Motor Control Timer – MCTM...............................................................................................12


General-Purpose Timer – GPTM.......................................................................................... 12


Single Channel Timer – SCTM............................................................................................. 13


Basic Function Timer – BFTM.............................................................................................. 13


Watchdog Timer – WDT........................................................................................................13


Low Speed Timer – LSTM....................................................................................................14


Inter-integrated Circuit – I
2
C.................................................................................................14


Serial Peripheral Interface – SPI.......................................................................................... 14


Universal Asynchronous Receiver Transmitter – UART....................................................... 15


Universal Synchronous Asynchronous Receiver Transmitter – USART............................... 15


Cyclic Redundancy Check – CRC........................................................................................ 16


Peripheral Direct Memory Access – PDMA.......................................................................... 16


Hardware Divider – DIV........................................................................................................17


Debug Support......................................................................................................................17


Package and Operation Temperature................................................................................... 17


**3  Overview................................................................................................................. 18**


Device Information................................................................................................................18


Block Diagram......................................................................................................................19


Memory Map.........................................................................................................................20


Clock Structure.....................................................................................................................23


Rev. 1.00	
3 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**Table of Contents**


**4  Gate-Driver............................................................................................................. 24**


5 V Voltage Regulator...........................................................................................................24


12 V Voltage Regulator.........................................................................................................24


Bootstrap Circuit Operation..................................................................................................24


Gate-Driver Control Logic.....................................................................................................27


Protection Function Operation..............................................................................................28


Power Supply Input Under Voltage Lock-Out – VCC_UVLO........................................................... 28
Bootstrap Output Under Voltage Lock-Out – VBST_UVLO............................................................. 28
12 V LDO Output Under Voltage Lock-Out – V12P_UVLO............................................................. 28
5 V LDO Output Under Voltage Lock-Out – VREG_UVLO.............................................................. 28
Over Temperature Protection – OTP............................................................................................... 29


Component Selections..........................................................................................................29


Gate Resistor Circuit........................................................................................................................ 29
Bootstrap Capacitor......................................................................................................................... 29
Current Sensing Resistors............................................................................................................... 29
Gate-Driver Supply Capacitor.......................................................................................................... 30
Power Supply Bypass Capacitor..................................................................................................... 30
Power Supply Input Series Resistor................................................................................................ 30
RC Snubbers................................................................................................................................... 30
Motor Supply Capacitor................................................................................................................... 30
12 V LDO Output Capacitor............................................................................................................. 30
5 V LDO Output Capacitor............................................................................................................... 30
Voltage Clamp Circuit...................................................................................................................... 30


**5  Pin Assignment...................................................................................................... 31**


Internal Connection Signal Lines.......................................................................................... 35


**6  Application Circuits............................................................................................... 36**


Typical Application Circuit – 1-Shunt Current Sensing......................................................... 36


**7  Electrical Characteristics...................................................................................... 37**


Absolute Maximum Ratings..................................................................................................37


Recommended DC Operating Conditions............................................................................ 37


On-Chip LDO Voltage Regulator Characteristics.................................................................. 38


Power Consumption.............................................................................................................38


Reset and Supply Monitor Characteristics............................................................................ 39


External Clock Characteristics..............................................................................................40


Internal Clock Characteristics...............................................................................................41


System PLL Characteristics..................................................................................................41


Memory Characteristics........................................................................................................42


I/O Port Characteristics.........................................................................................................42


ADC Characteristics.............................................................................................................43


Rev. 1.00	
4 of 55
April 29, 2022


**Table of Contents**


Comparator Characteristics..................................................................................................45


Operational Amplifier Characteristics.................................................................................... 45


MCTM/GPTM/SCTM Characteristics.................................................................................... 46


Gate-Driver Characteristics..................................................................................................46


I
2
C Characteristics................................................................................................................49


SPI Characteristics...............................................................................................................50


**8  Package Information............................................................................................. 52**


48-pin LQFP-EP (7mm × 7mm) Outline Dimensions............................................................ 53


SAW Type 32-pin QFN (4mm × 4mm × 0.75mm) Outline Dimensions................................. 54


Rev. 1.00	
5 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**List of Tables**


## List of Tables


Table 1.  Features and Peripheral List............................................................................................. 18
Table 2.  Register Map..................................................................................................................... 21
Table 3.  Gate-Driver Operation Truth Table.................................................................................... 27
Table 4.  Protection Function Conditions......................................................................................... 28
Table 5.  Pin Alternate Function....................................................................................................... 33
Table 6.  Pin Description.................................................................................................................. 34
Table 7.  Internal Connection Signal Lines...................................................................................... 35
Table 8.  Absolute Maximum Ratings............................................................................................... 37
Table 9.  Recommended DC Operating Conditions......................................................................... 37
Table 10.  LDO Characteristics........................................................................................................ 38
Table 11.  Power Consumption Characteristics............................................................................... 38
Table 12.  V
DD
 Power Reset Characteristics.................................................................................... 39
Table 13.  LVD/BOD Characteristics................................................................................................ 40
Table 14.  High Speed External Clock (HSE) Characteristics.......................................................... 40
Table 15.  High Speed Internal Clock (HSI) Characteristics............................................................ 41
Table 16.  Low Speed Internal Clock (LSI) Characteristics.............................................................. 41
Table 17.  System PLL Characteristics............................................................................................ 41
Table 18.  Flash Memory Characteristics......................................................................................... 42
Table 19.  I/O Port Characteristics................................................................................................... 42
Table 20.  ADC Characteristics........................................................................................................ 43
Table 21.  Comparator Characteristics............................................................................................ 45
Table 22.  Operational Amplifier Characteristics.............................................................................. 45
Table 23.  MCTM / GPTM / SCTM Characteristics.......................................................................... 46
Table 24.  Gate-Driver Characteristics............................................................................................. 46
Table 25.  I
2
C Characteristics........................................................................................................... 49
Table 26.  SPI Characteristics.......................................................................................................... 50


Rev. 1.00	
6 of 55
April 29, 2022


**List of Figures**


## List of Figures


Figure 1.  Block Diagram................................................................................................................. 19
Figure 2.  Memory Map.................................................................................................................... 20
Figure 3.  Clock Structure................................................................................................................ 23
Figure 4.  Bootstrap Capacitor (C
B
) Charging Current Path............................................................ 25
Figure 5.  Bootstrap Capacitor Charging Time (t
BST
)........................................................................ 26
Figure 6.  Bootstrap Capacitor (C
B
) Discharging Current Path........................................................ 26
Figure 7.  6-Wire Control................................................................................................................. 27
Figure 8.  Gate Voltage (V
GS
) Rising Time (t
r
) and Falling Time (t
f
).................................................. 29
Figure 9.  48-pin LQFP-EP Pin Assignment.................................................................................... 31
Figure 10.  32-pin QFN Pin Assignment.......................................................................................... 32
Figure 11.  1-Shunt FOC Application Circuit ................................................................................... 36
Figure 12.  ADC Sampling Network Model...................................................................................... 44
Figure 13.  Gate Drive Timing Diagram........................................................................................... 48
Figure 14.  I
2
C Timing Diagram........................................................................................................ 49
Figure 15.  SPI Timing Diagram – SPI Master Mode....................................................................... 51
Figure 16.  SPI Timing Diagram – SPI Slave Mode with CPHA = 1................................................ 51


Rev. 1.00	
7 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**1  General Description**


# 1 
# 1 
##  General Description


The Holtek HT32F65532G device is a high performance, low power consumption 32-bit 
microcontroller based around an Arm
®
 Cortex
®
-M0+ processor core. The Cortex
®
-M0+ is a next-
generation processor core which is tightly coupled with Nested Vectored Interrupt Controller 
(NVIC), SysTick timer and advanced debug support.


The device operates at a frequency of up to 60 MHz with a Flash accelerator to obtain maximum 
efficiency. It provides 32 KB of embedded Flash memory for code/data storage and 4 KB of 
embedded SRAM memory for system operation and application program usage. A variety of 
peripherals, such as Hardware Divider DIV, ADC, OPA, CMP, I
2
C, USART, UART, SPI, MCTM, 
GPTM, SCTM, BFTM, CRC-16/32, LSTM, WDT, PDMA, SW-DP (Serial Wire Debug Port), 
etc., are also implemented in the device. Several power saving modes provide the flexibility for 
maximum optimization between wakeup latency and power consumption, an especially important 
consideration in low power applications.


The device also includes a gate-driver for 3-phase motor driving applications. The gate-driver has 
several internal protection functions and provides an integrated 5V low quiescent current LDO 
which can provide power supply for external circuits.


The above features ensure that the device is suitable for use in a wide range of applications, 
especially in areas such as electric scooters, kitchen ventilators, vacuum cleaners, pumps, funs and 
so on.


Rev. 1.00	
8 of 55
April 29, 2022


**2  Features**


# 2 
# 2 
##  Features


**Core**


	
▆
32-bit Arm
®
 Cortex
®
-M0+ processor core


	
▆
Up to 60 MHz operating frequency


	
▆
Single-cycle multiplication


	
▆
Integrated Nested Vectored Interrupt Controller (NVIC)


	
▆
24-bit SysTick timer


The Cortex
®
-M0+ processor is a very low gate count, highly energy efficient processor that is 
intended for microcontroller and deeply embedded applications that require an area optimized, 
low-power processor. The processor is based on the ARMv6-M architecture and supports Thumb
®
 
instruction sets, single-cycle I/O ports, hardware multiplier and low latency interrupt respond time.


**On-Chip Memory**


	
▆
32 KB on-chip Flash memory for instruction/data and options storage


	
▆
4 KB on-chip SRAM


	
▆
Supports multiple booting modes


The Arm
®
 Cortex
®
-M0+ processor access and debug access share the single external interface to 
external AHB peripherals. The processor access takes priority over debug access. The maximum 
address range of the Cortex
®
-M0+ is 4 GB since it has a 32-bit bus address width. Additionally, 
a pre-defined memory map is provided by the Cortex
®
-M0+ processor to reduce the software 
complexity of repeated implementation by different device vendors. However, some regions are 
used by the Arm
®
 Cortex
®
-M0+ system peripherals. Refer to the Arm
®
 Cortex
®
-M0+ Technical 
Reference Manual for more information. Figure 2 in the Overview chapter shows the memory map 
of the HT32F65532G device, including code, SRAM, peripheral and other pre-defined regions.


**Flash Memory Controller – FMC**


	
▆
Flash accelerator to obtain maximum efficiency


	
▆
32-bit word programming with In System Programming Interface (ISP) and In Application 


Programming (IAP)


	
▆
Flash protection capability to prevent illegal access


The Flash Memory Controller, FMC, provides all the necessary functions and pre-fetch buffer for 
the embedded on-chip Flash Memory. Since the access speed of the Flash Memory is slower than 
the CPU, a wide access interface with a pre-fetch buffer is provided for the Flash Memory in order 
to reduce the CPU waiting time which will cause CPU instruction execution delays. Flash Memory 
word programming/page erase functions are also provided.


Rev. 1.00	
9 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**2  Features**


**Reset Control Unit – RSTCU**


	
▆
Supply supervisor


	
●
Power On Reset / Power Down Reset – POR / PDR


	
●
Brown-Out Detector – BOD


	
●
Programmable Low Voltage Detector – LVD


The Reset Control Unit, RSTCU, has three kinds of reset, a power on reset, a system reset and an 
APB unit reset. The power on reset, known as a cold reset, resets the full system during power up. 
A system reset resets the processor core and peripheral IP components with the exception of the 
SW-DP controller. The resets can be triggered by external signals, internal events and the reset 
generators.


**Clock Control Unit – CKCU**


	
▆
External 4 to 16 MHz crystal oscillator


	
▆
Internal 8 MHz RC oscillator trimmed to ± 2 % accuracy at 3.3 V operating voltage and 25 °C 


operating temperature


	
▆
Internal 32 kHz RC oscillator


	
▆
Integrated system clock PLL 


	
▆
Independent clock divider and gating bits for peripheral clock sources


The Clock Control Unit, CKCU, provides a range of oscillator and clock functions. These include 
High Speed Internal RC oscillator (HSI), High Speed External crystal oscillator (HSE), Low Speed 
Internal RC oscillator (LSI), Phase Lock Loop (PLL), HSE clock monitor, clock prescaler, clock 
multiplexer, APB clock divider and gating circuitry. The clocks of AHB, APB and Cortex
®
-M0+ 
are derived from system clock (CK_SYS) which can come from HSI, HSE, LSI or system PLL. 
Watchdog Timer (WDT) and Low Speed Timer (LSTM) use the LSI as their clock source.


**Power Management Control Unit – PWRCU**


	
▆
V
DD
 power supply: 2.5 V to 5.5 V


	
▆
Integrated 1.5 V LDO regulator for MCU core, peripherals and memories power supply


	
▆
V
DD
 and V
CORE
 power domains


	
▆
Two power saving modes: Sleep and Deep-Sleep modes


Power consumption can be regarded as one of the most important issues for many embedded 
system applications. Accordingly the Power Control Unit, PWRCU, in the device provides two 
types of power saving modes which are the Sleep and Deep-Sleep modes. These operating modes 
reduce the power consumption and allow the application to achieve the best trade-off between the 
conflicting demands of CPU operating time, speed and power consumption.


Rev. 1.00	
10 of 55
April 29, 2022


**2  Features**


**Gate-Driver**


	
▆
Wide power supply range: V
CC
 = 6 V ~ 40 V


	
▆
Maximum motor sustainable voltage up to 48 V


	
▆
3-channel half-bridge driver: Drives 3 high-side and 3 low-side N-type MOSFETs


	
▆
Integrated 5 V LDO regulator (V
REG
) with 50mA output drive current


	
▆
Integrated gate-driver power supplies:


	
●
High-side bootstrap driving: supports up to 50 kHz PWM operation


	
●
Low-side driving: 12 V linear regulator (V
12P
)


	
▆
Integrated 120ns fixed dead time control


	
▆
High-side and low-side gate-driver control


	
●
High-side: High active (INHx) 


	
●
Low-side: Low active (INLx)


	
▆
Protection features


	
●
V
CC
 Under Voltage Lock-Out (VCC_UVLO)


	
●
V
BSTx
 Under Voltage Lock-Out (VBST_UVLO)


	
●
V
12P
 Under Voltage Lock-Out (V12P_UVLO)


	
●
V
REG
 Under Voltage Lock-Out (VREG_UVLO)


	
●
Over Temperature Protection (OTP)


**External Interrupt/Event Controller – EXTI**


	
▆
Up to 16 EXTI lines with configurable trigger source and type


	
▆
All GPIO pins can be selected as EXTI trigger source


	
▆
Source trigger type includes high level, low level, negative edge, positive edge or both edges


	
▆
Individual interrupt enable, wakeup enable and status bits for each EXTI line


	
▆
Software interrupt trigger mode for each EXTI line


	
▆
Integrated deglitch filter for short pulse blocking


The External Interrupt/Event Controller, EXTI, comprises 16 edge detectors which can generate 
wake-up events or interrupt requests independently. Each EXTI line can also be masked 
independently.


**Analog to Digital Converter – ADC**


	
▆
12-bit SAR ADC engine


	
▆
Up to 2 Msps conversion rate


	
▆
Up to 12 external analog input channels


A 12-bit multi-channel Analog to Digital Converter is integrated in the device. There are 
multiplexed channels, which include 12 external channels on which the external analog signal can 
be supplied and 3 internal channels. If the input voltage is required to remain within a specific 
threshold window, the ADC analog watchdog function will monitor and detect the signal. An 
interrupt will then be generated to inform the device that the input voltage is higher or lower than 
the set thresholds. There are three conversion modes to convert an analog signal to digital data. The 
A/D conversion can be operated in one shot, continuous and discontinuous conversion modes.


Rev. 1.00	
11 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**2  Features**


**Operational Amplifier – OPA**


	
▆
Fixed dedicated I/O pins


	
▆
Internal output paths to the A/D converter or comparator


	
▆
Input offset calibration


	
▆
10-bit DAC offset voltage


**Comparator – CMP**


	
▆
Two rail-to-rail comparators


	
▆
Each comparator has configurable inverting or non-inverting inputs used for flexible voltage 


selection


	
●
Dedicated I/O pins


	
●
Internal voltage reference provided by 8-bit scaler – CMP0 only


	
●
Internal operational amplifier output


	
▆
Programmable hysteresis


	
▆
Programming response speed and power consumption


	
▆
Comparator output can be routed to I/O pin or to multiple timers or ADC trigger input


	
▆
8-bit scaler can be configured to dedicated I/O for voltage reference


	
▆
Configurable inverting input from CMP0N, CMP1N or CVREF


	
▆
Interrupt generation capability with wakeup from Sleep or Deep Sleep mode through the EXTI 


controller


Two general purpose comparators are implemented within the device. They can be configured 
either as standalone comparators or combined with different kinds of peripheral IP. Each 
comparator is capable of asserting interrupts to the NVIC or waking up the MCU from the Sleep or 
Deep Sleep mode through the EXTI wakeup event management unit.


**I/O Ports – GPIO**


	
▆
Up to 28 GPIOs


	
▆
Port A, B, C are mapped as 16 external interrupts – EXTI


	
▆
Almost all I/O pins have configurable output driving current


There are up to 28 General Purpose I/O pins, GPIO, for the implementation of logic input / output 
functions. Each of the GPIO ports has a series of related control and configuration registers to 
maximize flexibility and to meet the requirements of a wide range of applications.


The GPIO ports are pin-shared with other alternative functions (AFs) to obtain maximum 
functional flexibility on the package pins. The GPIO pins can be used as alternative functional 
pins by configuring the corresponding registers regardless of the input or output pins. The external 
interrupts on the GPIO pins of the device have related control and configuration registers in the 
External Interrupt Control Unit, EXTI. 


Rev. 1.00	
12 of 55
April 29, 2022


**2  Features**


**Motor Control Timer – MCTM**


	
▆
16-bit up / down auto-reload counter


	
▆
16-bit programmable prescaler that allows division of the prescaler clock source by any factor 


between 1 and 65536 to generate the counter clock frequency


	
▆
Input Capture function


	
▆
Compare Match Output


	
▆
PWM waveform generation with edge-aligned and center-aligned counting modes


	
▆
Single Pulse Mode Output


	
▆
Complementary outputs with programmable dead-time insertion


	
▆
Break input signals to assert the timer output signals in reset state or in a known fixed state


The Motor Control Timer, MCTM, consists of one 16-bit up / down-counter, four 16-bit Capture / 
Compare Registers (CCRs), one 16-bit Counter Reload Register (CRR), one 8-bit repetition counter 
and several control / status registers. It can be used for a variety of purposes which include input 
signal pulse width measurement, output waveform generation for signals such as compare match 
outputs, PWM outputs or complementary PWM outputs with dead-time insertion. The MCTM 
is capable of offering full functional support for motor control, hall sensor interfacing and break 
input.


**General-Purpose Timer – GPTM**


	
▆
16-bit up / down auto-reload counter


	
▆
Up to 4 independent channels for each timer 


	
▆
16-bit programmable prescaler that allows division of the prescaler clock source by any factor 


between 1 and 65536 to generate the counter clock frequency


	
▆
Input Capture function


	
▆
Compare Match Output


	
▆
PWM waveform generation with edge-aligned and center-aligned counting modes


	
▆
Single Pulse Mode Output


	
▆
Encoder interface controller with two inputs using quadrature decoder and Pulse/Direction Mode


	
▆
Master/Slave mode controller


The General-Purpose Timer, GPTM, consists of one 16-bit up / down-counter, four 16-bit Capture 
/ Compare Registers (CCRs), one 16-bit Counter Reload Register (CRR) and several control / status 
registers. It can be used for a variety of purposes including general timer, input signal pulse width 
measurement, output waveform generation such as single pulse generation or PWM outputs. The 
GPTM also supports an encoder interface using a quadrature decoder with two inputs.


Rev. 1.00	
13 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**2  Features**


**Single Channel Timer – SCTM**


	
▆
16-bit auto-reload up-counter


	
▆
One channel for each timer


	
▆
16-bit programmable prescaler that allows division of the prescaler clock source by any factor 


between 1 and 65536 to generate the counter clock frequency


	
▆
Input Capture function


	
▆
Compare Match Output


	
▆
PWM waveform generation with edge-aligned counting mode


The Single Channel Timer, SCTM, consists of one 16-bit up-counter, one 16-bit Capture / Compare 
Register (CCR), one 16-bit Counter-Reload Register (CRR) and several control / status registers. It 
can be used for a variety of purposes including general timer, input signal pulse width measurement 
or output waveform generation such as PWM outputs.


**Basic Function Timer – BFTM**


	
▆
32-bit compare match up-counter – no I/O control features


	
▆
One shot mode – stops counting when compare match occurs


	
▆
Repetitive mode – restarts counter when compare match occurs


The Basic Function Timer, BFTM, is a simple 32-bit up-counting counter designed to measure time 
intervals, generate one shot pulses or generate repetitive interrupts. The BFTM can operate in two 
modes which are repetitive and one shot modes. In the repetitive mode, the counter is restarted at 
each compare match event. The BFTM also supports a one shot mode which will force the counter 
to stop counting when a compare match event occurs.


**Watchdog Timer – WDT**


	
▆
12-bit down-counter with 3-bit prescaler


	
▆
Provides reset to the system


	
▆
Programmable watchdog timer window function


	
▆
Register write protection function


The Watchdog Timer is a hardware timing circuitry that can be used to detect a system lock-up 
due to software trapped in a deadlock. It includes a 12-bit count-down counter, a prescaler, a WDT 
delta value register, WDT operation control circuitry and a WDT protection mechanism. If the 
software does not reload the counter value before a Watchdog Timer underflow occurs, a reset will 
be generated when the counter underflows. In addition, a reset is also generated if the software 
reloads the counter before it reaches a delta value. It means that the counter reload must occur 
when the Watchdog timer value has a value within a limited window using a specific method. The 
Watchdog Timer counter can be stopped when the processor is in the debug mode. The register 
write protection function can be enabled to prevent an unexpected change in the Watchdog timer 
configuration.


Rev. 1.00	
14 of 55
April 29, 2022


**2  Features**


**Low Speed Timer – LSTM**


	
▆
24-bit up-counter with a programmable prescaler


	
▆
Alarm function


	
▆
Interrupt and wake-up control


The Low Speed Timer, LSTM, circuitry includes the APB interface, a 24-bit count-up counter, a 
control register, a prescaler, a compare register and a status register. The LSTM circuits are located 
in the V
CORE
 power domain. When the device enters the power-saving mode, the LSTM counter is 
used as a wakeup timer to let the system resume from the power saving mode.


**Inter-integrated Circuit – I**
**2**
**C**


	
▆
Supports both master and slave modes with a frequency of up to 1 MHz


	
▆
Provides an arbitration function and clock synchronization


	
▆
Supports 7-bit and 10-bit addressing modes and general call addressing


	
▆
Supports slave multi-addressing mode using address mask function


The I
2
C module is an internal circuit allowing communication with an external I
2
C interface which 
is an industry standard two-wire serial interface used for connection to external hardware. These 
two serial lines are known as a serial data line SDA, and a serial clock line SCL. The I
2
C module 
provides three data transfer rates: 100 kHz in the Standard mode; 400 kHz in the Fast mode; 1 
MHz in the Fast plus mode. The SCL period generation registers are used to set different kinds of 
duty cycle implementation for the SCL pulse.


The SDA line which is connected directly to the I
2
C bus is a bidirectional data line between the 
master and slave devices and is used for data transmission and reception. The I
2
C module also has 
an arbitration detection and clock synchronization function to prevent situations where more than 
one master attempts to transmit data to the I
2
C bus at the same time.


**Serial Peripheral Interface – SPI**


	
▆
Supports both master and slave modes 


	
▆
Frequency of up to (f
PCLK
/2) MHz for the master mode and (f
PCLK
/3) MHz for the slave mode


	
▆
FIFO Depth: 8 levels


	
▆
Multi-master and multi-slave operation


The Serial Peripheral Interface, SPI, provides an SPI protocol data transmit and receive function in 
both master and slave modes. The SPI interface uses 4 pins, among which are serial data input and 
output lines MISO and MOSI, the clock line SCK, and the slave select line SEL. One SPI device 
acts as a master who controls the data flow using the SEL and SCK signals to indicate the start of 
the data communication and the data sampling rate. To receive the data bits, the streamlined data 
bits are latched on a specific clock edge and stored in the data register or in the RX FIFO. Data 
transmission is carried out in a similar way but with the reverse sequence. The mode fault detection 
provides a capability for multi-master applications.


Rev. 1.00	
15 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**2  Features**


**Universal Asynchronous Receiver Transmitter – UART**


	
▆
Asynchronous serial communication operating baud-rate clock frequency up to (f
PCLK
/16) MHz


	
▆
Full duplex communication


	
▆
Fully programmable serial communication characteristics including:


	
●
Word length: 7, 8 or 9-bit character


	
●
Parity: Even, odd or no-parity bit generation and detection


	
●
Stop bit: 1 or 2 stop bits generation


	
●
Bit order: LSB-first or MSB-first transfer


	
▆
Error detection: Parity, overrun and frame error


The Universal Asynchronous Receiver Transceiver, UART, provides a flexible full duplex data 
exchange using asynchronous transfer. The UART is used to translate data between parallel and 
serial interfaces, and is commonly used for RS232 standard communication. The UART peripheral 
function supports Line Status Interrupt. The software can detect a UART error status by reading 
the UART Status & Interrupt Flag Register, URSIFR. The status includes the type and the 
condition of transfer operations as well as several error conditions resulting from Parity, Overrun, 
Framing and Break events.


**Universal Synchronous Asynchronous Receiver Transmitter – USART**


	
▆
Supports both asynchronous and clocked synchronous serial communication modes


	
▆
Programmable baud rate clock frequency up to (f
PCLK
/16) MHz for asynchronous mode and 


(f
PCLK
/8) MHz for synchronous mode 


	
▆
Full duplex communication


	
▆
Fully programmable serial communication characteristics including:


	
●
Word length: 7, 8 or 9-bit character


	
●
Parity: Even, odd or no-parity bit generation and detection


	
●
Stop bit: 1 or 2 stop bits generation


	
●
Bit order: LSB-first or MSB-first transfer


	
▆
Error detection: Parity, overrun and frame error


	
▆
Auto hardware flow control mode – RTS, CTS


	
▆
IrDA SIR encoder and decoder


	
▆
RS485 mode with output enable control


	
▆
FIFO Depth: 8-level for both receiver and transmitter 


The Universal Synchronous Asynchronous Receiver Transceiver, USART, provides a flexible 
full duplex data exchange using synchronous or asynchronous transfer. The USART is used to 
translate data between parallel and serial interfaces, and is commonly used for RS232 standard 
communication. The USART peripheral function supports four types of interrupt including Line 
Status Interrupt, Transmitter FIFO Empty Interrupt, Receiver Threshold Level Reaching Interrupt 
and Time Out Interrupt. The USART module includes an 8-level transmitter FIFO, (TX_FIFO) and 
an 8-level receiver FIFO (RX_FIFO). The software can detect a USART error status by reading 
USART Status & Interrupt Flag Register, USRSIFR. The status includes the type and the condition 
of the transfer operations as well as several error conditions resulting from Parity, Overrun, 
Framing and Break events.


Rev. 1.00	
16 of 55
April 29, 2022


**2  Features**


**Cyclic Redundancy Check – CRC**


	
▆
Supports CRC16 polynomial: 0x8005,



X
16
 + X
15
 + X
2
 + 1


	
▆
Supports CCITT CRC16 polynomial: 0x1021,



X
16
 + X
12
 + X
5
 + 1


	
▆
Supports IEEE-802.3 CRC32 polynomial: 0x04C11DB7,



X
32
 + X
26
 + X
23
 + X
22
 + X
16
 + X
12
 + X
11
 + X
10
 + X
8
 + X
7
 + X
5
 + X
4
 + X
2
 + X + 1


	
▆
Supports 1’s complement, byte reverse & bit reverse operation on data and checksum


	
▆
Supports byte, half-word & word data size


	
▆
Programmable CRC initial seed value


	
▆
CRC computation executed in 1 AHB clock cycle for 8-bit data and 4 AHB clock cycles for 32-bit 



data


	
▆
Supports PDMA to complete a CRC computation of a block of memory


The CRC calculation unit is an error detection technique test algorithm and is used to verify data 
transmission or storage data correctness. A CRC calculation takes a data stream or a block of data 
as its input and generates a 16-bit or 32-bit output remainder. Ordinarily, a data stream is suffixed 
by a CRC code and used as a checksum when being sent or stored. Therefore, the received or 
restored data stream is calculated by the same generator polynomial as described above. If the new 
CRC code result does not match the one calculated earlier, that means the data stream contains a 
data error.


**Peripheral Direct Memory Access – PDMA**


	
▆
6 channels with trigger source grouping


	
▆
8-bit, 16-bit and 32-bit width data transfer


	
▆
Supports linear address, circular address and fixed address modes


	
▆
4-level programmable channel priority


	
▆
Auto reload mode


	
▆
Supports trigger sources:


ADC, SPI, USART, UART, I
2
C, MCTM, GPTM, SCTM and software request


The Peripheral Direct Memory Access circuitry, PDMA, moves data between the peripherals 
and the system memory on the AHB bus. Each PDMA channel has a source address, destination 
address, block length and transfer count. The PDMA can exclude the CPU intervention and avoid 
interrupt service routine execution. It improves system performance as the software does not need 
to connect each data movement operation.


Rev. 1.00	
17 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**2  Features**


**Hardware Divider – DIV**


	
▆
Signed / unsigned 32-bit divider


	
▆
Calculate in 8 clock cycles, load in 1 clock cycle


	
▆
Division by zero error Flag


The divider is the truncated division and requires a software triggered start signal by controlling 
the “START” bit in the control register. The divider calculation complete flag will be set to 1 after 
8 clock cycles, however, if the divisor register data is zero during the calculation, the division by 
zero error flag will be set to 1.


**Debug Support**


	
▆
Serial Wire Debug Port – SW-DP


	
▆
4 comparators for hardware breakpoint or code / literal patch


	
▆
2 comparators for hardware watch points


**Package and Operation Temperature**


	
▆
48-pin LQFP-EP and 32-pin QFN packages


	
▆
Operation temperature range: -40 °C to 105 °C


Rev. 1.00	
18 of 55
April 29, 2022


**3  Overview**


# 3 
# 3 
##  Overview


**Device Information**


**Table 1.  Features and Peripheral List**


**Peripherals**
**HT32F65532G**


Main Flash (KB)
31


Option Bytes Flash (KB)
1


SRAM (KB)
4


Timers


MCTM
1


GPTM
1


SCTM
4


BFTM
2


WDT
1


LSTM
1


Communication


USART
1


UART
1


SPI
1


I
2
C
1


PDMA
6 channels


Hardware Divider
1


CRC-16/32
1


EXTI
16


12-bit ADC
Number of channels


1


12 channels


Comparator
2


Operational Amplifier
1


GPIO
Up to 28


CPU frequency
Up to 60 MHz


Power supply (V
CC
)  
6 V ~ 40 V


Operating voltage (V
DD
)
2.5 V ~ 5.5 V


5 V LDO output driving current
50 mA


Operating temperature
-40 °C ~ 105 °C


Package
48-pin LQFP-EP and 32-pin QFN


Rev. 1.00	
19 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**3  Overview**


**Block Diagram**


Control


Logic


VCC


V
REG


INHA
INHB
INHC


INLA
INLB
INLC


3


3


3


Dead-Time


Control


V
REG


3


5V


50mA, ±1.5%


LDO


V
REG
V
CC


V12P


VCC_UVLO


12V, ±5%


LDO
V
12P


V12P_UVLO


VBST_UVLO
OTP


Protections


BSTA/BSTB/BSTC


GHA/GHB/GHC


SHA/SHB/SHC


GLA/GLB/GLC


VREG_UVLO


3


3


3


3


V12P


VREG


V
REG


SW-DP


APB


AHB 


Peripherals


Flash 


Memory


Cortex
®
-M0+


Processor


System


NVIC


SRAM 


Controller


FMC


Control 


Registers
CKCU/RSTCU


Control Registers


PDMA
Control 


Registers


PDMA


6 Channels


DMA request


Interrupt request


CH3~CH0


BOOT


Clock and reset  control


Power control


Bus Matrix


Power supply: 


Bus:


Control signal:


Alternate function:
AF


Powered by V
CORE


SWCLK 
SWDIO


SDA, 
SCL


Powered by V
CORE


MOSI, MISO
SCK, SEL


Flash Memory 


Interface


LSI 


32 kHz


Powered by V
DD


LSTM


PWRCU


nRST


AHB to APB


Bridge


SRAM


PA ~ PC


TX, RX


RTS/TXE
CTS/SCK


CH2~CH3


BRK0, BRK1


IO Port


Powered by V
DD


POR


/PDR


BOD


LVD


XTALIN
XTALOUT


HSI 


8 MHz


HSE


4 ~ 16 MHz


LDO


 V
CORE


CLDO


CAP.


SCTM


PLL


f
Max
: 60 MHz


Powered by V
DDA


ADC_IN0


...


ADC_IN11


Analog 


CMP


Analog 


CMP0 ~1


Analog 


OPA


OPAN, OPAP 


OPAO


12-bit 


SAR ADC


TX, RX


GND


LSS


V12P


V
DD


V
SS


PC9
PB1
PA15


PC8
PB0
PA14


VREG


3


3


V
DDA


V
SSA


VDD


VSS


V
DD
V
SS


V
REG


EN
PC12


CMP0N, CMP0P 


CMP0O


CMP1N, CMP1P0~2, 


CMP1O


AF
AF
AF
AF
AF


AF
AF
AF
AF
AF
AF
AF
AF


**Figure 1.  Block Diagram**


Rev. 1.00	
20 of 55
April 29, 2022


**3  Overview**


**Memory Map**


Reserved


DIV


Reserved


EXTI


Reserved


Reserved


GPIO A 
～
 C


Reserved


Reserved


GPTM


WDT


CMP0 & CMP1


I
2
C


Reserved


Reserved


Reserved


Reserved


Reserved


Reserved


Reserved


Reserved


0x4001_8000


MCTM


32 KB on-chip Flash


0x0000_0000


Reserved


0x0000_8000


Boot loader


0x1F00_0000


Reserved


0x1F00_0800


Option byte alias


0x1FF0_0000


32 KB


2 KB


1 KB


0x1FF0_0400


Reserved


Code


SRAM


Peripheral


0x2000_0000


4 KB on-chip SRAM


Reserved


0x2000_1000


4 KB


APB peripherals


0x4000_0000


AHB peripherals


0x4008_0000


0x4010_0000


Private peripheral bus


0xE000_0000


Reserved


0xE010_0000


0xFFFF_FFFF


512 KB


512 KB


0x4000_0000


UART
0x4000_1000


SPI


0x4004_8000


SCTM0


0x4000_4000


0x4000_5000


SCTM2


ADC


Reserved


0x4001_0000


OPA


AFIO


0x4002_D000
Reserved


0x4003_5000


0x4002_2000


0x4002_3000


0x4005_8000


0x4003_6000


0x4005_9000


APB


FMC
0x4008_0000


Reserved
0x4008_2000


CKCU & RSTCU
0x4008_8000


CRC
0x4008_A000


PDMA
0x4009_0000


0x400F_FFFF


AHB


0x4000_2000


0x4003_4000


0x4001_9000


0x4002_C000


0x4008_C000


0x4009_2000


0x400B_0000


0x400B_6000


0x4001_1000


0x4004_9000


0x4006_8000


0x4006_E000


0x4006_F000


0x4002_4000


0x4002_5000


0x400C_A000


0x400C_C000


USART


Reserved


LSTM & PWRCU


0x4006_9000


0x4006_A000


Reserved
0x4006_B000


SCTM3
0x4007_5000


SCTM1
0x4007_4000


Reserved


BFTM1
0x4007_7000


0x4007_8000


BFTM0
0x4007_6000


**Figure 2.  Memory Map**


Rev. 1.00	
21 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**3  Overview**


**Table 2.  Register Map**


**Start Address**
**End Address**
**Peripheral**
**Bus**


0x4000_0000
0x4000_0FFF
USART


APB


0x4000_1000
0x4000_1FFF
UART


0x4000_2000
0x4000_3FFF
Reserved


0x4000_4000
0x4000_4FFF
SPI


0x4000_5000
0x4000_FFFF
Reserved


0x4001_0000
0x4001_0FFF
ADC


0x4001_1000
0x4001_7FFF
Reserved


0x4001_8000
0x4001_8FFF
OPA


0x4001_9000
0x4002_1FFF
Reserved


0x4002_2000
0x4002_2FFF
AFIO


0x4002_3000
0x4002_3FFF
Reserved


0x4002_4000
0x4002_4FFF
EXTI


0x4002_5000
0x4002_BFFF
Reserved


0x4002_C000
0x4002_CFFF
MCTM


0x4002_D000
0x4003_3FFF
Reserved


0x4003_4000
0x4003_4FFF
SCTM0


0x4003_5000
0x4003_5FFF
SCTM2


0x4003_6000
0x4004_7FFF
Reserved


0x4004_8000
0x4004_8FFF
I
2
C


0x4004_9000
0x4005_7FFF
Reserved


0x4005_8000
0x4005_8FFF
CMP0 & CMP1


0x4005_9000
0x4006_7FFF
Reserved


0x4006_8000
0x4006_8FFF
WDT


0x4006_9000
0x4006_9FFF
Reserved


0x4006_A000
0x4006_AFFF
LSTM & PWRCU


0x4006_B000
0x4006_DFFF
Reserved


0x4006_E000
0x4006_EFFF
GPTM


0x4006_F000
0x4007_3FFF
Reserved


0x4007_4000
0x4007_4FFF
SCTM1


0x4007_5000
0x4007_5FFF
SCTM3


0x4007_6000
0x4007_6FFF
BFTM0


0x4007_7000
0x4007_7FFF
BFTM1


0x4007_8000
0x4007_FFFF
Reserved


Rev. 1.00	
22 of 55
April 29, 2022


**3  Overview**


**Start Address**
**End Address**
**Peripheral**
**Bus**


0x4008_0000
0x4008_1FFF
FMC


AHB


0x4008_2000
0x4008_7FFF
Reserved


0x4008_8000
0x4008_9FFF
CKCU & RSTCU


0x4008_A000
0x4008_BFFF
CRC


0x4008_C000
0x4008_FFFF
Reserved


0x4009_0000
0x4009_1FFF
PDMA


0x4009_2000
0x400A_FFFF
Reserved


0x400B_0000
0x400B_1FFF
GPIOA


0x400B_2000
0x400B_3FFF
GPIOB


0x400B_4000
0x400B_5FFF
GPIOC


0x400B_6000
0x400C_9FFF
Reserved


0x400C_A000
0x400C_BFFF
DIV


0x400C_C000
0x400F_FFFF
Reserved


Rev. 1.00	
23 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**3  Overview**


**Clock Structure**


4-16 MHz 


HSE XTAL 


8 MHz 


 HSI RC


32 kHz 


LSI  RC 


Legend:
HSE = High Speed External clock
HSI = High Speed Internal clock
LSI = Low Speed Internal clock 


PLLSRC


AHB Prescaler  

 1,2,4,8,16,32


FCLK 
( free running clock)


STCLK
(to SysTick)


CK_WDT


WDTEN


CK_REF


CK_HSI/16


CK_HSE/16


CK_SYS/16


CKOUTSRC[2:0]


HSEEN


HSIEN


CK_LSI


HCLKC/16


CK_HSI


CK_HSE


PCLK (AFIO, ADC, 
CMPx, OPA, SPI, 
USART, UART, I
2
C, 
MCTM, GPTM, SCTMx, 
BFTMx, EXTI, LSTM, 
WDT)


System 


PLL


Clock 


Monitor


PLLEN


CK_PLL


**f**
**CK_PLL,max **
**= 60 MHz**


CK_LSI


HCLKS
( to SRAM)


HCLKF
( to Flash)


CM0PEN


FMCEN


CM0PEN


SRAMEN


CK_LSTM


LSTMEN


1


0


CK_AHB


000


001


010


011


100


110


CK_SYS


SW[2:0]



8


HCLKC
( to Cortex
® 
-M0+)
CM0PEN 


(control by HW)


HCLKBM
( to Bus Matrix)


CM0PEN


BMEN


HCLKAPB
( to APB Bridge)


CM0PEN


APBEN


CK_CRC
( to CRC)
CRCEN


Peripherals


Clock 


Prescaler
 

 1,2,4,8


00


01


10


11


CK_AHB


CK_AHB/2


CK_AHB/4


CK_AHB/8


SPIEN


I2CEN


CK_GPIO
( to GPIO port)


PCEN


PAEN
00x


011


010


111


Prescaler 



1 ~ 32
CK_REF
Divider



2
CKREFEN


CKREFPRE


HCLKD
( to PDMA)
PDMAEN


CK_DIV
( to DIV)
DIVEN


**Figure 3.  Clock Structure**


Rev. 1.00	
24 of 55
April 29, 2022


**4  Gate-Driver**


# 4 
# 4 
##  Gate-Driver


The device includes a 3-channel gate-driver, which can be used for external high-side and

low-side N-channel MOSFET driving. It includes a 5 V LDO, a 12 V LDO, 3-channel high-side and 
low-side gate-driver circuits. The gate-driver also has five protection functions, which are Power 
Supply Input Under Voltage Lock-Out, 5 V LDO Output Under Voltage Lock-Out, 12 V LDO 
Output Under Voltage Lock-Out, Bootstrap Output Under Voltage Lock-Out and Over Temperature 
Protection, to avoid abnormal output situations.


The input signals of INHx, INLx and EN are input to the control logic which will determine the 
high-side and low-side gate-driver outputs. The INHx and EN each have an internal pull-down 
resistor and the INLx has an internal pull-up resistor. Additionally, there is a fixed dead time 
insertion when switching between the high-side and low-side gate driving to avoid short-circuit 
between V
CC
 and ground.


The gate-driver output voltage will vary with the power supply when V
CC
 is less than 13 V. When 
V
CC
 is greater than 13 V, the gate-driver output will be clamped to 12 V, providing a 0.7 A peak 
source current and a 1 A peak sink current. Either high-side and low-side gate has an internal

hold-off resistor in order to avoid misconduction of external power MOSFET due to interference 
when the power is off.


The gate-driver also has integrated bootstrap diodes for bootstrap circuit implementation, allowing 
reduced system component requirements. 


**5 V Voltage Regulator**


The integrated 5 V LDO can supply power for both internal and external circuits, with a output 
current over 50mA. The LDO will act as a fully turned on switch when the power supply V
CC
 is less 
than 5 V, in which condition its output voltage is almost equal to the power supply if there is no load. 


**12 V Voltage Regulator**


The integrated 12 V LDO, which supplies power for the low-side gate-drivers, cannot be used as 
power supply for external circuits. 


**Bootstrap Circuit Operation**


The gate-driver uses 3 sets of bootstrap circuits as floating power supplies to power the high-side 
gate-driver circuits.


Each set of bootstrap circuit is composed of an external bootstrap capacitor, C
B
, and an internal 
bootstrap diode, D
BOOT
. The charging current path of the bootstrap capacitor in common 
applications is shown in Figure 4. The bootstrap capacitor is charged after the low-side power 
MOSFET is turned on. After the gate-driver is enabled, an input command of INHx = INLx = ‘L’ 


Rev. 1.00	
25 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**4  Gate-Driver**


should be arranged before switching to the high-side power MOSFET for the first time, so that the 
low-side power MOSFET will be turned on for a period of time to charge the bootstrap capacitor. 
As shown in Figure 5, the high-side gate-driver output could not be controlled by inputs until the 
bootstrap capacitor has been charged exceeding the bootstrap under voltage lock-out threshold, 
V
BST_UVLO+
. It is recommended to charge the bootstrap capacitor to the steady-state voltage of V1 
before proceeding. The equation for estimating the charging time t
BST
 of the bootstrap capacitor is 
as follows:


	
	
	
t
BST
 (ms) > 0.3 + 1.1 × C
B
 (μF) ÷ 2.2


Where C
B
 is the bootstrap capacitance. The larger the capacitance, the longer it will take to charge. 
For example, the charging time t
BST
 should be at least 1.5 ms for a capacitance of 2.2 μF. After the 
charging is completed, the bootstrap voltage will reach the steady-state voltage V1, as shown in 
Figure 5. When the power supply V
CC
 is less than or equal to 13 V, V1 will change along with V
CC
. 
Then V1 will be clamped to a fixed value of 12 V once V
CC
 is larger than 13 V. V1 is calculated as 
follows:


	
	
	
V1 = 12 V	
	
when V
CC 
> 13 V


	
	
	
V1 = V
CC
 – 1.5 V		
when V
CC 
≤ 13 V


LSS


BSTx


GHx


SHx


GLx


C
B


Q1


V
CC


Q2


**C**
**B**
** Charging Current Path**


D
BOOT


**Figure 4.  Bootstrap Capacitor (C**
**B**
**) Charging Current Path**


Rev. 1.00	
26 of 55
April 29, 2022


**4  Gate-Driver**


EN


INLx


V
(BSTx,SHx)


t
BST


V1


V
BST_UVLO+


INHx


**Figure 5.  Bootstrap Capacitor Charging Time (t**
**BST**
**)**


The charge stored in the bootstrap capacitor, C
B
, is discharged during the high-side gate-driver 
output and the internal bootstrap diode, D
BOOT
, is used to avoid current backflow, as shown in 
Figure 6. When discharging, pay attention to whether the bootstrap capacitance value is sufficient. 
If the bootstrap capacitance value is too small, it will affect the high-side gate driving capability. 
Refer to the “Component Selections” chapter for the bootstrap capacitance recommendation. 


LSS


BSTx


GHx


SHx


GLx


C
B


Q1


V
CC


Q2


D
BOOT


**C**
**B**
** Discharging Current Path**


**Figure 6.  Bootstrap Capacitor (C**
**B**
**) Discharging Current Path**


Rev. 1.00	
27 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**4  Gate-Driver**


**Gate-Driver Control Logic**


As a gate-driver for driving high-side and low-side N-channel MOSFETs, the control signals are input 
from EN, INHx, INLx. Usually a 6-wire input control method is used, where the dead time width is 
determined by the control signals but has a minimum value equal to the fixed dead time designed in 
the device.


Pay attention to whether the fixed dead time is sufficient when switching between the high-side and 
low-side power MOSFETs so that the power supply V
CC
 will not be short-circuited to the ground.


GND


INHA


IN1


INLA


IN2


INHB


IN3


INLB


IN4


INHC


IN5


INLC


IN6


GHA


GLA


GHB


GLB


GHC


GLC


**Gate-Driver**


**MCTM Outputs**


MT_CH0


MT_CH0N


MT_CH1


MT_CH1N


MT_CH2


MT_CH2N


**Figure 7.  6-Wire Control**


Both high-side and low-side gate-driver outputs are controlled by the EN, INHx and INLx input 
signals. For example, the on/off true table of the external N-channel power MOSFETs is shown as 
follows.


**Table 3.  Gate-Driver Operation Truth Table**


**EN**
**INHx**
**INLx**
**GHx-to-SHx**
**GLx-to-LSS**
**External H/S **


**Power MOSFET**


**External L/S **


**Power MOSFET**


0
X
X
L
L
OFF
OFF


1
0
0
L
H
OFF
ON


1
0
1
L
L
OFF
OFF


1
1
0
L
L
OFF
OFF


1
1
1
H
L
ON
OFF


Note: H/S indicates High-Side, L/S indicates Low-Side.


Rev. 1.00	
28 of 55
April 29, 2022


**4  Gate-Driver**


**Protection Function Operation**


When the device operates in an abnormal situation, such as a power supply input under voltage 
lock-out, bootstrap output under voltage lock-out, 12 V LDO output under voltage lock-out, 5 V 
LDO output under voltage lock-out or over temperature condition has occurred, it will activate 
the corresponding protection mechanism to turn off the affected N-channel power MOSFET. The 
protection mechanisms are summarized below.


**Table 4.  Protection Function Conditions**


**Protection**
**Protection Entry **


**Condition**


**Protection Reaction**
**Release **


**Condition**
**V**
**12P**
**GHx-to-SHx**
**GLx-to-LSS**
**Bootstrap **


**Function**


VCC_UVLO
V
CC 
< V
CC_UVLO-
0V
L
L
Disable
V
CC 
≥ V
CC_UVLO+


VBST_UVLO
V
(BSTx,SHx) 
< V
BST_UVLO-
—
L
—
Keep Active
V
(BSTx,SHx) 
≥ V
BST_UVLO+


V12P_UVLO
V
12P 
< V
12P_UVLO-
—
—
L
Disable
V
12P 
≥ V
12P_UVLO+


VREG_UVLO
V
REG 
< V
REG_UVLO-
—
L
L
Disable
V
REG 
≥ V
REG_UVLO+


OTP
T
j 
> T
SHD
—
L
L
Disable
T
j 
≤ T
REC


**Power Supply Input Under Voltage Lock-Out – VCC_UVLO**


This integrated protection function is to avoid unstable gate-driver output when the power supply 
voltage falls to a certain low level. During V
CC
 power-on period, both high-side and low-side power 
MOSFETs are turned off before the power supply voltage reaching the threshold V
CC_UVLO+
. When 
the power supply voltage is greater than V
CC_UVLO+
, the gate-driver outputs are determined by the 
input signals. If the power supply voltage falls below the under voltage lock-out threshold V
CC_UVLO-
,

both high and low-side power MOSFETs will remain off.


**Bootstrap Output Under Voltage Lock-Out – VBST_UVLO**


This integrated protection function is to avoid that when the bootstrap capacitor is insufficiently 
charged, the output voltage of the high-side gate-driver will be insufficient making the high-side 
power MOSFET fully turned on. When the bootstrap output voltage is larger than the threshold 
V
BST_UVLO+
, the high-side gate-driver output is determined by the input signals. If the bootstrap 
output voltage falls below the under voltage lock-out threshold V
BST_UVLO-
, the high-side power 
MOSFET will remain off.


**12 V LDO Output Under Voltage Lock-Out – V12P_UVLO**


When the internal 12 V LDO output voltage, V
12P
, is too low, the integrated 12 V LDO output under 
voltage lock-out function will be activated to avoid that the output voltage of the low-side gate-driver 
is insufficient making the low-side power MOSFET fully turned on. After V
12P
 exceeds the threshold 
V
12P_UVLO+
, the low-side gate-driver output is determined by the input signals. If V
12P
 is less than the 
under voltage lock-out threshold V
12P_UVLO-
, the low-side power MOSFET will remain off.


**5 V LDO Output Under Voltage Lock-Out – VREG_UVLO**


When the internal 5 V LDO output voltage, V
REG
, is too low, the integrated 5 V LDO output 
under voltage lock-out function will be activated to avoid unstable signals input from the external 
controller. After V
REG
 exceeds the threshold V
REG_UVLO+
, the gate-driver output is determined by 
the input signals. If V
REG
 is less than the under voltage lock-out threshold V
REG_UVLO-
, both high and 
low-side power MOSFETs will remain off.


Rev. 1.00	
29 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**4  Gate-Driver**


**Over Temperature Protection – OTP**


If the internal junction temperature of the gate-driver exceeds the limit threshold T
SHD
, the

high-side and low-side power MOSFETs will be turned off until the junction temperature drops 
below the recovery temperature level, T
REC
, at which the gate-driver output is determined by the 
input signals.


**Component Selections**


**Gate Resistor Circuit**


The main function of the gate resistors, R
G1
, R
G2
, R
G3
 and R
G4
, is to reduce the vibration of U, V, W 
output voltages and reduce the EMI noise generation. Adjusting R
G1
 and R
G3
 controls the on time of 
the high-side and low-side switches, adjusting R
G2
 and R
G4
 controls the off time of the high-side and 
low-side switches. The gate resistors are optional and can be used according to the requirements.


It is recommended to select the gate resistance value according to the desired gate voltage rising 
time (t
r
) or falling time (t
f
), which are shown in the figure below. R
G1
, R
G2
, R
G3
 and R
G4
, if used, are 
recommended to have a typical value of 10 Ω ~ 200 Ω. It is recommended to use a 1N4148 switch 
diode for both D
G1
 and D
G2
.


V
GS
10%


90%


10%


90%


t
r
t
f


**Figure 8.  Gate Voltage (V**
**GS**
**) Rising Time (t**
**r**
**) and Falling Time (t**
**f**
**)**


**Bootstrap Capacitor**


The power stored in the bootstrap capacitor, C
B
, services as a floating power supply for the

high-side gate-driver circuit. Generally speaking, the bootstrap capacitance value is recommended 
to be more than 50 times the input power capacitance value of the high-side power MOSFET, and is 
recommended to be at least 2.2 μF. 


**Current Sensing Resistors**


The current sensing resistor, R
S
, turns the current flowing through it into a voltage for the controller 
to detect. The current sensing resistor is optional and can be used according to the requirements. It 
is recommended that the current sensing resistors be used when the cross voltage is less than 0.5 V. 


Pay attention to the power that the current sensing resistor can withstand, P
RS
, which is calculated 
by P
RS 
= R
S
 × I
RMS


2
, where R
S
 is the resistance value, I
RMS
 is the effective value of the current 


flowing through the resistor. The package of the current sensing resistor should be selected based 
on the power calculated above.


Rev. 1.00	
30 of 55
April 29, 2022


**4  Gate-Driver**


**Gate-Driver Supply Capacitor**


The power supply regulator capacitor, C1, can reduce input voltage fluctuation. It is recommended 
to use at least a 4.7 μF capacitor.


**Power Supply Bypass Capacitor**


When the board power supply is mains, the power supply bypass capacitor, C5, can filter out the high-
frequency noise input from the power supply. It is recommended to use a 0.1 μF capacitor. This 
capacitor is optional and can be used according to the requirements.


**Power Supply Input Series Resistor**


In order to keep the junction temperature of the gate-driver within the operating range and 
maintain a stable output, it is necessary to distribute the power dissipation of the gate-driver 
through the power supply series resistor, R1, so that the total power dissipation P
D
 would not exceed 
the maximum power dissipation P
D(MAX)
. This resistor is optional and can be used or not according 
to needs. Usually, when the power dissipation P
D
 of the gate-driver exceeds the maximum allowable 
power dissipation P
D(MAX)
, over temperature protection will occur. it is recommended to use a 150 Ω

resistor for R1 and a package that can withstand at least 0.5 W for the resistor. 


**RC Snubbers**


In order to prevent the 3-channel U, V, W output voltages from vibrating too much and to reduce 
EMI, an RC snubber circuit composed of R
SN
 and C
SN
 can be used to reduce the peak value and 
frequency of the vibration. R
SN
 and C
SN
 should be designed based on the actual board parasitic 
inductance and parasitic resistance. The capacitor and resistor are optional and can be used 
according to requirements.


**Motor Supply Capacitor**


The motor power supply capacitor, C4, can absorb the current that is fed back to the V
CC
 power 
supply when the motor is running, and can also provide a transient power for motor to compensate 
for the power response speed or the influence of external wire length. It is recommended to use at 
least a 22 μF capacitor. 


**12 V LDO Output Capacitor**


The 12 V LDO output regulator capacitor, C2, can reduce the voltage ripple of the 12 V LDO 
output. It is recommended to use at least a 2.2 μF capacitor.


**5 V LDO Output Capacitor**


The 5 V LDO output regulator capacitor, C3, can reduce the voltage ripple of the 5 V LDO output. 
It is recommended to use at least a 2.2 μF capacitor.


**Voltage Clamp Circuit**


In order to prevent IC damage or malfunction when a large negative SHx transient occurs, a voltage 
clamp circuit can be used to reduce the negative SHx spike. It is recommended to use a 2.2 Ω 
resistor, R
SH
, and 1N5819 schottky diode, D
SH
.


Rev. 1.00	
31 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**5  Pin Assignment**


# 5 
# 5 
##  Pin Assignment


AF0


(Default)


AF0


(Default)


AF0


(Default)


VSS / VSSA


nRST


PB13


XTALOUT


P5
P15


**HT32F65532G**


**48 LQFP-EP-A**


VDD / VDDA


AF0


(Default)


P5


PB14


AF1


P15


5VA


5V


1.5 V Power Pad


5 V Digital & Analog I/O Pad


5 V Digital I/O Pad


PB8


PC2


PB7


PB6


PC3


PC1


PB5


48
47
46
45
44
43
42
41
40
39
38
37


13
14
15
16
17
18
19
20
21
22
23
24


1


2


3


4


5


6


7


8


9


10


11


PA0


PA1


PA2


PA3


PA4


PA5


PA6


PA7


PC5


PC6


5VA


5VA


5VA


5VA


5VA


5VA


5VA


12


PC4


5VA


5VA


35


34


33


32


31


30


29


28


27


26


25


36


P5
5 V Digital & Analog Power Pad


XTALIN


5V
5V


5VA
5VA
5VA
5VA
5VA


GD
Gate-Driver Pad


GD


GD


GD


GD


GD


GD


GD


GD


GD


GD


GD


5VA


5VA


5VA


CLDO


PB10


5VA


GDP
Gate-Driver Power Pad


5V
5V
5V


PA13


PA12


SWDIO


SWCLK


5V


GD


PB11


5V


PA8


PC7


PA9_BOOT


SHA


GHA


GLA


BSTB


SHB


GHB


GHC


BSTC


GLB


SHC


GLC


BSTA


VREG


VCC


V12P


LSS


PB4


GDP
GDP
GDP
5V


5VA
5VA
5V


GD


**Figure 9.  48-pin LQFP-EP Pin Assignment**


Rev. 1.00	
32 of 55
April 29, 2022


**5  Pin Assignment**


AF0


(Default)


AF0


(Default)


AF0


(Default)


**HT32F65532G**


**32 QFN-A**


AF0


(Default)


AF1


PA13


VDD / VDDA


VSS / VSSA


nRST


24


GLC


PA12


PA9_BOOT


P5
P15


CLDO


P5
5V


P15


5VA


5V


1.5 V Power Pad


5 V Digital & Analog I/O Pad


5 V Digital I/O Pad


VCC


PC3


VREG


V12P


LSS


BSTA


GHA


SHA


32
31
30
29
28
27
25
26


5VA


9
10
11
12
13
14
15
16


1


2


3


4


5


6


7


8


PB6


PB7


PB8


PA1


PA3


PA6


PA7


PC4
5VA


5VA


5VA


5VA


5VA


5VA


5VA


5VA


23


22


21


20


19


17


18


GLA


BSTB


SHB


GHB


GHC


BSTC


GLB


SHC


P5
5 V Digital & Analog Power Pad


5V


SWDIO


SWCLK


GDP
GDP
GDP
GD
GD
GD
GD


GD


GD


GD


GD


GD


GD


GD


GD


GD
5V
5V


GD
Gate-Driver Pad


GDP
Gate-Driver Power Pad


**Figure 10.  32-pin QFN Pin Assignment**


Rev. 1.00	
33 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**5  Pin Assignment**


**Table 5.  Pin Alternate Function**


**Package**


**Alternate Function Mapping**


**AF0**
**AF1**
**AF2**
**AF3**
**AF4**
**AF5**
**AF6**
**AF7**
**AF8**
**AF9**
**AF10**
**AF11**
**AF12**
**AF13**
**AF14**
**AF15**


**48
**


**LQFP-EP**


**32
**


**QFN**


**System **
**Default**
**GPIO**
**ADC**
**N/A**
**GPTM/**
**MCTM**
**SPI**
**USART/**


**UART**
**I**
**2**
**C**
**CMP/ **


**OPA**
**SCTM**
**N/A**
**N/A**
**N/A**
**MCTM**
**N/A**
**System **


**Other**


1
PA0
ADC_IN5
USR_RTS
SCTM0


2
4
PA1
ADC_IN6
USR_RX
I2C_SCL
SCTM1


3
PA2
ADC_IN7
MT_BRK0
SPI_SCK
USR_CTS
CMP0O


4
5
PA3
ADC_IN8
MT_BRK1
SPI_MISO
USR_TX
I2C_SDA
CMP0N


5
PA4
SPI_SEL
UR_TX
I2C_SCL
CMP0P
SCTM2


6
PA5
SPI_MOSI
UR_RX
I2C_SDA
SCTM3


7
6
PA6
OPAP


8
7
PA7
GT_CH0
OPAN
SCTM2


9
8
PC4
GT_CH1
SPI_MOSI
USR_TX
OPAO


10
PC5
ADC_IN9
GT_CH2
SPI_MISO
USR_RX
SCTM0


11
PC6
ADC_IN10
GT_CH3
SPI_SEL
USR_RTS


12
PC7
ADC_IN11
SPI_ SCK
USR_CTS
SCTM3


13
9
CLDO


14
10
VDD/VDDA


15
11
VSS/VSSA


16
12
nRST


17
PB10
UR_RX
I2C_SCL


18
PB11
UR_TX
I2C_SDA


19
XTALIN
PB13
MT_CH3
USR_RTS


20
XTALOUT
PB14
MT_BRK0
SPI_SCK
USR_CTS
SCTM1


21
13
SWDIO
PA13
UR_TX
I2C_SDA


22
14
SWCLK
PA12
UR_RX
I2C_SCL


23
PA8
GT_CH0
SPI_SCK
USR_TX
I2C_SCL
SCTM0


24
15
PA9_BOOT
GT_CH3
SPI_SEL
USR_RX
I2C_SDA
CKOUT


25
16
GLC


26
17
GHC


27
18
SHC


28
19
BSTC


29
20
GLB


30
21
GHB


31
22
SHB


32
23
BSTB


33
24
GLA


34
25
GHA


35
26
SHA


36
27
BSTA


37
28
LSS


38
29
V12P


39
30
VCC


40
31
VREG


41
PB4
MT_CH2
SPI_SEL
UR_TX
SCTM3
MT_CH2N


42
PB5
SPI_SCK


43
PC1
MT_BRK0
SPI_MOSI
UR_RX
CMP1O
SCTM0


44
PC2
ADC_IN0
MT_CH3
SPI_MISO
SCTM1


45
32
PC3
ADC_IN1
GT_CH3
CMP1N


46
1
PB6
ADC_IN2
GT_CH2
I2C_SCL
CMP1P2
SCTM2


47
2
PB7
ADC_IN3
GT_CH1
I2C_SDA
CMP1P1


48
3
PB8
ADC_IN4
GT_CH0
UR_TX
CMP1P0
SCTM3


Rev. 1.00	
34 of 55
April 29, 2022


**5  Pin Assignment**


**Table 6.  Pin Description**


**Pin Number**


**Pin Name**
**Type**
**(1)**
**I/O **


**Structure**
**(2)**


**Output**


**Driving**


**Description**


**48 LQFP-EP 32 QFN**
**Default Function (AF0)**


1
PA0
AI/O
5V
4/8/12/16 mA PA0


2
4
PA1
AI/O
5V
4/8/12/16 mA PA1


3
PA2
AI/O
5V
4/8/12/16 mA PA2


4
5
PA3
AI/O
5V
4/8/12/16 mA PA3


5
PA4
AI/O
5V
4/8/12/16 mA 
PA4, this pin provides a UART_TX function in the 


Boot loader mode


6
PA5
AI/O
5V
4/8/12/16 mA 
PA5, this pin provides a UART_RX function in the 


Boot loader mode


7
6
PA6
AI/O
5V
4/8/12/16 mA PA6


8
7
PA7
AI/O
5V
4/8/12/16 mA PA7


9
8
PC4
AI/O
5V
4/8/12/16 mA PC4


10
PC5
AI/O
5V
4/8/12/16 mA PC5


11
PC6
AI/O
5V
4/8/12/16 mA PC6


12
PC7
AI/O
5V
4/8/12/16 mA PC7


13
9
CLDO
P
—
—


Core power LDO V
CORE
 output
A 2.2 μF capacitor must be connected as close as 
possible between this pin and VSS


14
10
VDD/VDDA
P
—
—
Digital and analog voltage input


15
11
VSS/VSSA
P
—
—
Ground reference


16
12
nRST
(3)
I
5V_PU
—
External reset pin


17
PB10
(3)
I/O


(V
DD
)
5V
4/8/12/16 mA PB10


18
PB11
(3)
I/O


(V
DD
)
5V
4/8/12/16 mA PB11


19
PB13
AI/O
5V
4/8/12/16 mA XTALIN


20
PB14
AI/O
5V
4/8/12/16 mA XTALOUT


21
13
PA13
I/O
5V_PU
4/8/12/16 mA SWDIO


22
14
PA12
I/O
5V_PU
4/8/12/16 mA SWCLK


23
PA8
I/O
5V
4/8/12/16 mA PA8


24
15
PA9
I/O
5V_PU
4/8/12/16 mA PA9_BOOT


25
16
GLC
O
─
─
Low-side gate drive phase C


26
17
GHC
O
─
─
High-side gate drive phase C


27
18
SHC
I
─
─
High-side source connection phase C


28
19
BSTC
O
─
─
Bootstrap output phase C


29
20
GLB
O
─
─
Low-side gate drive phase B


30
21
GHB
O
─
─
High-side gate drive phase B


31
22
SHB
I
─
─
High-side source connection phase B


32
23
BSTB
O
─
─
Bootstrap output phase B


33
24
GLA
O
─
─
Low-side gate drive phase A


34
25
GHA
O
─
─
High-side gate drive phase A


35
26
SHA
I
─
─
High-side source connection phase A


36
27
BSTA
O
─
─
Bootstrap output phase A


37
28
LSS
I
—
—
Low-side source connection for phase A, B and C. 
Connect to ground of power stage.


38
29
V12P
O
—
—
Supplied from VCC. Regulated 12 V output (V12P 
only supplies power to the device internal circuit)


Rev. 1.00	
35 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**5  Pin Assignment**


**Pin Number**


**Pin Name**
**Type**
**(1)**
**I/O **


**Structure**
**(2)**


**Output**


**Driving**


**Description**


**48 LQFP-EP 32 QFN**
**Default Function (AF0)**


39
30
VCC
P
—
—
VCC power supply input


40
31
VREG
O
—
—
Supplied from VCC. Regulated 5 V output. Always 
active


41
PB4
I/O
5V
4/8/12/16 mA PB4


42
PB5
I/O
5V
4/8/12/16 mA PB5


43
PC1
AI/O
5V
4/8/12/16 mA PC1


44
PC2
AI/O
5V
4/8/12/16 mA PC2


45
32
PC3
AI/O
5V
4/8/12/16 mA PC3


46
1
PB6
AI/O
5V
4/8/12/16 mA PB6


47
2
PB7
AI/O
5V
4/8/12/16 mA PB7


48
3
PB8
AI/O
5V
4/8/12/16 mA PB8


Note: 1. I = Input, O = Output, A = Analog Port, P = Power Supply, V
DD
 = V
DD
 Power.


2. 5V = 5 V operation I/O type, PU = Pull-up.
3. These pins are located at the V
DD
 power domain.
4. The EP which means the thermally enhanced Exposed Pad on the packages must be connected to ground.


**Internal Connection Signal Lines**


The MCU generated signals such as the MCTM channel outputs have been internally connected to 
the gate-driver inputs for control purpose. The connections are listed in the following table and the 
related control registers should be configured correctly using application program.


**Table 7.  Internal Connection Signal Lines**


**MCU Signal Name**


**Connected **


**Gate-Driver **


**Signal Name**


**Description**


PC9 / MT_CH0 (MCTM)
INHA


Control input for high-side gate drive phase A, high active. 
The MCU AFIO setting should be AF4 to select the MCTM pin 
function.


PC8 / MT_CH0N (MCTM)
INLA


Control input for low-side gate drive phase A, low active. The 
MCU AFIO setting should be AF4 to select the MCTM pin 
function.


PB1/ MT_CH1 (MCTM)
INHB


Control input for high-side gate drive phase B, high active. 
The MCU AFIO setting should be AF4 to select the MCTM pin 
function.


PB0 / MT_CH1N (MCTM)
INLB


Control input for low-side gate drive phase B, low active. The 
MCU AFIO setting should be AF4 to select the MCTM pin 
function.


PA15 / MT_CH2 (MCTM)
INHC


Control input for high-side gate drive phase C, high active. 
The MCU AFIO setting should be AF4 to select the MCTM pin 
function.


PA14 / MT_CH2N (MCTM)
INLC


Control input for low-side gate drive phase C, low active. The 
MCU AFIO setting should be AF4 to select the MCTM pin 
function.


PC12 
EN


Gate-Driver enable pin. When EN=‘0’, in its internal circuits, 
only the 5V VREG keeps active. The MCU AFIO setting should 
be AF0 to select the General Purpose Input/Output pin function.


Rev. 1.00	
36 of 55
April 29, 2022


**6  Application Circuits**


# 6 
# 6 
##  Application Circuits


**Typical Application Circuit – 1-Shunt Current Sensing**


3


3


3


3


V
REG


(5V)


V
CC


(6V to 40V)


N


**HT32F65532G**


LSS


VCC


VREG


C3


2.2µF/16V


C1


4.7µF/50V


R
S


BSTx


GHx


SHx


GLx


C
B


2.2µF/25V


R
G1


R
G2
D
G1


R
G3


R
G4
D
G2


US


U


VS


V


W


WS


V12P


C2


2.2µF/25V


V
CC


C4
22µF/50V


VDD/VDDA


C6


0.1µF/16V


VSS/VSSA


V
REG
OP Amp Gain 


Circuit


OPAP


OPAN


OPAO


*Gate resistor block is optional


*Gate resistor block is optional


*Current sensing block is optional 


If not used, connect LSS to ground


R
SN


C
SN


*Snubber block 


is optional


R
SH


D
SH


*Voltage clamp


 block is optional


C5
0.1µF/50V


R1


*R1 is optional


*C5 is optional


OPAP
OPAN
OPAO


3


Note: V12P only supplies power to the device internal circuit.


**Figure 11.  1-Shunt FOC Application Circuit **


Rev. 1.00	
37 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


# 7 
# 7 
##  Electrical Characteristics


**Absolute Maximum Ratings**


The following table shows the absolute maximum ratings of the device. These are stress ratings 
only. Stresses beyond absolute maximum ratings may cause permanent damage to the device. Note 
that the device is not guaranteed to operate properly at the maximum ratings. Exposure to the 
absolute maximum rating conditions for extended periods may affect device reliability.


**Table 8.  Absolute Maximum Ratings**


**Parameter**
**Value**
**Unit**


V
CC
6 to 48
V


V
DD
, V
DDA
 
(V
SS
 - 0.3) to (V
SS
 + 5.5)
V


SHx
-2 (<1µs) to 48
V


BSTx, GHx
-0.3 to 60
V


V
(GHx, SHx)
, V
(BSTx, SHx)
-0.3 to 20
V


V12P, GLx
-0.3 to 20
V


VREG, INHx, INLx, EN
-0.3 to 7.0
V


Ambient Operating Temperature Range
-40 to 105
°C


Storage Temperature Range
-60 to 150
°C


Maximum Junction Temperature
125
°C


Electrostatic Discharge Voltage
Human Body Model
±4000
V


Junction-to-Ambient Thermal 
Resistance, θ
JA


48LQFP-EP
50
°C/W


32QFN
47
°C/W


**Recommended DC Operating Conditions**


**Table 9.  Recommended DC Operating Conditions**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
CC
Power Supply Voltage 
—
6
—
40
V


V
DD
Operating Voltage
—
2.5
5.0
5.5
V


V
DDA
Analog Operating Voltage
—
2.5
5.0
5.5
V


Rev. 1.00	
38 of 55
April 29, 2022


**7  Electrical Characteristics**


**On-Chip LDO Voltage Regulator Characteristics**


**Table 10.  LDO Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
LDO
Internal Regulator Output 
Voltage


V
DD
 ≥ 2.5 V Regulator input 
@ I
LDO
 = 35 mA and voltage 
variation = ± 5 %, After trimming


1.425
1.5
1.57
V


I
LDO
Output Current
V
DD
 = 2.5 V Regulator input 
@ V
LDO 
= 1.5 V
—
30
35
mA


C
LDO


External Filter Capacitor 
Value for Internal Core 
Power Supply


The capacitor value is 
dependent on the core power 
current consumption


1
2.2
—
μF


**Power Consumption**


**Table 11.  Power Consumption Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ. Max. Unit**


I
DD
Supply Current

(Run Mode)


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 60 MHz,
f
HCLK
 = 60 MHz, f
PCLK
 = 60 MHz, 
all peripherals enabled


—
16.76
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 60 MHz, 
f
HCLK
 = 60 MHz, f
PCLK
 = 60 MHz, 
all peripherals disabled


—
7.54
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 40 MHz, 
f
HCLK
 = 40 MHz, f
PCLK
 = 40 MHz, 
all peripherals enabled


—
13.9
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 40 MHz, 
f
HCLK
 = 40 MHz, f
PCLK
 = 40 MHz, 
all peripherals disabled


—
7.69
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 20 MHz, 
f
HCLK
 = 20 MHz, f
PCLK
 = 20 MHz, 
all peripherals enabled


—
6.56
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 20 MHz, 
f
HCLK
 = 20 MHz, f
PCLK
 = 20 MHz, 
all peripherals disabled


—
3.44
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL off, 
f
HCLK
 = 8 MHz, f
PCLK
 = 8 MHz, 
all peripherals enabled


—
2.69
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL off, 
f
HCLK
 = 8 MHz, f
PCLK
 = 8 MHz, 
all peripherals disabled


—
1.43
—
mA


V
DD
 = 5.0 V, HSI off, PLL off, LSI on, 
f
HCLK
 = 32 kHz, f
PCLK
 = 32 kHz, 
all peripherals enabled


—
34.6
—
μA


V
DD
 = 5.0 V, HSI off, PLL off, LSI on, 
f
HCLK
 = 32 kHz, f
PCLK
 = 32 kHz, 
all peripherals disabled


—
29.6
—
μA


Rev. 1.00	
39 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ. Max. Unit**


I
DD


Supply Current

(Sleep Mode)


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 60 MHz, 
f
HCLK
 = 0 MHz, f
PCLK
 = 60 MHz, 
all peripherals enabled


—
11.22
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 60 MHz, 
f
HCLK
 = 0 MHz, f
PCLK
 = 60 MHz, 
all peripherals disabled


—
1.19
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 40 MHz, 
f
HCLK
 = 0 MHz, f
PCLK
 = 40 MHz, 
all peripherals enabled


—
7.63
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 40 MHz, 
f
HCLK
 = 0 MHz, f
PCLK
 = 40 MHz, 
all peripherals disabled


—
0.94
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 20 MHz, 
f
HCLK
 = 0 MHz, f
PCLK
 = 20 MHz, 
all peripherals enabled


—
4.16
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL = 20 MHz, 
f
HCLK
 = 0 MHz, f
PCLK
 = 20 MHz, 
all peripherals disabled


—
0.73
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL off, 
f
HCLK
 = 0 MHz, f
PCLK
 = 8 MHz, 
all peripherals enabled


—
1.72
—
mA


V
DD
 = 5.0 V, HSI = 8 MHz, PLL off, 
f
HCLK
 = 0 MHz, f
PCLK
 = 8 MHz, 
all peripherals disabled


—
0.35
—
mA


Supply Current

(Deep-Sleep Mode)


V
DD
 = 5.0 V, all clock off (HSE/HSI), 
LDO in low power mode, LSI on, LSTM 
on


—
25
—
μA


Note: 1. HSE means high speed external oscillator. HSI means 8 MHz high speed internal oscillator.


2. LSI means 32 kHz low speed internal oscillator.
3. Code = while (1) { 208 NOP } executed in Flash.


**Reset and Supply Monitor Characteristics**


**Table 12.  V**
**DD**
** Power Reset Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
POR
Power On Reset Threshold
(Rising Voltage on V
DD
)


T
A
 = -40 °C ~ 105 °C


2.22
2.35
2.48
V


V
PDR
Power Down Reset Threshold
(Falling Voltage on V
DD
) 
2.09
2.20
2.33
V


V
PORHYST
POR Hysteresis
—
—
150
—
mV


t
POR
Reset Delay Time
V
DD
 = 5.0 V
—
0.1
0.2
ms


Note: 1. Data based on characterization results only, not tested in production.


2. If the LDO is turned on, the V
DD
 POR has to be in the de-assertion condition. When the V
DD
 


POR is in the assertion state then the LDO will be turned off.


Rev. 1.00	
40 of 55
April 29, 2022


**7  Electrical Characteristics**


**Table 13.  LVD/BOD Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
BOD
Voltage of Brown-Out 
Detection 


After factory-trimmed
V
DD
 Falling edge
2.37
2.45
2.53
V


V
LVD
Voltage of Low Voltage 
Detection
V
DD
 Falling edge


LVDS = 000
2.57
2.65
2.73
V


LVDS = 001
2.77
2.85
2.93
V


LVDS = 010
2.97
3.05
3.13
V


LVDS = 011
3.17
3.25
3.33
V


LVDS = 100
3.37
3.45
3.53
V


LVDS = 101
4.15
4.25
4.35
V


LVDS = 110
4.35
4.45
4.55
V


LVDS = 111
4.55
4.65
4.75
V


V
LVDHTST
LVD Hysteresis
V
DD 
= 5.0 V
—
—
100
—
mV


t
suLVD
LVD Setup Time
V
DD 
= 5.0 V
—
—
—
5
μs


t
atLVD
LVD Active Delay Time
V
DD 
= 5.0 V
—
—
—
—
ms


I
DDLVD
Operation Current
 (3)
V
DD 
= 5.0 V
—
—
10
20
μA


Note: 1. Data based on characterization results only, not tested in production.


2. Bandgap current is not included.
3. LVDS field is in the PWRCU LVDCSR register.


**External Clock Characteristics**


**Table 14.  High Speed External Clock (HSE) Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
DD
Operation Voltage Range
—
2.5
—
5.5
V


f
HSE
HSE Frequency 
—
4
—
16
MHz


C
L
Load Capacitance
V
DD
 = 5.0 V, R
ESR
 = 100 Ω 
@ 16 MHz
—
—
22
pF


R
FHSE


Internal Feedback Resistor 
between XTALIN and 
XTALOUT pins


—
—
0.5
—
MΩ


R
ESR
Equivalent Series Resistance


V
DD
 = 5.0 V, C
L
 = 12 pF 
@ 16 MHz, HSEDR = 0


—
—
160
Ω


V
DD
 = 2.5 V, C
L
 = 12 pF 
@ 16 MHz, HSEDR = 1


D
HSE
HSE Oscillator Duty Cycle
—
40
—
60
%


I
DDHSE
HSE Oscillator Current 
Consumption
V
DD
 = 5.0 V @ 16 MHz
—
TBD
—
mA


I
PWDHSE
HSE Oscillator Power Down 
Current
V
DD
 = 5.0 V
—
—
0.01
μA


t
SUHSE
HSE Oscillator Startup Time
V
DD
 = 5.0 V
—
—
4
ms


Rev. 1.00	
41 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


**Internal Clock Characteristics**


**Table 15.  High Speed Internal Clock (HSI) Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
DD
Operation Voltage Range
T
A
 = -40 °C ~ 105 °C
2.5
—
5.5
V


f
HSI
HSI Frequency
V
DD
 = 5.0 V @ 25 °C
—
8
—
MHz


ACC
HSI
Factory Calibrated HSI 
Oscillator Frequency Accuracy


V
DD
 = 5.0 V
T
A
 = 25 °C
-2
—
+2
%


V
DD
 = 2.5 V ~ 5.5 V 
T
A
 = -20 °C ~ 85 °C
-3
—
+3
%


V
DD
 = 2.5 V ~ 5.5 V 
T
A
 = 85 °C ~ 105 °C or    
T
A
 = -40 °C ~ -20 °C


-3.5
—
+3.5
%


Duty
Duty Cycle
f
HSI
 = 8 MHz
35
—
65
%


I
DDHSI


Oscillator Supply Current


f
HSI
 = 8 MHz


—
300
500


μA


Power Down Current
—
—
0.05


t
SUHSI
HSI Oscillator Startup Time
f
HSI
 = 8 MHz
—
—
10
μs


**Table 16.  Low Speed Internal Clock (LSI) Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
DD
Operation Voltage Range
—
2.5
—
5.5
V


f
LSI
LSI Frequency
V
DD
 = 5.0 V,
T
A
 = -40 °C ~ 105 °C
21
32
43
kHz


ACC
LSI
LSI Frequency Accuracy
After factory-trimmed, 
V
DD
 = 5.0 V, T
A
 = 25 °C
-10
—
+10
%


I
DDLSI
LSI Oscillator Operating Current
V
DD
 = 5.0 V, T
A
 = 25 °C
—
0.4
0.8
μA


t
SULSI
LSI Oscillator Startup Time
V
DD
 = 5.0 V, T
A
 = 25 °C
—
—
100
μs


**System PLL Characteristics**


**Table 17.  System PLL Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ. Max. Unit**


f
PLLIN
System PLL Input Clock
—
4
—
16
MHz


f
CK_PLL
System PLL Output Clock
—
16
—
60
MHz


t
LOCK
System PLL Lock Time
—
—
200
—
μs


Rev. 1.00	
42 of 55
April 29, 2022


**7  Electrical Characteristics**


**Memory Characteristics**


**Table 18.  Flash Memory Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


N
ENDU


Number of Guaranteed Program/
Erase Cycles before failure 
(Endurance)


T
A
 = -40 °C ~ 105 °C
10
—
—
K cycles


t
RET
Data Retention Time
T
A
 = -40 °C ~ 105 °C
10
—
—
Years


t
PROG
Word Programming Time
T
A
 = -40 °C ~ 105 °C
20
—
—
μs


t
ERASE
Page Erase Time
T
A
 = -40 °C ~ 105 °C
2
—
—
ms


t
MERASE
Mass Erase Time
T
A
 = -40 °C ~ 105 °C
10
—
—
ms


**I/O Port Characteristics**


**Table 19.  I/O Port Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


I
IL
Low Level Input 
Current


5.0 V I/O
V
I
 = V
SS
, On-chip pull-up 
resister disabled


—
—
3


μA


Reset pin
—
—
3


I
IH
High Level Input 
Current


5.0 V I/O
V
I 
= V
DD,
 On-chip pull-down 
resister disabled


—
—
3


μA


Reset pin
—
—
3


V
IL
Low Level Input 
Voltage


5.0 V I/O
-0.5
—
0.35 


× V
DD
 


V


Reset pin
-0.5
—
0.35 


× V
DD


V
IH
High Level Input 
Voltage


5.0 V I/O
0.65
 


× V
DD
 
—
V
DD


+ 0.5


V


Reset pin
0.65
 


× V
DD
—
V
DD


+ 0.5


V
HYS
Schmitt Trigger Input
Voltage Hysteresis


5.0 V I/O
—
0.12 


× V
DD
—


mV


Reset pin
—
0.12


× V
DD
—


I
OL


Low Level Output 
Current
(GPIO Sink Current)


5.0 V I/O 4 mA drive, V
OL 
= 0.4 V
4
—
—
mA


5.0 V I/O 8 mA drive, V
OL 
= 0.4 V
8
—
—
mA


5.0 V I/O 12 mA drive, V
OL 
= 0.4 V
12
—
—
mA


5.0 V I/O 16 mA drive, V
OL 
= 0.4 V
16
—
—
mA


V
DD
 Domain I/O drive @ V
DD
 = 5.0 V, 
V
OL 
= 0.4 V, PB10, PB11
4
—
—
mA


Rev. 1.00	
43 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


I
OH


High Level Output 
Current
(GPIO Source 
Current)


5.0 V I/O 4 mA drive, V
OH 
= V
DD
 - 0.4 V 
4
—
—
mA


5.0 V I/O 8 mA drive, V
OH 
= V
DD
 - 0.4 V 
8
—
—
mA


5.0 V I/O 12 mA drive, V
OH 
= V
DD
 - 0.4 V
12
—
—
mA


5.0 V I/O 16 mA drive, V
OH 
= V
DD
 - 0.4 V
16
—
—
mA


V
DD
 Domain I/O drive @ V
DD
 = 5.0 V,
V
OH 
= V
DD
 - 0.4 V, PB10, PB11
—
—
2
mA


V
OL
Low Level Output 
Voltage


5.0 V 4 mA drive I/O, I
OL 
= 4 mA
—
—
0.4


V


5.0 V 8 mA drive I/O, I
OL 
= 8 mA
—
—
0.4


5.0 V 12 mA drive I/O, I
OL 
= 12 mA
—
—
0.4


5.0 V 16 mA drive I/O, I
OL 
= 16 mA
—
—
0.4


V
OH
High Level Output 
Voltage


5.0 V 4 mA drive I/O, I
OH 
= 4 mA
V
DD


- 0.4
—
—


V


5.0 V 8 mA drive I/O, I
OH 
= 8 mA
V
DD


- 0.4
—
—


5.0 V 12 mA drive I/O, I
OH 
= 12 mA
V
DD


- 0.4
—
—


5.0 V 16 mA drive I/O, I
OH 
= 16 mA
V
DD


- 0.4
—
—


R
PU
Internal Pull-up 
Resistor
5.0 V I/O, V
DD
 = 5.0 V
—
60
—
kΩ


R
PD
Internal Pull-down 
Resistor
5.0 V I/O, V
DD
 = 5.0 V
—
60
—
kΩ


**ADC Characteristics**


**Table 20.  ADC Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min. Typ. Max.**
**Unit**


V
DDA
A/D Converter Operating Voltage
—
2.5
5.0
5.5
V


V
ADCIN
A/D Converter Input Voltage Range
—
0
—
V
REF+
V


V
REF+
A/D Converter Reference Voltage
—
—
V
DDA
V
DDA
V


I
ADC
A/D Converter Operating Current
V
DDA
 = 5.0 V
—
0.85
1
mA


I
ADC_DN
Power Down Current Consumption V
DDA
 = 5.0 V
—
—
0.1
μA


f
ADC
A/D Converter Clock Frequency
—
0.7
—
32
MHz


f
S
Sampling Rate
—
0.05
—
2
MHz


t
DL
Data Latency
—
—
12.5
—
1/f
ADC


Cycles


t
S&H
Sampling & Hold Time
—
—
3.5
—
1/f
ADC


Cycles


t
ADCCONV
A/D Converter Conversion Time
—
—
16
—
1/f
ADC


Cycles


R
I
Input Sampling Switch Resistance
—
—
—
1
kΩ


C
I
Input Sampling Capacitance
No pin / pad capacitance 
included
—
16
—
pF


Rev. 1.00	
44 of 55
April 29, 2022


**7  Electrical Characteristics**


**Symbol**
**Parameter**
**Conditions**
**Min. Typ. Max.**
**Unit**


t
SU
Startup Time
—
—
—
1
μs


N
Resolution
—
—
12
—
bits


INL
Integral Non-linearity Error
f
S
 = 750 kHz, V
DDA
 = 5.0 V
—
—
±2
LSB


DNL
Differential Non-linearity Error
f
S
 = 750 kHz, V
DDA
 = 5.0 V
—
—
±1
LSB


E
O
Offset Error
—
—
—
±10
LSB


E
G
Gain Error
—
—
—
±10
LSB


Note: 1. Data based on characterization results only, not tested in production.


2. The figure below shows the equivalent circuit of the A/D Converter Sample-and-Hold input 


stage where C
I
 is the storage capacitor, R
I
 is the resistance of the sampling switch and R
S
 
is the output impedance of the signal source V
S
. Normally the sampling phase duration is 
approximately, 3.5/f
ADC
. The capacitance, C
I
, must be charged within this time frame and 
it must be ensured that the voltage at its terminals becomes sufficiently close to V
S
 for 
accuracy. To guarantee this, R
S
 is not allowed to have an arbitrarily large value.


SAR ADC


C
I


sample


R
I


R
S


V
S


**Figure 12.  ADC Sampling Network Model**


The worst case occurs when the extremities of the input range (0 V and V
REF
) are sampled 
consecutively. In this situation a sampling error below ¼ LSB is ensured by using the following 
equation:


I
2
N


I
ADC


S
R
)
2
ln(
C
f


5.3
R





Where f
ADC
 is the ADC clock frequency and N is the ADC resolution (N = 12 in this case). A safe 
margin should be considered due to the pin/pad parasitic capacitances, which are not accounted for 
in this simple model.


If, in a system where the A/D Converter is used, there are no rail-to-rail input voltage variations 
between consecutive sampling phases, R
S
 may be larger than the value indicated by the equation 
above.


Rev. 1.00	
45 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


**Comparator Characteristics**


**Table 21.  Comparator Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min. Typ. Max. Unit**


V
DDA
Operating Voltage
Comparator mode
2.5
5.0
5.5
V


V
IN
Input Common Mode 
Voltage Range
CP or CN
V
SSA
—
V
DDA
V


V
IOS
Input Offset Voltage
(1)
—
-15
—
15
mV


V
HYS
Input Hysteresis
V
DDA
 = 5.0 V


No hysteresis, CMPHM [1:0] = 00
—
0
—
mV


Low hysteresis, CMPHM [1:0] = 01
—
30
—
mV


Middle hysteresis, CMPHM [1:0] = 10
—
60
—
mV


High hysteresis, CMPHM [1:0] = 11
—
100
—
mV


t
RT
Response Time
Input Overdrive = ±100 mV


High Speed Mode


V
DDA 
≥ 2.7 V
—
50
100


ns


V
DDA
 < 2.7 V
—
100
250


Low Speed Mode
—
2
5
µs


I
CMP
Current Consumption
V
DDA
 = 5.0 V


High Speed Mode
—
180
—
µA


Low Speed Mode
—
30
—
µA


t
CMPST
Comparator Startup Time Comparator enabled to output valid
—
—
50
µs


I
CMP_DN
Power Down Supply 
Current


CMPEN = 0
CVREN = 0
CVROE = 0


—
—
0.1
µA


**Comparator Voltage Reference (CVR)**


V
CVR
Output Range
—
V
SSA
—
V
DDA
V


N
Bits
CVR Scaler Resolution
—
—
8
—
bits


t
CVRST
Settling Time


CVR Scaler Settling Time 
from CVRVAL = “00000000” to 
“11111111” 


—
—
100
µs


I
CVR
Current Consumption
V
DDA
 = 5.0 V


CVREN = 1, CVROE = 0
—
65
—
µA


CVREN = 1, CVROE = 1
—
80
110
µA


Note: Data based on characterization results only, not tested in production.


**Operational Amplifier Characteristics**


**Table 22.  Operational Amplifier Characteristics**


T
A
 = 25 °C, unless otherwise specified.


**Symbol**
**Parameter**
**Conditions**
**Min. Typ. Max. Unit**


V
DDA
Operating Voltage
OPA mode
3.0
5.0
5.5
V


I
OPA_DN
Power Down Current
—
—
—
0.1
µA


I
OPA
Operating Current
V
DD
 = 5 V
—
800
—
µA


V
OS
Input Offset Voltage


Without calibration
(OOF[4:0] = 10000B)
-15
—
15


mV


With calibration
-2
—
2


Rev. 1.00	
46 of 55
April 29, 2022


**7  Electrical Characteristics**


**Symbol**
**Parameter**
**Conditions**
**Min. Typ. Max. Unit**


V
OR
Maximum Output Voltage 
Range
—
V
SS


+ 0.2
—
V
DD


- 0.2
V


I
OS
Input Offset Current
V
IN
 = 1/2 V
CM
—
1
10
nA


PSRR
Power Supply Rejection Ratio
—
—
60
—
dB


CMRR
Common Mode Rejection Ratio V
CM
 = 0 ~ V
DD
 - 1.4
—
60
—
dB


SR
Slew Rate+, Slew Rate-
R
L
 = 100 kΩ, C
L
 = 50 pF
—
6
—
V/µs


GBW
Gain Band Width
R
L
 = 100 kΩ, C
L
 = 50 pF
—
6
—
MHz


A
OL
Open Loop Gain
R
L
 = 100 kΩ, C
L
 = 50 pF
60
80
—
dB


PM
Phase Margin
R
L
 = 100 kΩ, C
L
 = 50 pF
50
60
—
Deg


V
CM
Common Mode Voltage Range
—
V
SS
—
V
DD


- 1.4
V


**MCTM/GPTM/SCTM Characteristics**


**Table 23.  MCTM / GPTM / SCTM Characteristics**


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


f
TM
Timer Clock Source for MCTM, 
GPTM and SCTM
—
—
—
f
PCLK
MHz


t
RES
Timer Resolution Time
—
1
—
—
1/f
TM


f
EXT
External Signal Frequency on 
Channel 0 ~ 3
—
—
—
1/2
f
TM


RES
Timer Resolution
—
—
—
16
bits


**Gate-Driver Characteristics**


**Table 24.  Gate-Driver Characteristics**


V
CC 
= 24 V, C1 = 4.7 μF, C2 = 2.2 μF, C3 = 2.2 μF, C4 = 22 μF,


C
B 
= 2.2 μF and T
A 
= 25˚C, unless otherwise specified.


**Symbol**
**Parameter**
** Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


**Power Supply / Regulators**


V
CC
Supply Voltage
—
6
—
40
V


I
CC
Supply Standby Current
EN = ‘1’, I
LOAD 
= 0 mA
(SHx = GND)
—
300
400
μA


I
CC(SLP)
Supply Sleep Current
EN = ‘0’ (only VREG is 
active without load)
—
2
4
μA


V
REG
VREG Output Voltage
I
LOAD
 = 1 mA
4.925
5.0
5.075
V


I
LOAD
 
(1)
VREG Output Current
V
CC
 = 6 V ~ 40 V
(without thermal limited)
50
—
—
mA


∆V
REG
VREG Load Regulation
I
LOAD
 = 0 mA ~ 30 mA
—
15
—
mV


∆V
REG


∆V
CC
×V
REG
VREG Linear Regulation 
V
CC
 rises from 6 V to 40 V
—
0.1
0.2
%/V


Rev. 1.00	
47 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


**Symbol**
**Parameter**
** Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


∆V
REG


∆T
A
×V
REG


VREG Temperature 
Coefficient


I
LOAD
 = 1 mA,
T
A
 = -40 ˚C ~ 105 ˚C
—
±100
—
ppm/˚C


PSRR
VREG Power Supply 
Rejection Ratio
I
LOAD
 = 30 mA
—
60
—
dB


Noise
VREG Output Noise
I
LOAD
 = 30 mA,
BW = 10 kHz ~ 100 kHz
—
50
—
μV
RMS


**Bootstrap**


I
BST
Current Consumption from 
BST
INHx = ‘1’ and INLx = ‘1’
—
80
100
μA


I
BSTC
Bootstrap Charging Current
INHx = ‘0’ and INLx = ‘1’ 
(SHx = GND)
—
25
—
mA


**Gate-Driver (GHx, SHx, GLx)**


V
GSH
High-Side V
GS
 Gate Drive – 
V
(GHx,SHx)


V
CC
 = 6 V ~ 13 V,
f
PWM
 = 25 kHz
V
CC
-2 V
CC
-1.5
—
V


V
CC
 = 13 V ~ 40 V,
f
PWM
 = 25 kHz
11
12
13
V


V
GSL
Low-Side V
GS
 Gate Drive – 
V
(GLx,LSS)


V
CC
 = 6 V ~ 13 V
V
CC
-1 V
CC
-0.5
—
V


V
CC
 = 13 V ~ 40 V
11
12
—
V


I
DRVP
High-Side and Low-Side 
Gate Peak Source Current


R
DRV
 = open,
C
GS
 = 200 nF
—
700
—
mA


I
DRVN
High-Side and Low-Side 
Gate Peak Sink Current


R
DRV
 = open,
C
GS
 = 200 nF
—
1000
—
mA


t
DEAD
Dead Time
—
—
120
200
ns


t
DEAD_MIS
Dead Time Mismatch


Dead time difference 
between rising and 
falling edges


—
50
—
ns


t
PD
Propagation Delay


INHx to GHx and INLx 
to GLx transition (No 
connected capacitor with 
GHx / GLx)


—
40
200
ns


t
PD_MIS


High-Side / Low-Side 
Propagation Delay 
Mismatch


Propagation delay 
difference between 
different phases or 
different sides


—
20
—
ns


t
ON_MIN
Minimum Input Pulse 
Width
(2)
—
—
—
150
ns


R
OFF1
Low-Side Gate Hold-off 
Resistor
GLx to LSS
—
200
—
kΩ


R
OFF2
High-Side Gate Hold-off 
Resistor
GHx to SHx
—
400
—
kΩ


**Protections**


V
CC_UVLO+
V
CC
 Turn On Level
V
CC
 rises
—
5.5
6
V


V
CC_UVLO-
V
CC
 Turn Off Level
V
CC
 falls
4.5
5.0
—
V


V
REG_UVLO+
V
REG
 Turn On Level
V
REG
 rises
—
—
4.0
V


V
REG_UVLO-
V
REG
 Turn Off Level
V
REG
 falls
3.0
—
—
V


V
12P_UVLO+
V
12P
 Turn On Level
V
12P
 rises, INLx = ‘0’
—
5.5
6
V


Rev. 1.00	
48 of 55
April 29, 2022


**7  Electrical Characteristics**


**Symbol**
**Parameter**
** Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


V
12P_UVLO-
V
12P
 Turn Off Level
V
12P
 falls, INLx = ‘0’
4.2
5.0
—
V


V
BST_UVLO+
V
(BSTx,SHx)
 Turn On Level
V
(BSTx,SHx)
 rises, INHx = ‘1’
—
3.7
4.2
V


V
BST_UVLO-
V
(BSTx,SHx)
 Turn Off Level
V
(BSTx,SHx)
 falls, INHx = ‘1’
2.2
2.6
—
V


T
SHD
Thermal Shutdown Threshold —
—
160
—
˚C


T
REC
Thermal Recovery Threshold —
—
120
—
˚C


**Control Logic**


V
IL
Input Logic Low Voltage
INHx, INLx, EN
—
—
0.8
V


V
IH
Input Logic High Voltage
INHx, INLx, EN
2.0
—
—
V


R
PD1
Input Logic Pull-down 
Resistor 1
INHx
—
100
—
kΩ


R
PD2
Input Logic Pull-down 
Resistor 2
EN
—
10
—
kΩ


R
PU
Input Logic Pull-up Resistor
INLx
—
100
—
kΩ


Note: 1. Output current standard: the output voltage might keep a 2% voltage drop compared to the 


original output voltage for a 1mA load current.


2. When the INHx or INLx input signal pulse width is less than t
ON_MIN
, the output may 


malfunction.


V
INLx


50%


V
(GHx_SHx)


V
INHx


50%


t
PD


V
(GLx_LSS)


t
DEAD


t


t


t


t


50%


50%


t
PD
t
PD


t
PD


Less than 150ns(t
ON_MIN
)


t
DEAD


Less than 150ns(t
ON_MIN
)


Abnormal Output


Abnormal Output


**Figure 13.  Gate Drive Timing Diagram**


Rev. 1.00	
49 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


**I**
**2**
**C Characteristics**


**Table 25.  I**
**2**
**C Characteristics**


**Symbol**
**Parameter**


**Standard **


**Mode**


**Fast **


**Mode**


**Fast Plus **


**Mode**
**Unit**


**Min.**
**Max.**
**Min.**
**Max.**
**Min.**
**Max.**


f
SCL
SCL Clock Frequency
—
100
—
400
—
1000
kHz


t
SCL(H)
SCL Clock High Time
4.5
—
1.125
—
0.45
—
μs


t
SCL(L)
SCL Clock Low Time
4.5
—
1.125
—
0.45
—
μs


t
FALL
SCL and SDA Fall Time
—
1.3
—
0.34
—
0.135
μs


t
RISE
SCL and SDA Rise Time
—
1.3
—
0.34
—
0.135
μs


t
SU(SDA)
SDA Data Setup Time
500
—
125
—
50
—
ns


t
H(SDA)
SDA Data Hold Time
0
—
0
—
0
—
ns


t
SU(STA)
START Condition Setup Time
500
—
125
—
50
—
ns


t
H(STA)
START Condition Hold Time
0
—
0
—
0
—
ns


t
SU(STO)
STOP Condition Setup Time
500
—
125
—
50
—
ns


Note: 1. Data based on characterization results only, not tested in production.


2. To achieve 100 kHz standard mode, the peripheral clock frequency must be higher than 2 MHz.
3. To achieve 400 kHz fast mode, the peripheral clock frequency must be higher than 8 MHz.
4. To achieve 1 MHz fast plus mode, the peripheral clock frequency must be higher than 20 MHz.
5. The above characteristic parameters of the I
2
C bus timing are based on: SEQFILTER = 01 


and COMBFILTEREN=0 that COMB filter is disabled.


t
SU(STA)


t
H(STA)


t
FALL


t
SCL(L)


t
RISE


t
SCL(H)


t
H(SDA)
t
SU(SDA)
t
SU(STO)


SCL


SDA


**Figure 14.  I**
**2**
**C Timing Diagram**


Rev. 1.00	
50 of 55
April 29, 2022


**7  Electrical Characteristics**


**SPI Characteristics**


**Table 26.  SPI Characteristics**


**Symbol**
**Parameter**
**Conditions**
**Min.**
**Typ.**
**Max.**
**Unit**


**SPI Master Mode**


f
SCK
SPI Master Output SCK Clock 
Frequency


Master mode
SPI peripheral clock 
frequency f
PCLK


—
—
f
PCLK
/2
MHz


t
SCK(H)
t
SCK(L)
SCK Clock High and Low Time
—
t
SCK
/2


- 2
—
t
SCK
/2


+ 1
ns


t
V(MO)
Data Output Valid Time
—
—
—
5
ns


t
H(MO)
Data Output Hold Time
—
2
—
—
ns


t
SU(MI)
Data Input Setup Time
—
5
—
—
ns


t
H(MI)
Data Input Hold Time
—
5
—
—
ns


**SPI Slave Mode**


f
SCK
SPI Slave Input SCK Clock 
Frequency


Slave mode
SPI peripheral clock 
frequency f
PCLK


—
—
f
PCLK
/3
MHz


Duty
SCK
SPI Slave Input SCK Clock Duty 
Cycle
—
30
—
70
%


t
SU(SEL)
SEL Enable Setup Time
—
3 t
PCLK
—
—
ns


t
H(SEL)
SEL Enable Hold Time
—
2 t
PCLK
—
—
ns


t
A(SO)
Data Output Access Time
—
—
—
3 t
PCLK
ns


t
DIS(SO)
Data Output Disable Time
—
—
—
10
ns


t
V(SO)
Data Output Valid Time
—
—
—
25
ns


t
H(SO)
Data Output Hold Time
—
15
—
—
ns


t
SU(SI)
Data Input Setup Time
—
5
—
—
ns


t
H(SI)
Data Input Hold Time
—
4
—
—
ns


Note: 1. f
SCK
 is SPI output/input clock frequency and t
SCK
 = 1/f
SCK
.


2. f
PCLK
 is SPI peripheral clock frequency and t
PCLK
 = 1/f
PCLK
.


Rev. 1.00	
51 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**7  Electrical Characteristics**


SCK


(CPOL=0)


SCK


(CPOL=1)


MOSI


MISO


MOSI


MISO


t
SCK


t
SCK(H)
t
SCK(L)


DATA VALID
DATA VALID
DATA VALID


t
SU(MI)


t
V(MO)
t
H(MO)


t
H(MI)


DATA VALID
DATA VALID
DATA VALID


t
V(MO)
t
H(MO)


DATA VALID
DATA VALID
DATA VALID


DATA VALID
DATA VALID
DATA VALID


t
SU(MI)
t
H(MI)


CPHA=1


CPHA=0


**Figure 15.  SPI Timing Diagram – SPI Master Mode**


SCK


(CPOL=0)


SCK


(CPOL=1)


MOSI


MISO


t
SCK


t
SCK(H)
t
SCK(L)


MSB/LSB IN


t
H(SI)


t
SU(SEL)
t
H(SEL)


t
SU(SI)


LSB/MSB IN


MSB/LSB OUT
LSB/MSB OUT


t
A(SO)
t
V(SO)
t
H(SO)
t
DIS(SO)


SEL


**Figure 16.  SPI Timing Diagram – SPI Slave Mode with CPHA = 1**


Rev. 1.00	
52 of 55
April 29, 2022


HT32F65532G
with 3-channel 48 V Half-bridge Gate-Driver


-M0+ BLDC MCU
®
 Cortex
®
32-Bit Arm


**8  Package Information**


# 8 
# 8 
##  Package Information


	
●
Package Information (include Outline Dimensions, Product Tape and Reel Specifications)


	
●
The Operation Instruction of Packing Materials


	
●


Note that the package information provided here is for consultation purposes only. As this 
information may be updated at regular intervals users are reminded to consult


Additional supplementary information with regard to packaging is listed below. Click on the 
relevant section to be transferred to the relevant website page.


Carton information


Rev. 1.00	
53 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**8  Package Information**


**48-pin LQFP-EP (7mm **
× 
**7mm) Outline Dimensions**


 
 


 
 


 


 


 






     


13


12


24


25


36


37
48


1


D2


E2


THERMALLY ENHANCED VARIATIONS ONLY


**Symbol**
**Dimensions in inch**


**Min.**
**Nom.**
**Max.**


A
—
0.354 BSC
—


B
—
0.276 BSC
—


C
—
0.354 BSC
—


D
—
0.276 BSC
—


D2
0.079 
—
—


E
—
0.020 BSC
—


E2
0.079 
—
—


F
0.007
0.009
0.011


G
0.053
0.055
0.057


H
—
—
0.063 


I
0.002 
—
0.006 


J
0.018 
0.024 
0.030 


K
0.004 
—
0.008 


α
0°
―
7°


**Symbol**
**Dimensions in mm**


**Min.**
**Nom.**
**Max.**


A
—
9.00 BSC
—


B
—
7.00 BSC
—


C
—
9.00 BSC
—


D
—
7.00 BSC
—


D2
2.00
—
—


E
—
0.50 BSC
—


E2
2.00
—
—


F
0.17
0.22 
0.27


G
1.35
1.40
1.45


H
—
—
1.60 


I
0.05 
—
0.15 


J
0.45 
0.60 
0.75 


K
0.09 
—
0.20 


α
0°
―
7°


Rev. 1.00	
54 of 55
April 29, 2022


**8  Package Information**


**SAW Type 32-pin QFN (4mm × 4mm × 0.75mm) Outline Dimensions**


 
 


 


 


 


 


 


 
 


**Symbol**
**Dimensions in inch**


**Min.**
**Nom.**
**Max.**


A
0.028 
0.030 
0.031 


A1
0.000 
0.001 
0.002 


A3
—
0.008 BSC
—


b
0.006
0.008 
0.010


D
—
0.157 BSC 
—


E
—
0.157 BSC 
—


e
—
0.016 BSC
—


D2
0.104 
0.106 
0.108 


E2
0.104 
0.106 
0.108 


L
0.014 
0.016 
0.018 


K
0.008
—
—


**Symbol**
**Dimensions in mm**


**Min.**
**Nom.**
**Max.**


A
0.70
0.75
0.80


A1
0.00
0.02
0.05


A3
—
0.203 BSC
—


b
0.15
0.20
0.25


D
—
4.00 BSC
—


E
—
4.00 BSC
—


e
—
0.40 BSC
—


D2
2.65
2.70
2.75


E2
2.65
2.70
2.75


L
0.35
0.40
0.45


K
0.20
—
—


Rev. 1.00	
55 of 55
April 29, 2022


32-Bit Arm
®
 Cortex
®
-M0+ BLDC MCU
with 3-channel 48 V Half-bridge Gate-Driver
HT32F65532G


**8  Package Information**


Copyright
©
 2022 by HOLTEK SEMICONDUCTOR INC.


The information provided in this document has been produced with reasonable care and 
attention before publication, however, Holtek does not guarantee that the information 
is completely accurate and that the applications provided in this document are for 
reference only. Holtek does not guarantee that these explanations are appropriate, nor 
does it recommend the use of Holtek's products where there is a risk of personal hazard 
due to malfunction or other reasons. Holtek hereby declares that it does not authorise 
the use of these products in life-saving, life-sustaining or critical equipment. Holtek 
accepts no liability for any damages encountered by customers or third parties due to 
information errors or omissions contained in this document or damages encountered 
by the use of the product or the datasheet. Holtek reserves the right to revise the 
products or specifications described in the document without prior notice. For the latest 
information, please contact us.

