import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, ' ', p.pizza_name)

p = Pizza.objects.get(id=1)

print(p.pizza_name)
print(p.date_added)

toppings = p.topping_set.all()

for t in toppings:
    print(t.topping_name)