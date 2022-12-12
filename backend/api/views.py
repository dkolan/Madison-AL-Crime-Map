from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import *

@api_view(['GET'])
def getIncident(request):
    incident = {
        'Datetime': datetime(2022, 12, 2, 7, 50, 22, 0),
        'Case Number': '22M005979',
        'Description': 'DOMESTIC VIOLENCE 3RD-CRIMINAL MISCHIEF 3RD',
        'Location': '100 Block of MEADOW DR MAD'
    }
    return Response(incident)