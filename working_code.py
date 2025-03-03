instrument_codes = input("List of instrument codes (in array format [...]):")
start_time = input("Start timestamp:")
end_time = input("End timestamp:")
fields = input("List of static and dynamic fields (in array format [...]):")

file = open("data.txt", "r")
static_file = open("StaticFields.Txt", "r")
dynamic_file = open("DynamicFields.Txt", "r")
lines = file.readlines()

filtered_data = []

for line in lines:
    line = line.strip()
    parts = line.strip().split("|")

    instrument_code = parts[3]
    timestamp_string = parts[1]
    field = parts[2]

    time_parts = timestamp_string.split(":")
    timestamp = f"{time_parts[0]}:{time_parts[1]}:{time_parts[2]}.{time_parts[3]}"
    if instrument_code in instrument_codes:
        if start_time <= timestamp <= end_time:
            filtered_data.append(line)

print(filtered_data)