from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, DNSQR, ARP, wrpcap


def yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter yes or no.")


displayed_count = 0
tcp_count = 0
udp_count = 0
arp_count = 0
icmp_count = 0
other_count = 0

source_ips = set()

a = int(input("How many packets do you want to capture? "))

target_ip = input("Enter target IP (or press Enter for all IPs): ").strip()

packets = sniff(count=a)

print("Captured", len(packets), "packets.")

print("\t Scapy Packet Analyzer \t")
print("1. Show all packets")
print("2. Show TCP packets")
print("3. Show UDP packets")
print("4. Show ICMP packets")
print("5. Show ARP packets")
print("6. Show DNS packets")

choice = input("Enter your choice: ")

protocol_choices = {
    "1": "ALL",
    "2": "TCP",
    "3": "UDP",
    "4": "ICMP",
    "5": "ARP",
    "6": "DNS"
}

selected_protocol = protocol_choices.get(choice)

if selected_protocol is None:
    print("Invalid choice!")
    exit()

filtered_packets = []

print("--------------------")

for number, packet in enumerate(packets, start=1):

    if ARP in packet:
        arp_count += 1
    elif TCP in packet:
        tcp_count += 1
    elif UDP in packet:
        udp_count += 1
    elif ICMP in packet:
        icmp_count += 1
    else:
        other_count += 1

    if IP in packet:
        source_ips.add(packet[IP].src)

    if target_ip:
        if IP not in packet:
            continue

        if packet[IP].src != target_ip and packet[IP].dst != target_ip:
            continue

    if selected_protocol == "TCP" and TCP not in packet:
        continue
    elif selected_protocol == "UDP" and UDP not in packet:
        continue
    elif selected_protocol == "ICMP" and ICMP not in packet:
        continue
    elif selected_protocol == "ARP" and ARP not in packet:
        continue
    elif selected_protocol == "DNS" and DNS not in packet:
        continue

    filtered_packets.append(packet)
    displayed_count += 1

    print("Packet number:", number)

    if ARP in packet:
        protocol = "ARP"
    elif TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"
    elif IP in packet:
        protocol = "Other IP"
    else:
        protocol = "Other"

    print("Protocol:", protocol)

    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
    else:
        print("No IP layer")

    if UDP in packet:
        print("Source port:", packet[UDP].sport)
        print("Destination port:", packet[UDP].dport)

    if TCP in packet:
        print("Source port:", packet[TCP].sport)
        print("Destination port:", packet[TCP].dport)
        print("TCP flags:", packet[TCP].flags)

    if DNS in packet and DNSQR in packet:
        print("DNS query:", packet[DNSQR].qname.decode(errors="replace"))

    print("--------------------")

if displayed_count == 0:
    print("No matching", selected_protocol, "packets found.")
    print("--------------------")

print("========== Capture Summary ==========")
print("Target IP:", target_ip if target_ip else "All IPs")
print("Selected protocol:", selected_protocol)
print("Packets displayed:", displayed_count)
print("Total ARP packets:", arp_count)
print("Total TCP packets:", tcp_count)
print("Total UDP packets:", udp_count)
print("Total ICMP packets:", icmp_count)
print("Total other packets:", other_count)
print("Total captured packets:", len(packets))
print("Unique source IPs:", len(source_ips), "\n", source_ips)

save_choice = yes_no("Do you want to save the packets as a .pcap file? (y/n): ")

if save_choice:
    filename = input("Enter filename (default: capture.pcap): ").strip()

    if not filename:
        filename = "capture.pcap"

    if not filename.lower().endswith(".pcap"):
        filename += ".pcap"

    try:
        wrpcap(filename, filtered_packets)
        print("Filtered packets saved successfully as", filename)
        print("Packets saved:", len(filtered_packets))
    except OSError as error:
        print("Error saving packets:", error)

else:
    print("Packets not saved.")
