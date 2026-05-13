# Conduit-Selection-Tool
### Personal Engineering Project

### **📝 Overview**
This project involved the development of a standalone desktop automation tool designed to streamline electrical engineering workflows by calculating **National Electrical Code (NEC)** compliant conduit fill requirements. Originally developed as a Python-based utility, the application automates complex regulatory lookups to determine the minimum required conduit size for multi-conductor cable schedules.

The tool bridges the gap between field engineering and software automation, utilizing a **SQLite** backend to manage cable specifications and a decision-logic engine to ensure safety and code compliance.

---
### **⚠️ Project Status & Technical Note**
The original source code for this project was lost due to a storage failure. The repository provided here serves as a technical archive of the project's logic and deployment strategy.

* **Binary Integrity:** The primary stable versions of this project are the **fully functional .exe binaries** (Main App and Setup Utility).
* **Decompilation & Recovery:** In an effort to document the internal logic, I performed a decompilation of the executable. The resulting script (`ConduitFill.py`) is included for **logic review only**; it contains formatting artifacts and requires refactoring to reach production-grade readability.
* **Current Utility:** The provided `.exe` files remain the recommended method for interacting with the tool's intended functionality.
---

### **🛠 Software Specifications**
* **Language:** Python 3.11
* **GUI Framework:** Tkinter
* **Database:** SQLite3
* **Deployment:** PyInstaller (Standalone Executable)
* **Compliance Standards:** NEC Chapter 9, Table 1

---

### **📂 Project Structure**
#### **Executables (Deployment)**
* `ConduitFill.exe`: The primary standalone application for conduit sizing.
* `Setup.exe`: A custom utility developed to **automatically initialize** required `.db` schemas and folder structures for new users.
#### **Reference Assets**
* `ConduitFill.py`: Recovered/Decompiled source code (provided for logic verification).
* `cable_book.db`: Relational database containing cable added in main window.
* `icon.ico`: Custom application branding assets.

---

### **⚙️ Technical Highlights**

#### **1. Automated Regulatory Decision Matrix**
The core engine implements a hierarchical decision matrix based on **NEC Chapter 9**. The system dynamically adjusts permissible fill ratios based on conductor count to ensure code-compliant installations:
* **1 Conductor:** 53% Fill
* **2 Conductors:** 31% Fill
* **3+ Conductors:** 40% Fill (Standard)

#### **2. Setup & Environment Provisioning**
To ensure "plug-and-play" reliability, I engineered a **Setup.exe** utility. This tool scans the local directory for `cable_book.db` and `areas.db`; if missing, it executes SQL commands to bootstrap the necessary tables and primary keys (OIDs), preventing initialization crashes.

#### **3. Algorithmic Conduit Selection**
The program iterates through a "ladder" of standard conduit sizes (0.5" to 6.0"). It calculates the cross-sectional area ($Area = \pi \times r^2$) of the cable bundle and matches it against the nearest compliant conduit diameter, optimizing for material efficiency while maintaining safety margins.

---
**Author:** Luca Daloia  
**Project Date:** Summer 2023
