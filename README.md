# 🔍 Simple Port Scanner (Python)

## 📌 Overview

This is a basic port scanner built using Python's `socket` module.

It scans a target IP address and identifies open ports by attempting TCP connections.

---

## ⚙️ How It Works

* The script loops through a range of ports
* For each port, it creates a socket
* It attempts a connection using `connect_ex()`
* If the connection succeeds, the port is marked as **OPEN**

---

## 🚀 Features

* Scans a custom IP address
* Custom port range
* Fast scanning using timeout
* Displays open ports only

---

## 🧪 Example Output

```
Scanning 127.0.0.1...
8080 is OPEN
```

---

## 🛠️ Requirements

* Python 3.x

---

## ▶️ Usage

```bash
python app.py
```

Then enter:

* Target IP
* Start port
* End port

---

## 📚 What I Learned

* Basics of networking (IP, ports, TCP)
* How socket connections work
* How port scanning identifies open services
* Real-world reconnaissance concepts

---

## ⚠️ Disclaimer

This tool is for educational purposes only.

Do not scan systems without permission.

---

## 🔗 Inspiration

This project is inspired by how tools like Nmap perform network scanning.
