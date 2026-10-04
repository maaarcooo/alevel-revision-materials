# 1.3.3 Networks

## Networks and Protocols

### Characteristics of a Network

A **network** is a set of two or more interconnected devices (computers, printers, servers) with the ability to transmit data between each other. The main purposes of a network are to enable **data** and **resource** sharing, **communication**, and **collaboration**.

There are two main types of network:

| Feature | LAN (Local Area Network) | WAN (Wide Area Network) |
|---|---|---|
| **Geographic area** | Small area or single site (e.g. a school) | Large geographical area (e.g. a country) |
| **Hardware ownership** | Typically all owned by a single entity | Uses third-party infrastructure (ISPs, telecoms companies) |
| **Security** | More secure, as connections are owned by the organisation | More vulnerable, as data travels across public networks |
| **Cost** | Lower cost for infrastructure | More expensive due to leased lines or ISP costs |
| **Speed** | Generally faster | Typically slower due to greater transmission distances |

A **LAN** is built using hubs and/or switches to connect devices. A hub or switch is commonly connected to a **router**, which allows the LAN to connect to other networks such as the Internet.

**LAN advantages:** centralised management of updates, backups and software installations; security through firewalls and antivirus; file sharing and collaboration with shared peripherals.

**LAN disadvantages:** hardware failure can disrupt the entire network; networks are more prone to attacks than standalone machines; access to data and peripherals can be slow under heavy traffic; maintenance, upgrades and backups can be costly.

A **WAN** connects multiple LANs over a large geographical area, typically using third-party connections such as leased lines, fibre, or satellite links provided by ISPs or telecommunications companies. The largest WAN is the **Internet**, which is made up of a series of smaller networks.

**WAN advantages:** enables communication and data sharing between offices in different locations; allows access to central servers and shared databases from anywhere.

**WAN disadvantages:** typically slower than LANs; more expensive to set up and maintain; more vulnerable to security risks.

### Protocols and Standards

A **protocol** is a set of rules defining how two computers communicate with each other. Protocols are standardised so that all devices have a designated method of communicating regardless of manufacturer.

A **standard** is a set of guidelines or frameworks governing how a task should be performed or how a product should function. Standards ensure **compatibility**, **interoperability**, and **consistency** across different devices and software. They support network expansion and integration of new technologies without disrupting existing operations, and foster innovation by providing a common ground for all manufacturers and developers.

### Common Internet Protocols

| Protocol | Full Name | Purpose |
|---|---|---|
| **HTTP** | HyperText Transfer Protocol | Primary protocol for transferring web content (text, images, video). Works as a request-response protocol in a client-server model. |
| **HTTPS** | HTTP Secure | Encrypted version of HTTP for secure transactions (e.g. online banking, shopping). |
| **FTP** | File Transfer Protocol | Used for transferring files between hosts over a network. Provides authentication and can manage file directories. |
| **SMTP** | Simple Mail Transfer Protocol | Standard for sending email messages between servers, and from a client to a server for forwarding. |
| **POP3** | Post Office Protocol (version 3) | Mailing protocol used for email access (downloads mail to local device). |
| **IMAP** | Internet Message Access Protocol | Mailing protocol for email access (keeps mail on server, synchronised across devices). |
| **TCP** | Transmission Control Protocol | Part of the Internet Protocol Suite. Provides reliable, ordered, and error-checked delivery of a stream of packets. |
| **UDP** | User Datagram Protocol | Simpler connectionless protocol. Does not guarantee delivery or order, making it faster (used for streaming, gaming). |
| **IP** | Internet Protocol | Addresses and routes packets of data from source to destination device. |
| **ARP** | Address Resolution Protocol | Translates IP addresses into MAC (Media Access Control) addresses, ensuring packets reach the correct device on a local network. |

---

## The Internet Structure

The **Internet** is a **network of networks** which allows computers on opposite sides of the globe to communicate. Continents are connected using large international **backbone cables**, many of which pass **underwater** linking continents to one another.

### The TCP/IP Stack and Protocol Layering

**TCP/IP** stands for **Transmission Control Protocol / Internet Protocol**. It is a suite (stack) of networking protocols that work together, passing packets during communication. The TCP/IP model splits protocols into **four layers**, each performing specific functions.

#### Why Use Layering?

**Protocol layering** is the division of network protocols into layers, each handling different aspects of communication. Benefits include:

- **Modularity:** breaking the complex process of networking into manageable layers makes it easier to design, implement, and troubleshoot networks.
- **Interoperability:** different technologies can work together seamlessly. An application can send data without knowing the details of the underlying network structure.
- **Ease of updates:** changes can be made to one layer without affecting others, so protocols at the network layer can be altered independently of application layer protocols.
- **Specialisation:** each layer can be optimised for its specific functions without worrying about the specifics of other layers.

#### The Four Layers

**Application Layer** (top of the stack)
- The layer where the communication process begins, interacting directly with software applications (web browsers, email clients).
- Specifies which protocol is needed to relate to the application being sent (e.g. a browser selects HTTP; an email client selects SMTP or POP3; a file transfer uses FTP).
- Prepares data for transmission by converting it into a format that can be sent over the network (known as **encapsulation**).

**Transport Layer**
- Uses **TCP** to establish an **end-to-end connection** between the source and recipient computer.
- Splits data into **packets** and labels each with: its **packet number**, the **total number of packets** the data was split into, and the **port number** being used for communication.
- If any packets are lost during transmission, the transport layer **requests retransmission** of those lost packets.

**Internet Layer** (also called **Network Layer**)
- Adds the **source and destination IP addresses** to each packet.
- The combination of an IP address and a port number is called a **socket address**.
- **Routers** operate at this layer, using IP addresses to forward packets.
- Sockets specify which device the packets must be sent to and which application on that device should receive them.
- Responsible for **routing** each packet across the network.

**Link Layer** (also called **Network Interface Layer**)
- Handles the connection between network devices.
- Adds the **MAC address** identifying the **Network Interface Cards (NICs)** of the source and destination computers.
- For devices on the **same network**, the destination MAC address is the address of the recipient computer. For devices on **different networks**, the destination MAC address is the MAC address of the **router**.
- Translates digital packets into an **electrical, optical, or wireless signal** for transmission over the physical network. At the receiving end, the link layer translates the signal back into digital packets.

#### Sending and Receiving Process

On the **sender's** side, data passes **top to bottom** through the stack: Application → Transport → Internet → Link. Each layer adds its own header (encapsulation).

On the **recipient's** side, the layers are processed **bottom to top**. The link layer removes the MAC address, the internet layer removes the IP addresses, the transport layer removes the port number and reassembles packets in order, and the application layer presents the data to the recipient in the requested format.

At each layer, specific tasks are performed to prepare data for transmission. The process is reversed at the receiving end, with each layer removing its specific header and performing its tasks to return data to a usable form.

### IP Addresses

An **IP address** is a unique identifier for a device on a network, used to deliver packets to the correct destination. Two versions are in use:
- **IPv4:** e.g. `104.22.74.202` (32-bit, four octets in dotted decimal)
- **IPv6:** e.g. `0000:0000:0000:0000:ffff:6816:4aca` (128-bit, eight groups of four hex digits)

### Domain Name System (DNS)

The **Domain Name System (DNS)** is the system used to name and organise internet resources. It functions as a **directory of domain names**, translating human-readable domain names into the numeric IP addresses that computers use.

DNS is a **hierarchy** in which each smaller domain is separated from the larger domain by a full stop. For example, in `leeds.gov.uk`: `uk` is the **TLD (Top Level Domain)**, `gov` is the **2LD (2nd Level Domain)**, and `leeds` is the subdomain.

Domain names are much easier to remember than IP addresses, which is why they are used to link to servers across the world. Without DNS, users would have to remember the IP address of every site they want to visit.

When a domain is newly registered or a server changes its IP address, the DNS record needs to be updated in a process known as **DNS propagation**.

#### Components of DNS

- **DNS Resolver:** the first stop in the lookup process, usually provided by the user's ISP or a third-party service (e.g. Google DNS, OpenDNS). Checks its cache first.
- **Root Servers:** the resolver asks a DNS root server to find the appropriate TLD server (e.g. `.com`, `.org`, `.edu`).
- **TLD Servers:** stores information about domains within that top-level domain. Directs the resolver to the authoritative DNS server.
- **Authoritative DNS Servers:** holds the actual IP address for the domain. Responds to the resolver with the IP.

#### What Happens When You Type a URL into a Web Browser

1. The user enters the URL into the web browser.
2. The computer checks its **local cache** for the IP address from a previous request.
3. If not cached, the browser sends a query to a **DNS resolver** (usually hosted by the ISP).
4. The DNS resolver checks its own cache. If the address is not found, it sends the request to a **DNS root server**.
5. The root server directs the resolver to the appropriate **TLD server** based on the URL's extension.
6. The TLD server provides the resolver with the address of the domain's **authoritative DNS server**.
7. The resolver queries the authoritative server, which responds with the **IP address**.
8. The browser sends an **HTTP or HTTPS request** to the IP address.
9. The server at that IP processes the request and sends back the web page data (HTML, CSS, JavaScript).
10. The browser **renders** the received data into the visible web page.

---

## Network Communication

### Data Packets

**Packets** are segments of data. Each packet is composed of three parts:

**Header** contains:
- **Source and destination IP addresses** allowing the packet to be delivered correctly and enabling the recipient to trace its origin.
- **Protocol** being used, so the recipient computer knows how to interpret the packet.
- **Sequence number** (order of the packets), so packets can be reconstructed in the correct order at the destination.
- **Time To Live (TTL) / Hop Limit**, telling the packet when to expire so it does not travel forever.
- **Packet length**, indicating the size of the packet.
- **Checksum**, a value used for error-checking.

**Payload** contains the actual raw data to be transmitted.

**Trailer (Footer)** contains a **checksum** or **cyclic redundancy check (CRC)**, a code used to detect whether errors have occurred during transmission.

### Packet Switching

**Packet switching** is a method of communication in which data is broken down into smaller packets, sent independently across the network via the **most efficient route** (which may vary for each packet), and **reassembled** at the destination.

| Benefits | Drawbacks |
|---|---|
| Efficient use of network resources as packets can follow different paths, using more of the available bandwidth | Not ideal for real-time services (video calling, VoIP) which require a steady data stream without delays |
| More reliable: if a single packet fails, only that packet needs to be resent, not the entire data stream | Packets can arrive out of order, requiring reassembly and error-checking |
| Multiple routes can be used, so if one path breaks, another can be used | Must wait for all packets to arrive before data can be fully received |
| Packets can be transferred over very large networks for global communication | Potential for network congestion leading to packet loss |
| Lower cost due to shared network resources | Time is spent deconstructing and reconstructing data packets |

### Circuit Switching

**Circuit switching** is a method of communication where a **dedicated, direct link** is created between two devices. This link is maintained for the **duration of the entire conversation**. Both devices must transfer and receive data at the **same rate**.

| Benefits | Drawbacks |
|---|---|
| Data arrives in logical order, resulting in quicker reconstruction | Bandwidth is wasted during periods when no data is being sent |
| Enables real-time communication (e.g. phone calls) with no delay in speech, constant and steady transmission rate | Devices must transfer and receive data at the same rate |
| No delays as a dedicated path is established | Using switches means electrical interference may be produced, which can corrupt or destroy data |
| | Ties up sections of the network which cannot be used by others until transmission is completed |
| | More costly due to dedicated line requirement |
| | Less flexible and scalable as adding new devices can be complex |

**Use cases:** packet switching is best for data that can tolerate some delay (emails, web pages). Circuit switching is ideal for real-time services requiring low latency (voice calls, video conferencing).

**Exam tip:** avoid talking about the "speed" of data transmission when comparing packet and circuit switching. This will not earn marks. Instead, discuss higher **bit rates**, **bandwidth** (bits per second), or the **efficiency** of the transmission.

---

## Network Security and Threats

### Common Network Threats

**Hackers** are individuals or groups who exploit system vulnerabilities to gain **unauthorised access** to data. Aims vary from personal gain to activism or cyber espionage.

**Viruses** are malicious software programs that attach to legitimate programs or files, **replicate** themselves to spread to other programs or files, and can cause damage including deleting data or damaging hardware.

**Malware** is malicious software designed to harm or gain unauthorised access to a system or network. Types include:

| Type | Description |
|---|---|
| **Worm** | Similar to a virus but is a standalone program that can spread and replicate over networks without attaching to other files. Can consume storage space or bandwidth. |
| **Trojan horse** | Disguises itself as a legitimate program or file, but once installed it can delete data or damage hardware. |
| **Spyware** | Records all key presses and transmits them to a third party. |
| **Adware** | Displays unwanted advertisements without consent. Some may contain spyware or link to viruses when clicked. |
| **Ransomware** | Encrypts the user's files and demands a ransom payment to decrypt them. Can cause data loss, financial damage, and disrupt business operations. |

**Denial of Service (DoS)** attack: a computer floods a server with large numbers of requests simultaneously, which the server cannot respond to, causing it to crash or become unavailable to users.

**Distributed Denial of Service (DDoS)** attack: similar to DoS but uses **multiple computers as bots** to send requests to the server.

**SQL injection:** an attack where **malicious SQL statements** are inserted into an entry field on a website for execution, potentially exposing a company's database to hackers.

**Phishing:** attempting to acquire sensitive information by masquerading as a trustworthy entity. The user receives an email that looks legitimate containing a link to a **fake website** where they are encouraged to enter personal details.

**Pharming:** a cyber attack that redirects a website's traffic to a **bogus site**. Malware is downloaded without the user's knowledge, redirecting them to a fake website where they enter personal details.

**Social engineering:** manipulating individuals to gain access to confidential information or perform an action benefiting the attacker. Techniques include posing as trusted personnel (co-worker, IT support, law enforcement), enticing with desirable items, leaving labelled USB drives in public places (baiting), or posing as bank representatives.

### Firewalls

A **firewall** is a device designed to **prevent unauthorised access** to a network. It consists of two **network interface cards (NICs)** between the user and the Internet. The firewall passes packets between these two NICs and compares them against a set of rules defined by the firewall software. These preconfigured rules are called **packet filters**.

**Packet filtering / static filtering** limits network access in accordance with administrator rules and policies. It works by examining the **source IP**, **destination IP**, the **protocols** being used, and the **ports** being requested.

When access is denied by a firewall, two outcomes are possible:
- **Rejected:** the packet is stopped and an alert is sent to the sender to notify them of the error.
- **Dropped:** the packet is silently discarded with no notification to the sender.

### Proxies

A **proxy server** acts as an **intermediary**, collecting and sending data on behalf of the user. Benefits include:
- The **privacy** of the user is protected and they remain **anonymous**.
- The proxy can **cache** frequently used website data, making pages faster to load.
- Proxies can **reduce overall web traffic**.
- Administrators can use proxies to **prevent access** to sensitive or irrelevant information at work or school.

### Encryption

**Encryption** is a way of keeping data secure when transmitting it over the Internet. Encryption makes data **unreadable** if it is intercepted. Data is encrypted and decrypted using a set of **keys**.

*(Beyond source: encryption is covered in more detail in specification section 1.3.1 Compression, Encryption and Hashing.)*

### Network Security Measures

- **Firewalls:** monitor and control incoming/outgoing traffic based on predetermined security rules.
- **Secure passwords:** strong, complex, and unique passwords protect against unauthorised access.
- **Anti-virus software:** detects, neutralises, or removes malicious software (viruses, worms, Trojans).
- **Anti-spyware software:** detects and removes spyware and other malware.
- **Two-factor authentication (2FA):** requires two forms of identification, usually a code sent to the user's phone or email as well as their password.
- **Regular software updates:** ensures all systems have the latest security patches.
- **Employee training:** instils a culture of security consciousness within the organisation.
- **Strong security policy:** e.g. insisting on regular password changes.

---

## Network Hardware

| Hardware | Description |
|---|---|
| **Network Interface Card (NIC)** | Hardware component (now usually built into the motherboard) that enables a device to connect to a network. Has a built-in Ethernet port. Each NIC has a unique **MAC address** (a **48-bit** value coded during manufacturing, usually written as a **twelve-digit hexadecimal** number). Its primary function is to send and receive data packets between the device and the network. |
| **Switch** | Connects devices on a network and directs the flow of data. Unlike a hub, a switch only sends data to the **intended device** by examining the destination MAC address and looking it up in a **lookup table** (mapping ports to MAC addresses). Commonly used in **star topology** networks. More efficient and more secure than a hub. |
| **Hub** | Connects multiple devices in a network but is a "dumb" device that **broadcasts** all received data to every connected device. Cheaper than switches but creates unnecessary traffic and poses security concerns, as every device receives every packet. |
| **Wireless Access Point (WAP)** | Allows devices to connect to a network **wirelessly**. Acts as a central transmitter and receiver of Wi-Fi signals. Connects to the wired network via Ethernet or fibre optic from a fixed location and projects a Wi-Fi signal. Often combined with a router. Used in **mesh networks**. |
| **Router** | Connects **two or more networks** together (e.g. a home LAN to the Internet). Analyses data packet headers, reads the destination IP address, looks it up in a **routing table**, and forwards the packet to the appropriate network. Each pass from router to router is called a **hop**. Has a public IP address assigned by an ISP. Can also assign IP addresses to devices within the LAN and filter incoming traffic. |
| **Gateway** | Used when protocols are **not the same** between networks. **Translates** protocols so networks can communicate by removing the header from packets and re-adding data using the new protocol. |
| **Modem** | **Mod**ulator-**dem**odulator. Converts digital signals into analogue for transmission over telephone or cable lines, and vice versa for receiving data. Used for DSL, cable, or dial-up connections. |
| **Cables** | Physical paths for data. **Ethernet cables** (Cat5, Cat5e, Cat6) are used for wired networks at various speeds (10 Mbps to 10 Gbps). **Fibre-optic cables** use light to transmit data, offering much higher speed and larger data capacity. |

**How a switch works:** when a switch receives a data packet, it examines the destination MAC address and looks it up in its lookup table. The table maps each port to the MAC address of the device connected to that port. Once the matching MAC address is found, the switch forwards the packet only to the corresponding port.

**How a router works:**
1. The router receives incoming data packets and analyses the header to determine the destination IP address.
2. It looks up the IP address in a **routing table** of known networks to determine the next network the packet should be sent to.
3. The router forwards the packet to the appropriate network or device.

This process repeats at every router the packet passes through until it reaches its destination.

---

## Client-Server and Peer-to-Peer

### Client-Server

A **client-server** network consists of terminals known as **clients** connected to a **server**. The server is a **powerful, central computer** that holds all of the important information and resources and has **greater processing power** than the clients. Clients can request to use the server's resources and services.

| Advantages | Disadvantages |
|---|---|
| More **secure** as data is stored in one central location | Relatively **expensive** to set up |
| **Central backups** are carried out, so no need for individual backups | Single point of failure: if the server fails, all client functionality is affected |
| Data and resources can be **shared** between clients | **Trained staff** are required to maintain the server |
| Easier **central management** | Can be expensive to maintain (dedicated teams) |
| **Scalable:** new clients can be added easily | |
| Higher reliability as resources are managed centrally | |

**Use case:** larger organisations where centralised control, reliability, and security are paramount.

### Peer-to-Peer

A **peer-to-peer (P2P)** network is one in which computers are connected to each other so they can share files. Each device has **equal status** and effectively acts as both a **server and a client**, as it can both provide and request resources. There is **no central server**. Each user is responsible for the security, backup, and maintenance of their own machine. Data is often spread around the network.

P2P networks have been associated with **piracy**, since it is almost impossible to trace the origin of files shared across such networks.

| Advantages | Disadvantages |
|---|---|
| **Cheaper** to set up | Impossible to trace the origin of files |
| Allows users to **share resources** directly without a central server | Backups must be performed **separately** on each machine |
| **Easy to maintain** | **Poorer security** due to lack of central control |
| **Not dependent** on a central server | May be **difficult to locate resources** |
| **Specialist staff are not required** | Not suitable for large networks (performance issues) |

**Use cases:** home networks, small businesses, or specific applications like file sharing.
