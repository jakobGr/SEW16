package decoratorpatternstenback;

public class Milk extends CondimentDecorator{
	Beverage beverage;

	public Milk(Beverage beverage){
		this.beverage = beverage;
	}
	public String getDescription() {
		// TODO Auto-generated method stub
		return beverage.getDescription() + ", Milk";
	}
	public double cost() {
		// TODO Auto-generated method stub
		return .6 + beverage.cost();
	}
	
}
