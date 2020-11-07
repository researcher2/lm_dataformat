from lm_dataformat import Reader
import tqdm
import os

def main():
    file_path = "/home/bmk/The-Pile/components/commoncrawl/pile_cc_filtered_deduped.jsonl.zst"
    reader = Reader(file_path)

    progress = tqdm.tqdm(total=os.path.getsize(file_path), dynamic_ncols=True, unit_scale=1, unit="byte")
    previous_file_position = 0
    for doc, meta in reader._stream_data(get_meta=True):
        current_file_position = reader.fh.tell()
        progress.update(current_file_position - previous_file_position)
        previous_file_position = current_file_position

    progress.close()
    
if __name__ == '__main__':
    main()