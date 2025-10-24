import time
from logging import info, warning, error, debug
from opcua import Client


class OPCClient:
    client: Client

    def __init__(self, url: str, user:str = None, password:str = None):
        self.client = Client(url)
        self.client.set_user(user)
        self.client.set_password(password) 
    
    def connect(self):
        """Connect to the OPC UA server"""
        try:
            self.client.connect()
            info("Connected to OPC UA server")
            return True
        except Exception as e:
            error(f"Failed to connect: {e}")
            return False
        
    def disconnect(self):
        """Disconnect from the OPC UA server"""
        try:
            self.client.disconnect()
            info("Disconnected from server")
        except Exception as e:
            error(f"Error during disconnection: {e}")
            
    def browse_nodes(self, node=None):
        """Browse and print the server's address space"""
        if node is None:
            node = self.client.get_root_node()
        # debug(f"Node: {node} | NodeName: {node.get_display_name().Text} | NodeId: {node.nodeid}")
        try:
            children = node.get_children()
            for child in children:
                child_node = self.client.get_node(child)
                # debug(f"ChildNode: {child_node.get_node_class()}, {child_node.get_browse_name()}")
        except Exception:
            error("No children exist in the current node")

    def read_data_temperature(self, topic):
        """Read all factory data and display it"""
        data = None
        try:
            temp1 = self.client.get_node("ns=2;i=10").get_value()
            temp2 = self.client.get_node("ns=2;i=11").get_value()
            motor_speed = self.client.get_node("ns=2;i=20").get_value()
            motor_status = self.client.get_node("ns=2;i=21").get_value()
            data = {"topic": topic,
                         "data": {"temp1": temp1,
                                  "temp2": temp2,
                                  "motor_speed": motor_speed,
                                  "motor_status": motor_status}}
            print(data)
        except Exception as e:
            error(f"Error reading data: {e}")
        return data
            