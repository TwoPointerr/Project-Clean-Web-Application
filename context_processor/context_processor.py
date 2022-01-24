from dashboard.models import Desk, Folders

def get_Desks(request):
    desks = Desk.objects.all()
    return {'desks':desks}
