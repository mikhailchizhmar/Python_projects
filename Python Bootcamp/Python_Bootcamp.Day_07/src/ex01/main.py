import json

G_RESPIRATION_RANGE = (12, 16)
G_HEART_RATE_RANGE = (60, 100)
G_BLUSHING_LEVELS = (1, 2, 3, 4, 5, 6)
G_PUPIL_DILATION_RANGE = (2, 8)
right_answers = [3, 1, 2, 1, 2, 3, 2, 1, 2, 3]


def load_questions(filename: str) -> list[dict]:
    """Loads list of questions and answers from the file

    :param filename: Name of a json file
    :return: List of questions and answers
    """
    try:
        with open(filename, 'r') as file:
            questions = json.load(file)["questions"]
            if not questions:
                raise ValueError("Question file is empty.")
            return questions
    except FileNotFoundError:
        print("Question file not found.")
        return []
    except ValueError as e:
        print(f"Error loading questions: {e}")
        return []


def print_q_n_a(n: int, q: dict) -> None:
    """Prints question and answer options

    :param n: The number of the question
    :param q: Dict which contains question and answer
    """
    print("\n", n + 1, ". ", q["question"], sep='')
    for i in range(3):
        print(i + 1, ") ", q["answer"][i], sep='')


def ask(n: int) -> int:
    """Accepts answer from user and checks if it is correct

    :param n: The number of the question
    :return: 1 if answer is correct, 0 otherwise
    """
    answer = input("Print the number of correct answer (1-3): ")
    if answer not in ("1", "2", "3"):
        raise ValueError("Answer must be between 1 and 3.")
    return answer == str(right_answers[n])


def validate_response() -> list[float]:
    """Accepts and validates parameters from user

    :return: List of parameters
    """
    while True:
        try:
            respiration = float(input("Enter respiration rate (BPM): "))
            if respiration < 0 or respiration > 500:
                raise ValueError("Respiration rate cannot be negative or larger than 499.")
            heart_rate = float(input("Enter heart rate: "))
            if heart_rate < 0 or heart_rate > 500:
                raise ValueError("Heart rate cannot be negative or larger than 499.")
            blushing_level = int(input("Enter blushing level (1-6): "))
            if not 1 <= blushing_level <= 6:
                raise ValueError("Blushing level must be between 1 and 6.")
            pupil_dilation = float(input("Enter pupil dilation (2-8 mm): "))
            if not 2 <= pupil_dilation <= 8:
                raise ValueError("Pupil dilation must be between 2 and 8 mm.")
            return [respiration, heart_rate, blushing_level, pupil_dilation]
        except ValueError as e:
            print(f"Invalid input: {e} Please try again.")


def assess_response(stats: list[float]) -> int:
    """Calculates score

    :param stats: List of parameters
    :return: score
    """
    human_score = 0

    if G_RESPIRATION_RANGE[0] <= stats[0] <= G_RESPIRATION_RANGE[1]:
        human_score += 1
    if G_HEART_RATE_RANGE[0] <= stats[1] <= G_HEART_RATE_RANGE[1]:
        human_score += 1
    if stats[2] < 4:
        human_score += 1
    if stats[3] <= 4:
        human_score += 1
    return human_score


def main() -> None:
    """The main function of the project."""
    questions = load_questions('../ex00/q_n_a.json')
    if not questions:
        print("No questions available. Exiting test.")
        return

    score = 0
    response_score = 0
    q_num = 0
    for question in questions:
        print_q_n_a(q_num, question)

        while True:
            try:
                score += ask(q_num)
                stats = validate_response()
                response_score += assess_response(stats)
                break
            except ValueError as e:
                print(f"Invalid input: {e} Please try again.")
        q_num += 1

    decision = "Human" if score >= 5 and response_score >= 30 else "Replicant"
    print(f"\nThe subject is classified as: {decision}")


if __name__ == '__main__':
    main()
