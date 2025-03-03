instrument_codes = input("List of instrument codes (in array format [...]):")
start_time = input("Start timestamp:")
end_time = input("End timestamp:")
fields = input("List of static and dynamic fields (in array format [...]):")
fields = fields.strip("[]").split(",")

file = open("data.txt", "r")
static_file = open("StaticFields.Txt", "r")
dynamic_file = open("DynamicFields.Txt", "r")
lines = file.readlines()

filtered_lines = []

static_input_ids = []
dynamic_input_ids = []
for field in fields:
    if field[0] == "S":
        static_input_ids.append(int(field[1:]))
    elif field[0] == "D":
        dynamic_input_ids.append(int(field[1:]))

print(static_input_ids)
print(dynamic_input_ids)

static_descriptions = []
dynamic_descriptions = []
for static_field_file in static_file:
    static_field, static_description = static_field_file.strip().split('\t')
    for static_input_id in static_input_ids:
        if static_input_id == int(static_field[1:]):
            static_descriptions.append(static_description)
for dynamic_field_file in dynamic_file:
    dynamic_field, dynamic_description = dynamic_field_file.strip().split('\t')
    for dynamic_input_id in dynamic_input_ids:
        if dynamic_input_id == int(dynamic_field[1:]):
            dynamic_descriptions.append(dynamic_description)
print(static_descriptions)
print(dynamic_descriptions)

line_number_data = 0
static_line_numbers = []
dynamic_line_numbers = []
for line in lines:
    line = line.strip()
    parts = line.strip().split("|")

    instrument_code = parts[3]
    timestamp_string = parts[1]
    message_type = parts[2]

    time_parts = timestamp_string.split(":")
    timestamp = f"{time_parts[0]}:{time_parts[1]}:{time_parts[2]}.{time_parts[3]}"

    if instrument_code in instrument_codes:
        if start_time <= timestamp <= end_time:
            if message_type == "S":
                static_line_numbers.append(line_number_data)
            elif message_type == "Q" or message_type == "C" or message_type == "T" or message_type == "R":
                dynamic_line_numbers.append(line_number_data)
    line_number_data = line_number_data + 1

print(static_line_numbers)
print(dynamic_line_numbers)

static_data_field_ids = []
dynamic_data_field_ids = []
n = 0
for line in lines:
    line = line.strip()
    parts = line.strip().split("|")

    instrument_code = parts[3]
    timestamp_string = parts[1]
    message_type = parts[2]
    static_line_field_ids = []
    dynamic_line_field_ids = []
    if n in static_line_numbers:
        for part in parts:
            if parts.index(part) > 6:
                static_data_field, static_data_field_value = part.strip().split("=")
                static_data_field_id = int(static_data_field[1:])
                static_line_field_ids.append(static_data_field_id)
    if n in dynamic_line_numbers:
        for part in parts:
            if parts.index(part) > 6:
                dynamic_data_field, dynamic_data_field_value = part.strip().split("=")
                dynamic_data_field_id = int(dynamic_data_field[1:])
                dynamic_line_field_ids.append(dynamic_data_field_id)
    static_data_field_ids.append(static_line_field_ids)
    dynamic_data_field_ids.append(dynamic_line_field_ids)
    n = n+1


print(static_data_field_ids)
print(dynamic_data_field_ids)
