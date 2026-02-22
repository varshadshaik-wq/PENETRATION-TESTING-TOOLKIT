# PENETRATION-TESTING-TOOLKIT
"COMPANY": CODTECH IT SOLUTIONS
NAME: SHAIK VARSHAD 
"INTERN ID*:CTIS2404 
"DOMAIN*: CYBER SECURITY & ETHICAL HACKING 
"DURATION*: 8 WEEEKS 
"MENTOR*: NEELA SANTOSH

# Penetration Testing Toolkit

## Overview

The **Penetration Testing Toolkit** is a Python-based modular toolkit designed for ethical hackers, cybersecurity enthusiasts, and students to perform basic penetration testing on systems they own or have explicit permission to test. This toolkit provides a hands-on, educational platform to explore core penetration testing techniques such as **port scanning**, **banner grabbing**, and **password brute-forcing** in a safe and controlled environment. The toolkit is built with Python and structured in a modular format, allowing easy extension and customization for advanced security testing exercises.

The primary goal of this project is to help learners understand how different penetration testing methods work, develop practical skills in network security, and demonstrate ethical hacking practices responsibly. All features are intended for educational use and authorized testing only.

---

## Features

The toolkit currently includes three main modules:

1. **Port Scanner**
   - Scans a range of TCP ports on a specified host to identify open services.
   - Helps users understand which ports are active and may potentially be vulnerable.
   - Displays a real-time list of open ports, providing immediate feedback during scanning.

2. **Banner Grabber**
   - Connects to a specified port and retrieves the service banner information.
   - Provides insight into running services such as HTTP, FTP, SSH, or other TCP-based protocols.
   - Useful for learning how attackers gather information about a target system without causing harm.

3. **Brute Force Simulation**
   - Simulates a password brute-force attack using a predefined wordlist.
   - Designed for educational purposes to demonstrate how attackers attempt to guess passwords.
   - Uses an absolute path to the wordlist to ensure consistent results across different environments.

Each module is implemented as a separate Python script in the `modules` folder. The main controller script, `main.py`, integrates all modules and provides a **command-line menu interface** for easy interaction. This modular design makes it easy to add additional features in the future, such as **multithreaded scanning**, **logging results**, or integrating other penetration testing tools.

# Output
# Main Menu Output
<img width="1919" height="1019" alt="Image" src="https://github.com/user-attachments/assets/d361684b-f5a1-4be5-a085-bb8e570e1f34" />
# Port Scanner Output
<img width="1913" height="1012" alt="Image" src="https://github.com/user-attachments/assets/9f758d8d-35d6-4414-894f-446b7eb899d1" />
# Banner Grabber Output
<img width="1912" height="1018" alt="Image" src="https://github.com/user-attachments/assets/de7bd0da-ee90-43ec-9968-ab1a5d6f1589" />
# Brute Force Module Output
<img width="1903" height="1014" alt="Image" src="https://github.com/user-attachments/assets/7e3bdb6e-0959-4fe1-8b23-22c497f7642e" />
