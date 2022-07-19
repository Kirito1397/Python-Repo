import re
import os
import tkinter as tk
from tkinter import filedialog

def clear_screen():
    '''Function to apply clear screen command on the Terminal/cli'''
    os.system('cls' if os.name == 'nt' else 'clear')

def user_prompt():
    '''Function to process user choices in Menu'''
    clear_screen()
    print("""Kindly select the desired option from below:\n\t1. New Build NDT\n\t2. Migration NDT\n\t3. Re-IP NDT\n""")
    main_menu_response = int(input())
    if main_menu_response != 2:
        return ("\t\tThe Feature is not yet ready!\t\t")
    else:
        clear_screen()
        print("""\nKindly confirm the type of Migration NDT from below options:\n\t1. Refresh\n\t2. Link Migration\n""")
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
    elif bool(re.findall("(?i)^\S+-\d+-\d+-\d+sw$", device)):
        # (?i) means case Insesitive
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

    clear_screen()

    def process_links(arr, func):
        seed_file = "<Seed>"

        # Run Loop to create and join wriring templates
        for link in arr:
            seed_file = "".join((seed_file, func(link)))
        print(seed_file)

    def refresh_ndt(content):
        items = len(content)

        if items == 10:
            # Gets the number of items provided as input per link
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, START_IPV4, START_IPV6, END_IPV4, END_IPV6, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="^{START_DEVICE}$" Scope="Datacenter" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}/31" IPv6="{START_IPV6}/126" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="^{END_DEVICE}$" Scope="Datacenter" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}/31" IPv6="{END_IPV6}/126" />
                        <LinkCount="1" LinkState="Migration" LinkCountScope="Local" />
                    </Wiring>""")
            return wiring_template

        elif items == 11:
            # Gets the number of items provided as input per link
            START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, CONNECTOR_TYPE = content

            # Provides with a Single wiring template per link
            wiring_template = (f"""
                    <Wiring>
                        <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="^{START_DEVICE}$" Scope="Datacenter" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}/31" IPv6="{START_IPV6}/126" />
                        <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="^{END_DEVICE}$" Scope="Datacenter" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}/31" IPv6="{END_IPV6}/126" />
                        <LinkCount="1" LinkState="Migration" LinkCountScope="Local" SrlgId="{SRLG_ID}" AppendOpticalOverlay="true" RefreshOpticalOverlay="True" />
                    </Wiring>""")
            return wiring_template
        else:
            return 'One or more field is missing!'

    def re_ip(content):
        items = len(content)

        START_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM, CDBID, CONNECTOR_TYPE = content

        wiring_template = (f"""
                <Wiring>
                    <Start DeviceType="{identify_device_type(START_DEVICE)}" DeviceRegex="^{START_DEVICE}$" Scope="Datacenter" ItfNames="{START_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{START_IPV4}/31" IPv6="{START_IPV6}/126" />
                    <End DeviceType="{identify_device_type(END_DEVICE)}" DeviceRegex="^{END_DEVICE}$" Scope="Datacenter" ItfNames="{END_PORT}" ConnectorType="{CONNECTOR_TYPE}" PortChannel="{PORT_CHANNEL}" IPv4="{END_IPV4}/31" IPv6="{END_IPV6}/126" />
                    <LinkCount="1" LinkState="Production" LinkCountScope="Local" SrlgId="{SRLG_ID}" AppendOpticalOverlay="true" SolutionId="{SOLUTION_ID}" Channel="{CHANNEL_NUM}" OpticalChannelType="Line" />
                    <Property Name="CDBID">{CDBID}</Property>
                </Wiring>""")
        return wiring_template

    # Making Decision based on User Input
    if option == '2.1':
        # Refresh-NDT
        print("\nProvide links as input in below format(if field is not present, just give blank):\n\n\tSTART_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, CONNECTOR_TYPE\n")
        process_links(link_input(), refresh_ndt)
    elif option == '1.3':
        print("\nProvide links as input in below format:\n\n\tSTART_DEVICE, START_PORT, END_DEVICE, END_PORT, PORT_CHANNEL, SRLG_ID, START_IPV4, START_IPV6, END_IPV4, END_IPV6, SOLUTION_ID, CHANNEL_NUM, CDBID, CONNECTOR_TYPE\n")
        process_links(link_input(), re_ip)
    else:
        print('\nFeature not Ready!')

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

# ier01.ztl91 et-0/0/1 eza01.ztl90 et-0/0/2 LR4
# ier02.ztl91 et-0/0/3 eza02.ztl90 et-0/0/4 LR4
# ier03.ztl91 et-0/0/3 eza04.ztl90 et-0/0/4 LR4
# ier04.ztl91 et-0/0/3 eza04.ztl90 et-0/0/4 LR4

# TESTCASE 2:

# ier01.ztl91 et-0/0/1 eza01.ztl90 et-0/0/2 21 100235 10.10.10.1/31 201::0/126 10.10.10.2/31 201::1/126 THN02 20 LR4
# ier02.ztl91 et-0/0/3 eza02.ztl90 et-0/0/4 21 100235 10.10.11.1/31 202::0/126 10.10.11.2/31 202::1/126 THN02 21 LR4
# ier03.ztl91 et-0/0/3 eza04.ztl90 et-0/0/4 21 100235 10.10.12.1/31 203::0/126 10.10.12.2/31 203::1/126 THN02 22 LR4
# ier04.ztl91 et-0/0/3 eza04.ztl90 et-0/0/4 21 100235 10.10.13.1/31 204::0/126 10.10.13.2/31 204::1/126 THN02 23 LR4

'''
