package MicroService;

public class Hello{
    public static void main(String[] args) {
	while (true) {
	
       System.out.println("Hello World, Saujan is trying containers");
	

	try {
		Thread.sleep(10000);

	} catch (InterruptedException e){
		e.printStackTrace();
	   }
	}
    }
}
