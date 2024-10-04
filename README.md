# Blockchain Security with Shamir's Secret Sharing for Secure Consensus

## Overview
This project explores blockchain security mechanisms, with a focus on secure consensus using Shamir's Secret Sharing (SSS) for key management. It integrates Byzantine fault tolerance, sealer threshold calculation, and SSS to ensure a robust system capable of withstanding malicious validators.

---

## Introduction
Blockchain technology is designed to provide decentralized, secure, and transparent transactions. However, it faces significant challenges related to security, consensus, and trust, especially in environments where participants may act maliciously. One of the most critical challenges is dealing with **Byzantine Faults**, where some network nodes behave unpredictably or maliciously, potentially compromising the entire system's integrity.

This project implements a secure blockchain system that combines **Byzantine Fault Tolerance (BFT)** with **Proof of Stake (PoS)** and **Shamir's Secret Sharing (SSS)** for key management. The goal is to ensure that even if up to one-third of validators behave maliciously, the blockchain can still reach consensus and maintain security.

Byzantine nodes may disrupt the consensus process or attack the network by colluding with other malicious actors. To address this issue, BFT is integrated into the system to ensure consensus as long as two-thirds of the validators remain honest. The PoS mechanism reinforces consensus by incentivizing honest validators and discouraging malicious behavior through penalties and rewards.

**Sybil attacks**, where malicious actors create multiple fake identities to overwhelm the network, are mitigated by PoS, which makes it financially prohibitive for attackers to create numerous identities.

To enhance security, **Shamir's Secret Sharing** is used for secure key management, distributing cryptographic secrets across multiple validators. Only a subset of validators can reconstruct the key, providing protection against key compromise.

Additionally, the system employs **dynamic validator management** and **periodic key rotation** to adapt to changes in the network, maintaining long-term security and integrity.


---

## System Requirements

### Hardware Requirements
- CPU: Dual-core processor or better
- RAM: Minimum 4GB
- Storage: At least 10GB of free space

### Software Requirements
- Operating System: Windows 10, Linux, or macOS
- Python 3.8 or higher
- Required Libraries: 
  - `math`
  - `random`
  - `functools`
  - `operator`

---

## System Architecture

### Conceptual Architecture

![diagram (2)](https://github.com/user-attachments/assets/03f2b01a-a858-4cdb-bc27-0837f9ab25d1)

---

## System Implementation

The blockchain security system was designed using a modular approach, allowing the various components (validators, consensus engine, PoS, and cryptographic modules) to interact and function seamlessly. Each module is implemented as a self-contained unit, with clear inputs and outputs, ensuring that the system can be expanded or modified as needed.

## Key Components

Validators: Nodes that vote on block validity and participate in consensus.

Consensus Engine: Handles the voting process and checks for consensus using the ⅔ majority rule.

Byzantine Fault Detection: Identifies malicious or faulty behavior among validators.

Proof of Stake (PoS): Manages validator stakes, rewards for honest behavior, and penalties for malicious actions.

Shamir's Secret Sharing (SSS): Provides secure key management by distributing shares of cryptographic keys to validators.

Key Rotation: Rotates cryptographic keys periodically to improve security.

Validator Management: Adds or removes validators dynamically based on their behavior and performance.

### System Testing: Expected Output

This simulation tests critical aspects of blockchain security and performance. Below is a summary of the key components tested:

1. **Validator Behavior**  
   - Honest validators should gain tokens.  
   - Byzantine validators may lose tokens for malicious behavior (e.g., conflicting transactions or vote withholding).

2. **Voting Mechanism**  
   - Blocks are accepted if they receive a two-thirds majority of valid votes, otherwise rejected.

3. **Byzantine Fault Detection**  
   - Detect malicious actions by Byzantine validators and log penalties accurately.

4. **Stake Management**  
   - Validators’ stakes adjust based on their actions.  
   - Remove low-stake validators and add high-performing ones.

5. **Shamir's Secret Sharing**  
   - Ensure correct distribution and reconstruction of secrets among validators for cryptographic key integrity.

6. **Key Rotation**  
   - Test the periodic generation and secure distribution of new keys after specified rounds.

7. **Logging and Monitoring**  
   - Track all significant system events and actions for comprehensive monitoring.

8. **System Robustness**  
   - Ensure stable performance under load during multiple voting rounds.

9. **Final Validator Count**  
   - Confirm the final validator set reflects expected behaviors throughout the simulation.


### Example Output

--- Round 1: Voting ---
Voting result: Block accepted!

--- Byzantine Fault Simulation ---
Validator 1: Submitting conflicting transactions! Lost 50 tokens. Stake: 50
Validator 2: Submitting conflicting transactions! Lost 50 tokens. Stake: 50
Validator 3: Acting honestly. Gained 10 tokens. Stake: 110
...

--- Shamir's Secret Sharing ---
Secret shares distributed: [(1, 1823), (2, 1398), (3, 924), (4, 571), (5, 388)]

--- Managing Validators ---
Validator 2 removed due to low stake (50).

...

--- Round 3: Voting ---
Voting result: Block rejected!

--- Key Rotation ---
Key rotated. New shares distributed: [(1, 1309), (2, 893), (3, 707), (4, 415), (5, 208)]

Simulation complete! Remaining validators: [3, 5, 6, 7, 8, 9, 10]



---
## Metrics

The following metrics are used to evaluate the performance and security of the blockchain system:

1. **Throughput (Transactions Per Second - TPS)**  
   Measures how many transactions the blockchain can process per second to ensure scalability.

2. **Latency (Block Finalization Time)**  
   Reflects the average time taken for a transaction to be confirmed and added to the blockchain.

3. **Fault Tolerance**  
   Assesses the network’s resilience against Byzantine Faults, ensuring consensus despite malicious validators.

4. **Sybil Resistance**  
   Protects against Sybil attacks by making it financially prohibitive to create multiple fake identities.

5. **Key Management Security**  
   Utilizes Shamir’s Secret Sharing to ensure no single entity can compromise cryptographic keys.

6. **Validator Participation Rate**  
   Tracks the percentage of validators involved in block validation and consensus, indicating the network's health.

7. **Energy Efficiency**  
   Monitors the power consumption per transaction, ensuring the eco-friendly nature of the PoS system.

8. **Network Scalability**  
   Measures the system’s ability to maintain performance as the number of validators and transactions increases.

9. **Key Rotation Frequency**  
   Ensures periodic cryptographic key updates to maintain long-term security.

10. **Validator Churn Rate**  
    Reflects the rate at which validators join or leave the network, helping maintain system stability.

---
## Results
The system successfully demonstrates that a secure consensus mechanism can be achieved even in the presence of Byzantine faults. It also proves the effectiveness of Shamir's Secret Sharing for secure key management.

<img width="382" alt="image" src="https://github.com/user-attachments/assets/1144efa5-c6de-4459-8ac2-55285d47482e">

<img width="344" alt="image" src="https://github.com/user-attachments/assets/f5494aa5-0d24-4c74-be27-621aa876e0f8">

<img width="352" alt="image" src="https://github.com/user-attachments/assets/a25a6b20-4e59-4435-a1c6-2bbb39a580a8">

<img width="326" alt="image" src="https://github.com/user-attachments/assets/25d1bbfa-d094-494e-8c8e-ae64345020f5">

### Interpretation

#### Voting Consensus and Fault Tolerance
- **Behavior**: Honest validators approve or reject blocks based on integrity, while Byzantine validators attempt to disrupt consensus.
- **Outcome**: The system withstood up to 3 Byzantine validators while maintaining consensus. The 2/3 majority rule prevented malicious actors from compromising the blockchain.

#### Byzantine Fault Simulation
- **Behavior**: Byzantine validators submitted conflicting transactions, while honest validators maintained system integrity.
- **Outcome**: Malicious validators were identified and penalized through stake reduction. Persistent bad behavior resulted in their removal from the network.

#### Shamir’s Secret Sharing for Key Management
- **Behavior**: Cryptographic secrets were distributed as shares to validators. A threshold number of shares is required to reconstruct the secret.
- **Outcome**: The secret was successfully shared, and key rotation ensured ongoing security, even in the presence of Byzantine validators.

#### Validator Management
- **Behavior**: Honest validators were rewarded, and Byzantine validators were penalized.
- **Outcome**: The system dynamically managed validator stakes, with malicious validators removed after continuous penalties.

#### Key Rotation Security
- **Behavior**: Cryptographic keys were rotated periodically to maintain security.
- **Outcome**: Key rotation occurred after three rounds, ensuring the system remained secure without breaches.

### Observations
- **Fault Tolerance**: Capable of handling Byzantine validators up to a certain threshold without disrupting consensus.
- **Secure Key Management**: Shamir’s Secret Sharing ensured secrets were securely distributed.
- **Dynamic Validator Management**: Incentivized honest behavior and removed malicious actors.
- **Periodic Key Rotation**: Strengthened network security through ongoing key updates.



---

## Conclusion
The integration of Byzantine Fault Tolerance and Shamir’s Secret Sharing forms the foundation of a secure, decentralized consensus mechanism that is resilient to both internal and external threats. By combining these elements with dynamic validator management and periodic key rotation, the system enhances trust and security while maintaining decentralization, making it highly adaptable for real-world blockchain applications.
As blockchain technology continues to evolve, expanding on these core principles will be essential for future innovations in decentralized systems, especially as scalability and privacy concerns grow in importance.

---

## Done By
1. **21Z202** - Aaditya R
2. **21Z232** - N Arun Eshwer
3. **21Z240** - Vishal R
4. **21Z242** - Rakkulpravesh M
5. **21Z258** - Soorya Subramani
6. **21Z270** - Yadavalli Jyaswanth Sai


