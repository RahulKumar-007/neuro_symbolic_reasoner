from pyswip import Prolog
import os

class PrologEngine:
    def __init__(self, domain):
        self.prolog = Prolog()
        self.domain = domain
        self.load_rules()


    def load_rules(self):
        rule_path = os.path.abspath(f"rules/{self.domain}.pl")
        self.prolog.consult(rule_path)

    def add_facts(self, facts):
        for fact in facts:
            fact = fact.strip().rstrip('.')  # Remove any trailing periods
            try:
                self.prolog.assertz(fact)
            except Exception as e:
                print(f"Error adding fact '{fact}': {str(e)}")


    def query(self, q):
        return list(self.prolog.query(q))

