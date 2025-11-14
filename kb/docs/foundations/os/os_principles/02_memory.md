# Memory

## 📖 What Is Main Memory

**Main memory**, also known as **RAM (Random Access Memory)**, is the primary volatile storage used by a computer to hold data and instructions that are actively being used or processed.

--- 

## 💡 Key Characteristics

**Volatile**: Contents are lost when the system is powered off.

**Fast Access**: Much quicker than secondary storage (e.g., SSDs or HDDs).

**Directly Accessible by CPU**: Instructions and data are fetched from RAM during execution.

---

## 🛞 Base Frequency vs Effective Data Rate

**Base Frequency (Clock Speed)**

  - The **base frequency** is the actual clock speed of the memory chip.
  - It’s measured in **megahertz (MHz)**.
  - This is the speed at which the memory controller and DRAM communicate per clock cycle.
  > Example: DDR4-3200 has a base frequency of **1600 MHz**.

**Effective Data Rate (Transfer Rate)**

  - The **effective data rate** is the **actual data throughput** — how much data istransferred per second.
  - Because DDR memory transfers **data on both the rising and falling edges** of theclock signal, it achieves **twice the base frequency** in data rate.
  - Measured in **MT/s (MegaTransfers per second)**.
  > Example: DDR4-3200 has an effective data rate of **3200 MT/s**, even though its base frequency is 1600 MHz.

---

## 🔢 Bit Width in Main Memory

**Bit width** refers to the number of bits that can be processed or transferred in parallel. In the context of main memory, it affects:

- **Data Bus Width**  
  Determines how many bits can be transferred between memory and CPU in one cycle. 
    - Example: 
        - A 64-bit data bus can transfer 64 bits (8 bytes) per cycle.

- **Address Bus Width**  
  Determines how much memory can be addressed directly.  
    - Example:  
        - 32-bit address bus → (2^32 = 4GB) addressable memory  
        - 64-bit address bus → (2^64 = 18.4EB) (Exabytes) addressable memory

- **Memory Module Width**  
  Refers to how many bits wide each memory module is (e.g., 64-bit DIMMs). Wider modules allow faster and more parallel access.

---

## 🗄️ Storage of Main Memory

Main memory (RAM) stores:

- **Active Program Instructions**  
  Code currently being executed by the CPU.

- **Runtime Data**  
  Variables, buffers, and temporary data used during execution.

- **Operating System Kernel & Services**  
  Core OS components that must remain in memory for system operation.

- **Memory-Mapped I/O**  
  Some hardware devices use memory addresses for communication.

Memory is volatile — it loses its contents when power is off. Common types include:

| Type     | Description                          |
|----------|--------------------------------------|
| **DRAM** | Dynamic RAM, slower but cheaper, used for main system memory |
| **SRAM** | Static RAM, faster and more expensive, used in CPU caches |

---

## 🚇 Dual-Tunnel Memory Architecture

**Dual-tunnel** (or **dual-channel**) architecture improves memory bandwidth by allowing simultaneous access to two memory modules.

**How It Works**

- Memory is split across two channels (e.g., Channel A and Channel B).
- CPU can read/write to both channels in parallel.
- Requires matched pairs of memory modules (same size, speed, and type).

**Benefits**

- Doubles theoretical memory bandwidth.
- Reduces latency for memory-intensive tasks.
- Improves performance in multi-threaded and high-throughput applications.

---

## 🧠 Address Space and Memory Addresses

**Address Space**

- The **address space** of a system defines the range of memory addresses it can use.
- It is determined by the **address width** of the architecture:
    - **32-bit systems**: (2^32 = 4GB) addressable space
    - **64-bit systems**: (2^64 = 18.4EB) addressable space
- Modern architectures (x86, ARM, RISC-V) use **byte-addressable memory**:
    - Each memory address refers to **exactly 1 byte**.
    - Larger data types (e.g., 32-bit integers, 64-bit doubles) span multiple consecutive addresses.
- The address space is **fixed by architecture**, but its usage is dynamic:
    - Operating systems and MMUs can map, remap, and reserve regions.
    - Virtual memory allows flexible use of physical memory.

**Memory Address**

- A **memory address** is a unique identifier for a location in memory.
- Common representations:
    - **Hexadecimal**: `0x00007FFDE3A4B000`
    - **Binary**: `0000000000000000000000000000000000000000000000000000000000000000`
    - **Decimal**: `140732919803904`
- The **lowest address** in a system is typically `0x0000000000000000`, especially if only one memory module is installed.
- In systems with reserved regions (e.g., BIOS, MMIO), RAM may start at a higher address.

> Note: Memory cards (e.g., SD cards) are not directly mapped into address space like RAM. They are accessed via controllers, which may themselves be memory-mapped.
