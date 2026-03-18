#!/bin/bash

if [ -z "$1" ]; then
    echo "Использование: ./bench.sh имя_файла.py"
    exit 1
fi

SCRIPT_NAME=$1
CSV_FILE="benchmark_stats.csv"

if [ ! -f "$CSV_FILE" ]; then
    echo "filename,run,time_seconds" > "$CSV_FILE"
fi

if [[ "$SCRIPT_NAME" == *.py ]]; then
    CMD="python3 $SCRIPT_NAME"
elif [[ "$SCRIPT_NAME" == *.cpp ]]; then
    g++ -O3 "$SCRIPT_NAME" -o my_prog
    CMD="./my_prog"
else
    chmod +x "$SCRIPT_NAME"
    CMD="./$SCRIPT_NAME"
fi

echo "--- Тестирование: $SCRIPT_NAME ---"

for i in {1..10}
do
    echo -n "Запуск #$i... "

    TIME_RESULT=$(/usr/bin/time -f "%e" $CMD 2>&1 >/dev/null)

    if [[ $? -ne 0 ]]; then
        echo "ОШИБКА выполнения:"
        echo "$TIME_RESULT"
        exit 1
    fi

    echo "$SCRIPT_NAME,$i,$TIME_RESULT" >> "$CSV_FILE"
    echo "Ок ($TIME_RESULT сек)"
done

echo "Данные добавлены в $CSV_FILE"
