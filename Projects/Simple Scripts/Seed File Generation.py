def seed_generation(content):
    START_DEVICE,START_DEVICE_INTERFACE,END_DEVICE,END_DEVICE_INTERFACE,CONNECTOR_TYPE = content
    wiring_template = (f"""<Seed>
               <Wiring>
                   <Start DeviceType="EdgeZoneAggregator" StartDevice="{START_DEVICE}" ItfNames="{START_DEVICE_INTERFACE}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                   <End DeviceType="InternetEdgeRouter" EndDevice="{END_DEVICE}" ItfNames="{END_DEVICE_INTERFACE}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
               </Wiring>
          </Seed>""")
    return wiring_template

if __name__ == "__main__":
    ndt_links = []
    print("Kindly enter the link details: \n")
    while True:
        per_line_input = list(map(str,input().split()))
        # print(per_line_input)
        if per_line_input != []:
            ndt_links.append(per_line_input)
        else:
            break

    # print(ndt_links)
    seed_file = ""
    for link in ndt_links:
        seed_file = "\n".join((seed_file,seed_generation(link)))
    print(seed_file)

# TESTCASE:

# ier01.atl31 et-0/0/1 eza01.ztl30 et-0/0/2 LR4
# ier02.atl31 et-0/0/3 eza02.ztl30 et-0/0/4 LR4
# ier03.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4
# ier04.atl31 et-0/0/3 eza04.ztl30 et-0/0/4 LR4