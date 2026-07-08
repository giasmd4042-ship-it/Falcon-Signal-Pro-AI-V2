"""
Falcon Signal Pro AI V7
Signal Filter Engine
"""


class SignalFilter:

    def validate(
        self,
        signal,
        confidence,
        trend,
        strength_score
    ):

        reasons = []

        approved = True

        if signal == "HOLD":
            approved = False
            reasons.append("Signal is HOLD")

        if confidence < 70:
            approved = False
            reasons.append("Low Confidence")

        if trend == "SIDEWAYS":
            approved = False
            reasons.append("Sideways Market")

        if strength_score < 6:
            approved = False
            reasons.append("Weak Signal Strength")

        return {
            "approved": approved,
            "reasons": reasons
        }
