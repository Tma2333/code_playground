#include <math.h>


struct double3 {
    double x;
    double y;
    double z;
};

/**
 * GPS(WGS84) to ECEF conversion function. Formula refer from: https://www.mathworks.com/help/aeroblks/llatoecefposition.html
 * WGS84 parameter obtained from: https://confluence.qps.nl/qinsy/en/world-geodetic-system-1984-wgs84-29855173.html
 * @param lat: latitude in radians
 * @param lon: longitude in radians
 * @param alt: altitude in meter
 */
void gps2ecef(double lat, double lon, double alt, double3 &ecef){
    const double a = 6378137.0;           // semi-major axis (WGS84) unit: m
    const double f = 1/298.257223563;     // flatening factor
    double latS, rS;                      // Geocentric Latitude, Surface Point Radius
    
    latS = atan(pow((1 - f), 2) * tan(lat));
    rS = sqrt(pow(a, 2) / (1 + ((1 / pow((1 - f), 2) - 1.0) * (pow(sin(latS), 2)))));
        
    ecef.x = rS * cos(latS) * cos(lon) + alt * cos(lat) * cos(lon);          // unit:m
    ecef.y = rS * cos(latS) * sin(lon) + alt * cos(lat) * sin(lon);          // unit:m
    ecef.z = rS * sin(latS) + alt * sin(lat);                                // unit:m
}