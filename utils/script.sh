#!/bin/bash

QUERY_FILE="POGZ.fasta"
PROTEOMES_DIR="/mnt/storage/project_2023/proteomes"
current_dir=$(pwd)

cd "$PROTEOMES_DIR"

for file in *.faa; do
  filename=$(basename "$file" .faa)
  blastp -query "$current_dir/$QUERY_FILE" -db "$PROTEOMES_DIR/$file" -out "$current_dir/$QUERY_FILE.$filename.blast" -outfmt 7
done
