from tqdm import tqdm

def load_input(filename):
    input = []
    for line in open(filename):
        parts = line.split(': ')
        assert len(parts) == 2
        result = int(parts[0])
        vals = [int(val) for val in parts[1].split(' ')]
        input.append((result, vals))
    return input

def find_combination(target, vals, with_concat):
    candidates = [(vals[0], [vals[0]])]
    vals_to_go = vals[1:]
    while len(vals_to_go) > 0:
        new_candidates = []
        next_val = vals_to_go[0]
        for result_so_far, term_so_far in candidates:
            addition_result = result_so_far + next_val
            if addition_result == target:
                return True, term_so_far + ['+', next_val]
            
            multiplication_result = result_so_far * vals_to_go[0]
            if multiplication_result == target:
                return True, term_so_far + ['*', next_val]
            
            if with_concat:
                concat_result = int(str(result_so_far) + str(next_val))
                if concat_result == target:
                    return True, term_so_far + ['||', next_val]
        
            if addition_result < target:
                add_term = term_so_far.copy()    
                add_term.append('+')
                add_term.append(next_val)
                new_candidates.append((addition_result, add_term))
            
            if multiplication_result < target:
                mult_term = term_so_far.copy()
                mult_term.append('*')
                mult_term.append(next_val)
                new_candidates.append((multiplication_result, mult_term))
            
            if with_concat and concat_result < target:
                concat_term = term_so_far.copy()
                concat_term.append('||')
                concat_term.append(next_val)
                new_candidates.append((concat_result, concat_term))

        candidates = new_candidates
        vals_to_go = vals_to_go[1:]
    return False, None

def main():
    input = load_input('test_input')
    found = 0
    total = 0
    pbar = tqdm(input)
    for result, vals in pbar:
        found, term = find_combination(result, vals)
        if found:
            total += result
            pbar.set_postfix({'found': found, 'total': total})
    print(f'Total: {total}')
            
if __name__ == '__main__':
    main()
