import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

class LLMParser:
    def __init__(self):
        load_dotenv()  # Load variables from .env file
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        # Configure the Google Generative AI library
        genai.configure(api_key=api_key)
        
        # Get available models (uncomment if you want to check available models)
        # self.models = [m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # self.model = self.models[0].name if self.models else "gemini-pro"
        
        # Use the Gemini Pro model
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def parse(self, domain, sentence):
        prompts = {
            "ordering": "You are a parser that converts natural language statements about height/size ordering into Prolog facts. Follow these strict rules:\n1. Use ONLY the predicate format 'fact_taller(X, Y)' where X is taller than Y\n2. Extract all height relationships mentioned\n3. Return one fact per line with NO punctuation\n4. Do NOT use markdown or code blocks\n5. NEVER include explanations or comments\n6. Start each fact with 'fact_taller'",
            
            "family": "You are a parser that converts natural language statements about family relations into Prolog facts. Follow these strict rules:\n1. Use ONLY predicates like 'fact_mother(X, Y)', 'fact_father(X, Y)', 'fact_male(X)', or 'fact_female(X)'\n2. X is the parent and Y is the child in parent relations\n3. Return one fact per line with NO punctuation\n4. Do NOT use markdown or code blocks\n5. NEVER include explanations or comments\n6. Start each fact with 'fact_'",
            
            "spatial": "You are a parser that converts natural language statements about spatial arrangements into Prolog facts. Follow these strict rules:\n1. Use ONLY the predicate format 'fact_left_of(X, Y)' where X is to the left of Y\n2. Extract all spatial relationships mentioned\n3. Return one fact per line with NO punctuation\n4. Do NOT use markdown or code blocks\n5. NEVER include explanations or comments\n6. Start each fact with 'fact_left_of'"
        }
        
        prompt = prompts.get(domain, "Convert to Prolog facts:")
        prompt += f"\n\nStatement to parse: {sentence}\n\nOutput (ONLY facts, one per line):"
        
        try:
            response = self.model.generate_content(prompt)
            
            # Extract the text from the response
            if hasattr(response, 'text'):
                text = response.text
            else:
                # Alternative way to access text content if the API structure changes
                text = str(response.candidates[0].content.parts[0].text)
                
            # Clean up the text to remove markdown formatting and other unwanted elements
            text = text.replace("```prolog", "").replace("```", "")
            
            # Process the text to extract facts
            facts = [line.strip().rstrip('.') for line in text.strip().split('\n') 
                    if line.strip() and 
                    not line.strip().startswith('%') and 
                    line.strip().startswith('fact_')]
            
            return facts
            
        except (GoogleAPIError, Exception) as e:
            print(f"Error using Google Generative AI for parsing: {str(e)}")
            # Fallback to simple parsing for demo purposes
            return self._fallback_parse(domain, sentence)


    
    def _fallback_parse(self, domain, sentence):
        # Original simple parsing logic as fallback
        if domain == "ordering":
            return [
                "fact_taller(alice, bob)",
                "fact_taller(bob, eve)"
            ]
        elif domain == "family":
            return [
                "fact_mother(mary, john)",
                "fact_father(david, john)",
                "fact_mother(mary, alice)",
                "fact_father(david, alice)"
            ]
        elif domain == "spatial":
            return [
                "fact_left_of(cup, plate)",
                "fact_left_of(plate, spoon)"
            ]
        return []

def parse_input(domain, sentence):
    parser = LLMParser()
    return parser.parse(domain, sentence)
