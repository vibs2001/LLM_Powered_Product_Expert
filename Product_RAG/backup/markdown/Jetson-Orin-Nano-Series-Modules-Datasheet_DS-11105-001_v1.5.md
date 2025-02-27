 
 


 
 
 
DS-11105-001_v1.5  |  December 2024 
 


# NVIDIA Jetson Orin Nano Series Modules 


## Ampere GPU + Arm Cortex-A78AE CPU + LPDDR5 


## Data Sheet 


 


 


 


 


 


 


 


 


 
 


 
 
 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  ii 


## Document History 


DS-11105-001_v1.5 


Version 
Date 
Description of Change 


v0.1 
September 20, 2022 
Initial preliminary release. 


v1.0 
February 22, 2023 
Updated: 


•
 
Minimum power ratings for Operating Requirements. 


•
 
USB 3.2 Operation text for clarification. 


•
 
Pin description for SYS_RESET* to 10k
Ω
 pull-up to VDD_1V8 on 
the module. 


•
 
Pin description for CLK_32K_OUT to 2.2k
Ω
 pull-up to VDD_1V8 on 
the module. 


•
 
PMIC_BBAT Pin Description table for clarity. 


Added: 


•
 
Absolute Maximum Ratings table. 


•
 
Storage and Handling table. 


•
 
Environmental Testing table. 


v1.1 
April 26, 2023 
Added: 


•
 
Note for internal USB 3.2 hub. 


•
 
Package drawing information. 


v1.2 
December 8, 2023 
Updated: 


•
 
UART block frequency from 200MHz to 68MHz and baud rate from 
12.5Mbps to 4.25Mbps. 


•
 
CUDA 10.2 to CUDA 11.4+ 


•
 
RTC accuracy under PMIC_BBAT. 


•
 
Open Drain Pin Type DC Characteristics table 


•
 
GEN3 to GEN4 


•
 
Pin direction in Camera Pin Descriptions table 


Added: 


•
 
Operating Lifetime (24x7): 5 years 


•
 
Notes below Supported Video Decode Streams table 


Removed features not supported: 


•
 
DMIC references 


•
 
DSPK references 


•
 
Color Decompression references 


v1.3 
August 14, 2024 
Operating Requirements: expanded temperature range (T
J
) from -25°C – 
90°C to -25°C – 105°C 


v1.4 
November 15, 2024 
Added: 


•
 
SPI timing diagrams and parameter tables 


Modified: 


•
 
Pin #217 (MODULE_ID) description. 


v1.5 
December 20, 2024 
Added: 


•
 
Extended support to include MAXN_SUPER operation 


•
 
CUDA Core Performance 


 


 
 
 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  iii 


## Table of Contents 


Chapter 1.
 
Overview ................................................................................................................................... 1
 


Chapter 2.
 
Functional Description ....................................................................................................... 4
 


2.1
 
Ampere GPU................................................................................................................................... 4
 


2.1.1
 
Compute Features .............................................................................................................. 5
 


2.1.2
 
Graphic Features.................................................................................................................. 6
 


2.2
 
Cortex CPU Complex .................................................................................................................. 6
 


2.3
 
Memory Subsystem .................................................................................................................... 7
 


2.4
 
Memory ............................................................................................................................................ 8
 


2.5
 
Video Input Interfaces ............................................................................................................... 9
 


2.5.1
 
MIPI Camera Serial Interface (CSI) ............................................................................... 9
 


2.5.2
 
Video Input (VI) ................................................................................................................... 11
 


2.5.3
 
Image Signal Processor (ISP) ........................................................................................ 11
 


2.6
 
Sensor Processing Engine ..................................................................................................... 12
 


2.7
 
Security Subsystem ................................................................................................................. 12
 


2.7.1
 
Platform Security Controller ......................................................................................... 12
 


2.7.2
 
Security Engine ................................................................................................................... 13
 


2.8
 
Display Controller ..................................................................................................................... 13
 


2.9
 
High-Definition Audio-Video Subsystem ......................................................................... 15
 


2.9.1
 
Multi-Standard Video Decoder ..................................................................................... 15
 


2.9.2
 
Video Image Compositor (VIC) ...................................................................................... 16
 


2.9.3
 
Audio Processing Engine (APE) .................................................................................... 16
 


2.9.4
 
High-Definition Audio (HDA) ......................................................................................... 17
 


2.10
 
Interface Descriptions ............................................................................................................ 18
 


2.10.1
 
Universal Serial Bus (USB) .............................................................................................. 18
 


2.10.1.1
 
USB 2.0 Operation .................................................................................................... 18
 


2.10.1.2
 
USB 3.2 Operation .................................................................................................... 19
 


2.10.2
 
PCI Express (PCIe) ............................................................................................................. 19
 


2.10.3
 
Serial Peripheral Interface (SPI) ................................................................................... 21
 


2.10.4
 
Universal Asynchronous Receiver/Transmitter (UART) ...................................... 25
 


2.10.5
 
Controller Area Network (CAN) .................................................................................... 26
 


2.10.6
 
Inter-Chip Communication (I2C) .................................................................................. 27
 


2.10.7
 
Inter-IC Sound (I2S) ........................................................................................................... 29
 


2.10.8
 
Gigabit Ethernet ................................................................................................................. 30
 


2.10.9
 
Fan ........................................................................................................................................... 30
 


2.10.10
 
Pulse Width Modulator (PWM) ..................................................................................... 30
 


Chapter 3.
 
Power and System Management ................................................................................ 32
 


3.1
 
Power Rails .................................................................................................................................. 33
 


3.2
 
Power Domains/Islands .......................................................................................................... 33
 


3.3
 
Power Management Controller (PMC) ............................................................................. 33
 


 
 
 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  iv 


3.4
 
Resets ............................................................................................................................................ 34
 


3.5
 
PMIC_BBAT ................................................................................................................................. 34
 


3.6
 
Power Sequencing .................................................................................................................... 34
 


3.6.1
 
Power Up ............................................................................................................................... 34
 


3.6.2
 
Power Down ......................................................................................................................... 35
 


3.7
 
Power States .............................................................................................................................. 35
 


3.7.1
 
ON State ................................................................................................................................ 35
 


3.7.2
 
OFF State .............................................................................................................................. 36
 


3.7.3
 
SLEEP State ......................................................................................................................... 36
 


3.8
 
Thermal and Power Monitoring ........................................................................................... 37
 


Chapter 4.
 
Pin Definitions..................................................................................................................... 38
 


4.1
 
Power-on Reset Behavior ...................................................................................................... 38
 


4.2
 
Sleep Behavior............................................................................................................................ 39
 


4.3
 
GPIO ............................................................................................................................................... 39
 


4.4
 
Pin List........................................................................................................................................... 40
 


Chapter 5.
 
Electrical, Mechanical, and Thermal Characteristics ........................................... 44
 


5.1
 
Operating and Absolute Maximum Ratings ................................................................... 44
 


5.2
 
Digital Logic ................................................................................................................................ 45
 


5.3
 
Environmental and Mechanical Screening ...................................................................... 46
 


5.4
 
Storage and Handling ............................................................................................................. 47
 


5.5
 
Drawing and Dimensions ....................................................................................................... 48
 


 
 
 


 
 
 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  v 


 
 


## List of Figures 


Figure 2-1: SPI Initiator Timing .............................................................................................................. 23
 
Figure 2-2: SPI Target Timing ................................................................................................................. 24
 
Figure 3-1:  Power State Transition Diagram ................................................................................... 35
 
Figure 5-1: Top View ................................................................................................................................... 48
 
Figure 5-2: Bottom View ........................................................................................................................... 49
 


 
## List of Tables 


Table 2-1: GPU Operation............................................................................................................................ 5
 
Table 2-2: CPU Operation ............................................................................................................................ 7
 
Table 2-3: CSI Pin Descriptions .............................................................................................................. 10
 
Table 2-4: Camera Pin Descriptions ..................................................................................................... 11
 
Table 2-5: Supported Video Decode Streams .................................................................................. 15
 
Table 2-6: USB 2.0 Pin Descriptions..................................................................................................... 18
 
Table 2-7: USB 3.2 Pin Descriptions..................................................................................................... 19
 
Table 2-8: PCIe Pin Descriptions ........................................................................................................... 20
 
Table 2-9: SPI Mode Descriptions ......................................................................................................... 22
 
Table 2-10: SPI Pin Descriptions ........................................................................................................... 22
 
Table 2-11: SPI Initiator Timing Parameters .................................................................................... 24
 
Table 2-12: SPI Target Timing Parameters ....................................................................................... 24
 
Table 2-13: UART Pin Descriptions ....................................................................................................... 26
 
Table 2-14: CAN Pin Descriptions ......................................................................................................... 27
 
Table 2-15: I2C Pin Descriptions ........................................................................................................... 28
 
Table 2-16: I2S Pin Descriptions ........................................................................................................... 29
 
Table 2-17: Gigabit Ethernet Pin Descriptions ................................................................................ 30
 
Table 2-18: PWM Pin Descriptions ....................................................................................................... 31
 
Table 3-1: Power and System Control Pin Descriptions .............................................................. 32
 
Table 3-2: PMIC_BBAT Pin Descriptions ............................................................................................ 34
 
Table 3-3: OFF State Events ................................................................................................................... 36
 
Table 3-4: SLEEP and WAKE Events .................................................................................................... 36
 
Table 4-1: GPIO Pin Descriptions .......................................................................................................... 39
 
Table 5-1: Recommended Operating Conditions ............................................................................ 44
 
Table 5-2: Absolute Maximum Ratings ............................................................................................... 45
 
Table 5-3: CMOS Pin Type DC Characteristics ................................................................................ 45
 
Table 5-4: Open Drain Pin Type DC Characteristics ...................................................................... 46
 
Table 5-5: Environmental Testing ......................................................................................................... 46
 
Table 5-6: Typical Handling and Storage Environment ................................................................ 47
 


 


 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
DS-11105-001_v1.5  |  1 


# Chapter 1.
#  
# Overview 


**Module **
**Description **


Jetson Orin Nano 8GB 
Ampere GPU + Arm Cortex-A78AE CPU + 8GB LPDDR5 


Jetson Orin Nano 4GB 
Ampere GPU + Arm Cortex-A78AE CPU + 4GB LPDDR5 


•
 
Note: References to Jetson Orin Nano can be read as Jetson Orin Nano 8GB and Jetson Orin Nano 4GB except 
where explicitly noted. 


 


**Description **
**Operation/Performance **


AI Performance 


Jetson Orin Nano 8GB 


Number of Operations (up to) 


Sparse 
•
 
40 INT8 TOPs 


•
 
67 INT8 TOPs (MAXN_SUPER) 


Dense 
•
 
20 INT8 TOPs 


•
 
33 INT8 TOPs (MAXN_SUPER) 


Jetson Orin Nano 4GB 


Number of Operations (up to) 


Sparse 
•
 
20 INT8 TOPs 


•
 
34 INT8 TOPs (MAXN_SUPER) 


Dense 
•
 
10 INT8 TOPs 


•
 
17 INT8 TOPs (MAXN_SUPER) 


Ampere GPU 


End-to-end lossless compression | Tile Caching | OpenGL® 4.6+ | OpenGL ES 3.2 | Vulkan™ 1.2
◊
 | CUDA 11.4
+
 


Operating Frequency (up to): 
•
 
625 MHz 


•
 
1020 MHz (MAXN_Super) 


Jetson Orin Nano 8GB 


CUDA Core Performance: Number of Operations (up to) 


1024 NVIDIA® CUDA® cores | 32 Tensor cores 


•
 
1.28 FP32 TFLOPs | 2.56 FP16 TFLOPs 


•
 
2.08 FP32 TFLOPs | 4.16 FP16 TFLOPs (MAXN_SUPER) 


Jetson Orin Nano 4GB 


CUDA Core Performance: Number of Operations (up to) 


512 NVIDIA® CUDA® cores | 16 Tensor cores  


•
 
0.64 FP32 TFLOPs | 1.28 FP16 TFLOPs 


•
 
1.04 FP32 TFLOPs | 2.08 FP16 TFLOPs (MAXN_SUPER) 


 
 
 
Overview 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  2 


**Description **
**Operation/Performance **


CPU Cluster 


Six-core Arm® Cortex® A78AE (64-bit) heterogeneous multi-processing (HMP) CPU architecture | 2x Clusters:  


•
 
1x 4-core cluster with 128 KB L1 + 256 KB L2 cache per core; 2 MB L3 cluster-level cache) 


•
 
1x 2- core cluster with 128 KB L1 + 256 KB L2 cache per core, 2 MB L3 cluster-level cache) 


•
 
System Cache: 4 MB (shared across all clusters) 


•
 
Spec_Int rate : 106 | 118 (MAXN_SUPER) 


Operating Frequency per Core (up to): 
•
 
1.5 GHz 


•
 
1.7 GHz (MAXN_SUPER) 


Memory Subsystem 


Maximum Capacity: 8 GiB | 64-bit or 128-bit wide data bus | 128-bit AES Encryption | System MMU | TrustZone (TZ) 
Secure and OS-protection regions 


Maximum Operating Frequency (up to) 
2133 MHz | 3199 MHz (MAXN_SUPER) 


Jetson Orin Nano 8GB 


Peak Memory Bandwidth: 


128-bit LPDDR5 DRAM  


68 GB/s | 102 GB/s (MAXN_SUPER) 


Jetson Orin Nano 4GB 


Peak Memory Bandwidth: 


64-bit LPDDR5 DRAM  


34 GB/s | 51 GB/s (MAXN_SUPER) 


HD Video 


**Decode  **


Supported Standards: H.265 (HEVC), H.264, VP9, AV1 (see Multi-Standard Video Decoder section for detailed 
description) 


**Encode  **
1080p30 Supported via CPU Cores with Software
 


Display Controller Subsystem 


Single display controller with support for eDP/DP/HDMI | 1x4K30 DP 1.2 (+MST for 2x 1080p60), HDMI 1.4, eDP 1.4 
(see the Display section for more details on additional compatibility to DP 1.4a and HDMI 2.1) 


Maximum Resolution eDP/DP/HDMI (up to) 
3840x2160 at 30 Hz 


PCLK (up to) 
388 MHz 


Always On Sensor Processor Engine 


The Always On (AO) Sensor Processor Engine (SPE) is a Cortex-R5 subsystem with integrated instruction cache (I-
cache), data cache (D-cache) and a tightly coupled memory (TCM) interface 


Audio Subsystem 


Dedicated programmable audio processor | Arm Cortex A9 with NEON | PDM in/out | Industry-standard High-
Definition Audio (HDA) controller provides a multi-channel audio path to the HDMI® interface 


Networking 


10/100/1000 Gigabit Ethernet | Media Access Controller (MAC) 


Imaging 


Eight lanes MIPI CSI-2 | D-PHY 2.1 (20 Gbps) 


 
 
 
Overview 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  3 


**Description **
**Operation/Performance **


Security 


Dedicated Platform Security Controller (PSC) for critical security use-cases, including secure boot and key 
management. Two dedicated NIST-compliant Security Engines (SE) for hashing, symmetric/public key cryptographic 
algorithms, key derivation, and random number generation. 


•
 
TrustZone technology support for DRAM and peripherals 


•
 
Side channel countermeasures (AES/RSA/ECC) 


•
 
Hardware acceleration for various cryptographic operations and hardware assisted Key protection 


•
 
Hardware random number generator 


•
 
Provides countermeasures against physical attacks (e.g., clock, voltage and temperature monitors) 


Storage 


Supports External Storage  


>
 
NVMe through PCIe 


•
 
PCIE0, x4 (Orin UPHY0 Lanes [7:4]), Ctrl #4  


•
 
PCIE2, x2 (Orin UPHY2 Lanes [1:0]), Ctrl #7  


•
 
PCIE2, x1 (Orin UPHY2 Lane [0]), Ctrl #7  


•
 
PCIE3, x1 (Orin UPHY2 Lane [1]), Ctrl #9  


>
 
SSD through USB 3.2:  


•
 
USB 3.2 Port 0, 1, or 2 


Peripheral Interfaces 


**USB:**
 xHCI host controller with integrated PHY (up to) 3x USB 3.2, 3x USB 2.0 


**PCIe:**
 Up to GEN4 | 3 x1 (or 1 x2 + 1 x1) + 1 x4 | x1 and x2 (supports Root Port only), x4 (supports Root Port or 
Endpoint modes) 


**Audio: **
2x I2S/2x Audio Hub (AHUB) | Supports I2S, RJM, LJM, PCM, TDM (multi-slot mode)
** **


**UART: **
3 x UART 


**CAN: **
Single independent CAN port/channel supports connectivity to one CAN network
** **


**SPI: **
2 x SPI
** **


**I2C: **
4 x I2C 


**PWM:**
 4 x PWM outputs 


**GPIO:**
 15 x GPIOs
** **


Mechanical 


Module Size: 69.6 mm x 45 mm | 260 pin SO-DIMM Connector 


Operating Requirements 


Temp. Range (T
J
)*: -25°C – 105F°C | Supported Power Input: 5V | Operating Lifetime (24x7): 5 years 
Jetson Orin Nano 8GB Modes: 7W | 15W | 25W (MAXN_SUPER) 
Jetson Orin Nano 4GB Modes: 7W | 10W | 25W (MAXN_SUPER)
 


Notes: 


•
 
Refer to the Software Features section of the latest L4T Development Guide for a list of supported features; all 
features may not be available. 


•
 
◊
  Product is based on a published Khronos Specification and is expected to pass the Khronos Conformance 
Process. Current conformance status can be found at 
www.khronos.org/conformance
. 


•
 
*  See the 
*Jetson Orin Nano Series Thermal Design Guide *
for details 


 


 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
DS-11105-001_v1.5  |  4 


# Chapter 2.
#  
# Functional Description 


The NVIDIA® Jetson Orin™ Nano brings AI supercomputer performance to the edge in a compact 
system-on-module (SOM) which is smaller than a credit card. Jetson Orin Nano is built around a 
low-power version of the NVIDIA Orin SoC, combining the NVIDIA Ampere™ GPU architecture with 
64-bit operating capability, integrated advanced multi-function video and image processing, and 
NVIDIA Deep Learning Accelerators. 


Compute performance up to 40 (Sparse) INT8 TOPs and 20 (Dense) INT8 TOPs on the Jetson Orin 
Nano 8GB and up to 20 (S) INT8 TOPs and 10 (D) INT8 TOPs on the Jetson Orin Nano 4GB enables 
these modules to run multiple neural networks in parallel and process data from multiple high-
resolution sensors simultaneously. It also offers a unique combination of performance and power 
advantages with a rich set of I/Os, from high-speed CSI and PCIe to low-speed I2Cs and GPIOs, 
allowing embedded and edge computing devices that demand increased performance but are 
constrained by size, weight, and power budgets. 


 


 
**Note:**
 If MAXN_SUPER is enabled, the compute performance increases up to 67 (Sparse) 
INT8 TOPs and 33 (Dense) INT8 TOPs on Jetson Orin Nano 8GB, and up to 34 (S) and 17 (D) 
on Jetson Orin Nano 4GB 


# 2.1
#  
# Ampere GPU 


The NVIDIA Ampere GPU introduces a new design for the Streaming Multiprocessor (SM) that 
dramatically improves performance per watt and performance per area, along with supporting 
Tensor Cores and TensorRT cores. Ampere GPUs improve on the previous NVIDIA Turing™ 
generation; and are software compatible so that the same APIs are used.  


The NVIDIA Ampere Architecture GPU has several enhancements for compute and graphics 
capability that include:  


>
 
Sparsity: fine grained structured sparsity doubles throughput and reduces memory usage.  


>
 
2x CUDA floating-point performance: higher compute math speed.  


>
 
SM architecture improves bandwidth to the L1 cache and shared memory and reduces L1 
miss latency.  


>
 
Improved async compute, and post-L2 cache compression compared to NVIDIA Turing.  


The GPC is a dedicated hardware block for rasterization, shading, texturing, and compute. The 
GPU’s core graphics functions are performed inside the GPC. Inside the GPC, the SM CUDA cores 
perform pixel/vertex/geometry shading and physics/compute calculations. Texture units perform 
texture filtering and load/store units fetch and save data to memory. Special Function Units 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  5 


(SFUs) handle transcendental and graphics interpolation instructions. Tensor cores perform 
matrix multiplies to greatly accelerate DL inferencing. The RTcore unit assists Ray Tracing by 
accelerating Bounding Volume Hierarchy (BVH) traversal and intersection of scene geometry 
during Ray Tracing. 


There are multiple texture processing clusters (TPC) units within a graphics processing cluster 
(GPC), each TPC includes two SMs, a Polymorph Engine, two Texture Units, and a Ray Tracing core 
(RTcore). Each GPC includes a Raster Engine (ROP), which can access all of memory. Each SM is 
partitioned into four separate processing blocks, each with its own instruction buffer, scheduler 
and 128 CUDA cores. 


Finally, the PolyMorph engine handles vertex fetch, tessellation, viewport transform, attribute    
setup, and stream output. The SM geometry and pixel processing performance make it highly 
suitable for rendering advanced user interfaces and complex gaming applications. The power 
efficiency of the Ampere GPU enables this performance on devices with power-limited 
environments. 


## 2.1.1
##  
## Compute Features  


Ampere introduces third-generation NVIDIA Tensor Cores which offer a wider range of precisions 
including TensorFloat-32 (TF32), bfloat16, FP16, and INT8 all of which provide unmatched 
versatility and performance.  


TensorFloat-32 (TF32) is a new format that uses the same 10-bit Mantissa as half-precision 
(FP16) math and is shown to have more than sufficient margin for the precision requirements of 
AI workloads. In addition, since the TF32 adopts the same 8-bit exponent as FP32 it can support 
the same numeric range.  


Ampere adds support for structured sparsity. Not all the parameters of modern AI networks are 
needed for accurate predictions and inference, and some can be converted to zeros to make the 
models “sparse” without compromising accuracy. The Tensor Cores in Ampere can provide up to 
2x higher performance for inference of sparse models.  


Ampere supports Compute Data Compression which can accelerate unstructured sparsity and 
other compressible data patterns. Compression in L2 provides up to a 4x improvement in DRAM 
read/write bandwidth, up to 4x improvement in L2 read bandwidth, and up to a 2x improvement in 
L2 capacity.  


Ampere also supports many other enhancements for higher compute throughput. 


Table 2-1: GPU Operation  


**Module **
**CUDA Cores **
**Tensor Cores **
**Operating Frequency per Core **
**(up to) **


Jetson Orin Nano 8GB  
1024 
32 
625 MHz | 1020 MHz (MAXN_SUPER) 


Jetson Orin Nano 4GB  
512 
16 
625 MHz | 1020 MHz (MAXN_SUPER) 


 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  6 


## 2.1.2
##  
## Graphic Features 


Ampere graphics capabilities include: 


>
 
End-to-end lossless compression, including Post-L2 compression, enabling compression of M 
stores. 


>
 
Tiled Caching 


>
 
OpenGL 4.6+, Vulkan 1.2+, CUDA 11.4+ 


>
 
Adaptive Scalable Texture Compression (ASTC) LDR profile supported. 


>
 
Modern Graphics features: 


•
 
Ray Tracing 


•
 
DL Inferencing 


•
 
Mesh Shaders 


•
 
Sampler Feedback 


•
 
Variable Rate Shading 


•
 
Texture LOD in compute programs 


>
 
Iterated blend, ROP OpenGL-ES blend modes. 


>
 
2D BLIT from 3D class avoids channel switch. 


>
 
2D color compression. 


>
 
Constant color render SM bypass. 


>
 
2x, 4x, 8x MSAA with color and Z compression. 


>
 
Non-power-of-2 and 3D textures, FP16 texture filtering. 


>
 
FP16 shader support. 


>
 
Geometry and Vertex attribute Instancing. 


>
 
Parallel pixel processing. 


>
 
Early-z reject: Fast rejection of occluded pixels acts as multiplier on pixel shader and texture 
performance while saving power and bandwidth. 


>
 
Video protection region. 


# 2.2
#  
# Cortex CPU Complex  


The CPU cluster is comprised of six cores of Arm Cortex-A78AE Core processors organized as one 
quad-core clusters, and one dual-core cluster. Clusters contain private L1 and L2 caches per core, 
a Snoop Control Unit (SCU), and a cluster-level L3 cache (shared by the four cores), an 
interconnect fabric and debug support modules (CoreSight).  


Features:  


>
 
Superscalar, variable-length, out-of-order pipeline.  


>
 
Dynamic branch prediction with Branch Target Buffer (BTB) and a branch direction predictor 
using previous branch history, a return stack, a static predictor, and an indirect predictor.  


>
 
A 1.5K entry, 4-way skewed associative L0 Macro-OP (MOP) cache.  


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  7 


>
 
32-entry fully-associative L1 instruction TLB with native support for 4KB, 16KB, 64KB, and 
2MB page sizes.  


>
 
32-entry fully-associative L1 data TLB with native support for 4KB, 16KB, 64KB, 2MB, and 
512MB page sizes.  


>
 
4-way set-associative unified 1024-entry Level 2 (L2) TLB in each processor.  


>
 
L1 caches – separate 64 KB I-cache and 64 KB D-cache for each core.  


>
 
L2 cache – a unified, 8-way set associative, 256 KB L2 cache per core.  


>
 
40-bit Physical Address (PA).  


Cortex-A78AE CPU supports:  


>
 
Full implementation of Armv8.2-A architecture instruction set and select instructions from 
Armv8.3-A, Armv8.4-A, and Armv8.5-A extensions.  


>
 
Embedded Trace Microcell (ETM) based on the ETMv4.2 architecture.  


>
 
Performance Monitor Unit (PMU) based on the PMUv3 architecture.  


>
 
CoreSight for debugging based on CoreSightv3 architecture.  


>
 
Cross Trigger Interface (CTI) for multiprocessor debugging.  


>
 
Generic Timer Interface based on Armv8-A architecture and 64-bit count input from external 
system counter.  


>
 
Cryptographic Engine for crypto function support.  


>
 
Interface to an external Generic Interrupt Controller based on GICv3 architecture.  


>
 
Power management with multiple power domains.  


Table 2-2: CPU Operation  


**Module **
**CPU Cores **
**CPU Maximum Frequency **


Orin Nano 8GB 
6 
1.5 GHz | 1.7 GHz (MAXN_SUPER) 


Orin Nano 4GB 
6 
1.5 GHz | 1.7 GHz (MAXN_SUPER) 


# 2.3
#  
# Memory Subsystem  


8GB 128-bit LPDDR5 DRAM is used on the Jetson Orin Nano 8GB, and 4GB 64-bit LPDDR5 DRAM 
is used in the Jetson Orin Nano 4GB. It supports the following:  


>
 
Secure external memory access using TrustZone technology.  


>
 
System MMU  


>
 
Maximum operating frequency: 2133 MHz or 3199 MHz (MAXN_SUPER) 


The Memory Subsystem (MSS) provides access to local DRAM, SysRAM, and provides a SyncPoint 
Interface for inter-processor signaling. The MSS supports full-speed I/O coherence by routing 
requests through a scalable coherence fabric. It also supports a comprehensive set of safety and 
security mechanisms. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  8 


Structurally, the MSS consists of: 


>
 
MSS Data Backbone - routes requests from clients to the MSS Hub and responses from MSS 
Hub to the clients. 


>
 
MSS Hub - receives and arbitrates among client requests, performs SMMU translation, and 
sends requests to MCF. 


>
 
Memory Controller Fabric (MCF) - performs security checks, feeds I/O coherent requests to 
the Scalable Coherence Fabric (SCF), and directs requests to the multiple memory channels. 


>
 
Memory Controller (MC) Channels - row sorter/arbiter and DRAM controllers. 


>
 
DRAM I/O - channel-to-pad fabric, DRAM I/O pads, and PLLs. 


Jetson Orin Nano provides three independent column address bits to each sub-partition, allowing 
it access different 32-byte sectors of a Group of Bytes (GOB) between the sub-partitions. It 
provides connections between a wide variety of clients, supporting their bandwidth, latency, 
quality-of-service needs, and any special ordering requirements that are needed. The MSS 
supports a variety of security and safety features and address translation for clients that use 
virtual addresses. 


Features: 


>
 
LPDDR5 


>
 
64-bit or 128-bit wide data bus. 


>
 
Low latency path and fast read/response path support for the CPU complex cluster. 


>
 
Support for low-power modes: 


•
 
Software controllable entry/exit from self-refresh, power down, and deep power down 


•
 
Hardware dynamic entry/exit from power down, self-refresh 


•
 
Pads use DPD mode during idle periods. 


>
 
High-bandwidth interface to the integrated Ampere GPU. 


>
 
Full-speed I/O coherence with bypass for Isochronous (ISO) traffic. 


>
 
System Memory-Management Unit (SMMU) for address translation based on the Arm SMMU-
500. 


>
 
High-bandwidth PCIe ordered writes. 


>
 
AES-XTS encryption with 128-bit key. 


# 2.4
#  
# Memory 


The Jetson Orin Nano 8GB integrates 8GB 128-bit LPDDR5 DRAM, and Jetson Orin Nano 4GB 
integrates 4GB 64-bit LPDDR5 DRAM. Maximum frequency of Jetson Orin Nano Memory is 2133 
MHz or 3199MHz (MAXN_SUPER). The theoretical peak memory bandwidth on Orin Nano 8GB is 
68 GB/s or 102 GB/s (MAXN_SUPER), and on Orin Nano 4GB is 34 GB/s or 51 GB/s (MAXN_SUPER). 


The Memory Controller (MC) maximizes memory utilization while providing minimum latency 
access for critical CPU requests. An arbiter is used to prioritize requests, optimizing memory 
access efficiency and utilization and minimizing system power consumption. The MC provides 
access to main memory for all internal devices. It provides an abstract view of memory to its 
clients via standardized interfaces, allowing the clients to ignore details of the memory hierarchy. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  9 


It optimizes access to shared memory resources, balancing latency and efficiency to provide best 
system performance, based on programmable parameters. 


Features: 


>
 
TrustZone (TZ) Secure and OS-protection regions. 


>
 
System Memory Management Unit. 


>
 
Dual CKE signals for dynamic power down per device. 


>
 
Dynamic Entry/Exit from Self-Refresh and Power Down states. 


# 2.5
#  
# Video Input Interfaces 


## 2.5.1
##  
## MIPI Camera Serial Interface (CSI)  


 


**Standard **


MIPI CSI 2.0 Receiver specification 


MIPI D-PHY® 2.1 Physical Layer specification 


 


The NVIDIA Camera Serial Interface (NVCSI) works with the Video Input (VI) unit to capture an 
image from a sensor, where NVCSI is a source of pixel data to VI. NVCSI works in streaming mode 
while VI captures the required frames using a single-shot mode of operation. All sync point 
generation for software is handled at VI; the delay between NVCSI and VI is negligible in software 
terms. NVCSI does not have a direct memory port, instead it sends the pixel data to memory 
through the VI.  


Fifth-generation NVIDIA camera solution (NVCSI 2.0, VI 5.0, and ISP 6.x) provides a combination 
host that supports enhanced MIPI D-PHY (with lane deskew support) physical layer options in two 
4-lane or four 2-lane configurations; or combinations of these. Orin Nano can support up to 16 
virtual channels (VC) and supports data type interleaving.   


>
 
Virtual Channel Interleaving: VCs are defined in the CSI-2 specification and are useful when 
supporting multiple camera sensors. With the VC capability, a one-pixel parser (PP) can de-
interleave up to 16 image streams.  


>
 
Data Type Interleaving: In HDR line-by-line mode, the sensor can output long/short exposure 
lines using the same VC and a different programmable data type (DT). 


>
 
Frequency Target: The parallel pixel processing rate, measured in pixels-per-clock (PPC), is 
increased to allow higher throughput and lower clock speeds. To support higher bandwidth 
without increasing the operating frequency, the host processes multiple pixels in one clock. 
NVCSI is capable of processing four PPCs when bits-per-pixel (BPP) is greater than 16, and 
eight PPC when BPP is less than or equal to 16. 


>
 
With the new streaming mode in NVCSI, one PP can handle all traffic (embedded data and 
image data) from one camera device, including 16 VCs. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  10 


Features: 


>
 
Supports the MIPI D-PHY v2.1 physical layer option: 


•
 
MIPI D-PHY supports up to 2.5 Gbits/sec per pair, for an aggregate bandwidth of 20 Gbps 
from eight pairs. 


>
 
Based on MIPI CSI-2 v3.0 protocol stack. 


>
 
Includes six-pixel parsers (PP). 


>
 
Supports up to 16 virtual channels.  


>
 
Supported input data formats: 


•
 
RGB: RGB888, RGB666, RGB565, RGB555, RGB444 


•
 
YUV: YUV420-8b (legacy), YUV420-8b  


•
 
RAW: RAW6, RAW7, RAW8, RAW10, RAW12, RAW14, RAW16,  


>
 
Data Type Interleave support.  


Table 2-3: CSI Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


10 
CSI0_CLK_N 
Camera, CSI 0 Clock– 
Input 
MIPI D-PHY 


12 
CSI0_CLK_P 
Camera, CSI 0 Clock+ 
Input 
MIPI D-PHY 


4 
CSI0_D0_N 
Camera, CSI 0 Data 0– 
Input 
MIPI D-PHY 


6 
CSI0_D0_P 
Camera, CSI 0 Data 0+ 
Input 
MIPI D-PHY 


16 
CSI0_D1_N 
Camera, CSI 0 Data 1– 
Input 
MIPI D-PHY 


18 
CSI0_D1_P 
Camera, CSI 0 Data 1+ 
Input 
MIPI D-PHY 


9 
RSVD (CSI1_CLK_N) 
Camera, CSI 1 Clock– 
Input 
MIPI D-PHY 


11 
RSVD (CSI1_CLK_P) 
Camera, CSI 1 Clock+ 
Input 
MIPI D-PHY 


3 
CSI1_D0_N 
Camera, CSI 1 Data 0– 
Input 
MIPI D-PHY 


5 
CSI1_D0_P 
Camera, CSI 1 Data 0+ 
Input 
MIPI D-PHY 


15 
CSI1_D1_N 
Camera, CSI 1 Data 1– 
Input 
MIPI D-PHY 


17 
CSI1_D1_P 
Camera, CSI 1 Data 1+ 
Input 
MIPI D-PHY 


28 
CSI2_CLK_N 
Camera, CSI 2 Clock– 
Input 
MIPI D-PHY 


30 
CSI2_CLK_P 
Camera, CSI 2 Clock+ 
Input 
MIPI D-PHY 


22 
CSI2_D0_N 
Camera, CSI 2 Data 0– 
Input 
MIPI D-PHY 


24 
CSI2_D0_P 
Camera, CSI 2 Data 0+ 
Input 
MIPI D-PHY 


34 
CSI2_D1_N 
Camera, CSI 2 Data 1– 
Input 
MIPI D-PHY 


36 
CSI2_D1_P 
Camera, CSI 2 Data 1+ 
Input 
MIPI D-PHY 


27 
CSI3_CLK_N 
Camera, CSI 3 Clock– 
Input 
MIPI D-PHY 


29 
CSI3_CLK_P 
Camera, CSI 3 Clock+ 
Input 
MIPI D-PHY 


21 
CSI3_D0_N 
Camera, CSI 3 Data 0– 
Input 
MIPI D-PHY 


23 
CSI3_D0_P 
Camera, CSI 3 Data 0+ 
Input 
MIPI D-PHY 


33 
CSI3_D1_N 
Camera, CSI 3 Data 1– 
Input 
MIPI D-PHY 


35 
CSI3_D1_P 
Camera, CSI 3 Data 1+ 
Input 
MIPI D-PHY 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  11 


Table 2-4: Camera Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


116 
CAM0_MCLK 
Camera 0 Reference Clock 
Output 
CMOS – 1.8V 


114 
CAM0_PWDN 
Camera 0 Powerdown or GPIO 
Output 
CMOS – 1.8V 


122 
CAM1_MCLK 
Camera 1 Reference Clock 
Output 
CMOS – 1.8V 


120 
CAM1_PWDN 
Camera 1 Powerdown or GPIO 
Output 
CMOS – 1.8V 


## 2.5.2
##  
## Video Input (VI) 


The VI block receives data from the CSI receiver and prepares it for presentation to system 
memory or the dedicated image signal processor execution resources. The VI block provides 
formatting for RGB, YCbCr, and raw Bayer data in support of several camera user models. These 
models include single and multi-camera systems, which may have up to six active streams. The 
input streams are obtained from MIPI compliant CMOS sensor camera modules. 


## 2.5.3
##  
## Image Signal Processor (ISP)  


The ISP module takes data from the VI/CSI module or memory in raw Bayer format and processes 
it to YUV output. The imaging subsystem supports raw (Bayer) image sensors up to 10 million 
pixels. Advanced image processing is used to convert input to YUV data and remove artifacts 
introduced by high-megapixel CMOS sensors and optics with up to 30-degree CRA. 


The ISP in the Jetson Orin Nano supports a maximum frequency of 704 MHz, with two 
pixels/clock is equivalent to approximately 1408 MPixels.  


Features: 


>
 
Flexible post-processing architecture for supporting custom computer vision and 
computational imaging operations. 


>
 
Hardware noise reduction 


>
 
Black-level compensation 


>
 
Lens-shading compensation 


>
 
Bad pixel correction 


>
 
Edge enhancement 


>
 
Color and gamma correction  


>
 
Global and local tone mapping 


>
 
Color-space conversion (RGB to YUV) 


 
#  


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  12 


# 2.6
#  
# Sensor Processing Engine  


The Cortex-R5 processor in the Always On (AON) block is also referred to as the Sensor 
Processing Engine (SPE). The AON cluster provides all the necessary hardware features to 
support low power sensor management and wake use cases. The cluster consists of an Arm 
Cortex-R5 processor core with a tightly coupled RAM, supporting peripherals (such as timers and 
an interrupt controller), various I/O controller peripherals, and routing logic.  


AON Cortex-R5 implementation:  


>
 
Arm v7-R ISA  


>
 
Integrated instruction and data caches  


>
 
Tightly coupled memory (TCM) interface for local SRAM  


>
 
Vectored interrupt support  


>
 
64-bit AXI Initiator interface for DRAM requests  


>
 
32-bit AXI Initiator interface for MMIO requests  


>
 
32-bit AHB Initiator interface for Arm Vectored Interrupt Controller (AVIC) access  


>
 
AXI Target interface for DMA access to the local SRAM  


# 2.7
#  
# Security Subsystem  


This subsystem is comprised of the following:  


>
 
Platform Security Controller (PSC)  


>
 
Security Engine (SE)  


## 2.7.1
##  
## Platform Security Controller 


The Platform Security Controller (PSC) is a highly secure subsystem to protect and manage 
assets (keys, fuses, functions, and features) within the SoC, provide trusted services, increase 
resilience against attacks on the SoC, and provide a greater level of protection against software 
and hardware attacks on the subsystem itself.  


**Key Management and Protection:**
 The PSC will be the only mechanism with access to the most 
critical secrets in the chip. This subsystem represents the highest level of protection in Orin and 
the subsystem itself is highly resilient to a wide range of software and hardware attacks.  


**Trusted Services:**
 The primary PSC services include secure authentication (for example, during 
SoC secure boot), provisioning of additional keys, ID, data, key access and management, random 
number generation, and trusted time reporting.  


**Security Monitor:**
 The PSC will be responsible for periodic security housekeeping tasks, including 
continually assessing the security status of the SoC, actively monitor known or potential attack 
patterns (for example, such as voltage glitching or thermal attacks), mitigate hardware attack 
risks, and to take action in the case of a detected attack. The PSC will have the ability to accept 
updates as workarounds to improve the robustness of the system in the field.  


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  13 


## 2.7.2
##  
## Security Engine  


The Security Engine (SE) provides hardware acceleration for cryptographic algorithms. There are 
two instances of SE available for software usage:  


>
 
TZ-SE: accessible only by TrustZone software.  


>
 
NS/TZ-SE: configurable to be accessible only by TrustZone software or TrustZone and non-
secure software.  


The SE provides hardware acceleration for various cryptographic operations and hardware 
assisted Key protection. The crypto operations that the SE provides can be used by software to 
build crypto protocols and security features. All of these crypto operations are based on Crypto 
algorithms approved by the National Institute of Standards and Technology (NIST).  


The SE supports the following:  


>
 
NIST-compliant asymmetric, symmetric cryptography and hashing 


>
 
Side channel countermeasures [AES/RSA/ECC]  


>
 
Independent channels for parallelization  


>
 
Hardware Key Access Controls (KAC): Rule-based, hardware-enforced access control for 
symmetric keys 


>
 
16× AES, 4× RSA/ECC key slots  


>
 
Hardware key isolation (only AES keyslots)  


>
 
Read protection (only AES keyslots)  


>
 
Hardware keyslot functions 


>
 
Key wrap and unwrap functionality (AES -> AES keyslot)  


>
 
Key derivation into a keyslot (KDF -> AES keyslot)  


>
 
Random key generation (RNG -> AES keyslot) 


# 2.8
#  
# Display Controller  


The NVIDIA Jetson Orin Nano provides 1x HDMI and DP port. The HDMI and DisplayPort (DP) 
interfaces share the same set of interface pins. The Jetson Orin Nano maximum pixel clock is 388 
MHz. Due to the above pixel clock, Jetson Orin Nano will not be able to get official DP/HDMI 
certification for DP 1.4a and HDMI 2.1. However, software/hardware are still compatible with all 
other parts of the DP1.4a and HDMI2.1 specs listed below.  


 
**Note**
: 4K@30fps is an example of a resolution that can still be supported with a 388 MHz 
pixel clock. However, resolutions which require a pixel clock higher than 388 MHz (e.g., 
4k@60) cannot be supported. The 388 MHz pixel clock enables compliance to DP 1.2, HDMI 
1.4, and eDP 1.4. 


HDMI provides a unified method of transferring both audio and video data. The HDMI block 
receives video from either display controller and audio from a separate high-definition audio 
(HDA) controller; it combines and transmits them as appropriate. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  14 


Supported HDMI features are: 


>
 
Compliant to the HDMI 1.4 Specification 


>
 
Compatible with HDMI 2.1 Specification 


>
 
HDCP 2.2  


>
 
On-chip HDCP key storage, no external SecureROM required. 


>
 
Multichannel audio from HDA controller, up to eight channels 192 kHz 24-bit 


>
 
24-bit RGB and 24-bit YUV444 (HDMI) pixel formats 


DisplayPort (DP) is a digital display interface often used to connect a video source to a display 
device over a cable, in consumer or commercial applications. For embedded use cases that require 
multiple display support using MST, DP is intended to interface with SerDes devices that in turn 
supports up to four displays. 


Supported DisplayPort features are: 


>
 
Compliant to the DisplayPort 1.2 Specification 


>
 
Compatible to the DisplayPort 1.44 Specification 


•
 
Support 16 bpp YUV422 


•
 
Support 18 bpp RGB 


•
 
Support 24 bpp RGB/YUV444 


•
 
Support 30 bpp RGB/YUV444 


•
 
Support 36 bpp RGB/YUV444 


•
 
Support up to 388 MHz pixel clock. 


•
 
Support for 1/2/4 lanes 


>
 
Support for following bit rates: 


•
 
RBR (Reduced Bit Rate, 1.62 Gbps) 


•
 
HBR (High Bit Rate, 2.7 Gbps) 


•
 
HBR2 (High Bit Rate 2, 5.4 Gbps) 


•
 
HBR3 (High Bit Rate 3, 8.1 Gbps) 


>
 
Multi-Stream Transport (MST) 


>
 
Support for 2-8 channel audio streaming up to 96 kHz sample rate 


>
 
Support additional eDP 1.4 features: 


•
 
Additional link rates (2.16, 2.43, 3.24, 4.32 Gbps) 


•
 
Enhanced framing 


•
 
Power sequencing 


•
 
Reduced AUX timing 


•
 
Reduced main voltage swing. 


•
 
Alternate Seed Scrambler Reset (ASSR) for internal eDP panels. 


 


 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  15 


# 2.9
#  
# High-Definition Audio-Video Subsystem 


 


**Standard **


High-Definition Audio Specification Version 1.0a 


 


The HD Audio-Video Subsystem uses a collection of functional blocks to off-load audio and video 
processing activities from the CPU complex, resulting in fast, fully concurrent, and highly efficient 
operation. This subsystem is comprised of the following: 


>
 
Multi-standard video decoder 


>
 
Video Image Compositor (VIC) 


>
 
Audio Processing Engine (APE) 


>
 
High-Definition Audio (HDA) 


## 2.9.1
##  
## Multi-Standard Video Decoder 


The Jetson Orin Nano incorporates the NVIDIA Multi-Standard Video Decoder (NVDEC). This video 
decoder accelerates video decode, supporting low resolution mobile content, Standard Definition 
(SD), High Definition (HD) and UltraHD (8K, 4K, etc.) video profiles. The video decoder is designed 
to be extremely power efficient without sacrificing performance. The video decoder 
communicates with the memory controller through the video DMA which supports a variety of 
memory format output options. For low-power operations, the video decoder can operate at the 
lowest possible frequency while maintaining real-time decoding using dynamic frequency scaling 
techniques.  


Video decode standards supported: H.265 (HEVC), H.264, VP9, VP8, AV1, MPEG-4, MPEG-2, and 
VC-1.  


Table 2-5: Supported Video Decode Streams 


**Standard **
**Profile(s) **
**Resolution (Maximum Number of **
**Streams) **


**Throughput **
**MPix/s (Up **
**to) **


**Maximum **
**Cumulative **
**Bitrate (Mbps) **


H.264 
Baseline, Main, High 
4K30 (1) | 1080p60 (3) | 1080p30 (7) 
450  
115 


High 444, High 444 
Predictive, MVC (per view 
considering two views) 
(see note) 


1x1080p60 | 3x 1080p30 
225 
100 


H.265 
(HEVC) 


Main, Main10 
4K60 (1) | 4K30 (2) | 1080p60 (5) | 
1080p30 (11) 


690 
150 


Main 444, Main 444 10, 
MV (per view) 


4K30 (1) | 1080p60 (2) | 1080p30 (5) 
340 
100 


AV1 
Main Profile 
4K60 (1) | 4K30 (2) | 1080p60 (5) | 
1080p30 (10) 


625 
75 


VP9 
Profile 0, Profile 2 
4K60 (1) | 4K30 (2) | 1080p60 (5) | 
1080p30 (10) 


625 
100 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  16 


 


 
**Note:**
 1. For 444-related profiles, perf numbers given are for YUV444 input; for other 
profiles it is for YUV420 input. 


2. The perf data is indicative, based on varied content/bitrate evaluations, and should serve 
as general performance guidance. 


## 2.9.2
##  
## Video Image Compositor (VIC) 


VIC implements various 2D image and video operations in a power-efficient manner. It handles 
various system UI scaling, blending, rotation operations, video post-processing functions needed 
during video playback, and advanced de-noising functions used for camera capture. 


Features:  


>
 
High-quality Deinterlacing 


>
 
Inverse Teleciné 


>
 
Temporal Noise Reduction 


•
 
New Bilateral Filter as spatial filter 


•
 
Improved TNR3 algorithm 


>
 
Scaling 


>
 
Color Conversion 


>
 
Memory Format Conversion 


>
 
Blend/Composite 


>
 
2D Bit BLIT operation 


>
 
Rotation 


>
 
Geometry Transform Processing 


•
 
Programmable nine-points controlled warp patch for distortion correction 


•
 
Real-time on-the-fly position generation from sparse warp map surface 


•
 
Pincushion/barrel/moustache distortion correction 


•
 
Distortion correction of 180- and 360-degree wide FOV lens 


•
 
Scene perspective orientation adjustment with IPT 


•
 
Full warp map capability 


•
 
Non-fixed Patch size with 4x4 regions 


•
 
External Mask bit map surface 


## 2.9.3
##  
## Audio Processing Engine (APE)  


The Audio Processing Engine (APE) is a self-contained unit with dedicated audio clocking that 
enables Ultra Low Power (ULP) audio processing. Software based post processing effects enable 
the ability to implement custom audio algorithms. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  17 


Features: 


>
 
96 KB Audio RAM 


>
 
Audio Hub (AHUB) I/O Modules 


•
 
2x I2S Audio Hub (AHUB) Internal Modules 


>
 
Sample Rate converter 


>
 
Mixer 


>
 
Audio Multiplexer 


>
 
Audio De-multiplexer 


>
 
Master Volume Controller 


>
 
Multi-Channel IN/OUT 


•
 
Digital Audio Mixer: 10-in/5-out 


-
 
Up to eight channels per stream 


-
 
Simultaneous Multi-streams 


-
 
Flexible stream routing 


•
 
Parametric equalizer: up to 12 bands 


•
 
Low latency sample rate conversion (SRC) and high-quality asynchronous sample rate 
conversion (ASRC). 


## 2.9.4
##  
## High-Definition Audio (HDA) 


 


**Standard **


Intel High-Definition Audio Specification Revision 1.0a 


 


The Jetson Orin Nano implements an industry-standard High-Definition Audio (HDA) controller. 
This controller provides a multi-channel audio path to the HDMI interface. The HDA block also 
provides an HDA-compliant serial interface to an audio codec. A maximum of four streams are 
supported.  


Features: 


>
 
Supports HDMI 2.1 and DP1.4 


>
 
Support up to two audio streams for use with HDMI/DP 


>
 
Supports striping of audio out across 1,2,4[a] SDO lines 


>
 
Supports DVFS with maximum latency up to 208 
µ
s for eight channels 


>
 
Supports Multi-Stream Transport (MST) 


>
 
Audio Format Support 


•
 
Uncompressed Audio (LPCM): 16/20/24 bits at 32/44.1/48/88.2/96/176.4/192[b] kHz 


•
 
Compressed Audio format: AC3, DTS5.1, MPEG1, MPEG2, MP3, DD+, MPEG2/4 AAC, 
TrueHD, DTS-HD 


-
 
[a] Four SDO lines: cannot support one stream, 48 kHz, 16-bits, two channels; for this 
case, use a one or two SDO line configuration. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  18 


-
 
[b] DP protocol sample frequency limitation: cannot support >96 kHz; that is, it does 
not support 176.4 kHz and 196 kHz. 


# 2.10
#  
# Interface Descriptions 


The following sections outline the interfaces available on the Jetson Orin Nano module and 
details the module pins used to interact with and control each interface. See the 
*Jetson Orin Nano *
*Series Product Design Guide*
 for complete functional descriptions, programming guidelines, and 
register listings for each of these blocks. 


## 2.10.1
##  
## Universal Serial Bus (USB)  


 


**Standard **
**Notes **


Universal Serial Bus Specification Revision 3.2 Gen1 and Gen2 
- 


Universal Serial Bus Specification Revision 2.0 

 
Modes: Host and Device (Only USB 2.0 port 
USB0 supports RCM, Host, Device Mode. 
All other ports are Host only) 



 
Speeds: Low, Full, and High 



 
USB Battery Charging 1.2 Specifications 


Enhanced Host Controller Interface Specification for Universal 
Serial Bus revision 1.0 


- 


 


An xHCI/Device controller (named XUSB) supports the xHCI programming model for scheduling 
transactions and interface managements as a host that natively supports USB 3.2, USB 2.0, and 
USB 1.1 transactions with its USB 3.2 and USB 2.0 interfaces. The XUSB controller supports USB 
2.0 L1 and L2 (suspend) link power management and USB 3.2 U1, U2, and U3 (suspend) link power 
managements. The XUSB controller supports remote wakeup, wake on connect, wake on 
disconnect, and wake on overcurrent in all power states, including sleep mode. 


2.10.1.1
 
USB 2.0 Operation 


Each USB 2.0 port (3x) operates in USB 2.0 high-speed mode when connecting directly to a USB 
2.0 peripheral and operates in USB 1.1 full- and low-speed modes when connecting directly to a 
USB 1.1 peripheral. When operating in High-Speed mode, each USB 2.0 port is allocated with one 
High-Speed unit bandwidth. Approximately a 480 Mb/s bandwidth is allocated to each USB 2.0 
port. All USB 2.0 ports operating in full- or low-speed modes share one full- and low-speed bus 
instance, which means 12 Mb/s theoretical bandwidth is distributed across these ports. 


Table 2-6: USB 2.0 Pin Descriptions  


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


109 
USB0_D_N 
USB 2.0 Port 0 Data– 
Bidir 
USB PHY 


111 
USB0_D_P 
USB 2.0 Port 0 Data+ 
Bidir 
USB PHY 


115 
USB1_D_N 
USB 2.0 Port 1 Data– 
Bidir 
USB PHY 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  19 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


117 
USB1_D_P 
USB 2.0 Port 1 Data+ 
Bidir 
USB PHY 


121 
USB2_D_N 
USB 2.0 Port 2 Data– 
Bidir 
USB PHY 


123 
USB2_D_P 
USB 2.0 Port 2 Data+ 
Bidir 
USB PHY 


2.10.1.2
 
USB 3.2 Operation 


In host mode, the USB3.2 host controller supports Gen2 Super Speed+, 10 Gbps transfer rates. In 
device mode, the USB3.2 controller supports Gen1 Super Speed. 


 


 
**Note:**
 There is an internal USB 3.2 hub for ports 0 and 1. The hub supports 10Gbps 
bandwidth which would be shared between the two ports. 


Table 2-7: USB 3.2 Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


161 
USBSS0_RX_N 
USB SS Receive– (USB 3.2 Ctrl #0) 
Input 
USB SS PHY 


163 
USBSS0_RX_P 
USB SS Receive+ (USB 3.2 Ctrl #0) 
Input 
USB SS PHY 


166 
USBSS0_TX_N 
USB SS Transmit– (USB 3.2 Ctrl #0) 
Output 
USB SS PHY 


168 
USBSS0_TX_P 
USB SS Transmit+ (USB 3.2 Ctrl #0) 
Output 
USB SS PHY 


39 
USBSS1_RX_N 
USB SS Receive– (USB 3.2 Ctrl #1) 
Input 
USB SS PHY 


41 
USBSS1_RX_P 
USB SS Receive+ (USB 3.2 Ctrl #1) 
Input 
USB SS PHY 


45 
USBSS1_TX_N 
USB SS Transmit– (USB 3.2 Ctrl #1) 
Output 
USB SS PHY 


47 
USBSS1_TX_P 
USB SS Transmit+ (USB 3.2 Ctrl #1) 
Output 
USB SS PHY 


51 
USBSS2_RX_N 
USB SS Receive– (USB 3.2 Ctrl #2) 
Input 
USB SS PHY 


53 
USBSS2_RX_P 
USB SS Receive+ (USB 3.2 Ctrl #2) 
Input 
USB SS PHY 


57 
USBSS2_TX_N 
USB SS Transmit– (USB 3.2 Ctrl #2) 
Output 
USB SS PHY 


59 
USBSS2_TX_P 
USB SS Transmit+ (USB 3.2 Ctrl #2) 
Output 
USB SS PHY 


## 2.10.2
##  
## PCI Express (PCIe)  


 


**Standard **
**Notes **


PCI Express Base Specification Revision 4.0 
 


 


The Jetson Orin Nano module integrates four PCIe controllers supporting: 


>
 
Connections to two interfaces, 3 x1 (or 1 x2 + 1 x1) + 1 x4 GEN4.  


>
 
x1 and x2 (supports Root Port only), x4 (supports Root Port or Endpoint modes) upstream and 
downstream AXI interfaces that serve as the control path from the Jetson Orin Nano to the 
external PCIe device.  


>
 
Gen4 (16 GT/s) supported on all controllers/lanes 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  20 


>
 
Four PCIe controllers, seven lanes for a total of 112GT/s.  


>
 
Controller #0 can operate in x1, x2, or x4 mode.   


>
 
Controller #1 operates in x1 mode only.  


>
 
Controller #2 can operate in x1, x2 mode.   


>
 
Controller #3 is available if Controller #2 is not used or only used in x1 mode. In these cases, 
Controller #3 can operate in x1 mode.  


Table 2-8: PCIe Pin Descriptions  


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


131 
PCIE0_RX0_N 
PCIe 0 Receive 0– (PCIe Ctrl #4 Lane 0) 
Input 
PCIe PHY 


133 
PCIE0_RX0_P 
PCIe 0 Receive 0+ (PCIe Ctrl #4 Lane 0) 
Input 
PCIe PHY 


137 
PCIE0_RX1_N 
PCIe 0 Receive 1– (PCIe Ctrl #4 Lane 1) 
Input 
PCIe PHY 


139 
PCIE0_RX1_P 
PCIe 0 Receive 1+ (PCIe Ctrl #4 Lane 1) 
Input 
PCIe PHY 


149 
PCIE0_RX2_N 
PCIe 0 Receive 2– (PCIe Ctrl #4 Lane 2) 
Input 
PCIe PHY 


151 
PCIE0_RX2_P 
PCIe 0 Receive 2+ (PCIe Ctrl #4 Lane 2) 
Input 
PCIe PHY 


155 
PCIE0_RX3_N 
PCIe 0 Receive 3– (PCIe Ctrl #4 Lane 3) 
Input 
PCIe PHY 


157 
PCIE0_RX3_P 
PCIe 0 Receive 3+ (PCIe Ctrl #4 Lane 3) 
Input 
PCIe PHY 


134 
PCIE0_TX0_N 
PCIe 0 Transmit 0– (PCIe Ctrl #4 Lane 0) 
Output 
PCIe PHY 


136 
PCIE0_TX0_P 
PCIe 0 Transmit 0+ (PCIe Ctrl #4 Lane 0) 
Output 
PCIe PHY 


140 
PCIE0_TX1_N 
PCIe 0 Transmit 1– PCIe Ctrl #4 Lane 1) 
Output 
PCIe PHY 


142 
PCIE0_TX1_P 
PCIe 0 Transmit 1+ (PCIe Ctrl #4 Lane 1) 
Output 
PCIe PHY 


148 
PCIE0_TX2_N 
PCIe 0 Transmit 2– (PCIe Ctrl #4 Lane 2) 
Output 
PCIe PHY 


150 
PCIE0_TX2_P 
PCIe 0 Transmit 2+ (PCIe Ctrl #4 Lane 2) 
Output 
PCIe PHY 


154 
PCIE0_TX3_N 
PCIe 0 Transmit 3– (PCIe Ctrl #4 Lane 3) 
Output 
PCIe PHY 


156 
PCIE0_TX3_P 
PCIe 0 Transmit 3+ (PCIe Ctrl #4 Lane 3) 
Output 
PCIe PHY 


181 
PCIE0_RST* 
PCIe 0 Reset (PCIe Ctrl #4). 4.7k
Ω
 pull-up to 3.3V on 
the module. Output when Orin Nano is Root Port or 
input when Orin Nano is Endpoint. 


Bidir 
Open Drain 3.3V 


180 
PCIE0_CLKREQ* 
PCIE 0 Clock Request (PCIe Ctrl #4). 47k
Ω
 pull-up to 
3.3V on the module. Input when Orin Nano is Root 
Port or output when Orin Nano is Endpoint. 


Bidir 
Open Drain 3.3V 


160 
PCIE0_CLK_N 
PCIe #0 Reference Clock- (reference clock input when 
Orin Nano is an Endpoint). 


Bidir 
PCIe PHY 


162 
PCIE0_CLK_P 
PCIe #0 Reference Clock+ (reference clock input 
when Orin Nano is an Endpoint). 


Bidir 
PCIe PHY 


167 
PCIE1_RX0_N 
PCIe 1 Receive 0– (PCIe Ctrl #1 Lane 0) 
Input 
PCIe PHY 


169 
PCIE1_RX0_P 
PCIe 1 Receive 0+ (PCIe Ctrl #1 Lane 0) 
Input 
PCIe PHY 


172 
PCIE1_TX0_N 
PCIe 1 Transmit 0– (PCIe Ctrl #1 Lane 0) 
Output 
PCIe PHY 


174 
PCIE1_TX0_P 
PCIe 1 Transmit 0+ (PCIe Ctrl #1 Lane 0) 
Output 
PCIe PHY 


183 
PCIE1_RST* 
PCIe 1 Reset (PCIe Ctrl #1). 4.7k
Ω
 pull-up to 3.3V on 
the module. 


Output 
Open Drain 3.3V 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  21 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


182 
PCIE1_CLKREQ* 
PCIe 1 Clock Request (PCIe Ctrl #1). 47k
Ω
 pull-up to 
3.3V on the module. 


Bidir 
Open Drain 3.3V 


173 
PCIE1_CLK_N 
PCIe 1 Reference Clock– (PCIe Ctrl #1) 
Output 
PCIe PHY 


175 
PCIE1_CLK_P 
PCIe 1 Reference Clock+ (PCIe Ctrl #1) 
Output 
PCIe PHY 


179 
PCIE_WAKE* 
PCIe Wake. 47k
Ω
 pull-up to 3.3V on the module. 
Bidir 
Open Drain 3.3V 


40 
PCIE2_RX0_N 
PCIe 2 Receive 0– (PCIe Ctrl #7 Lane 0) 
Input 
PCIe PHY 


42 
PCIE2_RX0_P 
PCIe 2 Receive 0+ (PCIe Ctrl #7 Lane 0) 
Input 
PCIe PHY 


46 
PCIE2_TX0_N 
PCIe 2 Transmit 0– (PCIe Ctrl #7 Lane 0) 
Output 
PCIe PHY 


48 
PCIE2_TX0_P 
PCIe 2 Transmit 0+ (PCIe Ctrl #7 Lane 0) 
Output 
PCIe PHY 


58 
PCIE2_RX1_N 
(PCIE3_RX0_N) 


PCIe 2 Receive 1– (PCIe Ctrl #7 Lane 1) or PCIe 3 
Receive 0– (PCIe Ctrl #9 Lane 0) 


Input 
PCIe PHY 


60 
PCIE2_RX1_P 
(PCIE3_RX0_P) 


PCIe 2 Receive 1+ (PCIe Ctrl #7 Lane 1) or PCIe 3 
Receive 0+ (PCIe Ctrl #9 Lane 0) 


Input 
PCIe PHY 


64 
PCIE2_TX1_N 
(PCIE3_TX0_N) 


PCIe 2 Transmit 1– (PCIe Ctrl #7 Lane 1) or PCIe 3 
Transmit 0– (PCIe Ctrl #9 Lane 0) 


Output 
PCIe PHY 


66 
PCIE2_TX1_P 
(PCIE3_TX0_P) 


PCIe 2 Transmit 1+ (PCIe Ctrl #7 Lane 1) or PCIe 3 
Transmit 0+ (PCIe Ctrl #9 Lane 0) 


Output 
PCIe PHY 


52 
PCIE2_CLK_N 
PCIe 2 Reference Clock– (PCIe Ctrl #7) 
Output 
PCIe PHY 


54 
PCIE2_CLK_P 
PCIe 2 Reference Clock+ (PCIe Ctrl #7) 
Output 
PCIe PHY 


219 
PCIE2_RST* 
PCIe 2 Reset (PCIe Ctrl #7). 4.7k
Ω
 pull-up to 3.3V on 
the module. 


Output 
Open Drain 3.3V 


221 
PCIE2_CLKREQ* 
PCIe 2 Clock Request (PCIe Ctrl #7). 47k
Ω
 pull-up to 
3.3V on the module. 


Bidir 
Open Drain 3.3V 


229 
PCIE3_CLK_P 
PCIe 3 Reference Clock– (PCIe Ctrl #9) 
Output 
PCIe PHY 


227 
PCIE3_CLK_N 
PCIe 3 Reference Clock+ (PCIe Ctrl #9) 
Output 
PCIe PHY 


223 
PCIE3_RST* 
PCIe 3 Reset (PCIe Ctrl #9). 4.7k
Ω
 pull-up to 3.3V on 
the module. 


Output 
Open Drain 3.3V 


225 
PCIE3_CLKREQ* 
PCIe 3 Clock Request (PCIe Ctrl #9). 47k
Ω
 pull-up to 
3.3V on the module. 


Bidir 
Open Drain 3.3V 


 


See the 
*Jetson Orin Nano Product Design Guide*
 for supported USB 3.2/PCIe configuration and 
connection examples. 


## 2.10.3
##  
## Serial Peripheral Interface (SPI)  


The Serial Peripheral Interface (SPI) controller allows a duplex, synchronous, serial communication 
between the controller and external peripheral devices; it supports both Master and Slave modes 
of operation on the SPI bus. See the 
*Jetson Orin Nano Product Design Guide*
 for more information. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  22 


Features: 


>
 
2x SPI Interface. 


>
 
Master mode operation. 


•
 
All transfer modes (Mode 0, Mode 1, Mode 2, Mode 3) supported for both transmit and 
receive transactions. 


>
 
FIFO Size: 64 x 32 bits 


>
 
Programmable packet sizes of 4 to 32 bits. 


>
 
Programmable clock phase and polarity. 


>
 
Programmable delay between consecutive transfers. 


>
 
Chip select controllable by software or generated by hardware on packet boundaries. 


Table 2-9: SPI Mode Descriptions 


**SPI **
**Mode **


**Clock **
**Polarity **


**Clock **
**Phase **


**SCK **


**Inactive State **


**Data Latch In **
**Data Latch Out **


0 
0 
0 
Low 
Latched IN on the positive 
edge of clock 


Latched OUT on the negative 
edge of clock 


1 
0 
1 
Low 
Latched IN on the negative 
edge of clock 


Latched OUT on the positive 
edge of clock 


2 
1 
0 
High 
Latched IN on the negative 
edge of clock 


Latched OUT on the positive 
edge of clock 


3 
1 
1 
High 
Latched IN on the positive 
edge of clock 


Latched OUT on the negative 
edge of clock 


Table 2-10: SPI Pin Descriptions  


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


91 
SPI0_SCK 
SPI 0 Clock 
Bidir 
CMOS – 1.8V 


89 
SPI0_MOSI 
SPI 0 Master Out / Slave In 
Bidir 
CMOS – 1.8V 


93 
SPI0_MISO 
SPI 0 Master In / Slave Out 
Bidir 
CMOS – 1.8V 


95 
SPI0_CS0* 
SPI 0 Chip Select 0 
Bidir 
CMOS – 1.8V 


97 
SPI0_CS1* 
SPI 0 Chip Select 1 
Bidir 
CMOS – 1.8V 


106 
SPI1_SCK 
SPI 1 Clock 
Bidir 
CMOS – 1.8V 


104 
SPI1_MOSI 
SPI 1 Master Out / Slave In 
Bidir 
CMOS – 1.8V 


108 
SPI1_MISO 
SPI 1 Master In / Slave Out 
Bidir 
CMOS – 1.8V 


110 
SPI1_CS0* 
SPI 1 Chip Select 0 
Bidir 
CMOS – 1.8V 


112 
SPI1_CS1* 
SPI 1 Chip Select 1 
Bidir 
CMOS – 1.8V 


 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  23 


Figure 2-1: SPI Initiator Timing 


SPIx_MOSI


SPIx_MISO


SPIx_CSx_N


tCS


tCSH
tCSS


tHD
tSU


tCSH


0
n
SPIx_SCK


MSB   IN
LSB   IN


tCSS


tCH
tCL


MSB   OUT
LSB   OUT


tDD


 


 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  24 


Table 2-11: SPI Initiator Timing Parameters 


**Symbol **
**Parameter **
**Min **
**Max **
**Unit **


Fsck 
SCK Clock Frequency 
 
81.6 
MHz 


Fsck 
SCK Clock Frequency (FSI SPI) 
 
40 
MHz 


tSCP 
SCK Period 
1000 * 
1/Fsck(max) 


1000 * 
1/Fsck(min) 
ns 


tCH 
SCK high time 
45% * tSCP 
55% * tSCP 
ns 


tCL 
SCK low time 
45% * tSCP 
55% * tSCP 
ns 


tCRT 
SCK Rise time (slew rate) 
0.1 
 
V/ns 


tCFT 
SCK Fall time (slew rate) 
0.1 
 
V/ns 


tSU 
Data setup time (MISO) 
2 
 
ns 


tHD 
Data hold time (MISO) 
3 
 
ns 


tDD 
Active Clock edge to MOSI data Output Valid 
 
6 
ns 


tCSS 
CSx_N setup time 
2 
 
ns 


tCSH 
CSx_N hold time 
3 
 
ns 


tCS 
CSx_N high time 
10 
 
ns 


 


Figure 2-2: SPI Target Timing 


SPIx_MISO


SPIx_MOSI


SPIx_CSx_N


0
1
n
SPIx_SCK


tCS


tCSH


tDD


tCH
tCL
tSCP
tCSS


tDSU
tDH


 


 


Table 2-12: SPI Target Timing Parameters 


**Symbol Parameter **
**Min **
**Max **
**Unit **


Fsck  
SCK Clock Frequency 
 
51 
MHz 


Fsck  
SCK Clock Frequency (FSI SPI) 
 
26 
MHz 


tSCP 
SCK Period 
20 
 
ns 


tCH 
SCK high time 
45% * tSCP 
55% * tSCP 
ns 


tCL 
SCK low time 
45% * tSCP 
55% * tSCP 
ns 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  25 


**Symbol Parameter **
**Min **
**Max **
**Unit **


tCSS 
CSx_N setup time  
1 * tSCP 
 
ns 


tCSH 
CSx_N hold time 
1 * tSCP 
 
ns 


tCS 
CSx_N high time 
1 * tSCP 
 
ns 


tSU 
Data setup time (MOSI) 
4 
 
ns 


tHD 
Data hold time (MOSI) 
2 
 
ns 


tDD 
Active Clock edge to MISO data Output Valid 
2.5 
17 
ns 


tHO 
MISO Output Hold Time 
2 
 
ns 


 


## 2.10.4
##  
## Universal Asynchronous Receiver/Transmitter 
## (UART)  


The UART controller provides serial data synchronization and data conversion (parallel-to-serial 
and serial-to-parallel) for both receiver and transmitter sections. Synchronization for serial data 
stream is accomplished by adding start and stop bits to the transmit data to form a data 
character. Data integrity is accomplished by attaching a parity bit to the data character. The 
parity bit can be checked by the receiver for any transmission bit errors. 


 


 
**Note:**
 The UART receiver input has low baud rate tolerance in 1-stop bit mode. External 
devices must use two stop bits. In 1-stop bit mode, the UART receiver can lose sync 
between the receiver and the external transmitter resulting in data errors/corruption. In 2-
stop bit mode, the extra stop bit allows the UART receiver logic to align properly with the 
UART transmitter. 


 


Features: 


>
 
3x UART Interface. 


>
 
Synchronization for the serial data stream with start and stop bits to transmit data and form 
a data character. 


>
 
Supports both 16450- and 16550-compatible modes. Default mode is 16450. 


>
 
Device clock up to 68 MHz, baud rate of 4.25 Mbits/second. 


>
 
Support for word lengths from five to eight bits, an optional parity bit and one or two stop 
bits. 


>
 
Support for modem control inputs. 


>
 
Auto sense baud detection. 


>
 
Timeout interrupts to indicate if the incoming stream stopped. 


>
 
Priority interrupts mechanism. 


>
 
Flow control support on RTS and CTS. 


>
 
SIR encoding/decoding (3/16 or 4/16 baud pulse widths to transmit bit zero). 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  26 


Table 2-13: UART Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


99 
UART0_TXD 
UART #0 Transmit 
Output 
CMOS – 1.8V 


101 
UART0_RXD 
UART #0 Receive 
Input 
CMOS – 1.8V 


103 
UART0_RTS* 
UART #0 Request to Send 
Output 
CMOS – 1.8V 


105 
UART0_CTS* 
UART #0 Clear to Send 
Input 
CMOS – 1.8V 


203 
UART1_TXD 
UART #1 Transmit 
Output 
CMOS – 1.8V 


205 
UART1_RXD 
UART #1 Receive 
Input 
CMOS – 1.8V 


207 
UART1_RTS* 
UART #1 Request to Send 
Output 
CMOS – 1.8V 


209 
UART1_CTS* 
UART #1 Clear to Send 
Input 
CMOS – 1.8V 


236 
UART2_TXD 
UART #2 Transmit 
Output 
CMOS – 1.8V 


238 
UART2_RXD 
UART #2 Receive 
Input 
CMOS – 1.8V 


## 2.10.5
##  
## Controller Area Network (CAN) 


 


**Standard **
**Notes **


ISO/DIS 16845-2 
CAN conformance test 


ISO 11898-1:2015 
Data link layer and physical signaling; CAN FD Frame formats 


ISO 11898-4:2004 
Time-triggered communication 


 


The Jetson Orin Nano integrates the Bosch Time-Triggered Controller Area Network (M_TTCAN) 
controller version 3.2.0. One independent CAN port/channel supports connectivity to one CAN 
network. Each port instantiates the Bosch M_TTCAN module, a message RAM module, an APB 
slave interface module, interrupt aggregator, time-triggered control module, and a wake detect 
module. All M_TTCAN external modules have direct connections to M_TTCAN except for the wake 
detect module.   


Features:  


>
 
Standard frame and extended frame transmission/reception enable.  


>
 
Transfer rate: programmable bit rates up to 15 Mbps.  


>
 
0 – 8-byte data length, with the ability to receive the first 8 bytes when data length coding is > 
8 Bytes.  


>
 
32 message buffers per channel.  


>
 
Prioritization of transmit buffers.  


>
 
Receive/transmit history list function.  


>
 
Automatic block transmission function.  


>
 
Multi-buffer receives block function.  


>
 
Flexible maskable identifier filter support for two 32-bit, or four 16-bit, or eight 8-bit filters for 
each channel.  


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  27 


>
 
Programmable data bit time, communication baud rate, and sample point.  


•
 
As an example, the following sample-point configurations can be configured: 66.7%, 70.0%, 
75.0%, 80.0%, 81.3%, 85.0%, and 87.5%  


•
 
Baud rates in the range of 10 kbps up to 1000 kbps can be configured.  


>
 
Enhanced features:  


•
 
Each message buffer can be configured to operate as a transmit or a receive message 
buffer.  


•
 
Transmission priority is controlled by the identifier or by mailbox number (selectable).  


•
 
A transmission request can be aborted by clearing the dedicated Transmit-Request flag of 
the concerned message buffer.  


•
 
Automatic block transmission (ABT) operation mode. 


•
 
Time stamp function for CAN channels 0 to n in collaboration with timers.  


>
 
Release from bus-off state by software.  


>
 
Wake-up with integrated low-pass filter (debounce) option to prevent short glitches on CAN 
bus, through CAN receive signal toggling from CAN transceiver.  


•
 
For normal operation (after wake) there is a digital filter in the CAN controller.  


>
 
Listen-only mode to monitor CAN bus.  


>
 
Wake-up signal to both internal and external (either interrupt signal or GPIO) to initiate power 
up if needed.  


•
 
Ready to receive the first CAN message within 10ms of wake event generated by the CAN 
master.  


•
 
Ready to transmit the first CAN message within 50ms of wake event generated by the 
CAN master.  


>
 
Loop back for self-test. 


Table 2-14: CAN Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


145 
CAN_TX 
CAN Transmit 
Output 
CMOS – 3.3V 


143 
CAN_RX 
CAN Receive 
Input 
CMOS – 3.3V 


 


## 2.10.6
##  
## Inter-Chip Communication (I2C)  


**Standard **
**Notes **


NXP inter-IC-bus (I2C) specification 
https://i2c.info/i2c-bus-specification 


This general purpose I2C controller allows system expansion for I2C-based devices as defined in 
the NXP inter-IC-bus (I2C) specification. The I2C bus supports serial device communications to 
multiple devices. (4x I2C) The I2C controller handles clock source negotiation, speed negotiation 
for standard and fast devices, 7-bit slave address support according to the I2C protocol and 
supports master and slave modes of operation. 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  28 


The I2C controller supports the following operating modes:  


>
 
Master – Standard-mode (up to 100 Kbit/s), Fast-mode (up to 400 Kbit/s), Fast-mode plus 
(Fm+, up to 1 Mbit/s). 


>
 
Slave – Standard-mode (up to 100 Kbit/s), Fast-mode (up to 400 Kbit/s), Fast-mode plus (Fm+, 
up to 1 Mbit/s). 


Table 2-15: I2C Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


185 
I2C0_SCL 
General I2C 0 Clock. 1.5k
Ω
 pull-up to 3.3V on 
module. 


Bidir 
Open Drain – 3.3V 


187 
I2C0_SDA 
General I2C 0 Data. 1.5k
Ω
 pull-up to 3.3V on the 
module. 


Bidir 
Open Drain – 3.3V 


189 
I2C1_SCL 
General I2C 1 Clock. 2.2k
Ω
 pull-up to 3.3V on the 
module. 


Bidir 
Open Drain – 3.3V 


191 
I2C1_SDA 
General I2C 1 Data. 2.2k
Ω
 pull-up to 3.3V on the 
module. 


Bidir 
Open Drain – 3.3V 


232 
I2C2_SCL 
General I2C 2 Clock. 2.2k
Ω
 pull-up to 1.8V on the 
module. 


Bidir 
Open Drain – 1.8V 


234 
I2C2_SDA 
General I2C 2 Data. 2.2k
Ω
 pull-up to 1.8V on the 
module. 


Bidir 
Open Drain – 1.8V 


213 
CAM_I2C_SCL 
Camera I2C Clock. 2.2k
Ω
 pull-up to 3.3V on the 
module. 


Bidir 
Open Drain – 3.3V 


215 
CAM_I2C_SDA 
Camera I2C Data. 2.2k
Ω
 pull-up to 3.3V on the 
module. 


Bidir 
Open Drain – 3.3V 


 


 
##  


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  29 


## 2.10.7
##  
## Inter-IC Sound (I2S) 


 


**Standard **


Inter-IC Sound (I2S) specification 


 


The I2S controller transports streaming audio data between system memory and an audio codec. 
The I2S controller supports I2S format, left-justified mode format, right-justified mode format, 
and DSP mode format, as defined in the Philips inter-IC-sound (I2S) bus specification. 


The I2S and PCM (master and slave modes) interfaces support clock rates up to 24.5760 MHz. 


The I2S controller supports point-to-point serial interfaces for the I2S digital audio streams. I2S-
compatible products, such as compact disc players, digital audio tape devices, digital sound 
processors, and those with digital TV sound may be directly connected to the I2S controller. The 
controller also supports the PCM and telephony mode of data-transfer. Pulse-Code-Modulation 
(PCM) is a standard method used to digitize audio (particularly voice) patterns for transmission 
over digital communication channels. The Telephony mode is used to transmit and receive data to 
and from an external mono CODEC in a slot-based scheme of time-division multiplexing (TDM). 
The I2S controller supports Bidirectional audio streams and can operate in half-duplex or full-
duplex mode. 


Features: 


>
 
Basic I2S modes to be supported (I2S, RJM, LJM, and DSP) in both master and slave modes. 


>
 
PCM mode with short (one bit-clock wide) and long-fsync (two bit-clock wide) in both master 
and slave modes. 


>
 
NW-mode with independent slot-selection for both transmit and receive. 


>
 
TDM mode with flexibility in number of slots and slot(s) selection. 


>
 
Capability to drive-out a high-z outside the prescribed slot for transmission. 


>
 
Flow control for the external input/output stream. 


Table 2-16: I2S Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


199 
I2S0_SCLK 
I2S Audio Port 0 Clock 
Bidir 
CMOS – 1.8V 


197 
I2S0_FS 
I2S Audio Port 0 Left/Right Clock 
Bidir 
CMOS – 1.8V 


193 
I2S0_DOUT 
I2S Audio Port 0 Data Out 
Output 
CMOS – 1.8V 


195 
I2S0_DIN 
I2S Audio Port 0 Data In 
Input 
CMOS – 1.8V 


226 
I2S1_SCLK 
I2S Audio Port 1 Clock 
Bidir 
CMOS – 1.8V 


224 
I2S1_FS 
I2S Audio Port 1 Left/Right Clock 
Bidir 
CMOS – 1.8V 


220 
I2S1_DOUT 
I2S Audio Port 1 Data Out 
Output 
CMOS – 1.8V 


222 
I2S1_DIN 
I2S Audio Port 1 Data In 
Input 
CMOS – 1.8V 


 


 
##  


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  30 


## 2.10.8
##  
## Gigabit Ethernet 


**Standard **
**Notes **


Gigabit Ethernet (GbE) 
 IEEE 802.3ab 


The on-module Ethernet controller supports: 


>
 
10/100/1000 Gigabit Ethernet  


>
 
IEEE 802.3u Media Access Controller (MAC) 


Table 2-17: Gigabit Ethernet Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


184 
GBE_MDI0_N 
GbE Transformer Data 0– 
Bidir 
MDI 


186 
GBE_MDI0_P 
GbE Transformer Data 0+ 
Bidir 
MDI 


190 
GBE_MDI1_N 
GbE Transformer Data 1– 
Bidir 
MDI 


192 
GBE_MDI1_P 
GbE Transformer Data 1+ 
Bidir 
MDI 


196 
GBE_MDI2_N 
GbE Transformer Data 2– 
Bidir 
MDI 


198 
GBE_MDI2_P 
GbE Transformer Data 2+ 
Bidir 
MDI 


202 
GBE_MDI3_N 
GbE Transformer Data 3– 
Bidir 
MDI 


204 
GBE_MDI3_P 
GbE Transformer Data 3+ 
Bidir 
MDI 


188 
GBE_LED_LINK 
Ethernet Link LED (Green) 
Output 
 - 


194 
GBE_LED_ACT 
Ethernet Activity LED (Yellow) 
Output 
 - 


## 2.10.9
##  
## Fan 


The Jetson Orin Nano includes a Pulse Width Modulator (PWM) and Tachometer functionality to 
enable fan control as part of a thermal solution. The PWM controller is a frequency divider with a 
varying pulse width. The PWM runs off a device clock programmed in the Clock and Reset 
controller and can be any frequency up to the device clock maximum speed of 48 MHz. The PWM 
gets divided by 256 before being subdivided based on a programmable value. 


## 2.10.10
##  
## Pulse Width Modulator (PWM) 


Jetson Orin Nano has four PWM outputs. Each PWM output is based on a frequency divider 
whose pulse width varies. Each has a programmable frequency divider and a programmable pulse 
width generator. The PWM controller supports one PWM output for each of its four instances. 
Each instance is allocated a 64 KB independent address space. 


Frequency division is a 13-bit programmable value, and pulse division is an 8-bit value. The PWM 
can run at a maximum frequency of up to 408 MHz. The PWM controller can source its clock from 
either CLK_M or PLLP. CLK_M (19.2 MHz) is derived from the OSC clock (38.4 MHz). PLLP 
operates at 408 MHz. 


The PWM clock frequency is divided by 256 before subdividing it based on the programmable 
frequency division value to generate the required frequency for the PWM output. The maximum 


 
 
 
Functional Description 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  31 


output frequency that can be achieved from this configuration is 408 MHz/256 = 1.6 MHz. This 
1.6 MHz frequency can be further divided using the frequency divisor in PWM. 


The OSC clock is the primary/default source for the PWM IP clock. For higher PWM output 
frequency requirements, PLLP is the clock source (up to 408 MHz). 


Table 2-18: PWM Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


206 
GPIO07 
Pulse Width Modulator or GPIO #7  
Bidir  
CMOS – 1.8V 


218 
GPIO12 
Pulse Width Modulator or GPIO #12  
Bidir  
CMOS – 1.8V 


228 
GPIO13 
Pulse Width Modulator or GPIO #13  
Bidir 
CMOS – 1.8V 


230 
GPIO14 
Pulse Width Modulator or GPIO #14  
Bidir 
CMOS – 1.8V 


 


 


 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
DS-11105-001_v1.5  |  32 


# Chapter 3.
#  
# Power and System Management 


See the 
*Jetson Orin Nano Product Design Guide*
 for details on connecting to each of the 
interfaces. 


Table 3-1: Power and System Control Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


251 


252 


253 


254 


255 


256 


257 


258 


259 


260 


VDD_IN 
Main power – Supplies PMIC and other registers 
Input 
5V  


235 
PMIC_BBAT 
Real Time Clock. Optionally used to provide back-
up power for the RTC in the Power Sequencer. 
Connects to a Lithium Cell or similar power source. 
The cell sources power for the RTC when system is 
disconnected from power. 


Note: This pin is input only and rechargeable cells 
or devices such as Super Caps cannot be 
supported. 


Input 
1.85V to 5.5V 


214 
FORCE_RECOVERY* 
Force Recovery strap pin. Held low when 
SYS_RESET* goes high (i.e., during power-on) 
places system in USB recovery mode. 


Input 
CMOS – 1.8V 


240 
SLEEP/WAKE* 
Configured as GPIO for optional use to indicate 
the system should enter or exit sleep mode. 


Input 
CMOS – 5.0V 


233 
SHUTDOWN_REQ* 
When driven/pulled low by the module, requests 
the carrier board to shut down. ~5k
Ω
 pull-up to 
VDD_IN on the module. 


Output 
Open Drain, 
VDD_IN 


237 
POWER_EN 
Signal for module on/off: high level on, low level 
off. Connects to module power sequencer/PMIC 
power on/off control input through converter 
logic. POWER_EN is routed to a Schmitt trigger 


Input 
Analog 5.0V 


 
 
 
Power and System Management 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  33 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


buffer on the module. A 100k
Ω
 pulldown is also on 
the module. 


239 
SYS_RESET* 
Module Reset. Reset to the module when driven 
low by the carrier board. Used as carrier board 
supply enable when driven high by the module 
when module power sequence is complete. Used 
to ensure proper power on/off sequencing 
between module and carrier board supplies. 10k
Ω
 
pull-up to VDD_1V8 on the module. 


Bidir 
Open Drain, 
1.8V 


178 
MOD_SLEEP* 
Module Sleep. When active (low), indicates module 
has gone to Sleep (SC7) mode. 


Output 
CMOS – 1.8V 


210 
CLK_32K_OUT 
Sleep/Suspend clock. 2.2k
Ω
 pull-up to VDD_1V8 on 
the module. If used on the carrier board, a buffer 
should be implemented close to the module pin. If 
not used, leave NC. 


Bidir 
CMOS – 1.8V 


217 
MODULE_ID 
When tied to GND, the module is a legacy type 
supporting only 5V on VDD_IN. 
When floating, the module is an advanced type 
supporting 5V to 20V on VDD_IN. 


- 
Strap 


# 3.1
#  
# Power Rails  


VDD_IN must be supplied by the carrier board that the Jetson Orin Nano is designed to connect 
to. All Jetson Orin Nano interfaces are referenced to on-module voltage rails and no I/O voltage is 
required to be supplied to the module. See the 
*Jetson Orin Nano Product Design Guide*
 for details 
of connecting to each of the interfaces. 


# 3.2
#  
# Power Domains/Islands  


Jetson Orin Nano has a single three-channel INA that can measure power of CPU_GPU_CV 
combined rail, Core, and module input power. 


# 3.3
#  
# Power Management Controller (PMC) 


The PMC power management features enable both high speed operation and very low-power 
standby states. The PMC primarily controls voltage transitions for the SoC as it transitions 
to/from different low power modes; it also acts as a slave receiving dedicated power/clock 
request signals as well as wake events from various sources (e.g., SPI, I2C, RTC, USB) which can 
wake the system from deep sleep state. The PMC enables aggressive power-gating capabilities on 
idle modules and integrates specific logic to maintain defined states and control power domains 
during sleep and deep sleep modes.  


 
 
 
Power and System Management 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  34 


# 3.4
#  
# Resets 


If reset is asserted, the Jetson Orin Nano SoC and onboard storage is reset. This signal is also 
used for baseboard power sequencing. 


# 3.5
#  
# PMIC_BBAT  


An optional back up battery can be attached to the PMIC_BBAT module input to maintain the 
module real-time clock (RTC) when VDD_IN is not present. Batteries can be used to power the pin, 
but charging is not supported. This pin is connected directly to the onboard PMIC. RTC accuracy 
is -11 ~ +20 seconds/day. 


Table 3-2: PMIC_BBAT Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


235 
PMIC_BBAT 
Real Time Clock. Optionally used to provide back-up 
power for the RTC in the Power Sequencer. Connects 
to a Lithium Cell or similar power source. The cell 
sources power for the RTC when system is 
disconnected from power. Power consumption on 
battery backup operation is 12 to 50
μ
A. 


Input 
1.85V to 5.5V 


# 3.6
#  
# Power Sequencing 


The Jetson Orin Nano is required to be powered on and off in a known sequence. Sequencing is 
determined through a set of control signals; the SYS_RESET* signal (when deasserted) is used to 
indicate when the carrier board can power on. The following sections provide an overview of the 
power sequencing steps between the carrier board and Jetson Orin Nano. Refer to the 
*Jetson *
*Orin Nano Product Design Guide*
 for system level details on the application of power, power 
sequencing, and monitoring. The Jetson Orin Nano and the product carrier board must be power 
sequenced properly to avoid potential damage to components on either the module or the carrier 
board system. 


## 3.6.1
##  
## Power Up  


During power up, the carrier board must wait until the signal SYS_RESET* is deasserted from the 
Jetson module before enabling its power; the Jetson module will deassert the SYS_RESET* signal 
to enable the complete system to boot. 


 


 
**Note:**
 I/O pins cannot be high (>0.5V) before SYS_RESET* goes high. When SYS_RESET* is 
low, the maximum voltage applied to any I/O pin is 0.5V. 


 
 
 
Power and System Management 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  35 


## 3.6.2
##  
## Power Down  


Shutdown events can be triggered by either the module or the baseboard, but the shutdown 
event will always be serviced by the baseboard. To do so, the baseboard deasserts POWER_EN, 
which begins the shutdown power sequence on the module. If the module needs to request a 
shutdown event in the case of thermal, software, or under-voltage events, it will assert 
SHUTDOWN_REQ*. When the baseboard sees low SHUTDOWN_REQ*, it should deassert 
POWER_EN as soon as possible. 


Once POWER_EN is deasserted, the module will assert SYS_RESET*, and the baseboard may shut 
down. SoC 3.3V I/O must reach 0.5V or lower at most 1.5ms after SYS_RESET* is asserted. SoC 
1.8V I/O must reach 0.5V or lower at most 4ms after SYS_RESET* is asserted. 


# 3.7
#  
# Power States  


The Jetson Orin Nano operates in three main power modes: OFF, ON, and SLEEP. The module 
transitions between these states are based on various events from hardware or software. The 
figure below shows the transitions between these three states. 


Figure 3-1:  Power State Transition Diagram 


**OFF**
**ON**
**SLEEP**


**ON**


**EVENT**


**OFF**


**EVENT**


**WAKE**


**EVENT**


**SLEEP**


**EVENT**


 


 


## 3.7.1
##  
## ON State 


The ON power state is entered from either OFF or SLEEP states. In this state, the Jetson Orin 
Nano module is fully functional and operates normally. An ON event must occur for a transition 
between OFF and ON states. The only ON EVENT currently used is a low to high transition on the 
POWER_EN pin. This must occur with VDD_IN connected to a power rail and POWER_EN is 
asserted (at a logic1). The POWER_EN control is the carrier board indication to the Jetson module 
that the VDD_IN power is good. The carrier board should assert this high only when VDD_IN has 
reached its required voltage level and is stable. This prevents the Jetson Orin Nano Module from 
powering up until the VDD_IN power is stable. 


 
 
 
Power and System Management 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  36 


## 3.7.2
##  
## OFF State 


The OFF state is the default state when the system is not powered. It can only be entered from 
the ON state, through an OFF event. OFF events are listed in the table below. 


Table 3-3: OFF State Events 


**Event **
**Details **
**Preconditions **


HW Shutdown 
Set POWER_EN pin to zero for at least 10 
µ
s, the internal 
PMIC starts the shutdown sequence. 


In ON State  


SW Shutdown 
Software initiated shutdown  
ON state, software 
operational 


Thermal Shutdown 
If the internal temperature of the Jetson Orin Nano module 
reaches an unsafe temperature, the hardware is designed to 
initiate a shutdown. 


Any power state 


 


 
**Note:**
 HW shutdown, SW shutdown, and Thermal shutdown all assert SHUTDOWN_REQ* 
low. System on Module does not initiate power supply shutdown sequence until POWER_EN 
is deasserted. 


## 3.7.3
##  
## SLEEP State 


The SLEEP state can only be entered from the ON state. This state allows the module to quickly 
resume to an operational state without performing a full boot sequence. The SLEEP state also 
includes a low power mode SC7 (deep sleep) where the module operates only with enough 
circuitry powered to allow the device to resume and re-enter the ON state. During this state the 
output signals from the module are maintained at their logic level prior to entering the state (i.e., 
they do not change to a 0V level). To exit the SLEEP state a WAKE event must occur; WAKE 
events can occur from within the module or from external devices through various pins on the 
module connector. 


Table 3-4: SLEEP and WAKE Events 


**Event **
**Details **


Thermal Condition 
If the module internal temperature exceeds programmed hot and cold limits the system 
is forced to wake up, so it can report and take appropriate action (shut down for 
example). 


USB VBUS detection 
If VBUS is applied to the system (USB cable attached) then the device can be configured 
to Wake and enumerate. 


Module connector 
Interface WAKE signals 


Programmable signals on the module connector. 


 
 
 
Power and System Management 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  37 


# 3.8
#  
# Thermal and Power Monitoring 


The Jetson Orin Nano is designed to operate under various workloads and environmental 
conditions. It has been designed so that an active or passive heat sink solution can be attached. 
The module contains various methods through hardware and software to limit the internal 
temperature to within operating limits. See the 
*Jetson Orin Nano Thermal Design Guide*
 for more 
details. 


 


 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
DS-11105-001_v1.5  |  38 


# Chapter 4.
#  
# Pin Definitions 


The function(s) for each pin on the module is fixed to a single Special-Function I/O (SFIO) or 
software-controlled General Purpose I/O (GPIO). The Jetson Orin Nano has multiple dedicated 
GPIOs and each GPIO is individually configurable as Output/Input/Interrupt sources with 
level/edge controls. SFIO and GPIO functionality is configured using Multi-Purpose I/O (MPIO) 
pads with each MPIO pad consisting of: 


>
 
An output driver with tristate capability, drive strength controls and push-pull mode, open-
drain mode, or both. 


>
 
An input receiver with either Schmitt mode, CMOS mode, or both. 


>
 
A weak pull-up and a weak pull-down. 


MPIO pads are partitioned into multiple pad control groups with controls being configured for the 
group. During normal operation, these per-pad controls are driven by the pinmux controller 
registers. During deep sleep, the PMC bypasses and then resets the pinmux controller registers. 
Software reprograms these registers as necessary after returning from deep sleep. 


Refer to the 
*Jetson Orin Nano Product Design Guide*
 and the 
*Pinmux Spreadsheet*
 for more 
information. 


# 4.1
#  
# Power-on Reset Behavior  


Each MPIO pad has a deterministic power-on reset (PoR) state. The reset state for each pad is 
chosen to minimize the need of additional on-board components; for example, on-chip weak pull-
ups are enabled during PoR for pads which are usually used to drive active-low chip selects 
eliminating the need for additional pull-up resistors. 


The following list is a simplified description of the boot process focusing on those aspects which 
relate to the MPIO pins: 


>
 
System-level hardware executes the power-up sequence. This sequence ends when system-
level hardware releases SYS_RESET_N. 


>
 
The Boot ROM begins executing and programs the on-chip I/O controllers to access the 
secondary boot device (QSPI). 


>
 
The Boot ROM fetches the Boot Configuration Table (BCT) and boot loader from the 
secondary boot device. 


>
 
If the BCT and boot loader are fetched successfully, the boot ROM transfers control to the 
boot loader. 


>
 
Otherwise, the Boot ROM enters USB recovery mode. 


 
 
 
Pin Definitions 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  39 


# 4.2
#  
# Sleep Behavior  


Sleep is an ultra-low-power standby state in which the module maintains much of its I/O state 
while most of the chip is powered off. During deep sleep most of the pads are put in a state called 
Deep Power Down (DPD). The sequence for entering DPD is same across pads. 


MPIO pads can vary during deep sleep. They differ regarding: 


>
 
Input buffer behavior during deep sleep 


•
 
Forcibly disabled OR 


•
 
Enabled for use as a GPIO wake event, OR 


•
 
Enabled for some other purpose (e.g., a clock request pin) 


>
 
Output buffer behavior during deep sleep 


•
 
Maintain a static programmable (0, 1, or tristate) constant value OR 


•
 
Capable of changing state (i.e., dynamic while the chip is still in deep sleep) 


>
 
Weak pull-up/pull-down behavior during deep sleep 


•
 
Forcibly disabled OR 


•
 
Can be configured 


>
 
Pads that do not enter deep sleep 


•
 
Some of the pads whose outputs are dynamic during deep sleep are of special type and do 
not enter deep sleep. 


# 4.3
#  
# GPIO  


The Jetson Orin Nano has multiple dedicated GPIOs. Each GPIO can be individually configurable as 
an Output, Input, or Interrupt source with level/edge controls. The pins listed in the following 
table are dedicated GPIOs; some with alternate SFIO functionality. Many other pins not included 
in this list are capable of being configured as GPIOs instead of the SFIO functionality the pin 
name suggests (e.g., UART, SPI, I2S, etc.). All pins that can support GPIO functionality have this 
exposed in the Pinmux. 


Table 4-1: GPIO Pin Descriptions 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


87 
GPIO00 
GPIO #0 or USB 0 VBUS Enable #0 
Bidir 
CMOS – 1.8V 


118 
GPIO01 
GPIO #1 or Generic Clock 
Bidir 
CMOS – 1.8V 


124 
GPIO02 
GPIO #2 
Bidir 
CMOS – 1.8V 


126 
GPIO03 
GPIO #3 
Bidir 
CMOS – 1.8V 


127 
GPIO04 
GPIO #4 
Bidir 
CMOS – 1.8V 


128 
GPIO05 
GPIO #5 
Bidir 
CMOS – 1.8V 


130 
GPIO06 
GPIO #6 
Bidir 
CMOS – 1.8V 


206 
GPIO07 
GPIO #7 or Pulse Width Modulator 
Bidir  
CMOS – 1.8V 


208 
GPIO08 
GPIO #8 or Fan Tachometer 
Bidir 
CMOS – 1.8V 


 
 
 
Pin Definitions 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  40 


**Pin # **
**Signal Name **
**Description **
**Direction **
**Pin Type **


211 
GPIO09 
GPIO #9 or Audio Codec Master Clock 
Bidir 
CMOS – 1.8V 


212 
GPIO10 
GPIO #10 
Bidir 
CMOS – 1.8V 


216 
GPIO11 
GPIO #11 or Generic Clock 
Bidir 
CMOS – 1.8V 


218 
GPIO12 
GPIO #12 or Pulse Width Modulator 
Bidir 
CMOS – 1.8V 


228 
GPIO13 
GPIO #13 or Pulse Width Modulator 
Bidir 
CMOS – 1.8V 


230 
GPIO14 
GPIO #14 or Pulse Width Modulator 
Bidir 
CMOS – 1.8V 


# 4.4
#  
# Pin List 


 


 
**Note:**
 For cell shading, light green indicates ground; light blue indicates Jetson Orin Nano 
specific functionality. 


 


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


**Pin # **
**Top **
**Odd **


** **
**Pin # **
**Bottom **
**Even **


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


GND 
GND 
1 
 
2 
GND 
GND 


CSI1_D0_N 
CSI1_D0_N 
3 
 
4 
CSI0_D0_N 
CSI0_D0_N 


CSI1_D0_P 
CSI1_D0_P 
5 
 
6 
CSI0_D0_P 
CSI0_D0_P 


GND 
GND 
7 
 
8 
GND 
GND 


CSI1_CLK_N 
CSI1_CLK_N 
9 
 
10 
CSI0_CLK_N 
CSI0_CLK_N 


CSI1_CLK_P 
CSI1_CLK_P 
11 
 
12 
CSI0_CLK_P 
CSI0_CLK_P 


GND 
GND 
13 
 
14 
GND 
GND 


CSI1_D1_N 
CSI1_D1_N 
15 
 
16 
CSI0_D1_N 
CSI0_D1_N 


CSI1_D1_P 
CSI1_D1_P 
17 
 
18 
CSI0_D1_P 
CSI0_D1_P 


GND 
GND 
19 
 
20 
GND 
GND 


CSI3_D0_N 
CSI3_D0_N 
21 
 
22 
CSI2_D0_N 
CSI2_D0_N 


CSI3_D0_P 
CSI3_D0_P 
23 
 
24 
CSI2_D0_P 
CSI2_D0_P 


GND 
GND 
25 
 
26 
GND 
GND 


CSI3_CLK_N 
CSI3_CLK_N 
27 
 
28 
CSI2_CLK_N 
CSI2_CLK_N 


CSI3_CLK_P 
CSI3_CLK_P 
29 
 
30 
CSI2_CLK_P 
CSI2_CLK_P 


GND 
GND 
31 
 
32 
GND 
GND 


CSI3_D1_N 
CSI3_D1_N 
33 
 
34 
CSI2_D1_N 
CSI2_D1_N 


CSI3_D1_P 
CSI3_D1_P 
35 
 
36 
CSI2_D1_P 
CSI2_D1_P 


GND 
GND 
37 
 
38 
GND 
GND 


DP0_TXD0_N 
USBSS1_RX_N 
39 
 
40 
CSI4_D2_N 
PCIE2_RX0_N 


DP0_TXD0_P 
USBSS1_RX_P 
41 
 
42 
CSI4_D2_P 
PCIE2_RX0_P 


GND 
GND 
43 
 
44 
GND 
GND 


DP0_TXD1_N 
USBSS1_TX_N 
45 
 
46 
CSI4_D0_N 
PCIE2_TX0_N 


 
 
 
Pin Definitions 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  41 


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


**Pin # **
**Top **
**Odd **


** **
**Pin # **
**Bottom **
**Even **


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


DP0_TXD1_P 
USBSS1_TX_P 
47 
 
48 
CSI4_D0_P 
PCIE2_TX0_P 


GND 
GND 
49 
 
50 
GND 
GND 


DP0_TXD2_N 
USBSS2_RX_N 
51 
 
52 
CSI4_CLK_N 
PCIE2_CLK_N  


DP0_TXD2_P 
USBSS2_RX_P 
53 
 
54 
CSI4_CLK_P 
PCIE2_CLK_P  


GND 
GND 
55 
 
56 
GND 
GND 


DP0_TXD3_N 
USBSS2_TX_N 
57 
 
58 
CSI4_D1_N 
PCIE2_RX1_N 
(PCIE3_RX0_N) 


DP0_TXD3_P 
USBSS2_TX_P 
59 
 
60 
CSI4_D1_P 
PCIE2_RX1_P 
(PCIE3_RX0_P) 


GND 
GND 
61 
 
62 
GND 
GND 


DP1_TXD0_N 
DP1_TXD0_N 
63 
 
64 
CSI4_D3_N 
PCIE2_TX1_N 
(PCIE3_TX0_N) 


DP1_TXD0_P 
DP1_TXD0_P 
65 
 
66 
CSI4_D3_P 
PCIE2_TX1_P 
(PCIE3_TX0_P) 


GND 
GND 
67 
 
68 
GND 
GND 


DP1_TXD1_N 
DP1_TXD1_N 
69 
 
70 
DSI_D0_N 
RSVD 


DP1_TXD1_P 
DP1_TXD1_P 
71 
 
72 
DSI_D0_P 
RSVD 


GND 
GND 
73 
 
74 
GND 
GND 


DP1_TXD2_N 
DP1_TXD2_N 
75 
 
76 
DSI_CLK_N 
RSVD 


DP1_TXD2_P 
DP1_TXD2_P 
77 
 
78 
DSI_CLK_P 
RSVD 


GND 
GND 
79 
 
80 
GND 
GND 


DP1_TXD3_N 
DP1_TXD3_N 
81 
 
82 
DSI_D1_N 
RSVD 


DP1_TXD3_P 
DP1_TXD3_P 
83 
 
84 
DSI_D1_P 
RSVD 


GND 
GND 
85 
 
86 
GND 
GND 


GPIO00 
GPIO00 
87 
 
88 
DP0_HPD 
RSVD 


SPI0_MOSI 
SPI0_MOSI 
89 
 
90 
DP0_AUX_N 
RSVD 


SPI0_SCK 
SPI0_SCK 
91 
 
92 
DP0_AUX_P 
RSVD 


SPI0_MISO 
SPI0_MISO 
93 
 
94 
HDMI_CEC 
HDMI_CEC 


SPI0_CS0* 
SPI0_CS0* 
95 
 
96 
DP1_HPD 
DP1_HPD 


SPI0_CS1* 
SPI0_CS1* 
97 
 
98 
DP1_AUX_N 
DP1_AUX_N 


UART0_TXD 
UART0_TXD 
99 
 
100 
DP1_AUX_P 
DP1_AUX_P 


UART0_RXD 
UART0_RXD 
101 
 
102 
GND 
GND 


UART0_RTS* 
UART0_RTS* 
103 
 
104 
SPI1_MOSI 
SPI1_MOSI 


UART0_CTS* 
UART0_CTS* 
105 
 
106 
SPI1_SCK 
SPI1_SCK 


GND 
GND 
107 
 
108 
SPI1_MISO 
SPI1_MISO 


USB0_D_N 
USB0_D_N 
109 
 
110 
SPI1_CS0* 
SPI1_CS0* 


USB0_D_P 
USB0_D_P 
111 
 
112 
SPI1_CS1* 
SPI1_CS1* 


GND 
GND 
113 
 
114 
CAM0_PWDN 
CAM0_PWDN 


 
 
 
Pin Definitions 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  42 


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


**Pin # **
**Top **
**Odd **


** **
**Pin # **
**Bottom **
**Even **


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


USB1_D_N 
USB1_D_N 
115 
 
116 
CAM0_MCLK 
CAM0_MCLK 


USB1_D_P 
USB1_D_P 
117 
 
118 
GPIO01 
GPIO01 (CLK) 


GND 
GND 
119 
 
120 
CAM1_PWDN 
CAM1_PWDN 


USB2_D_N 
USB2_D_N 
121 
 
122 
CAM1_MCLK 
CAM1_MCLK 


USB2_D_P 
USB2_D_P 
123 
 
124 
GPIO02 
GPIO02 


GND 
GND 
125 
 
126 
GPIO03 
GPIO03 


GPIO04 
GPIO04 
127 
 
128 
GPIO05 
GPIO05 


GND 
GND 
129 
 
130 
GPIO06 
GPIO06 


PCIE0_RX0_N 
PCIE0_RX0_N 
131 
 
132 
GND 
GND 


PCIE0_RX0_P 
PCIE0_RX0_P 
133 
 
134 
PCIE0_TX0_N 
PCIE0_TX0_N 


GND 
GND 
135 
 
136 
PCIE0_TX0_P 
PCIE0_TX0_P 


PCIE0_RX1_N 
PCIE0_RX1_N 
137 
 
138 
GND 
GND 


PCIE0_RX1_P 
PCIE0_RX1_P 
139 
 
140 
PCIE0_TX1_N 
PCIE0_TX1_N 


GND 
GND 
141 
 
142 
PCIE0_TX1_P 
PCIE0_TX1_P 


CAN_RX 
CAN_RX 
143 
 
144 
GND 
GND 


CAN_TX 
CAN_TX 
145 
 
146 
GND 
GND 


GND 
GND 
147 
 
148 
PCIE0_TX2_N 
PCIE0_TX2_N 


PCIE0_RX2_N 
PCIE0_RX2_N 
149 
 
150 
PCIE0_TX2_P 
PCIE0_TX2_P 


PCIE0_RX2_P 
PCIE0_RX2_P 
151 
 
152 
GND 
GND 


GND 
GND 
153 
 
154 
PCIE0_TX3_N 
PCIE0_TX3_N 


PCIE0_RX3_N 
PCIE0_RX3_N 
155 
 
156 
PCIE0_TX3_P 
PCIE0_TX3_P 


PCIE0_RX3_P 
PCIE0_RX3_P 
157 
 
158 
GND 
GND 


GND 
GND 
159 
 
160 
PCIE0_CLK_N 
PCIE0_CLK_N 


USBSS_RX_N 
USBSS0_RX_N 
161 
 
162 
PCIE0_CLK_P 
PCIE0_CLK_P 


USBSS_RX_P 
USBSS0_RX_P 
163 
 
164 
GND 
GND 


GND 
GND 
165 
 
166 
USBSS_TX_N 
USBSS0_TX_N 


PCIE1_RX0_N 
PCIE1_RX0_N 
167 
 
168 
USBSS_TX_P 
USBSS0_TX_P 


PCIE1_RX0_P 
PCIE1_RX0_P 
169 
 
170 
GND 
GND 


GND 
GND 
171 
 
172 
PCIE1_TX0_N 
PCIE1_TX0_N 


PCIE1_CLK_N 
PCIE1_CLK_N 
173 
 
174 
PCIE1_TX0_P 
PCIE1_TX0_P 


PCIE1_CLK_P 
PCIE1_CLK_P 
175 
 
176 
GND 
GND 


GND 
GND 
177 
 
178 
MOD_SLEEP* 
MOD_SLEEP* 


PCIE_WAKE* 
PCIE_WAKE* 
179 
 
180 
PCIE0_CLKREQ* 
PCIE0_CLKREQ* 


PCIE0_RST* 
PCIE0_RST* 
181 
 
182 
PCIE1_CLKREQ* 
PCIE1_CLKREQ* 


PCIE1_RST* 
PCIE1_RST* 
183 
 
184 
GBE_MDI0_N 
GBE_MDI0_N 


I2C0_SCL 
I2C0_SCL 
185 
 
186 
GBE_MDI0_P 
GBE_MDI0_P 


I2C0_SDA 
I2C0_SDA 
187 
 
188 
GBE_LED_LINK 
GBE_LED_LINK 


 
 
 
Pin Definitions 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  43 


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


**Pin # **
**Top **
**Odd **


** **
**Pin # **
**Bottom **
**Even **


**Jetson SODIMM **
**Signal Name **


**Jetson Orin Nano **
**Function **


I2C1_SCL 
I2C1_SCL 
189 
 
190 
GBE_MDI1_N 
GBE_MDI1_N 


I2C1_SDA 
I2C1_SDA 
191 
 
192 
GBE_MDI1_P 
GBE_MDI1_P 


I2S0_DOUT 
I2S0_DOUT 
193 
 
194 
GBE_LED_ACT 
GBE_LED_ACT 


I2S0_DIN 
I2S0_DIN 
195 
 
196 
GBE_MDI2_N 
GBE_MDI2_N 


I2S0_FS 
I2S0_FS 
197 
 
198 
GBE_MDI2_P 
GBE_MDI2_P 


I2S0_SCLK 
I2S0_SCLK 
199 
 
200 
GND 
GND 


GND 
GND 
201 
 
202 
GBE_MDI3_N 
GBE_MDI3_N 


UART1_TXD 
UART1_TXD 
203 
 
204 
GBE_MDI3_P 
GBE_MDI3_P 


UART1_RXD 
UART1_RXD 
205 
 
206 
GPIO07 
GPIO07 


UART1_RTS* 
UART1_RTS* 
207 
 
208 
GPIO08 
GPIO08 


UART1_CTS* 
UART1_CTS* 
209 
 
210 
CLK_32K_OUT 
CLK_32K_OUT 


GPIO09 
GPIO09 
211 
 
212 
GPIO10 
GPIO10 


CAM_I2C_SCL 
CAM_I2C_SCL 
213 
 
214 
FORCE_RECOVERY* 
FORCE_RECOVERY* 


CAM_I2C_SDA 
CAM_I2C_SDA 
215 
 
216 
GPIO11 
GPIO11 


GND 
MODULE_ID 
217 
 
218 
GPIO12 
GPIO12 


SDMMC_DAT0 
PCIE2_RST* 
219 
 
220 
I2S1_DOUT 
I2S1_DOUT 


SDMMC_DAT1 
PCIE2_CLKREQ* 
221 
 
222 
I2S1_DIN 
I2S1_DIN 


SDMMC_DAT2 
PCIE3_RST* 
223 
 
224 
I2S1_FS 
I2S1_FS 


SDMMC_DAT3 
PCIE3_CLKREQ* 
225 
 
226 
I2S1_SCLK 
I2S1_SCLK 


SDMMC_CMD 
PCIE3_CLK_N 
227 
 
228 
GPIO13 
GPIO13 


SDMMC_CLK 
PCIE3_CLK_P 
229 
 
230 
GPIO14 
GPIO14 


GND 
GND 
231 
 
232 
I2C2_SCL 
I2C2_SCL 


SHUTDOWN_REQ* 
SHUTDOWN_REQ* 
233 
 
234 
I2C2_SDA 
I2C2_SDA 


PMIC_BBAT 
PMIC_BBAT 
235 
 
236 
UART2_TXD 
UART2_TXD 


POWER_EN 
POWER_EN 
237 
 
238 
UART2_RXD 
UART2_RXD 


SYS_RESET* 
SYS_RESET* 
239 
 
240 
SLEEP/WAKE* 
SLEEP/WAKE* 


GND 
GND 
241 
 
242 
GND 
GND 


GND 
GND 
243 
 
244 
GND 
GND 


GND 
GND 
245 
 
246 
GND 
GND 


GND 
GND 
247 
 
248 
GND 
GND 


GND 
GND 
249 
 
250 
GND 
GND 


VDD_IN 
VDD_IN 
251 
 
252 
VDD_IN 
VDD_IN 


VDD_IN 
VDD_IN 
253 
 
254 
VDD_IN 
VDD_IN 


VDD_IN 
VDD_IN 
255 
 
256 
VDD_IN 
VDD_IN 


VDD_IN 
VDD_IN 
257 
 
258 
VDD_IN 
VDD_IN 


VDD_IN 
VDD_IN 
259 
 
260 
VDD_IN 
VDD_IN 


 


 
 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
DS-11105-001_v1.5  |  44 


# Chapter 5.
#  
# Electrical, Mechanical, and 


# Thermal Characteristics
##  


# 5.1
#  
# Operating and Absolute Maximum Ratings 


The parameters listed in following table are specific to a temperature range and operating 
voltage. Operating the Jetson Orin Nano beyond these parameters is not recommended. 


 


 
**Warning:**
 
Exceeding the listed conditions may damage and/or affect long-term reliability of 
the part. The Jetson Orin Nano 8GB module should never be subjected to conditions 
extending beyond the ratings listed below 


Table 5-1: Recommended Operating Conditions  


**Symbol **
**Parameter **
**Minimum **
**Typical **
**Maximum **
**Unit **


VDDDC 
VDD_IN (MODULE_ID low) (see note) 
4.75 
5 
5.25 
V 


VDD_IN (MODULE_ID high) (see note) 
4.75 
- 
20 
V 


PMIC_BBAT 
1.85 
- 
5.5 
V 


 


 
**Note:**
 MODULE_ID low is for Nano and MODULE_ID high is for NX. 


 


Absolute maximum ratings describe stress conditions. These parameters do not set minimum and 
maximum operating conditions that will be tolerated over extended periods of time. If the device 
is exposed to these parameters for extended periods of time, performance is not guaranteed, and 
device reliability may be affected. It is not recommended to operate the Jetson Orin Nano module 
under these conditions. 


 


 
 
 
Electrical, Mechanical, and Thermal Characteristics 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  45 


Table 5-2: Absolute Maximum Ratings 


**Symbol **
**Parameter **
**Minimum **
**Maximum **
**Unit **
**Notes **


VDDMAX 
VDD_IN (MODULE_ID 
low) 


-0.5 
5.5 
V 
 


VDD_IN (MODULE_ID 
high) 


-0.5 
20.5 
V 
 


PMIC_BBAT 
-0.3 
6.0 
V 
 


IDDMAX 
VDD_IN Imax 
- 
5 
A 
 


VM_PIN 
Voltage applied to any 
powered I/O pin 


-0.5 
VDD + 0.5 
V 
VDD + 0.5V when SYS_RESET* is high 
and associated I/O rail powered. I/O pins 
cannot be high (>0.5V) before 
SYS_RESET* goes high. When 
SYS_RESET* is low, the maximum voltage 
applied to any I/O pin is 0.5V 


DD pins configured as 
open drain 


-0.5 
3.63 
V 
The pin’s output-driver must be set to 
open-drain mode. 


TOP 
Operating 
Temperature 


-25 
See Note 
°C 
See the 
*Jetson Orin Nano Series Thermal *
*Design Guide*
 for details. 


TSTG 
Storage Temperature 
(ambient) 


-40 
80 
°C 
 


MMAX 
Mounting Force 
- 
8.2 
kgf1 
Maximum force applied to PCB. See the 
*Jetson Orin Nano Series Thermal Design *
*Guide*
 for additional details on mounting 
a thermal solution. 


Note: kgf stands for kilogram-force. 


# 5.2
#  
# Digital Logic  


Voltages less than the minimum stated value can be interpreted as an undefined state or logic 
level low which may result in unreliable operation. Voltages exceeding the maximum value can 
damage and/or adversely affect device reliability. 


Table 5-3: CMOS Pin Type DC Characteristics 


**Symbol **
**Description **
**Minimum **
**Maximum **
**Units **


VIL 
Input Low Voltage 
-0.5 
0.25 x VDD 
V 


VIH 
Input High Voltage 
0.75 x VDD 
0.5 + VDD 
V 


VOL 
Output Low Voltage (IOL = 1mA) 
- 
0.15 x VDD 
V 


VOH 
Output High Voltage (IOH = -1mA) 
0.85 x VDD 
- 
V 


 
 
 
Electrical, Mechanical, and Thermal Characteristics 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  46 


Table 5-4: Open Drain Pin Type DC Characteristics 


**Symbol **
**Description **
**Minimum **
**Maximum **
**Units **


VIL 
Input Low Voltage 
-0.5 
0.2 x VDD 
V 


VIH 
Input High Voltage 
0.8 x VDD 
3.63 
V 


VOL 
Output Low Voltage (IOL = 1mA) 
- 
0.15 x VDD 
V 


I2C [1,0] Output Low Voltage (IOL = 2mA) (see 
note) 


- 
0.3 x VDD 
V 


VOH 
Output High Voltage (IOH = -1mA) 
0.7 x VDD 
- 
V 


 


 
**Note:**
 I2C[1,0]_[SCL, SDA] pins pull-up to 3.3V through on module 2.2k
Ω
 resistor. I2C2_[SCL, SDA] 
pins pull-up to 1.8V through on module 2.2k
Ω
 resistor. 


# 5.3
#  
# Environmental and Mechanical Screening 


Table 5-5: Environmental Testing 


**Test **
**Conditions **
**Reference Standard **
**Results **


Temperature Humidity 
Biased 


85°C / 85% RH, 168 hours, Power ON 
JESD22-A101 
PASS 


Temperature Cycling 
-40°C to 105°C, 375 cycles, non-operational 
JESD22-A104, IPC9701 
PASS 


Temp/Humidity Cycle 
25°C to 65°C, 93% RH, six cycles 
NV Standard 
PASS 


Mechanical Shock – 
140G Non-Op 


140G, 2 msec, half sine, one shock/orientation, 
six orientations total, non-operational 


JESD22-B110 
PASS 


Mechanical Shock – 
50G Op 


50G, 6 msec, half sine, three shocks/orientation, 
six orientations total, operational 


IEC 600068 2-27 
PASS 


Connector Insertion 
Cycling 


Insert/Withdraw SD card and connector, 30 
cycles 


EIA-364 
PASS 


Random Vibration – 2G 
Non-Op 


5-500 Hz, 2 Grms, 1 hour/axis, three axes total, 
non-operational 


IEC60068-2-64 
PASS 


Random Vibration – 1G 
Op 


10-500 Hz, 1 Grms, 30 min/axis, three axes total, 
operational 


IEC60068-2-64 
PASS 


Hard Boot  
Power ON/OFF, ON for 150 sec, OFF for 30 sec 


2000 cycles at 25°C 


1000 cycles at -5°C 


1000 cycles at 45°C 


NV Standard 
PASS 


Operational Low Temp 
-5°C, 24 hours, operational 
NV Standard 
PASS 


 
 
 
Electrical, Mechanical, and Thermal Characteristics 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  47 


**Test **
**Conditions **
**Reference Standard **
**Results **


Operational High Temp  
45°C, 90%RH, 336 hours, operational 
NV Standard 
PASS 


MTBF / Failure Rate 
Controlled Environment (GB), T = 35°C or 50°C, 
CL = 90% 


Telcordia (TelC4) SR-332, 
ISSUE4 Parts Count 
(Method 1) 


See 
notes 
below 


MTBF / Failure Rate 
Uncontrolled Environment (GF) 


T = 35°C or 50°C, CL = 90% 


Telcordia (TelC4) SR-332, 
ISSUE4 Parts Count 
(Method 1) 


See 
notes 
below 


 


 
**Notes:**
 MTBF numbers below are based on Telcordia (TelC4) SR-332, ISSUE4, Calculation 
Methodology:  
Parts Count (Method 1), UCL = 90%, Quality level: II 
>
 
Orin Nano 8GB: GB at 35: 3,911,708 hours GB at 50: 2,107,458 hours GF at 35: 


2,888,137 hours GF at 50: 1,468,031 hours. 


>
 
Orin Nano 4GB: GB at 35: 4,558,489 hours GB at 50: 2,250,633 hours GF at 35: 


3,210,552 hours GF at 50: 1,535,375 hours. 


# 5.4
#  
# Storage and Handling 


Table 5-6: Typical Handling and Storage Environment 


**Parameter **
**Description **


Storage temperature (ambient)1 
18°C to 30°C 


Storage humidity 
30% to 70% RH 


Storage life2 
5 years from NVIDIA shipment date to customers 


 


 
**Note:**
 Transportation is a limited range of time that is covered by AEC grade 3 specs (-40°C to 
85°C). Longer term storage at hubs, distribution points, and warehousing where climate controls 
are in place should follow conditions mentioned above. 


Duration based on product being packed and stored in a controlled environment without power on.
 


 


 


 
 


 
 
 
Electrical, Mechanical, and Thermal Characteristics 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  48 


# 5.5
#  
# Drawing and Dimensions 


 


**Module Size:**
 69.6 mm x 45 mm 


**Module Weight:**
 0.028kg 


 


 
**Note**
: 


**>**
** **
All dimensions are in millimeters unless otherwise specified. 


**>**
** **
Tolerances are:  .X ± 0.25, XX ± is 0.1, Angle ± is 1. 


Figure 5-1: Top View 


 


 
 


 
 
 
Electrical, Mechanical, and Thermal Characteristics 


 
 
NVIDIA Jetson Orin Nano Series Modules Data Sheet 
 
DS-11105-001_v1.5  |  49 


Figure 5-2: Bottom View 


 


 


 


 


 


 


 


 
 


 
NVIDIA Corporation | 2788 San Tomas Expressway, Santa Clara, CA 95051  
**http://www.nvidia.com**
  


Notice 


This document is provided for information purposes only and shall not be regarded as a warranty of a certain functionality, condition, or quality of a 
product. NVIDIA Corporation (“NVIDIA”) makes no representations or warranties, expressed or implied, as to the accuracy or completeness of the 
information contained in this document and assumes no responsibility for any errors contained herein. NVIDIA shall have no liability for the 
consequences or use of such information or for any infringement of patents or other rights of third parties that may result from its use. This document 
is not a commitment to develop, release, or deliver any Material (defined below), code, or functionality. 


NVIDIA reserves the right to make corrections, modifications, enhancements, improvements, and any other changes to this document, at any time 
without notice. 


Customer should obtain the latest relevant information before placing orders and should verify that such information is current and complete. 


NVIDIA products are sold subject to the NVIDIA standard terms and conditions of sale supplied at the time of order acknowledgement, unless otherwise 
agreed in an individual sales agreement signed by authorized representatives of NVIDIA and customer (“Terms of Sale”). NVIDIA hereby expressly objects 
to applying any customer general terms and conditions with regards to the purchase of the NVIDIA product referenced in this document. No contractual 
obligations are formed either directly or indirectly by this document. 


NVIDIA products are not designed, authorized, or warranted to be suitable for use in medical, military, aircraft, space, or life support equipment, nor in 
applications where failure or malfunction of the NVIDIA product can reasonably be expected to result in personal injury, death, or property or 
environmental damage. NVIDIA accepts no liability for inclusion and/or use of NVIDIA products in such equipment or applications and therefore such 
inclusion and/or use is at customer’s own risk. 


NVIDIA makes no representation or warranty that products based on this document will be suitable for any specified use. Testing of all parameters of 
each product is not necessarily performed by NVIDIA. It is customer’s sole responsibility to evaluate and determine the applicability of any information 
contained in this document, ensure the product is suitable and fit for the application planned by customer, and perform the necessary testing for the 
application in order to avoid a default of the application or the product. Weaknesses in customer’s product designs may affect the quality and reliability 
of the NVIDIA product and may result in additional or different conditions and/or requirements beyond those contained in this document. NVIDIA 
accepts no liability related to any default, damage, costs, or problem which may be based on or attributable to: (i) the use of the NVIDIA product in any 
manner that is contrary to this document or (ii) customer product designs. 


No license, either expressed or implied, is granted under any NVIDIA patent right, copyright, or other NVIDIA intellectual property right under this 
document. Information published by NVIDIA regarding third-party products or services does not constitute a license from NVIDIA to use such products 
or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual 
property rights of the third party, or a license from NVIDIA under the patents or other intellectual property rights of NVIDIA. 


Reproduction of information in this document is permissible only if approved in advance by NVIDIA in writing, reproduced without alteration and in full 
compliance with all applicable export laws and regulations, and accompanied by all associated conditions, limitations, and notices. 


THIS DOCUMENT AND ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS 
(TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR 
OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, 
AND FITNESS FOR A PARTICULAR PURPOSE. TO THE EXTENT NOT PROHIBITED BY LAW, IN NO EVENT WILL NVIDIA BE LIABLE FOR ANY DAMAGES, 
INCLUDING WITHOUT LIMITATION ANY DIRECT, INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES, HOWEVER CAUSED AND 
REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF ANY USE OF THIS DOCUMENT, EVEN IF NVIDIA HAS BEEN ADVISED OF THE POSSIBILITY 
OF SUCH DAMAGES. Notwithstanding any damages that customer might incur for any reason whatsoever, NVIDIA’s aggregate and cumulative liability 
towards customer for the products described herein shall be limited in accordance with the Terms of Sale for the product.  


Trademarks 


NVIDIA, the NVIDIA logo, are trademarks and/or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and 
product names may be trademarks of the respective companies with which they are associated. 


VESA DisplayPort 


DisplayPort and DisplayPort Compliance Logo, DisplayPort Compliance Logo for Dual-mode Sources, and DisplayPort Compliance Logo for Active Cables 
are trademarks owned by the Video Electronics Standards Association in the United States and other countries. 


HDMI 


HDMI, the HDMI logo, and High-Definition Multimedia Interface are trademarks or registered trademarks of HDMI Licensing LLC. 


Arm 


Arm, AMBA, and ARM Powered are registered trademarks of Arm Limited. Cortex, MPCore, and Mali are trademarks of Arm Limited. All other brands or 
product names are the property of their respective holders. 
ʺ
Arm
ʺ
 is used to represent ARM Holdings plc; its operating company Arm Limited; and the 
regional subsidiaries Arm Inc.; Arm KK; Arm Korea Limited.; Arm Taiwan Limited; Arm France SAS; Arm Consulting (Shanghai) Co. Ltd.; Arm Germany 
GmbH; Arm Embedded Technologies Pvt. Ltd.; Arm Norway, AS, and Arm Sweden AB. 


OpenCL 


OpenCL is a trademark of Apple Inc. used under license to the Khronos Group Inc. 


Copyright  


© 2022-2024 NVIDIA Corporation. All rights reserved.    

