dna_sequence = input("Enter a DNA sequence: ").upper()

valid_bases = {"A", "T", "G", "C"}

if not set(dna_sequence).issubset(valid_bases):
    print("Invalid DNA sequence. Please use only A, T, G, C.")
else:
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    gc_content = (gc_count / len(dna_sequence)) * 100

    print("DNA sequence:", dna_sequence)
    print("GC content:", gc_content, "%")

