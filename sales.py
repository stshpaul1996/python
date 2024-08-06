class Customer:

    def __init__(self,name,address):
        self.name=name
        self.address=address
    def create(self):
        #DB connection and inserting data
        if not self.name.isalnum():
            print("Issue with name")
        else:
            print("Inserted data")
            return True