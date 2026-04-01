#!/bin/bash

cleanup() {
    echo -e "\n[!] cleaning up mounts..."
    sudo umount -l ~/riscv_vm/root/simd_blur 2>/dev/null
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

sudo sysctl -w kernel.perf_event_paranoid=-1
sudo sysctl -w kernel.kptr_restrict=0

sudo mount --bind ~/Projects/python/simd_blur ~/riscv_vm/root/simd_blur

echo "entering chroot"
sudo chroot ~/riscv_vm /bin/bash --login -c "cd /root/simd_blur && exec /bin/bash -i"