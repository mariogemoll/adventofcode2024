import sys
from tqdm import tqdm

from twenty_two import load_input, price_seq

def main():
    input = load_input(sys.argv[1])

    # First, calculate prices and changes for each buyer
    seqs = []
    for seed in tqdm(input):
        seqs.append(price_seq(seed, 2000))

    # Find all sequences of 4 changes.
    change_seqs = {}
    for i, seq in enumerate(tqdm(seqs)):
        for j in range(len(seq)):
            if j < 4:
                continue
            change_seq = (seq[j-3][1], seq[j-2][1], seq[j-1][1], seq[j][1])
            # Store that buyer's price for the sequence (only the first time the sequence occurs)
            if change_seq not in change_seqs:
                change_seqs[change_seq] = {}
            prices = change_seqs[change_seq]
            if i not in prices:
                prices[i] = seq[j][0]

    num_buyers = len(seqs)
    max = 0
    best_change_seq = None
    pbar = tqdm(change_seqs.items())
    for change_seq, prices in pbar:
        sum = 0
        for i in range(num_buyers):
            if i in prices:
                sum += prices[i]
        if sum > max:
            max = sum
            best_change_seq = change_seq
            pbar.write(f'New best sequence: {best_change_seq}, yields {sum} bananas')


if __name__ == '__main__':
    main()
