package decoratorpatternstenback;

public class sternbackcoffeeshop {
	
	public static void main(String args[]){
		Beverage beverage = new HouseBlend();
		System.out.println(beverage.getDescription() + " $" + beverage.cost());
		
		Beverage beverage2 = new DarkRoast();
		beverage2 = new Milk(beverage2);
		beverage2 = new Milk(beverage2);
		beverage2 = new Whip(beverage2);
		System.out.println(beverage2.getDescription() + " $" + beverage2.cost());
		

		Beverage beverage3 = new DarkRoast();
		beverage3 = new Milk(beverage3);
		beverage3 = new Mocha(beverage3);
		beverage3 = new Whip(beverage3);
		System.out.println(beverage3.getDescription() + " $" + beverage3.cost());
	}

}
