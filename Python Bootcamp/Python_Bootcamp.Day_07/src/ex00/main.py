import json

G_RESPIRATION_RANGE = (12, 16)
G_HEART_RATE_RANGE = (60, 100)
G_BLUSHING_LEVELS = (1, 2, 3, 4, 5, 6)
G_PUPIL_DILATION_RANGE = (2, 8)
right_answers = [3, 1, 2, 1, 2, 3, 2, 1, 2, 3]


def ask(n: int, q: dict) -> int:
    """Asks question, accepts answer from the user and checks if it is correct

    :param n: The number of the question
    :param q: Dict which contains question and answer
    :return: 1 if answer is correct, 0 otherwise
    """
    print("\n", n + 1, ". ", q["question"], sep='')
    for i in range(3):
        print(i + 1, ") ", q["answer"][i], sep='')
    answer = input("Print the number of correct answer (1-3): ")
    return answer == str(right_answers[n])


def decide_response() -> int:
    """Accepts parameters from user and calculates score

    :return: score
    """
    respiration = float(input("Enter respiration rate (BPM): "))
    heart_rate = float(input("Enter heart rate: "))
    blushing_level = int(input("Enter blushing level (1-6): "))
    pupil_dilation = float(input("Enter pupil dilation (2-8 mm): "))
    human_score = 0

    if G_RESPIRATION_RANGE[0] <= respiration <= G_RESPIRATION_RANGE[1]:
        human_score += 1
    if G_HEART_RATE_RANGE[0] <= heart_rate <= G_HEART_RATE_RANGE[1]:
        human_score += 1
    if blushing_level in G_BLUSHING_LEVELS:
        human_score += 1
    if G_PUPIL_DILATION_RANGE[0] <= pupil_dilation <= G_PUPIL_DILATION_RANGE[1]:
        human_score += 1

    return human_score


def main() -> None:
    """The main function of the project."""
    with open("q_n_a.json", "r") as file:
        questions = json.load(file)["questions"]

    score = 0
    response_score = 0
    for question, q_num in zip(questions, range(10)):
        score += ask(q_num, question)
        response_score += decide_response()
    decision = "Human" if score >= 5 and response_score >= 30 else "Replicant"
    print(f"\nThe subject is classified as: {decision}")


if __name__ == "__main__":
    main()
