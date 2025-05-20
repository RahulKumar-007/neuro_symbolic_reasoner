from parser import parse_input
from prolog_engine import PrologEngine

def run_interactive():
    print("Welcome to the Neuro-Symbolic Reasoning Engine!")
    print("Available domains: ordering, family, spatial")
    
    while True:
        print("\n" + "="*50)
        domain = input("Enter domain (or 'quit' to exit): ").strip().lower()
        
        if domain == 'quit':
            break
            
        if domain not in ['ordering', 'family', 'spatial']:
            print("Invalid domain. Please choose from: ordering, family, spatial")
            continue
            
        print(f"\nEnter your statements about the {domain} domain (empty line to finish):")
        sentences = []
        while True:
            line = input("> ").strip()
            if not line:
                break
            sentences.append(line)
        
        if not sentences:
            print("No statements provided.")
            continue
            
        # Combine sentences
        sentence = " ".join(sentences)
        
        # Parse and add facts
        facts = parse_input(domain, sentence)
        print("\nParsed Facts:")
        for fact in facts:
            print(f"  {fact}")
            
        # Create engine and add facts
        engine = PrologEngine(domain)
        engine.add_facts(facts)
        
        # Query loop
        print("\nYou can now query the knowledge base (empty line to finish):")
        while True:
            query = input("Query> ").strip()
            if not query:
                break
                
            try:
                results = engine.query(query)
                if results:
                    print("Results:")
                    for result in results:
                        print(f"  {result}")
                else:
                    print("No results found.")
            except Exception as e:
                print(f"Error executing query: {str(e)}")

def run_examples():
    # Keep your original examples for testing
    print("Running examples...")
    run("ordering", "Alice is taller than Bob. Bob is taller than Eve.", "shortest(X)")
    run("family", "Mary is the mother of John. David is the father of John. Mary is the mother of Alice. David is the father of Alice.", "sibling(X, Y)")
    run("spatial", "The cup is to the left of the plate. The plate is to the left of the spoon.", "right_of(spoon, X)")

def run(domain, sentence, query):
    print(f"\n[Domain: {domain}]")
    facts = parse_input(domain, sentence)
    print("Parsed Facts:", facts)

    engine = PrologEngine(domain)
    engine.add_facts(facts)

    results = engine.query(query)
    print("Query Results:", results)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--examples":
        run_examples()
    else:
        run_interactive()
