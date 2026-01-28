dna_sequence = "ATGCGTACGTTAGC"

gc_count = dna_sequence.count("G") + dna_sequence.count("C")
gc_content = (gc_count / len(dna_sequence)) * 100

print("DNA sequence:", dna_sequence)
print("GC content:", gc_content, "%")
