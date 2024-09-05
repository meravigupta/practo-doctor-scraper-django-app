import requests
import math
import json
from django.core.management.base import BaseCommand
from doctors.models import Doctor
from scrapy.http import HtmlResponse

class Command(BaseCommand):
    help = 'Scrape doctors data from Practo'

    def handle(self, *args, **kwargs):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }
        response = requests.get('https://www.practo.com/mumbai/doctors', headers=headers)
        page_source = HtmlResponse(url="my HTML string", body=response.text, encoding='utf-8')

        total_count = page_source.xpath("//h1[@class='u-xx-large-font u-bold']//text()").extract()[0].split(' ')[0]
        page_count = math.ceil(int(total_count)/10)

        for i in range(page_count + 1):
            response_1 = requests.get(f'https://www.practo.com/mumbai/doctors?page={i}', headers=headers)
            page_source_1 = HtmlResponse(url="my HTML string", body=response_1.text, encoding='utf-8')

            doctors_lists = page_source_1.xpath("//div[@class='u-border-general--bottom']//script[@type='application/ld+json']//text()").extract()
            for doctors_list in doctors_lists:
                all_doctors = json.loads(doctors_list)

                # Provide default values if postal_code or other fields are missing
                doctor, created = Doctor.objects.get_or_create(
                    name=all_doctors.get('name', '-'),
                    defaults={
                        'specialization': all_doctors.get('@type', '-'),
                        'address': all_doctors.get('address', {}).get('streetAddress', '-'),
                        'postal_code': all_doctors.get('address', {}).get('postalCode') or 'N/A',  # Use 'N/A' or another default value
                        'address_region': all_doctors.get('address', {}).get('addressRegion', '-'),
                        'address_locality': all_doctors.get('address', {}).get('addressLocality', '-'),
                        'address_country': all_doctors.get('address', {}).get('addressCountry', '-'),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Doctor {doctor.name} created'))
                else:
                    self.stdout.write(f'Doctor {doctor.name} already exists')

