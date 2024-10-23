package Geometry3d;

import Exeptions.NegativeRadiusExeption;
import Exeptions.NegativeSideException;
import Geometry2d.Circle;

import java.io.IOException;
import java.util.logging.*;

public class Cylinder {
    private static final Logger LOGGER = Logger.getLogger(Cylinder.class.getName());
    {
        try {
            FileHandler fileHandler = new FileHandler("/home/andrew/IdeaProjects/laba--5/cylinder.log");
            LOGGER.addHandler(fileHandler);
            LOGGER.setUseParentHandlers(false);
            fileHandler.setFormatter(new SimpleFormatter());
            LOGGER.setLevel(Level.FINEST);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private Circle bottom;
    private Double height;

    public Cylinder(Double R, Double H) throws NegativeSideException {
        if (H<=0) throw new NegativeSideException("Height <= 0");
        else height = H;

        try {
            bottom = new Circle(R);
        } catch (NegativeRadiusExeption e) {
            LOGGER.finest("Cylinder not created.");
            throw new RuntimeException(e);
        }
        LOGGER.finest("Cylinder created.");
    }

    public Double Volume() {
        LOGGER.finest("Volume calculated.");
        return bottom.area() * height;
    }
}
