voltage = input("Enter Voltage (5v if empty): ")
if voltage == "":
    voltage = 5.0
else:
    voltage = float(voltage)

pulldown = input("Enter pulldown resistance in Ohms (10kOhm if empty): ")
if pulldown == "":
    pulldown = 10000.0
else:
    pulldown = float(pulldown)

resistors = []
count = 0

print()

while True:
    print(f"Resistor number {count}: ")
    resistance = input("Enter resistance in Ohms (empty to proceed): ")
    if resistance == "":
        if len(resistors) < 2:
            print("minimum amount of resistors is 2")
            continue
        else:
            break
    else:
        resistors.append(float(resistance))
        count += 1

print()
print()
print("Pairs' resistance:")

pair_resistance = []
pair_names = []
# pair's resistance
for first in range(len(resistors)):
    for second in range(first + 1, len(resistors)):
        # 1/Rt = 1/R1+1/R2
        # Rt = (1/R1+1/R2)^-1
        pair = (1/resistors[first] + 1/resistors[second]) ** -1
        pair_names.append(f"{resistors[first]} Ohm || {resistors[second]} Ohm ")
        print(f"{resistors[first]} Ohm || {resistors[second]} Ohm = {pair} Ohm")
        pair_resistance.append(pair)

print()
print()
print("Resistors: ")

# Voltage drop and current for individual resistors
for resistor in resistors:
    current = voltage / (resistor + pulldown)
    voltage_drop = current * resistor
    voltage_read = current * pulldown
    print(
        f"{resistor: .2f} Ohm resistor will have current of {current: .6f}A, "
        f"voltage drop of {voltage_drop: .3f}v "
        f"and voltmeter will read {voltage_read: .3f}v")

print()
print()
print("Pairs:")

#Voltage drop and current for pairs
for count in range(len(pair_resistance)):
    resistor = pair_resistance[count]
    name = pair_names[count]
    current = voltage / (resistor + pulldown)
    voltage_drop = current * resistor
    voltage_read = current * pulldown
    print(
        f"{name}pair will have current of {current: .6f}A, "
        f"voltage drop of {voltage_drop: .3f}v "
        f"and voltmeter will read {voltage_read: .3f}v")
