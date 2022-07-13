# Below function fetches the Device Type of a Device.
def identify_device_type(device):
    device_types = {'ier': 'InternetEdgeRouter',
                    'eza': 'EdgeZoneAggregator',
                    'ibr': 'InternetBackboneRouter',
                    'icr': 'InternetCoreRouter',
                    'rwa': 'RegionalAggregatorRouter',
                    'car': 'CoreAggregatorRouter',
                    'ear': 'EdgeAggregatorRouter',
                    'ter': 'TransitEdgeRouter',
                    'owr': 'OneWanRouter'}
    return device_types.get(device[:3].lower())

def seed_generation(content):

    # Gets the number of items provided as input per link
    items = len(content)

    if items < 6:
        START_DEVICE, START_PORT, END_DEVICE, END_PORT, CONNECTOR_TYPE = content

        # Provides with a Single wiring template per link
        wiring_template = (f"""
                   <Wiring>
                       <Start DeviceType="{identify_device_type(START_DEVICE)}" StartDevice="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                       <End DeviceType="{identify_device_type(END_DEVICE)}" EndDevice="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                       <LinkCount="1" LinkState="Production" />
                   </Wiring>""")
        return wiring_template

    elif items == 6:
        START_DEVICE, START_PORT, END_DEVICE, END_PORT, CONNECTOR_TYPE, SRLG_ID = content

        # Provides with a Single wiring template per link
        wiring_template = (f"""
                   <Wiring>
                       <Start DeviceType="{identify_device_type(START_DEVICE)}" StartDevice="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                       <End DeviceType="{identify_device_type(END_DEVICE)}" EndDevice="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                       <LinkCount="1" LinkState="Production" SrlgId="{SRLG_ID}" />
                   </Wiring>""")
        return wiring_template

    elif items == 10:
        START_DEVICE, START_PORT, END_DEVICE, END_PORT, CONNECTOR_TYPE, SRLG_ID, START_IPV4, START_IPV46, END_IPV4, END_IPV6 = content

        # Provides with a Single wiring template per link
        wiring_template = (f"""
                   <Wiring>
                       <Start DeviceType="{identify_device_type(START_DEVICE)}" StartDevice="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                       <End DeviceType="{identify_device_type(END_DEVICE)}" EndDevice="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                       <LinkCount="1" LinkState="Production" SrlgId="{SRLG_ID}" />
                   </Wiring>""")
        return wiring_template


if __name__ == "__main__":
    
    ndt_links = []
    print("Kindly enter the link details: \n")
    # Get all the links as input
    while True:
        per_line_input = list(map(str, input().split()))
        if per_line_input != []:
            ndt_links.append(per_line_input)
        else:
            # Breaks the loop if an empty input is provided
            break

    # Input the desired File Name for the seed.
    seed_file_name = str(input("Provide the desired file name for the Seed: "))

    # Define an string with <Seed> tag and then later join all the wriring templates to it.
    seed_file = "<Seed>"

    # Run Loop to create and join wriring templates
    for link in ndt_links:
        seed_file = "".join((seed_file, seed_generation(link)))
    print(seed_file)

    # Define a variable conatining system location of the Seed to be generated.
    FILE_PATH = "C:/Users/Kirito/Desktop/"+seed_file_name+".xml"

    # Write the contents of the Seed file, and add the closing </Seed> tag with it.
    try:
        with open(FILE_PATH, 'x') as file:
            file.writelines(seed_file + '\n</Seed>')
    except OSError as e:
        print(e,"\nKindly provide another seed name.")
        exit()



'''
# TESTCASE:

# ier01.atl31 et-0/0/1 eza01.ztl30 et-0/0/2 LR4
# ier02.atl31 et-0/0/3 eza02.ztl30 et-0/0/4 LR4
# ier03.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4
# ier04.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4
'''
