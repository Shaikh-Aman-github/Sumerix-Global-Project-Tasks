# Cyber Security & Ethical Hacking Internship — Task 1

## Secure Network Asset Inventory & System Information Scanner

This repository contains my work for **Task 1** of the **Cyber Security & Ethical Hacking Internship**.

Task 1 focuses on cybersecurity foundations, Linux administration, networking fundamentals, virtualization, Python for security, Git & GitHub, and secure cybersecurity laboratory setup.


## Setup & Run Instructions

### 1. Prerequisites

Before running the project, make sure the following are installed:

- Kali Linux
- Python 3.12 or higher
- Git
- VS Code (optional)
- VirtualBox or VMware (if running Kali as a virtual machine)

Check Python version:

```bash
python3 --version

---

## Task Information

| Item | Details |
|---|---|
| Internship Domain | Cyber Security & Ethical Hacking |
| Task | Task 1 |
| Difficulty | Beginner |
| Project | Secure Network Asset Inventory & System Information Scanner |
| Operating System | Kali Linux |
| Virtualization | Oracle VirtualBox |
| Programming Language | Python |

---

## 1. Task Objectives

The objectives of Task 1 are:

- Understand cybersecurity fundamentals.
- Understand ethical hacking principles and responsibilities.
- Build a secure cybersecurity laboratory.
- Install and configure Kali Linux.
- Understand virtualization and virtual machines.
- Learn Linux filesystem navigation and terminal commands.
- Manage users, groups, and file permissions in Linux.
- Understand networking fundamentals.
- Learn IPv4 addressing and subnet basics.
- Understand the OSI and TCP/IP models.
- Understand common networking protocols and ports.
- Use Git and GitHub for version control.
- Develop a Python-based security utility.
- Generate a structured system inventory report.

---

## 2. Cybersecurity Lab Environment

The cybersecurity laboratory uses Kali Linux running inside Oracle VirtualBox.

### Lab Architecture

```text
Host Operating System
        |
        v
    VirtualBox
        |
        v
   Kali Linux VM
        |
        +-------------------+
        |                   |
       NAT             Host-Only
        |                   |
        v                   v
    Internet           Isolated Lab
