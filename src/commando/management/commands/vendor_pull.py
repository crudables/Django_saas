from django.core.management.base import BaseCommand
from typing import Any
import helpers
from django.conf import settings

STATICFILES_VENDOR_DIR = getattr(settings,"STATICFILES_VENDOR_DIR")
VENDOR_STATICFILES = {
    "flowbite.min.css":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    }
class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading Static Files")
        completed_url = []
        for name,url in VENDOR_STATICFILES.items():
            outpath = STATICFILES_VENDOR_DIR/name
            dl_success = helpers.download_to_local(url,outpath)
            if dl_success:
                completed_url.append(url)
            
            else: 
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )
        
        if set(completed_url) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated vendor static files")
            )

        else:
            self.stdout.write(
                self.style.WARNING("Some files were not updated")
            )