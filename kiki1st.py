code10 = 'OFR001'
code7 = 'OFR002'
code5 = 'OFR003'

class KikiShop:
    pkgs = []
    # pkgs = {}
    def __init__(self, base_delivery_cost, no_of_pkgs, no_of_vehicles, max_speed, max_carriage_weight):
        self.base_delivery_cost = base_delivery_cost
        self.no_of_pkgs = no_of_pkgs
        self.no_of_vehicles = no_of_vehicles
        self.max_speed = max_speed
        self.max_carriage_weight = max_carriage_weight

    def __str__(self):
        return f'Base cost: ${self.base_delivery_cost}, number of packages: {self.no_of_pkgs} \nNumber of vehicles: {self.no_of_vehicles}, max speed: {self.max_speed}kph, max carriage weight: {self.max_carriage_weight}kg'

    def input_pkg_detail(self):
        dict = {}
        for i in range(self.no_of_pkgs):
            pkg_id = input(f'Enter package {i+1} ID: ')
            pkg_weight = int(input(f'Enter package {i+1} weight: '))
            pkg_distance = int(input(f'Enter package {i+1} distance: '))
            offer_code = input(f'Enter package {i+1} offer code: ')
            dict = {f'pkg_id{i+1}': pkg_id, f'pkg_weight{i+1}': pkg_weight, f'pkg_distance{i+1}': pkg_distance, f'offer_code{i+1}': offer_code}
            # self.pkgs[f'pkg{i}'] = dict
            self.pkgs.append(dict)
    
    def deliveryCost(self):
        """
        Delivery cost = base cost + (weight * 10) + (distance * 5)
        code10 = 10% discount on d < 200km && w [70:200]kg
        code7 = 7% discount on d [50:150]km && w [50:200]kg
        code5 = 5% discount on d [50:250]km && w [10:150]kg
        """
        pkgs = self.pkgs
        # pkgs = [{'pkg_id1': 'pkg1', 'pkg_weight1': 5, 'pkg_distance1': 5, 'offer_code1': 'OFR001'}, {'pkg_id2': 'pkg2', 'pkg_weight2': 15, 'pkg_distance2': 5, 'offer_code2': 'OFR002'}, {'pkg_id3': 'pkg3', 'pkg_weight3': 10, 'pkg_distance3': 100, 'offer_code3': 'OFR003'}]
        for i in range(len(pkgs)):
            print(f'package {i+1}: ', end = '')
            # pkg = pkgs[f'pkg{i}']
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

    def deliveryTime(self):
        """
        Max load weight = max_carriage_weight
        Same max speed, same route, single route, nonstop
        Multiple shipments -> heavier first -> closer first
        Finish delivery comeback, deliver again (2*time)
        """
        # pkgs = self.pkgs
        pkgs = [{'pkg_id1': 'PKG1', 'pkg_weight1': 50, 'pkg_distance1': 20, 'offer_code1': 'OFR001', 'discount1': 0, 'total_cost1': 700}, {'pkg_id2': 'PKG2', 'pkg_weight2': 75, 'pkg_distance2': 125, 'offer_code2': 'OFR008', 'discount2': 0, 'total_cost2': 1475}, {'pkg_id3': 'PKG3', 'pkg_weight3': 175, 'pkg_distance3': 100, 'offer_code3': 'OFR003', 'discount3': 0, 'total_cost3': 2350}, {'pkg_id4': 'PKG4', 'pkg_weight4': 110, 'pkg_distance4': 60, 'offer_code4': 'OFR002', 'discount4': 105, 'total_cost4': 1395}, {'pkg_id5': 'PKG5', 'pkg_weight5': 155, 'pkg_distance5': 95, 'offer_code5': 'NA', 'discount5': 0, 'total_cost5': 2125}]
        max_weight = self.max_carriage_weight
        speed = self.max_speed
        vehicles = self.no_of_vehicles
        # print(pkgs)
        weight_objs = {}
        weight_obj = {}
        """
        Drivers
        """
        drivers = []
        for i in range(vehicles):
            drivers.append({'driver': i+1, 'pkgs': [], 'available_time': 0, 'available': True})
        # print(drivers)
        """
        Packages to deliver
        """
        for i in range(len(pkgs)):
            pkg = pkgs[i]
            # pkg = pkgs[f'pkg{i}']
            pkg_id = pkg['pkg_id{}'.format(i+1)]
            distance = pkg['pkg_distance{}'.format(i+1)]
            weight = pkg['pkg_weight{}'.format(i+1)]
            time = distance / speed
            weight_objs[weight] = {'index': i, 'pkg_id': pkg_id, 'time': time, 'weight': weight, 'distance': distance}
            # print(f'type of weight_ob[weight] is {type(int(weight_obj[weight]))}')
        
        to_deliver_pkg = {}
        print(weight_objs)
        def assign_driver(self, to_deliver_pkg, total_weight):
                min_avail = max_weight - total_weight
                weight_obj = {}
                max_obj = {}
                print(min_avail)
                for key in weight_objs.keys():
                    if key <= min_avail:
                        weight_obj[key] = weight_objs[key]
                print(max_obj)
                    # min_avail = max_weight - max(weight_objs.keys())
                print(min_avail)
                print(weight_obj)
                if len(weight_obj) == 0 and len(to_deliver_pkg) == 0:
                    key = max(weight_objs.keys())
                    # print(key)
                    to_deliver_pkg[key] = weight_objs.pop(key)
                elif len(weight_obj) > 0:
                    temp1 = max(weight_objs.keys())
                    temp2 = max(weight_obj.keys())
                    distance1 = weight_objs[temp1]['distance']
                    distance2 = weight_objs[temp2]['distance']
                    to_deliver_pkg[distance1] = weight_objs.pop(temp1)
                    to_deliver_pkg[distance2] = weight_objs.pop(temp2)
                    total_weight = temp1 + temp2
                    weight_obj.clear()
                    assign_driver(self, to_deliver_pkg, total_weight)
                if len(to_deliver_pkg) == 0:
                    return
                driver = {}
                for i in range(len(drivers)):
                    if drivers[i]['available'] == True:
                        driver = drivers[i]
                        break
                    mintime = min(drivers, key=lambda x: x['available_time'])
                    if drivers[i]['available_time'] == mintime['available_time']:
                        # print(len(to_deliver_pkg))
                        drivers[i]['available'] = True
                        driver = drivers[i]
                        break
                    
                print(driver)
                time = 0
                time_total = 0
                for i in range(len(to_deliver_pkg)):
                    driver['pkgs'].append(to_deliver_pkg[min(to_deliver_pkg.keys())]['pkg_id'])
                    pkg = to_deliver_pkg[min(to_deliver_pkg.keys())]
                    time = pkg['time']
                    driver['available'] = False
                    index = pkg['index']
                    pkgs[index]['delivered'] = True 
                    pkgs[index]['driver'] = driver['driver']
                    pkgs[index][f'estimated_delivery_time{index+1}_in_hours'] = time + driver['available_time']
                    to_deliver_pkg.pop(min(to_deliver_pkg.keys()))
                driver['available_time'] += time * 2
                # print(weight_objs)
        max_of_weight = 0
        for i in range(len(weight_objs)):
            # print(len(weight_objs))
            max_of_weight = max(weight_objs.keys())
            assign_driver(self, to_deliver_pkg, max_of_weight)
            print(len(weight_objs))
            if len(weight_objs) == 1:
                break
        print(drivers)
        print(max(weight_objs.keys()))
        print(len(to_deliver_pkg))
        to_deliver_pkg = weight_objs[max(weight_objs.keys())]
        # print(to_deliver_pkg)
        driver = {}
        for i in range(len(drivers)):
            mintime = min(drivers, key=lambda x: x['available_time'])
            if drivers[i]['available_time'] == mintime['available_time']:
                drivers[i]['available'] = True
                driver = drivers[i]
                driver['available'] = False
                driver['pkgs'].append(to_deliver_pkg['pkg_id'])
                driver['available_time'] += to_deliver_pkg['time'] * 2
        weight_objs.clear()
        to_deliver_pkg.clear()
        print(drivers)
        print(pkgs)

deliveryCost = KikiShop(100, 5, 2, 70, 200)
# print(deliveryCost)
# deliveryCost.input_pkg_detail()
# deliveryCost.deliveryCost()
deliveryCost.deliveryTime()