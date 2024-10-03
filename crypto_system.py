import random
import math
import logging
from functools import reduce
from operator import mul

logging.basicConfig(level=logging.INFO)

# Validator Class
class Validator:
    def __init__(self, id, stake, is_byzantine=False):
        self.id = id
        self.is_byzantine = is_byzantine
        self.stake = stake
        self.reputation = 100  # Reputation for adding/removing validators
    
    def act(self, round_num):
        if self.is_byzantine:
            # Dynamic Byzantine behavior
            if round_num % 2 == 0:
                self.stake -= 50  # Penalty for malicious actions
                return f"Validator {self.id}: Submitting conflicting transactions! Lost 50 tokens. Stake: {self.stake}"
            else:
                self.stake -= 30  # Penalty for withholding votes
                return f"Validator {self.id}: Withholding votes! Lost 30 tokens. Stake: {self.stake}"
        else:
            # Honest behavior earns rewards
            self.stake += 10
            return f"Validator {self.id}: Acting honestly. Gained 10 tokens. Stake: {self.stake}"

# Sealer threshold calculation for consensus
def calculate_sealer_threshold(total_validators):
    min_honest_validators = math.ceil((2 * total_validators) / 3)
    return min_honest_validators

# Byzantine fault simulation
def simulate_byzantine_faults(validators, round_num):
    for validator in validators:
        logging.info(validator.act(round_num))

# Voting mechanism for block validation
def vote_on_block(validators, round_num):
    votes = {"valid": 0, "invalid": 0}
    for validator in validators:
        action = validator.act(round_num)
        if "honestly" in action:
            votes["valid"] += 1
        else:
            votes["invalid"] += 1
    
    if votes["valid"] >= (2 / 3) * len(validators):
        return "Block accepted!"
    else:
        return "Block rejected!"

# Shamir's Secret Sharing (SSS)
def mod_inverse(a, p):
    return pow(a, p - 2, p)

def create_shares(secret, total_shares, threshold, prime=2087):
    coefficients = [secret] + [random.randint(0, prime - 1) for _ in range(threshold - 1)]
    
    def polynomial(x):
        return sum([coefficients[i] * pow(x, i) for i in range(threshold)]) % prime

    shares = [(x, polynomial(x)) for x in range(1, total_shares + 1)]
    return shares

def reconstruct_secret(shares, prime=2087):
    def lagrange_interpolate(x, x_s, y_s):
        total = 0
        for i in range(len(x_s)):
            xi, yi = x_s[i], y_s[i]
            numer = reduce(mul, [(x - x_s[m]) % prime for m in range(len(x_s)) if m != i], 1)
            denom = reduce(mul, [(xi - x_s[m]) % prime for m in range(len(x_s)) if m != i], 1)
            total += yi * numer * mod_inverse(denom, prime)
            total %= prime
        return total
    
    x_vals, y_vals = zip(*shares)
    return lagrange_interpolate(0, x_vals, y_vals)

# Key rotation
def rotate_keys(current_secret, total_shares, threshold):
    new_secret = random.randint(1000, 9999)  # Generate new secret
    new_shares = create_shares(new_secret, total_shares, threshold)
    logging.info(f"New Secret: {new_secret}, New Shares: {new_shares}")
    return new_shares

# Managing validator reputation and dynamic addition/removal
def manage_validators(validators):
    for validator in validators[:]:
        if validator.stake < 50:  # Remove validators with low stake
            logging.info(f"Removing Validator {validator.id} due to low stake ({validator.stake}).")
            validators.remove(validator)
        elif validator.stake > 150:  # Add new validators
            new_validator = Validator(id=len(validators) + 1, stake=100)
            validators.append(new_validator)
            logging.info(f"Adding new Validator {new_validator.id} due to high stake.")
    return validators

# Main interactive simulation
def blockchain_security_simulation():
    # User input for network configuration
    total_validators = int(input("Enter the total number of validators: "))
    byzantine_count = int(input("Enter the number of Byzantine (malicious) validators: "))
    secret = int(input("Enter the secret (private key) for Shamir's Secret Sharing: "))
    total_shares = int(input("Enter the total number of shares: "))
    threshold = int(input("Enter the threshold for shares needed to reconstruct the secret: "))

    logging.info("\n--- Step 1: Sealer Threshold for Consensus ---")
    min_honest = calculate_sealer_threshold(total_validators)
    logging.info(f"Minimum honest validators required: {min_honest}")

    # Initialize validators
    validators = [Validator(id=i+1, stake=100, is_byzantine=(i < byzantine_count)) for i in range(total_validators)]
    
    # Multiple rounds to simulate network behavior
    rounds = int(input("Enter the number of rounds to simulate: "))
    
    for round_num in range(1, rounds + 1):
        logging.info(f"\n--- Round {round_num}: Byzantine Fault Simulation and Voting ---")
        simulate_byzantine_faults(validators, round_num)
        block_result = vote_on_block(validators, round_num)
        logging.info(f"Voting result: {block_result}")
        
        logging.info("\n--- Key Management ---")
        shares = create_shares(secret, total_shares, threshold)
        logging.info(f"Generated Shares: {shares}")
        
        subset_of_shares = random.sample(shares, threshold)
        reconstructed_secret = reconstruct_secret(subset_of_shares)
        logging.info(f"Reconstructed Secret: {reconstructed_secret}")
        
        logging.info("\n--- Key Rotation and Validator Management ---")
        shares = rotate_keys(secret, total_shares, threshold)
        validators = manage_validators(validators)

# Run the interactive simulation
blockchain_security_simulation()
