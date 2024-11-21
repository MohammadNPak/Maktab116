from django.core.management.base import BaseCommand
from blog.models import Post
import json

class Command(BaseCommand):
    help = "report all posts"
    
    def handle(self, *args, **options):
        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(
        #         self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
        #     )
        
        posts = Post.objects.all()
        with open("post_reports.json","a",encoding="utf8") as fp:
            data = list(Post.objects.all().values())
            for post in data:
                post['created_at'] = post['created_at'].strftime("%Y-%m-%d %H:%M:%S")
            json.dump(data,fp)
        self.stdout.write(self.style.SUCCESS('Successfully saved reportpost'))