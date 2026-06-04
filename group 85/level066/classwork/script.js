function LicensePlate(plateNum) {
  return { plateNum: plateNum }
}

function CreateCar(manufacturer, model, year, plateNum) {
  return {
    manufacturer: manufacturer,
    model: model,
    year: year,
    license: LicensePlate(plateNum)
  }
}
const CarPark = {
  capacity: 10,
  parkedCars: [],

  Park(car) {
    if (this.parkedCars.length >= this.capacity) {
      return false
    }
    const exists = this.parkedCars.find(c => c.license.plateNum === car.license.plateNum)
    if (exists) {
      return "ისედაც დგას"
    }

    this.parkedCars.push(car)
    return true
  },

  UnPark(plateNum) {
    const index = this.parkedCars.findIndex(c => c.license.plateNum === plateNum)
    if (index === -1) {
      return false
    }
    this.parkedCars.splice(index, 1)
    return true
  }
}