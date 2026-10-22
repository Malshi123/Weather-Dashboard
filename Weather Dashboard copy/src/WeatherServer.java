public class WeatherServer {
    public static void main(String[] args) {

        if (args.length==0) {
            System.out.println("Please enter the city name.");
            return;
        }
        String city = args[0].trim();

        if (city.equalsIgnoreCase("Colombo")) {
            System.out.println("🌧️ Rainy | Temperature: 28'C | Humidity:85%");
        } else if (city.equalsIgnoreCase("Kandy")) {
            System.out.println("⛅️ Cloudy | Temperature: 24'C | Humidity: 70%");
        } else if (city.equalsIgnoreCase("Galle")) {
            System.out.println("☀️ Windy | Temperature: 30'C | Humidity: 60%");
        } else if (city.equalsIgnoreCase("Kalutara")) {
            System.out.println("️🌦 Light Rainy️ | Temperature: 27'C | Humidity: 80%");
        } else {
            System.out.println("Data for this city is not available. (Try Colombo, Kandy, Galle, or Kalutara");
        }
    }

}
