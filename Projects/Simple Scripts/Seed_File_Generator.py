import re
import tkinter as tk
from tkinter import filedialog


def user_prompt():
    '''Function to process user choices in Menu'''

    print("""Kindly select the desired option from below:\n\t1. New Build NDT\n\t2. Migration NDT\n\t3. Re-IP NDT\n""")
    main_menu_response = int(input())
    if main_menu_response != 2:
        return ("\t\tThe Feature is not yet ready!\t\t")
    else:
        print("""\nKindly confirm the type of Migration NDT from below options:\n\t1. Refresh\n\t2. Link Migration""")
        migration_menu_response = int(input())
        return seed_generation('2.' + str(migration_menu_response))


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
    '''Function used to store all the provided links in a list'''

    ndt_links = []
    while True:
        per_line_input = list(map(str, input().split()))
        if bool(per_line_input):
            ndt_links.append(per_line_input)
        else:
            # Breaks the loop if an empty input is provided
            return ndt_links


def seed_generation(option):

    def process_links(arr, func):
        seed_file = "<Seed>"

        # Run Loop to create and join wriring templates
        for link in arr:
            seed_file = "".join((seed_file, func(link)))
        print(seed_file)

    def refresh_ndt(content):

        # Gets the number of items provided as input per link
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}" IPv6="{START_IPV6}" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}" IPv6="{END_IPV6}" />
                        <LinkCount="1" LinkState="Migration" SrlgId="{SRLG_ID}" AppendOpticalOverlay="true" RefreshOpticalOverlay="True" />
                    </Wiring>""")
            return wiring_template

    def re_ip(content):

            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM , CDBID, CONNECTOR_TYPE = content

            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="{START_DEVICE}" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}" IPv6="{START_IPV6}" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="{END_DEVICE}" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}" IPv6="{END_IPV6}" />
                        <LinkCount="1" LinkState="Production" SrlgId="{SRLG_ID}" AppendOpticalOverlay="true" SolutionId="{SOLUTION_ID}" Channel="{CHANNEL_NUM}" OpticalChannelType="Line" />
                        <Property Name="CDBID">{CDBID}</Property>
                    </Wiring>""")
            return wiring_template

    if option == '2.1':
        print("\nProvide links as input in below format:\n\n\tSTART_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM, CONNECTOR_TYPE\n")
        process_links(link_input(), refresh_ndt)
    elif option == 1:
        print("\nProvide links as input in below format:\n\n\tSTART_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM, CDBID, CONNECTOR_TYPE\n")
        process_links(link_input(), re_ip)
    else:
        return 'Feature not Ready!'

def save_file(data):
    '''Function to save the Seed contents/data'''
    
    #Removes the root tkinter window from the screen (without destroying it)
    root = tk.Tk()   #Create Tkinter Top Window
    root.withdraw()  #Hide Tkinter Top Window

    file_path = filedialog.asksaveasfile(confirmoverwrite=True, initialfile = 'myseed.xml',defaultextension=".xml",filetypes=[("All Files","*.*"),("XML Documents","*.xml")])

    with open(file_path.name,'w') as f:
        f.writelines(data+ '\n</Seed>')
        f.close()
    return 'File Saved!'



if __name__ == "__main__":

    user_prompt()

    # Input the desired File Name for the seed.
    # seed_file_name = str(input("Provide the desired file name for the Seed: "))

    # Define an string with <Seed> tag and then later join all the wriring templates to it.

    # Define a variable conatining system location of the Seed to be generated.
    # FILE_PATH = "C:/Users/Kirito/Desktop/"+seed_file_name+".xml"

    # Write the contents of the Seed file, and add the closing </Seed> tag with it.
    # try:
    #     with open(FILE_PATH, 'x') as file:
    #         file.writelines(seed_file + '\n</Seed>')
    # except OSError as e:
    #     print(e,"\nKindly provide another seed name.")
    #     exit()


'''
# TESTCASE 1:

# ier01.atl31 et-0/0/1 eza01.ztl30 et-0/0/2 LR4
# ier02.atl31 et-0/0/3 eza02.ztl30 et-0/0/4 LR4
# ier03.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4
# ier04.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4

# TESTCASE 2:

# ier01.atl31 et-0/0/1 eza01.ztl30 et-0/0/2 21 100235 10.10.10.1/31 201::0/126 10.10.10.2/31 201::1/126 THN02 20 LR4
# ier02.atl31 et-0/0/3 eza02.ztl30 et-0/0/4 21 100235 10.10.11.1/31 202::0/126 10.10.11.2/31 202::1/126 THN02 21 LR4
# ier03.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 21 100235 10.10.12.1/31 203::0/126 10.10.12.2/31 203::1/126 THN02 22 LR4
# ier04.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 21 100235 10.10.13.1/31 204::0/126 10.10.13.2/31 204::1/126 THN02 23 LR4

'''
