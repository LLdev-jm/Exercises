//Part One
class Vehicle{
    constructor (make,model,year){
        this.make = make;
        this.model = model;
        this.year = year;
    }
    honk(){
        return 'Beep.'
    }
    toString(){
        return `The vehicle is a ${this.make} ${this.model} ${this.year}`
    }
}

//Part Two

class Car extends Vehicle{
    constructor(make,model,year){
        super(make,model,year)
        this.numWheels = 4;
    }
}

//Part Three
class Motorcycle extends Vehicle{
    constructor(make,model,year){
        super(make,model,year);
        this.numWheels = 2;
    }
    revEngine(){
        return 'VROOM!'
    }
}

//Part Four
class Garage{
    constructor(capacity){
        this.capacity = capacity;
        this.vehicles = [];
    }
    add(newVeh) {
        if(!(newVeh instanceof Vehicle)){
            return 'Only vehicles are allowed';
        }
        if(this.vehicles.length >= this.capacity){
            return 'Sorry we are full';
        }else{
            this.vehicles.push(newVeh);
            return 'New vehicle added to array'
        }
    }
}