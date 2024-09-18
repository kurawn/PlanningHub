from django.shortcuts import render

from .models import Restriction, Detail


def restriction_list_view(request):
    restrictions = Restriction.objects.prefetch_related('details').all()
    return render(request, 'restriction_list.html', {'restrictions': restrictions})


def check_permission_htmx(request):
    if request.method == "POST":
        detail_ids = request.POST.getlist('details')
        selected_details = Detail.objects.filter(id__in=detail_ids)

        universal_codes = []
        other_codes = []
        permission_required = False

        for detail in selected_details:
            for code in detail.planning_codes.all():
                if code.category == "universal" and code.requires_permission:
                    permission_required = True
                    universal_codes.append(code.code)
                elif code.category == "other" and code.requires_permission:
                    permission_required = True
                    other_codes.append(code.code)

        if permission_required:
            response = {
                'result': "Planning permission required.",
                'universal_codes': universal_codes,
                'other_codes': other_codes,
            }
        else:
            response = {
                'result': "No planning permission required."
            }
        return render(request, 'permission_result.html', response)
