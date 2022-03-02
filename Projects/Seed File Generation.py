def seed_generation(content):
    START_DEVICE,START_DEVICE_INTERFACE,END_DEVICE,END_DEVICE_INTERFACE,CONNECTOR_TYPE = content
    print(f"""<Seed>
               <Wiring>
                   <Start DeviceType="EdgeZoneAggregator" StartDevice="{START_DEVICE}" ItfNames="{START_DEVICE_INTERFACE}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
                   <End DeviceType="InternetEdgeRouter" EndDevice="{END_DEVICE}" ItfNames="{END_DEVICE_INTERFACE}" ConnectorType="{CONNECTOR_TYPE}" NewPortChannel="True" />
               </Wiring>
          </Seed>""")


if __name__ == "__main__":
    input_details = list(map(str,input("Kindly enter the link details: ").split()))
    print(input_details)
    seed_generation(input_details)


# ier01.atl31 et-0/0/1 eza01.ztl30 et-0/0/2 LR4