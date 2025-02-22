class Utils:
    # Static class variable for system prompt
    system_prompt = """
    You run in a loop of Thought, Action, PAUSE, Observation.
    At the end of the loop you output an Answer
    Use Thought to describe your thoughts about the question you have been asked.
    Use Action to run one of the actions available to you - then return PAUSE.
    Observation will be the result of running those actions.

    Your available actions are:

    calculate:
    e.g. calculate: 4 * 7 / 3
    Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

    get_planet_mass:
    e.g. get_planet_mass: Earth
    returns weight of the planet in kg

    Example session:

    Question: What is the mass of Earth times 2
    Thought: I need to find the mass of Earth
    Action: get_planet_mass: Earth
    PAUSE 

    You will be called again with this:

    Observation: 5.972e24

    Thought: I need to multiply this by 2
    Action: calculate: 5.972e24 * 2
    PAUSE

    You will be called again with this: 

    Observation: 1,1944×10e25

    If you have the answer, output it as the Answer.

    Answer: The mass of Earth times 2 is 1,1944×10e25.

    Now it's your turn:
    """.strip()

    @staticmethod
    def get_system_prompt():
        """Returns the system prompt for the agent."""
        return Utils.system_prompt
    
    @staticmethod
    def calculate(operation: str) -> float:
        return eval(operation)

    @staticmethod
    def get_planet_mass(planet) -> float:
        match planet.lower():
            case "earth":
                return 5.972e24
            case "jupiter":
                return 1.898e27
            case "mars":
                return 6.39e23
            case "mercury":
                return 3.285e23
            case "neptune":
                return 1.024e26
            case "saturn":
                return 5.683e26
            case "uranus":
                return 8.681e25
            case "venus":
                return 4.867e24
            case _:
                return 0.0