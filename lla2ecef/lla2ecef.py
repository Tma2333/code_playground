import numpy as np

def lla2ecef(lat, lon, alt, model = 'WGS84', f = None, a = None):
    """
	Reference: https://www.mathworks.com/help/aeroblks/llatoecefposition.html
	WGS84 Parameter from: https://confluence.qps.nl/qinsy/en/world-geodetic-system-1984-wgs84-29855173.html
	"""
    if model not in ('WGS84', 'geocentric', 'custom'):
	    raise ValueError('Currently only support WGS84, geocentric, or custom model') 
  
	# default
    if model == 'WGS84':
	    f = np.float64(1/298.257223563)
	    a = np.float64(6378137.0) # m
  
    if model == 'geocentric':
	    f = 0.0
	    if a == None:
		    a = np.float64(6378137.0) # m
      
    if model == 'custom':
	    if f == None:
		    raise ValueError ('Missing kwarg (f: flattening factor) for custom model')
	    elif a == None:
		    raise ValueError ('Missing kwarg (a: semi-major axis) for custom model')
	    elif a == None and f == None:
	    	raise ValueError ('Missing kwarg (f: flattening factor, a: semi-major axis) for custom model')
      
	# math
    lat_r = np.radians(lat) # radians
    lon_r = np.radians(lon) # radians
    lat_s = np.arctan((1-f)**2*np.tan(lat_r)) # radians
    r_s = np.sqrt(a**2/(1+((1/(1-f)**2)-1)*(np.sin(lat_s)**2))) # m
  
    ecef_x = r_s*np.cos(lat_s)*np.cos(lon_r) + alt*np.cos(lat_r)*np.cos(lon_r) # m
    ecef_y = r_s*np.cos(lat_s)*np.sin(lon_r) + alt*np.cos(lat_r)*np.sin(lon_r) # m
    ecef_z = r_s*np.sin(lat_s) + alt*np.sin(lat_r) # m
  
    return ecef_x, ecef_y, ecef_z