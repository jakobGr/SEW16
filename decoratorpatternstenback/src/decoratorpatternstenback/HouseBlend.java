package decoratorpatternstenback;

public class HouseBlend extends Beverage{
	
	public HouseBlend(){
		description = "HouseBlend";
	}

	@Override
	public double cost() {
		// TODO Auto-generated method stub
		return 2.30;
	}

}
