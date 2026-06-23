# 🌐 DNS Cache Poisoning & Local DNS Spoofing Attack Lab

## 📌 Overview

This lab demonstrates how DNS spoofing and DNS cache poisoning attacks can be performed against a local DNS infrastructure.

Using Scapy and Python, forged DNS responses were injected into the network to manipulate domain resolution, poison DNS caches, alter authoritative nameserver records, and study how DNS servers process malicious authority and additional sections.

The lab explores several DNS attack scenarios ranging from simple response spoofing to advanced cache poisoning techniques.

---

## 🎯 Objectives

- Understand DNS request and response structures
- Perform DNS response spoofing using Scapy
- Poison a DNS server cache
- Manipulate DNS authority records
- Inject malicious NS records
- Analyze DNS cache behavior
- Observe handling of authority and additional records
- Verify successful DNS poisoning attacks

---

## 🛠️ Technologies Used

- Python
- Scapy
- Linux
- Docker
- DNS
- BIND DNS Server
- TCP/IP Networking

---

## 🧠 Concepts Covered

- DNS Resolution
- DNS Spoofing
- DNS Cache Poisoning
- DNS Authority Records
- DNS Additional Records
- Packet Forgery
- DNS Response Injection
- Network Security Testing

---

# DNS Response Spoofing

## Step 1: Build and Start the Lab Environment

The DNS attack environment is initialized using Docker containers.

![Step 1](images/task1-lab-setup.png)

---

## Step 2: Identify Target IP and Network Interface

The victim IP address and active network interface are identified for packet interception.

![Step 2](images/task1-network-enumeration.png)

---

## Step 3: Modify the Scapy Attack Script

The attack script is configured to intercept DNS requests and return a forged DNS response.

Spoofed Address:

```python
1.2.3.4
```

![Step 3](images/task1-script-modification.png)

---

## Step 4: Verify Normal DNS Resolution

Before launching the attack, DNS resolution returns the legitimate IP address.

![Step 4](images/task1-before-attack.png)

---

## Step 5: Flush DNS Cache

The local DNS cache is cleared to ensure fresh DNS lookups.

![Step 5](images/task1-cache-flush.png)

---

## Step 6: Execute DNS Spoofing Attack

The Scapy script is executed on the attacker machine.

![Step 6](images/task1-attack-execution.png)

---

## Step 7: Verify Spoofed DNS Resolution

The DNS query now resolves to the attacker-controlled IP address.

```text
www.example.com → 1.2.3.4
```

![Step 7](images/task1-spoofed-result.png)

---

# Direct DNS Server Targeting

## Step 1: Launch Attack Against DNS Server

The DNS server IP is specified directly during execution.

![Task 2 Attack](images/task2-attack-execution.png)

---

## Step 2: Verify Poisoned Response

DNS queries continue resolving to the forged address.

```text
1.2.3.4
```

![Task 2 Result](images/task2-verification.png)

---

# DNS Cache Poisoning with Malicious NS Records

## Step 1: Modify DNS Authority Section

The attack script is enhanced to inject malicious NS records.

![Task 3 Script](images/task3-script-update.png)

---

## Step 2: Execute Cache Poisoning Attack

The spoofed response is transmitted to the DNS server.

![Task 3 Execution](images/task3-attack-execution.png)

---

## Step 3: Verify Multiple Poisoned Domains

Multiple subdomains now resolve to attacker-controlled addresses.

Examples:

```text
www.example.com
abc.example.com
xyz.example.com
```

![Task 3 Result 1](images/task3-domain-verification-1.png)

![Task 3 Result 2](images/task3-domain-verification-2.png)

![Task 3 Result 3](images/task3-domain-verification-3.png)

---

# Poisoning Additional Domains

## Step 1: Review Existing Cache Entries

Previously poisoned records are verified.

![Task 4 Cache Review](images/task4-cache-review.png)

---

## Step 2: Modify Attack Logic

The script is updated to inject authority information for additional domains.

![Task 4 Script](images/task4-script-modification.png)

---

## Step 3: Execute Attack

The modified attack is launched.

![Task 4 Execution](images/task4-attack-execution.png)

---

## Step 4: Verify DNS Resolution

The forged DNS response is successfully delivered.

![Task 4 Result](images/task4-verification.png)

---

# Authority vs Additional Record Caching

## Step 1: Create Enhanced DNS Response

The spoofed response includes:

- Authority Section
- Additional Section
- Forged A Records
- Forged NS Records

![Task 5 Script](images/task5-script-modification.png)

---

## Step 2: Execute Enhanced Attack

The response packet is generated and transmitted.

![Task 5 Execution 1](images/task5-execution-1.png)

![Task 5 Execution 2](images/task5-execution-2.png)

![Task 5 Execution 3](images/task5-execution-3.png)

![Task 5 Execution 4](images/task5-execution-4.png)

---

## Step 3: Analyze DNS Cache Behavior

Results show:

- Authority records were cached successfully.
- Additional records were not stored.
- DNS servers selectively cache information based on trust rules.

![Task 5 Final Result](images/task5-cache-analysis.png)

---

# Key Findings

✅ Successfully spoofed DNS responses

✅ Redirected victim DNS requests

✅ Poisoned local DNS cache

✅ Injected malicious NS records

✅ Controlled DNS resolution for multiple domains

✅ Demonstrated authority record poisoning

✅ Analyzed DNS cache handling behavior

✅ Evaluated DNS trust relationships

---

# Security Lessons

DNS servers trust responses that appear legitimate and arrive before valid replies. Cache poisoning attacks can redirect users to malicious systems, enable phishing campaigns, and compromise network integrity.

Mitigations include:

- DNSSEC
- Source Port Randomization
- Transaction ID Randomization
- Response Validation
- Cache Monitoring
- Network Segmentation

---

# Disclaimer

This project was conducted in an isolated educational laboratory environment for cybersecurity learning and research purposes only.

Do not perform these techniques on systems or networks without explicit authorization.
