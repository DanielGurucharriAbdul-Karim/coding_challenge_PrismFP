instrument_codes = input("List of instrument codes (in array format [...]):")
start_time = input("Start timestamp:")
end_time = input("End timestamp:")
fields = input("List of static and dynamic fields (in array format [...]):")

file = open("data.txt", "r")
static_file = open("StaticFields.Txt", "r")
dynamic_file = open("DynamicFields.Txt", "r")
lines = file.readlines()

##############################################################################
for line in static_file:
    field, description = line.strip().split('\t')
    field_type = field[0]
    field_id = field[1:]

for line in dynamic_file:
    field, description = line.strip().split('\t')
    field_type = field[0]
    field_id = field[1:]
#################################################################################

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
            for field in fields:
                field_type = field[0]
                field_id = field[1:]
                if field_type == "S":
                    if parts[2] == "S":
                        line_fields = {}
                        descriptions = {}
                        for part in parts:
                            if parts.index(part) > 6:
                                data_field, data_field_value = part.strip().split("=")
                                data_field_id = data_field[1:]
                                if field_id == data_field_id:
                                    for line_s in static_file:
                                        field_file, description = line_s.strip().split('\t')
                                        if field_file == field:
                                            line_fields.append(data_field_value)
                                            descriptions.append(description)
                        filtered_data.append({"Timestamp":timestamp_string, "Instrument Code":instrument_code, descriptions : line_fields})
                                    #append field value, with corresponding field to an array

                #field_parts # working
                #filtered_data.append(line) # working

print(filtered_data)