import pandas as pd
from openpyxl import load_workbook
from django.core.management.base import BaseCommand
from main.models import Info
from django.core.files import File
import os


class Command(BaseCommand):
    help = 'Save data from Excel to MyModel'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        excel_file = options['excel_file']
        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            latitude=row['latitude']
            longitude=row['longitude']
            name=row['name']
            floor=row['floor']
            depart=row['depart']
            near=row['near']
            image=row['image']
            if pd.notnull(image):  # 이미지 필드가 비어 있지 않고, NaN 값이 아닌 경우에만 처리
                if isinstance(image, str) and os.path.exists(image):
                    with open(image, 'rb') as file:
                        relative_path = '/'.join(image.split('/')[2:])
                        info = Info(latitude=latitude, longitude=longitude, name=name, floor=floor, depart=depart, near=near)
                        info.image = relative_path
                        info.save()
                else:
                    print(f"Invalid image path: {image}")
            else:
                info = Info(latitude=latitude, longitude=longitude, name=name, floor=floor, depart=depart, near=near)
                info.save()
                print("Empty image field, skipping...")

        self.stdout.write(self.style.SUCCESS('Data saved successfully!'))
