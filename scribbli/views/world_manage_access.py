from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from scribbli.models import World, WorldShare


class WorldManageAccess(LoginRequiredMixin, DetailView):
    model = World
    template_name = 'universe/world-manage-access.html'

    toggle_fields = ["can_create_characters", "can_create_stories", "can_edit_world"]

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            return Http404()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        """
        Sample POST payloads:

        Add new user
        ------------
            {
              'csrfmiddlewaretoken': '<token>',
              'username': 'something',
              'can_create_characters': 'on',
              'can_create_stories': 'on',
              'can_edit_world': 'on',
              'action': 'add',
            }


        """
        print(self.request.POST.dict())
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            return Http404()
        action = self.request.POST.get("action")
        if not action:
            return HttpResponse(status=400)
        action = action.lower()
        if action == 'remove' and 'id' in self.request.POST:
            share = WorldShare.objects.select_related("user").get(id=self.request.POST['id'])
            share.delete()
            return HttpResponse(
                f'{share.user.username} access removed.',
                content_type='text/plain',
                status=200,
            )
        elif action == 'edit' and 'id' in self.request.POST:
            share = WorldShare.objects.select_related("user").get(id=self.request.POST['id'])
            for field in self.toggle_fields:
                setattr(share, field, (self.request.POST.get(field) == "on"))
            share.save()
            return render(self.request, "_partials/world-manage-access-share-row.html", {"share": share})
            # return HttpResponse(
            #     f'{share.user.username} access edited.',
            #     content_type='text/plain',
            #     status=200,
            # )
        elif action == 'add' and 'username' in self.request.POST:
            username = self.request.POST['username']
            target_user = self.request.user.__class__.objects.filter(username=username).first()
            if target_user is None:
                return HttpResponse(
                    f'That user does not exist.',
                    content_type='text/plain',
                    status=404,
                )
            if target_user.id == self.object.owner.id or WorldShare.objects.filter(user=target_user, world=self.object).exists():
                return HttpResponse(
                    f'{username} already has access.',
                    content_type='text/plain',
                    status=409,
                )
            WorldShare.objects.get_or_create(
                user=target_user,
                world=self.object,
                defaults={
                    key: (value == "on") for key, value in self.request.POST.items()
                    if key in self.toggle_fields
                },
            )
            return HttpResponse(
                f'Successfully added {username}.',
                content_type='text/plain',
                status=201,
                headers={"HX-Refresh": "true"},
            )
        return HttpResponse(status=400)

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            'share_list': self.get_share_list()
        })
        return kwargs

    def get_share_list(self):
        world_shares = WorldShare.objects.select_related("user").filter(world=self.object)
        return list(world_shares)
