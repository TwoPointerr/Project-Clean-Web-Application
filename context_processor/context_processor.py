from django.core.exceptions import ObjectDoesNotExist

def get_Desks(request):
    try:
        if request.user.is_authenticated and not request.user.is_superuser:
            request.user.mcprofile
            mc_profile = request.user.mcprofile
            desks = mc_profile.desk_set.all()
            print(desks)
            return {'desks':desks}
        else:
            return {'desks':[]}

    except ObjectDoesNotExist:
        print("There is no restaurant here.")

# def get_Grievance(request):
#     grievance = Grievance.objects.all()
#     return {'grievances':grievance}