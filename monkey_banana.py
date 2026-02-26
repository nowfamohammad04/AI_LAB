#Hard-Core(Brute-force)
def monkey_banana(initial_state):
    print("Initial state:",initial_state)
    initial_state["monkey"]:initial_state["box"]
    initial_state["box"]:initial_state["window"]
    initial_state["banana"]:initial_state["monkey"]
    print("Final_state:",initial_state)
monkey=input("Enter monkey position:")
box=input("Enter box position:")
banana=input("Enter banana postion:")
initial_state={"monkey":monkey, "box":box, "banana":banana}
monkey_banana(initial_state)