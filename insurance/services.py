import datetime


class RiskCalculator:
    def calculate_score(self, profile_data):
        base_score = self.__calculate_base_score(profile_data)

        lines_score = {
            "auto": base_score,
            "disability": base_score,
            "home": base_score,
            "life": base_score,
        }

        self.__consider_dependents(lines_score, profile_data)
        self.__consider_marital_status(lines_score, profile_data)
        self.__consider_vehicle(lines_score, profile_data)
        self.__consider_income(lines_score, profile_data)
        self.__consider_house_mortage(lines_score, profile_data)
        self.__consider_senior_age(lines_score, profile_data)

        return {
            line: self.__classify_score(score) for line, score in lines_score.items()
        }

    def __calculate_base_score(self, profile_data):
        base_score = sum([int(rq) for rq in profile_data["risk_questions"]])

        if int(profile_data["age"]) < 30:
            base_score -= 2
        elif int(profile_data["age"]) in range(30, 41):
            base_score -= 1

        return base_score

    def __consider_dependents(self, lines_score, profile_data):
        if int(profile_data["dependents"]) >= 1:
            lines_score.update(
                {
                    line: score + 1
                    for line, score in lines_score.items()
                    if line in ["life", "disability"]
                }
            )

    def __consider_marital_status(self, lines_score, profile_data):
        if profile_data["marital_status"] == "married":
            lines_score["life"] += 1
            lines_score["disability"] += 1

    def __consider_vehicle(self, lines_score, profile_data):
        if "vehicle" not in profile_data:
            lines_score["auto"] = "ineligible"
        elif int(profile_data["vehicle"]["year"]) >= (
            datetime.datetime.today().year - 5
        ):
            lines_score["auto"] += 1

    def __consider_income(self, lines_score, profile_data):
        if "income" not in profile_data or float(profile_data["income"]) <= 0:
            lines_score["disability"] = "ineligible"
        elif float(profile_data["income"]) > 200000:
            lines_score = {line: score - 1 for line, score in lines_score.items()}

    def __consider_house_mortage(self, lines_score, profile_data):
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

    def __consider_senior_age(self, lines_score, profile_data):
        if int(profile_data["age"]) > 60:
            lines_score["life"] = "ineligible"
            lines_score["disability"] = "ineligible"

    def __classify_score(self, score):
        if score == "ineligible":
            return score
        elif score <= 0:
            return "economic"
        elif score in range(1, 3):
            return "regular"
        elif score >= 3:
            return "responsible"

