# Scapy Packet Analyzer

A Python command-line network packet analyzer developed using Scapy. This tool captures, filters, and analyzes network packets in an authorized lab environment.

## Features

- Capture a specified number of network packets.
- Filter packets using a target IP address.
- Display all captured packets.
- Filter TCP, UDP, ICMP, ARP, and DNS packets.
- Display source and destination IP addresses.
- Display source and destination ports.
- Display TCP flags.
- Extract DNS queries.
- Count packets according to their protocols.
- Identify unique source IP addresses.
- Save filtered packets as PCAP files.
- Analyze saved PCAP files using Wireshark.

## Requirements

- Python 
- Scapy
- libpcap
- Wireshark (recommended for PCAP analysis)

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Scapy-Packet-Analyzer
```

### 2. Install system dependencies

Update Kali Linux and install the required packages:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv libpcap-dev wireshark
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 4. Install Python dependencies

Install the required Python libraries using the requirements file:

```bash
pip install -r requirements.txt
```

## Usage

Run the packet analyzer with the necessary network capture permissions:

```bash
sudo ./venv/bin/python analyzer.py
```

### Step 1: Enter packet count

Specify how many packets you want to capture.

### Step 2: Enter target IP

Enter a target IP address to filter packets associated with that IP.

Press Enter to include all IP addresses.

### Step 3: Select a protocol

The analyzer provides the following options:

| Option | Protocol |
|---|---|
| 1 | Show all packets |
| 2 | Show TCP packets |
| 3 | Show UDP packets |
| 4 | Show ICMP packets |
| 5 | Show ARP packets |
| 6 | Show DNS packets |

### Step 4: View packet information

The analyzer displays relevant packet information, including:

- Protocol
- Source IP
- Destination IP
- Source port
- Destination port
- TCP flags
- DNS query

### Step 5: View capture summary

After packet analysis, the program displays:

- Total captured packets
- Packets displayed
- TCP packet count
- UDP packet count
- ARP packet count
- ICMP packet count
- Other packet count
- Number of unique source IP addresses

### Step 6: Save packets

Choose whether to save the matching packets as a `.pcap` file.

Enter a filename or use the default filename:

```text
capture.pcap
```

The generated PCAP file can be opened using Wireshark.

## PCAP Analysis

The analyzer supports saving captured packets in PCAP format.

To inspect a saved capture:

1. Open Wireshark.
2. Select File → Open.
3. Select your `.pcap` file.
4. Inspect the captured packets and their protocol layers.

## Packet Layers and Protocols

| Protocol | Description |
|---|---|
| Ethernet | Handles communication using MAC addresses. |
| IP | Provides source and destination IP addresses. |
| TCP | Provides reliable, connection-oriented communication. |
| UDP | Provides connectionless communication. |
| ICMP | Used for network diagnostics and error reporting. |
| ARP | Resolves IPv4 addresses into MAC addresses. |
| DNS | Resolves domain names into IP addresses. |

## Permissions

Packet capturing requires sufficient privileges to access network interfaces.

On Kali Linux, run the analyzer using root privileges:

```bash
sudo ./venv/bin/python analyzer.py
```

Only capture network traffic on systems and networks where you have authorization.

## Limitations

- The analyzer captures only the specified number of packets.
- Packet filtering is performed after packet capture.
- Encrypted traffic cannot normally be inspected as plaintext.
- Some packets may not contain an IP layer.
- Packet visibility depends on the network interface and capture permissions.
- Wireless monitor-mode capture requires additional hardware and configuration.
- The analyzer is designed for educational and authorized laboratory use.

## Demonstration

The project includes demonstration screenshots and PCAP files showing:

1. General packet capture and analysis.
2. Protocol-filtered packet capture.
3. Saving filtered packets in PCAP format.
4. Inspecting captured packets using Wireshark.

## Author

**Sagnik Mridha**

Cybersecurity & Ethical Hacking Student

GitHub: https://github.com/dr-hackersmm006

---

**Disclaimer:** This project is developed for educational purposes and authorized network analysis only. The author is not responsible for unauthorized use of this tool.


<img width="1917" height="1020" alt="Screenshot 2026-11-01 025015" src="https://github.com/user-attachments/assets/811dfa47-ba87-4587-b805-52d79428f398" />

<img width="1917" height="1017" alt="Screenshot 2026-11-01 025058" src="https://github.com/user-attachments/assets/7d0a3c9d-3c76-4efb-b52a-1d701efdfeca" />

<img width="1917" height="983" alt="Screenshot 2026-11-01 025112" src="https://github.com/user-attachments/assets/ee6460fc-1dd3-4b83-9766-5ab91e174ed3" />

<img width="1917" height="1021" alt="Screenshot 2026-11-01 025210" src="https://github.com/user-attachments/assets/8155539b-2c8d-4901-acfb-c754d0c2cd6d" />

<img width="1917" height="1015" alt="Screenshot 2026-11-01 030747" src="https://github.com/user-attachments/assets/9fa1e6ff-892b-4510-86ec-844e648647f6" />

<img width="1897" height="845" alt="Screenshot 2026-11-01 025759" src="https://github.com/user-attachments/assets/a3509032-38ea-45b3-ad0b-6a44da18f201" />

<img width="1902" height="846" alt="Screenshot 2026-11-01 025858" src="https://github.com/user-attachments/assets/61ad5f06-6fab-4ce3-89a4-60e43a26146f" />

<img width="1911" height="762" alt="Screenshot 2026-11-01 025950" src="https://github.com/user-attachments/assets/702edd39-24ef-412a-a300-b92e440040a5" />

<img width="1916" height="838" alt="Screenshot 2026-11-01 025929" src="https://github.com/user-attachments/assets/740dfbb1-6a9f-4fc0-8d88-a9f744664403" />

<img width="1901" height="842" alt="Screenshot 2026-11-01 030039" src="https://github.com/user-attachments/assets/4bc4aec7-86b4-4300-977d-3b40d9e77b3b" />

<img width="1898" height="832" alt="Screenshot 2026-11-01 030108" src="https://github.com/user-attachments/assets/b642af9c-e37b-4cb5-93d3-cdfbe32e41f6" />
<img width="1902" height="840" alt="Screenshot 2026-11-01 030128" src="https://github.com/user-attachments/assets/50fd6b25-8af5-4bc1-9359-1762258378ca" />
<img width="1886" height="837" alt="Screenshot 2026-11-01 030513" src="https://github.com/user-attachments/assets/ccd1df87-658d-464e-8ce5-5f72d45d3da6" />
