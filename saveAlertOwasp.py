import json
import sqlite3

class AlertDetail:
    def __init__(self, alert, reference, cweid, desc, solution, otherinfo, alertRef):
        self.alert = alert
        self.reference = reference
        self.cweid = cweid
        self.desc = desc
        self.solution = solution
        self.otherinfo = otherinfo
        self.alertRef = alertRef  

class JSONDataSearcher:
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
        self.searchAlertResults = []
        self.searchReferenceResults = []
        self.searchCweIdResults = []
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

    def saveOwaspToClass(self):
        jsData = JSONDataSearcher("json/report_owaspZap_2024-02-14_14:43.json", "vulnerabilities.db")
        
        jsData.search([f"site/alerts/alert"])
        self.alert = jsData.get_search_results()

        jsData.search([f"site/alerts/desc"])
        self.desc = jsData.get_search_results()

        jsData.search([f"site/alerts/solution"])
        self.solution = jsData.get_search_results()

        jsData.search([f"site/alerts/otherinfo"])
        self.otherinfo = jsData.get_search_results()

        jsData.search([f"site/alerts/reference"])
        self.reference = jsData.get_search_results()
        
        jsData.search([f"site/alerts/cweid"])
        self.cweid = jsData.get_search_results()

        jsData.search([f"site/alerts/alertRef"])
        self.alertRef = jsData.get_search_results()
        
        alertClass = AlertDetail(self.alert, self.reference, self.cweid, self.desc, self.solution, self.otherinfo, self.alertRef)
        return alertClass
    
    def saveOwaspToDB(self):
        saved = self.saveOwaspToClass()
        try:
            for alert, description, cweid, solution, otherinfo in zip(saved.alert, saved.desc, saved.cweid, saved.solution, saved.otherinfo):
                values_to_insert = (alert, description, cweid, solution, otherinfo)
                query = "INSERT INTO alertOwasp (alert, description, cwe_id, solution, otherinfo) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(query, values_to_insert)
            self.conn.commit()
            print("Data saved to database successfully!")
        except sqlite3.Error as e:
            print(f"Error saving data to database: {e}")
        finally:
            self.conn.close()


