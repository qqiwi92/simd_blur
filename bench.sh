#!/bin/bash

scripts=("no_optimization.py" "flatten_optimization.py" "numpy_optimization.py" "numpy_no_cycles_optimization.py")
CSV_FILE="benchmark_stats.csv"

echo "script,run,elapsed_time,cpu_time,page_faults" > "$CSV_FILE"

for script in "${scripts[@]}"; do
    if [ -f "$script" ]; then
        echo "Testing $script..."
        for i in {1..3}; do
            output=$(python3 "$script")
            
            time_res=$(echo "$output" | grep "Чистое время:" | awk '{print $3}')
            cpu_res=$(echo "$output" | grep "CPU Time:" | awk '{print $3}')
            pf_res=$(echo "$output" | grep "Page Faults:" | awk '{print $3}')

            echo "$script,$i,$time_res,$cpu_res,$pf_res" >> "$CSV_FILE"
            echo "  Run $i: $time_res sec"
        done
    else
        echo "File $script not found, skipping."
    fi
done

