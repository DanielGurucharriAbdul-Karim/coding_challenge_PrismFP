instrument_codes = input("List of instrument codes (in array format [...]):")
start_time = input("Start timestamp:")
end_time = input("End timestamp:")
fields = input("List of static and dynamic fields (in array format [...]):")

file = open("data.txt", "r")
static_file = open("StaticFields.Txt", "r")
dynamic_file = open("DynamicFields.Txt", "r")
lines = file.readlines()

filtered_lines = [] # for checks

######
#for static_line in static_file:
#    static_field, static_description = static_line.strip().split('\t')
#    static_field_id = static_field[1:]
#
#for dynamic_line in dynamic_file:
#    dynamic_field, dynamic_description = dynamic_line.strip().split('\t')
#    dynamic_field_id = dynamic_field[1:]
#######

for line in lines:
    line = line.strip()
    parts = line.strip().split("|")

    instrument_code = parts[3]
    timestamp_string = parts[1]
    message_type = parts[2]

    time_parts = timestamp_string.split(":")
    timestamp = f"{time_parts[0]}:{time_parts[1]}:{time_parts[2]}.{time_parts[3]}"

    field_ids = [] # for checks
    output_fields = []
    if instrument_code in instrument_codes:
        if start_time <= timestamp <= end_time:
            filtered_lines.append(line) # for checks
            for part in parts:
                if parts.index(part) > 6:
                    data_field, data_field_value = part.strip().split("=")
                    #data_field_id = data_field[1:] # no need anytmore
                    #field_ids.append(data_field_id) # for checks
                    for field in fields:
                        if field[1:] == data_field[1:]:
                            if field[0] == "S" and message_type == "S":
                                for static_line in static_file:
                                    static_field, static_description = static_line.strip().split('\t')
                                    if static_field == field:
                                        output_fields.append({static_description:data_field_value})
                                        print(output_fields)
                                        # do something here
                            #elif field[0] == "D":
                                #if message_type == "Q" or message_type == "C" or message_type =="T" or message_type =="R":

    print(output_fields)

            #print(field_ids) # for checks
            #for field in fields:
                #if field[1:] in field_ids:



#print(filtered_lines) #for checks

