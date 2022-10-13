def read_reads(input_fastq: str) -> list:
    with open(input_fastq) as fastq_file:
        reads_fast = fastq_file.readlines()

        all_reads = []
        seq = 0
        for read in reads_fast:
            seq += 1
            if seq % 2 == 0 and seq % 4 != 0:
                all_reads.append(read)
        fastq_file.close()

        return all_reads


def gc_read(reads: list, borders=(0, 100)) -> list:
    reads_count = []
    for seq in reads:
        gc_count = 0
        for nucl in seq:
            if nucl == 'G' or nucl == 'C':
                gc_count += 1
        gc_content = (gc_count / len(seq)) * 100
        reads_count.append(gc_content)

    filtered_rd = []
    for count in reads_count:
        if type(borders) is int:
            high_bord = borders
            filtered_rd.append(count < high_bord)

        if type(borders) is tuple:
            low_bord = borders[0]
            high_bord = borders[1]
            filtered_rd.append(low_bord < count < high_bord)

    return filtered_rd


def length(reads: list, borders=(0, 2 ** 32)) -> list:
    read_length = []
    for single_read in reads:
        if type(borders) is int:
            read_length.append(len(single_read) < borders)

        if type(borders) is tuple:
            low_bord = borders[0]
            high_bord = borders[1]
            read_length.append(low_bord < len(single_read) < high_bord)

    return read_length


def read_phred(input_fastq: str) -> list:
    with open(input_fastq) as fastq_file:
        quality_fast = fastq_file.readlines()

        phreds = []
        quality_seq = 0
        for read in quality_fast:
            quality_seq += 1
            if quality_seq % 4 == 0:
                phreds.append(read)
        fastq_file.close()

        return phreds


def mean_quality(phreads: list, border=0) -> list:
    reads_qual = []
    filtered_phred = []
    for string in phreads:
        ord_find = 0
        for nucl in string:
            ord_find += ord(nucl) - 33
        quality_mean = ord_find / len(phreads)
        reads_qual.append(quality_mean)

    for phred in reads_qual:
        filtered_phred.append(phred > border)

    return filtered_phred


def read_the_whole(reads: list, phreads: list, gc_bounds=None, length_bounds=None, quality_threshold=None) -> list:
    gc_result = gc_read(reads, gc_bounds)
    length_result = length(reads, length_bounds)
    quality_result = mean_quality(phreads, quality_threshold)
    
    i = 0
    gc_length_filtered = []
    while i in range(len(reads)):
        a = gc_result[i] and length_result[i]
        gc_length_filtered.append(a)
        i += 1

    z = 0
    all_filtered = []
    while z in range(len(phreads)):
        b = gc_length_filtered[z] and quality_result[z]
        all_filtered.append(b)
        z += 1

    return all_filtered


def main(input_fastq: str, output_file_prefix: str, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0,
         save_filtered=False):
    nucleotide_reads = read_reads(input_fastq)
    quality_sequence = read_phred(input_fastq)
    result = read_the_whole(nucleotide_reads, quality_sequence, gc_bounds, length_bounds, quality_threshold)

    return result
