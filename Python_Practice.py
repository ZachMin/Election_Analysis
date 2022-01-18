counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "ElPaso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties")
for i in range(len(counties)):
    print(counties[i])