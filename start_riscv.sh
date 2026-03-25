#!/bin/bash

cleanup() {
    echo "cleaning"
    sudo umount -l ~/riscv_vm/dev/pts 2>/dev/null
    sudo umount -l ~/riscv_vm/dev 2>/dev/null
    sudo umount -l ~/riscv_vm/sys 2>/dev/null
    sudo umount -l ~/riscv_vm/proc 2>/dev/null
    echo "done"
}

trap cleanup EXIT INT TERM

sudo mount --bind /dev ~/riscv_vm/dev
sudo mount --bind /sys ~/riscv_vm/sys
sudo mount --bind /proc ~/riscv_vm/proc
sudo mount --bind /dev/pts ~/riscv_vm/dev/pts

echo "entering chroot"
sudo chroot ~/riscv_vm /bin/bash