from django.core.management.base import BaseCommand
from employees.models import Department, Employee, Attendance, Performance
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake employee, attendance, and performance data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        departments = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']
        for name in departments:
            Department.objects.get_or_create(name=name)

        for _ in range(50):
            dept = Department.objects.order_by('?').first()
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=dept
            )

            for _ in range(5):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date='-60d', end_date='today'),
                    status=random.choice(['P', 'A', 'L'])
                )

                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS("✅ Fake data seeded successfully!"))
