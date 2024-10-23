package Geometry2d;

import Exeptions.NegativeRadiusExeption;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.FileHandler;
import java.util.logging.Handler;
import java.util.logging.Logger;

public class Circle implements Figure {
    private static final Logger LOGGER = Logger.getLogger(Circle.class.getName());
    {
        try {
            FileHandler fileHandler = new FileHandler("/home/andrew/IdeaProjects/laba--5/figures.log");
            LOGGER.addHandler(fileHandler);
            LOGGER.setUseParentHandlers(false);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private final Double radius;

    public Circle(Double R) throws NegativeRadiusExeption {
        if (R <= 0) throw new NegativeRadiusExeption();
        else radius = R;
        LOGGER.severe("Circle created.");
    }

    public Double area() {
        LOGGER.severe("Area calculated.");
        return Math.PI * Math.pow(radius, 2);
    }

    public Double perimeter() {
        LOGGER.severe("perimeter calculated.");
        return 2 * Math.PI * radius;
    }

    public String ToString() {
        Map<String, Double> stringCircle = new HashMap<>();
        stringCircle.put("Radius", radius);
        stringCircle.put("Area", area());
        stringCircle.put("Perimeter", perimeter());

        LOGGER.severe("CircleToString finished.");
        return stringCircle.toString();
    }
}
