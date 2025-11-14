# CPU
The **Central Processing Unit (CPU)** is the core of a computer system responsible for executing instructions and managing data flow.

---

## 🧩 CPU Components

The CPU consists of the following key components:

- **Control Unit (CU)**  
  Coordinates and directs operations within the CPU, managing the execution of instructions.

- **Arithmetic Logic Unit (ALU)**  
  Performs arithmetic operations (like addition and subtraction) and logical operations (like comparisons).

- **Registers**  
  Small, fast storage locations inside the CPU used to hold data, instructions, and addresses temporarily.

- **Cache Memory**  
    High-speed memory used to store frequently accessed data and instructions:
    - **L1 Cache**: Closest to the CPU core, fastest and smallest.
    - **L2 Cache**: Larger and slightly slower, often shared between cores.
    - **L3 Cache**: Largest and slowest, shared across all cores.

- **Instruction Set Architecture (ISA)**  
  Defines the set of instructions the CPU can execute:
    - **RISC (Reduced Instruction Set Computer)**: Simplified instructions for faster execution.
    - **CISC (Complex Instruction Set Computer)**: Richer instruction set allowing more complex operations per instruction.

---

## 🔁 Memory Interaction

The CPU interacts with memory by **reading** instructions and data, and **writing** results. This constant exchange enables the CPU to perform tasks and communicate with other components.

---

## 🔄 Data Flow: Memory to CPU

Here’s the typical flow of data from memory into the CPU for processing:

`Main Memory → Cache (L3 → L2 → L1) → Registers → CU/ALU`

This hierarchy ensures that the CPU accesses data as quickly and efficiently as possible.

---

## 🧮 Bit Width Explained

**Bit width** refers to the number of bits the CPU can process at once. It affects several architectural elements:

| Component         | Bit Width Meaning                                                                 |
|-------------------|-----------------------------------------------------------------------------------|
| **Registers**      | Determines the size of data the CPU can handle in a single operation (e.g., 32-bit vs 64-bit). |
| **Cache**          | Influences how much data can be stored and accessed quickly. Wider bit widths allow faster data movement. |
| **Data Bus**       | Affects how much data can be transferred between CPU and memory per cycle.       |
| **Address Bus**    | Determines the maximum addressable memory space (e.g., 32-bit = 4GB, 64-bit = 16EB). |

---

> 💡 A 64-bit CPU can handle larger data types and access more memory than a 32-bit CPU, making it ideal for modern computing tasks.