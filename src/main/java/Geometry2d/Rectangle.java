package Geometry2d;

import Exeptions.NegativeSideException;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.*;

public class Rectangle implements Figure{
    private static final Logger LOGGER = Logger.getLogger(Rectangle.class.getName());
    {
        try {
            Handler fileHandler = new FileHandler("/home/andrew/IdeaProjects/laba--5/figures.log");
            LOGGER.addHandler(fileHandler);
            LOGGER.setUseParentHandlers(false);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private final Double a;
    private final Double b;

    public Rectangle(Double A, Double B) throws NegativeSideException {
        if (A <= 0) throw new NegativeSideException("A<=0");
        if (B <= 0) throw new NegativeSideException("B<=0");
        else {a = A; b = B;}
        LOGGER.info("Rectangle created.");
    }

    public Double area() {
        LOGGER.info("Area calculated.");
        return a * b;
    }

    public Double perimeter() {
        LOGGER.info("Perimeter calculated.");
        return a * 2 + b * 2;
    }

    public String ToString() {
        Map<String, Double> stringRectangle = new HashMap<>();
        stringRectangle.put("A", a);
        stringRectangle.put("B", a);
        stringRectangle.put("Area", area());
        stringRectangle.put("Perimeter", perimeter());

        LOGGER.info("RectangleToString finished.");
        return stringRectangle.toString();
    }
}
