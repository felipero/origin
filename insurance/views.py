from rest_framework import viewsets
from rest_framework.response import Response
from .services import RiskCalculator


class RiskProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for calculating and retrieving the risk profile.
    """
