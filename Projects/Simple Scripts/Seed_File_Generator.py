import re


def user_prompt():
    print("""Kindly select the desired option from below:\n\t1. New Build NDT\n\t2. Migration NDT\n""")
    main_menu_response = int(input())
    if main_menu_response == 1:
        return ("\t\tThe Feature is not yet ready!\t\t")
    else:
        print("""Kindly confirm the type of Migration NDT from below options:\n\t1. Refresh\n\t2. Link Migration""")
        migration_menu_response = int(input())
        return seed_generation(migration_menu_response)


def identify_device_type(device):
    '''Function fetches the Device Type of a Device.'''

    device_types = {'ier': 'InternetEdgeRouter',
                    'eza': 'EdgeZoneAggregator',
                    'ibr': 'InternetBackboneRouter',
                    'icr': 'InternetCoreRouter',
                    'rwa': 'RegionalAggregatorRouter',
                    'car': 'CoreAggregatorRouter',
                    'ear': 'EdgeAggregatorRouter',
                    'ter': 'TransitEdgeRouter',
                    'owr': 'OneWanRouter',
                    'sw': 'SwanRouter',
                    '96cbe': 'CoreRouter'}
    if bool(re.findall("^\S+-96cbe-\d\w$", device)):
        return device_types.get('96cbe')
    elif bool(re.findall("^\S+-\d+-\d+-\d+sw$", device)):
        return device_types.get('sw')
    else:
        return device_types.get(device[:3].lower())


def link_input():
    ndt_links = []
    while True:
        per_line_input = list(map(str, input().split()))
        if bool(per_line_input):
            ndt_links.append(per_line_input)
        else:
            # Breaks the loop if an empty input is provided
            return ndt_links


def seed_generation(option):

    print('Provide the input links:')

    def process_link(arr, func):
        seed_file = "<Seed>"

        # Run Loop to create and join wriring templates
        for link in arr:
            seed_file = "".join((seed_file, func(link)))
        print(seed_file)

    def refresh_ndt(content):

        # Gets the number of items provided as input per link
        items = len(content)

        if items < 6:
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                        <LinkCount="1" LinkState="Migration" />
                    </Wiring>""")
            return wiring_template

        elif items == 6:
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, SRLG_ID, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                        <LinkCount="1" LinkState="Migration" SrlgId="{SRLG_ID}" />
                    </Wiring>""")
            return wiring_template

        elif items == 10:
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" IPv4="{START_IPV4}" IPv6="{START_IPV6}"/>
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" IPv4="{END_IPV4}" IPv6="{END_IPV6}"/>
                        <LinkCount="1" LinkState="Migration" SrlgId="{SRLG_ID}" />
                    </Wiring>""")
            return wiring_template
        
        elif items == 11:
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, START_IPV4, START_IPV6, END_IPV4, END_IPV6, CDBID, CONNECTOR_TYPE  = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}" IPv6="{START_IPV6}" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}" IPv6="{END_IPV6}" />
                        <LinkCount="1" LinkState="Migration" />
                        <Property Name="CDBID">{CDBID}</Property>
                    </Wiring>""")
            return wiring_template

        elif items == 13:
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}" IPv6="{START_IPV6}" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}" IPv6="{END_IPV6}" />
                        <LinkCount="1" LinkState="Migration" SrlgId="{SRLG_ID}" AppendOpticalOverlay="true" SolutionId="{SOLUTION_ID}" Channel="{CHANNEL_NUM}" OpticalChannelType="Line" />
                    </Wiring>""")
            return wiring_template

        elif items == 14:
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM , CDBID, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}" IPv6="{START_IPV6}" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}" IPv6="{END_IPV6}" />
                        <LinkCount="1" LinkState="Migration" SrlgId="{SRLG_ID}" AppendOpticalOverlay="true" SolutionId="{SOLUTION_ID}" Channel="{CHANNEL_NUM}" OpticalChannelType="Line" />
                        <Property Name="CDBID">{CDBID}</Property>
                    </Wiring>""")
            return wiring_template
        else:
            return f'\nProvide Current number of fields. One of the field is missing.'
    if option == 1:
        process_link(link_input(), refresh_ndt)
    else:
        return 'Feature not Ready!'


if __name__ == "__main__":

    user_prompt()

    # Input the desired File Name for the seed.
    seed_file_name = str(input("Provide the desired file name for the Seed: "))

    # Define an string with <Seed> tag and then later join all the wriring templates to it.

    # Define a variable conatining system location of the Seed to be generated.
    FILE_PATH = "C:/Users/Kirito/Desktop/"+seed_file_name+".xml"

    # Write the contents of the Seed file, and add the closing </Seed> tag with it.
    # try:
    #     with open(FILE_PATH, 'x') as file:
    #         file.writelines(seed_file + '\n</Seed>')
    # except OSError as e:
    #     print(e,"\nKindly provide another seed name.")
    #     exit()


'''
# TESTCASE:

# ier01.atl31 et-0/0/1 eza01.ztl30 et-0/0/2 LR4
# ier02.atl31 et-0/0/3 eza02.ztl30 et-0/0/4 LR4
# ier03.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4
# ier04.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4
'''
