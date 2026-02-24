from django.views.generic import (
    TemplateView,
)

from home_pages.utils import TimeGreeting


class HomeView(TemplateView):
    """Контроллер представления главной страницы."""

    template_name = "home_pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["greeting"] = TimeGreeting.get_greeting()  # Применяем класс приветствия

        return context
