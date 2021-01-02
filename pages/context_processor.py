from pages.models import Page

def get_pages(request):
    pages= Page.objects.filter(visible=True).values_list("id", "title", "slug").order_by("order")#Solo quiero esos 3 datos que me muestre.

    return {
        "pages": pages
    }