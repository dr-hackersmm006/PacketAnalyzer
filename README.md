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

## Project Structure

```text
Scapy-Packet-Analyzer/
│
├── analyzer.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── all_packets.png
│   └── filtered_packets.png
│
└── captures/
    ├── all_packets.pcap
    └── filtered_packets.pcap
```

## Requirements

- Kali Linux
- Python 3
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