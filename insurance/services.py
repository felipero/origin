import datetime


class RiskCalculator:
    def calculate_score(self, profile_data):
        base_score = sum([int(rq) for rq in profile_data["risk_questions"]])
        lines_score = {
            "auto": base_score,
            "disability": base_score,
            "home": base_score,
            "life": base_score,
        }

        if int(profile_data["age"]) < 30:
            lines_score = {line: score - 2 for line, score in lines_score.items()}
        elif int(profile_data["age"]) in range(30, 41):
            lines_score = {line: score - 1 for line, score in lines_score.items()}

        if int(profile_data["dependents"]) >= 1:
            lines_score.update(
                {
                    line: score + 1
                    for line, score in lines_score.items()
                    if line in ["life", "disability"]
                }
            )

        if profile_data["marital_status"] == "married":
            lines_score["life"] += 1
            lines_score["disability"] += 1

        if "vehicle" not in profile_data:
            lines_score["auto"] = "ineligible"
        elif int(profile_data["vehicle"]["year"]) >= (
            datetime.datetime.today().year - 5
        ):
            lines_score["auto"] += 1

        if "income" not in profile_data or float(profile_data["income"]) <= 0:
            lines_score["disability"] = "ineligible"
        elif float(profile_data["income"]) > 200000:
            lines_score = {line: score - 1 for line, score in lines_score.items()}

        if "house" not in profile_data:
            lines_score["home"] = "ineligible"
        elif profile_data["house"]["ownership_status"] == "mortgaged":
            lines_score.update(
                {
                    line: score + 1
                    for line, score in lines_score.items()
                    if line in ["home", "disability"]
                }
            )

        if int(profile_data["age"]) > 60:
            lines_score["life"] = "ineligible"
            lines_score["disability"] = "ineligible"

        return {line: self.classify_score(score) for line, score in lines_score.items()}

    def classify_score(self, score):
        if score == "ineligible":
            return score
        elif score <= 0:
            return "economic"
        elif score in range(1, 3):
            return "regular"
        elif score >= 3:
            return "responsible"

