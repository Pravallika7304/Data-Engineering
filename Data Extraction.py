from lxml import etree

def extract_abr_data(xml_path):
    tree = etree.parse(xml_path)
    orgs = []

    for org in tree.xpath("//Organisation"):
        abn = org.findtext("ABN")
        name = org.findtext("EntityName")
        entity_type = org.findtext("EntityType")
        status = org.findtext("EntityStatus")
        address = org.findtext("MainBusinessPhysicalAddress/AddressLine")
        postcode = org.findtext("Postcode")
        state = org.findtext("State")
        start_date = org.findtext("EntityStartDate")

        orgs.append({
            "abn": abn,
            "entity_name": name,
            "entity_type": entity_type,
            "status": status,
            "address": address,
            "postcode": postcode,
            "state": state,
            "start_date": start_date
        })

    return orgs

if __name__ == "__main__":
    abr_data = extract_abr_data("abr_sample.xml")
    print(abr_data)
