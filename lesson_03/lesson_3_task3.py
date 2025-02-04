from address import Address
from mailing import Mailing

from_address = Address("347340", "Волгодонск", "Ленина", "64", "20")
to_address = Address("347340", "Волгодонск", "Степная", "100", "1")
my_mailing = Mailing(to_address,from_address, 300, "FD11111111")

print(my_mailing)
