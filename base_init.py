import json
import os
from django.core.management import call_command


def generate_fixture():
    products = []
    for i in range(1, 301):
        product = {
            "model": "products.product",
            "pk": i,
            "fields": {
                "name": f"Produto {i}",
                "status": "available" if i % 3 == 0 else "reserved" if i % 3 == 1 else "unavailable",
            }
        }
        products.append(product)

    customers = []
    for i in range(1, 41):
        customer = {
            "model": "customers.customer",
            "pk": i,
            "fields": {
                "name": f"Cliente {i}"
            }
        }
        customers.append(customer)

    data = products + customers

    fixture_file = 'db_fixture.json'
    with open(fixture_file, 'w') as f:
        json.dump(data, f, indent=4)

    return fixture_file


def load_fixture(fixture_file):
    call_command('loaddata', fixture_file)
    print("Data successfully loaded into the database.")


def main():
    fixture_file = generate_fixture()
    load_fixture(fixture_file)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
    import django
    django.setup()
    main()
