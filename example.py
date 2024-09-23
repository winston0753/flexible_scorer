
# Example usage
from flexible_scorer import FlexibleScorer

if __name__ == "__main__":
    criteria = "humor"
    scorer = FlexibleScorer(criteria)
    texts = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "This is a very serious statement with no humor whatsoever.",
        "Why did the chicken cross the road? To get to the other side!",
        """Paddy died in a fire and was burnt pretty badly. So the morgue needed someone to identify the body. His two best friends, Seamus and Sean, were sent for. Seamus went in and the mortician pulled back the sheet.

Seamus said "Yup, he's burnt pretty bad. Roll him over".

So the mortician rolled him over. Seamus looked and said "Nope, it ain't Paddy."

The mortician thought that was rather strange and then he brought Sean in to identify the body.

Sean took a look at him and said, "Yup, he's burnt real bad, roll him over."

The mortician rolled him over and Sean looked down and said, "No, it ain't Paddy."

The mortician asked, "How can you tell?"

Sean said, "Well, Paddy had two arseholes."

"What? He had two arseholes?" asked the mortician.

"Yup, everyone knew he had two arseholes. Every time we went into town, folks would say, 'Here comes Paddy with them two arseholes....'"""
    ]

    additional_instructions = "Consider dark humor and cultural references in your evaluation."

    scores = []
    for text in texts:
        print(f"\nText: {text}")
        score = scorer.score(text, additional_instructions)
        scores.append(score)
        print(f"Final {criteria.capitalize()} Score: {score}")
        print()

    scorer.plot_results(texts, scores)