import mensuration; #use any now
print(mensuration.circumference_circle(7))
print(mensuration.area_circle(7))
#or


import mensuration as ms;
print(ms.circumference_circle(7))
print(ms.area_circle(7))
# # or 

from mensuration import area_circle;
# can only use whats imported
print(area_circle(7))

# or
from mensuration import area_sphere as asp
print(asp(7))

