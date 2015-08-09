ARM_EABI_PATH=/path/to/your/prebuilts/arm-eabi-4.7/bin

$ARM_EABI_PATH/arm-eabi-gcc -c shellcode.S -o shellcode
$ARM_EABI_PATH/arm-eabi-objcopy -O binary shellcode shellcode.bin        
#$ARM_EABI_PATH/arm-eabi-objdump -D -b binary -m arm -EL -M force-thumb shellcode.bin
$ARM_EABI_PATH/arm-eabi-objdump -d shellcode
