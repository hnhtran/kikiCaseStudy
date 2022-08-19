code10 = 'OFR001'
code7 = 'OFR002'
code5 = 'OFR003'

class KikiShop:
    pkgs = []
    def __init__(self, base_delivery_cost, no_of_pkgs):
        self.base_delivery_cost = base_delivery_cost
        self.no_of_pkgs = no_of_pkgs

    def __str__(self):
        return f'Base cost: ${self.base_delivery_cost}, number of packages: {self.no_of_pkgs}'

    def input_pkg_detail(self):
        dict = {}
        for i in range(self.no_of_pkgs):
            pkg_id = input(f'Enter package {i+1} ID: ')
            pkg_weight = int(input(f'Enter package {i+1} weight: '))
            pkg_distance = int(input(f'Enter package {i+1} distance: '))
            offer_code = input(f'Enter package {i+1} offer code: ')
            dict = {f'pkg_id{i+1}': pkg_id, f'pkg_weight{i+1}': pkg_weight, f'pkg_distance{i+1}': pkg_distance, f'offer_code{i+1}': offer_code}
            self.pkgs.append(dict)
    
    def deliveryCost(self):
        """
        Delivery cost = base cost + (weight * 10) + (distance * 5)
        code10 = 10% discount on d < 200km && w [70:200]kg
        code7 = 7% discount on d [50:150]km && w [50:200]kg
        code5 = 5% discount on d [50:250]km && w [10:150]kg
        """
        pkgs = self.pkgs
        print(self.pkgs)
        # pkgs = [{'pkg_id1': 'pkg1', 'pkg_weight1': 5, 'pkg_distance1': 5, 'offer_code1': 'OFR001'}, {'pkg_id2': 'pkg2', 'pkg_weight2': 15, 'pkg_distance2': 5, 'offer_code2': 'OFR002'}, {'pkg_id3': 'pkg3', 'pkg_weight3': 10, 'pkg_distance3': 100, 'offer_code3': 'OFR003'}]
        for i in range(len(pkgs)):
            print(f'package {i+1}: ', end = '')
            pkg = pkgs[i]
            discount = pkg[f'discount{i+1}'] = 0
            total_cost = f'total_cost{i+1}'
            pkg_id = pkg['pkg_id{}'.format(i+1)]
            distance = pkg['pkg_distance{}'.format(i+1)]
            weight = pkg['pkg_weight{}'.format(i+1)]
            offer_code = pkg['offer_code{}'.format(i+1)]
            cost = self.base_delivery_cost + (weight * 10) + (distance * 5)
            if (offer_code == code10) and (distance < 200) and (weight in range(70, 200)):
                    discount = int(cost * 0.1)
            elif (offer_code == code7) and (distance in range(50, 150)) and (weight in range(50, 200)):
                    discount = int(cost * 0.07)
            elif (offer_code == code5) and (distance in range(50, 250)) and (weight in range(10, 150)):
                    discount = int(cost * 0.05)
            pkg[f'discount{i+1}'] = discount
            pkg[total_cost] = cost - discount
            print(f'{pkg_id} {discount} {pkg[total_cost]}')
                

deliveryCost = KikiShop(100, 3)
# print(deliveryCost)
deliveryCost.input_pkg_detail()
deliveryCost.deliveryCost()