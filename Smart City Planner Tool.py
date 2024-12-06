def calculate_solar_panels(population):
    # Simplified calculation: 1 solar panel per 10 people
    panels_needed = population // 10
    return panels_needed

def calculate_light_energy_saved(bulb):
    # Simplified calculation: 1 incandecent bulb requires 216kjh ,LEDs use at least 75% less energy than incandescent light bulbs
    light_energy_saved = (bulb*216)25//100
    return light_energy_saved

def calculate_wind_turbines(population):
    # Simplified calculation: 1 bulb requires 216kjh but 1 LED bulb requires 8kjh
    turbines_needed = population // 5000
    return turbines_needed

def calculate_waste_to_energy(waste_amount):
    # Assume 1 ton of waste generates 0.5 MW of energy
    energy_generated = waste_amount * 0.5
    return energy_generated

def generate_report(city_name, population, area,vehicles_count, waste_amount, bulb,car,truck,vans,bus,rickshaws):

    # Calculate energy 
    solar_panels = calculate_solar_panels( population)
    wind_turbines = calculate_wind_turbines(population)
    energy_from_waste = calculate_waste_to_energy(waste_amount)
    light_energy_saved = calculate_light_energy_saved(bulb)

    #avarage Energy Savings per mile kWh/mile
    #car 1.126kWh/mile
    #Truck 2.87kWh/mile
    #Van 1.964kWh/mile
    #Bus 4.953kWh/mile
    #Rickshaw 0.718kWh/mile
    #electric vehicles
    car_energy_saved = car*1.126
    Truck_energy_saved = truck*2.87
    Van_energy_saved = vans*1.964
    Bus_energy_saved = bus*4.953
    Rickshaw_energy_saved = rickshaws*0.718
    total_vehicles_energy_saved = car_energy_saved+Truck_energy_saved+Van_energy_saved+Bus_energy_saved+Rickshaw_energy_saved



    
    # Generate the text-based report
    print("\n--- Smart City Sustainability Report ---")
    print("City Name: {city_name}")
    print(f"Population: {population}")
    print(f"City Area: {area} km²\n")
    
    print(f"Energy Solutions:")
    print(f"  - Solar Panels Needed: {solar_panels} panels")
    print(f"  - Wind Turbines Needed: {wind_turbines} turbines")
    
    print("\nWaste Management:")
    print(f"  - Energy from Waste-to-Energy: {energy_from_waste} MW")

    print("\nLight solutionS")
    print(f"  - Energy saved if you use LED bulbs: {light_energy_saved} kjh")

    print("\nTransportation solutions")
    print(f"  - Energy saved from {vehicles_count} Electric vehicles: {total_vehicles_energy_saved} kwh/mile")
    
    print("\n--- Sustainability Summary ---")
    total_savings = energy_from_waste * 100  
    print(f"  - Total CO2 Savings per year: {total_savings} tons")


def main():
 

    print("-----Welcome to the Smart City Planner Tool!-----")
    city_name = input("\nEnter the city name: ")
    population = int(input("Enter the population size: "))
    area = float(input("Enter the city area in square kilometers: "))
    energy = float(input("Enter the total energy consumed in the cityin Mkh: "))

    #Initiallising the variables
    vehicles_count=0
    waste_amount=0
    bulb=0
    car=0
    truck=0
    rickshaws=0
    bus=0
    vans=0
    
    #Menu to Enter data
    while True:
        print("\n\n-----Please enter the data-----")
        print("\n\n\n 1  Enter transportation data")
        print(" 2  Enter waste generated data")
        print(" 3  Enter number of incandecend light bulbs used")
        print(" 0  Exit and get the report ")
        option=eval(input("\n\nplease enter option(0-3):"))
    
        if option == 1:
            car = int(input("\n\nEnter the number of Eletric cars : "))
            truck = int(input("Enter the number of Eletric Trucks : "))
            rickshaws = int(input("Enter the number of Electric rickshaws : "))
            bus = int(input("Enter the number of Electric bus : "))
            vans = int(input("Enter the number of Electric Vans : "))
            vehicles_count = car+truck+rickshaws+bus+vans
    
        elif option == 2:
            waste_amount = float(input("\n\nEnter the amount of waste generated per year (in tons): "))

        elif option == 3:
            bulb = int(input("\n\nEnter the no:of incandecent bulbs used: "))
    
        elif option == 0:
            #Returns the Report
            generate_report(city_name, population, area, vehicles_count, waste_amount, bulb,car,truck,vans,bus,rickshaws)
            break
        else:
            print("\n\nenter a valid option")

            
if __name__ == "__main__":
    main()
