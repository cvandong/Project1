class parse:

    def __init__(self, data):
        self.data = data
        
    def parseJson(self):
        #json parse
        import json
        import yaml

        parsed_data = json.loads(self.data)

        print("Parsed JSON:")
        print(parsed_data)
        print("\n\n---")
        print("YAML Representation:")
        print(yaml.dump(parsed_data))


    def parseXML(self):
        #parse xml
        import xml.etree.ElementTree as ET
        import re
        import json
        import yaml

        xml = ET.ElementTree(ET.fromstring(self.data))
        root = xml.getroot()
        match = re.match(r'{(.*)}', root.tag)
        ns = match.group(1) if match else ""
        print(f'Namespace: {ns}')

        editconf = root.find(f'{{{ns}}}edit-config') if ns else root.find('edit-config')
        if editconf is None:
                raise ValueError("edit-config not found")

        defop = editconf.find(f'{{{ns}}}default-operation') if ns else editconf.find('default-operation')
        testop = editconf.find(f'{{{ns}}}test-option') if ns else editconf.find('test-option')

        if defop is not None:
                print("The default-operation contains: {}".format(defop.text))
        else:
                print("default-operation element not found")

        if testop is not None:
                print("The test-option contains: {}".format(testop.text))
        else:
                print("test-option element not found")
        
        config = editconf.find(f'{{{ns}}}config')
        if config is None:
            raise ValueError("config not found")

            # Find the 'int8.1' element
        int_element = config.find(f'{{{ns}}}int8.1')
        if int_element is not None:
            print("The int8.1 element contains: {}".format(int_element.text))
        else:
            print("int8.1 element not found")
        
        
    def parseYAML(self):
        #parse yaml
        import yaml
        from pprint import pprint
        
        parsed_data = yaml.safe_load(self.data)

        print('Parsed YAML:')
        pprint(parsed_data)
        print('\n')

    def parse(self, data_format):
        if data_format == 'json':
            return self.parseJson()
        elif data_format == 'xml':
            return self.parseXML()
        elif data_format == 'yaml':
            return self.parseYAML()
        else:
            raise ValueError("Unsupported format! Use 'json', 'xml', or 'yaml'.")

