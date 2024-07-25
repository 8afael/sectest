import json
import sqlite3

class AlertDetail:
    def __init__(self, classification, description, solution):
        self.classification = classification
        self.description = description
        self.solution = solution

class references:
    def __init__(self, reference):
        self.reference = reference

class wapitiSearcher:
    def __init__(self, filename, database):
            self.alertDetail = []
            self.filename = filename
            self.database = database       
            self.conn = sqlite3.connect(database)
            self.cursor = self.conn.cursor()
            self.data = self._load_data()

    def _load_data(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def search(self, subkeys):
        self.search_results = []

        def _search_recursive(data, current_key=""):
            if isinstance(data, dict):
                for key, value in data.items():
                    new_key = current_key + "/" + key if current_key else key
                    if new_key in subkeys:
                        self.search_results.append(value)
                    _search_recursive(value, new_key)
            elif isinstance(data, list):
                for item in data:
                    _search_recursive(item, current_key)

        _search_recursive(self.data)

    
    def get_search_results(self):
        return self.search_results
    
    
    def saveWapitiAlertToClass(self):
        self.jsData = wapitiSearcher("json/report_wapiti_2024-02-14_14:43.json", "vulnerabilities.db")    
        
        self.jsData.search(["classifications"])
        self.classifications = self.jsData.get_search_results()
        #print(self.classifications)

        for section in self.data:
            self.jsData.search([f"classifications/"+section+"/desc"])
            self.description = self.jsData.get_search_results()
            print(self.description)

        self.jsData.search([f"classifications/Backup file/sol"])
        self.solution = self.jsData.get_search_results()
        #print(self.solution)
      
        alertClass = AlertDetail(self.classifications, self.description, self.solution)
        return alertClass
    
    
    def saveWapitiReferenceToClass(self):
        self.jsData.search(["classifications/ref"])
        self.reference = self.jsData.get_search_results()
       
        refClass = references(self.reference)
        return refClass
    
    def saveWapitiToDB(self):
        saved = self.saveWapitiAlertToClass()
        try:
            for classification, description, solution in zip(saved.classification, saved.description, saved.solution):
                values_to_insert = (classification, description, solution)
                query = "INSERT INTO alertsWapiti (classifications, description, solution) VALUES (?, ?, ?)"
                self.cursor.execute(query, values_to_insert)
            self.conn.commit()
            print("Data saved to database successfully!")
        except sqlite3.Error as e:
            print(f"Error saving data to database: {e}")
        finally:
            self.conn.close()


