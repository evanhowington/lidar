"""
visualizing lidar data for youtube video
"""

#%%
# Import packages
import numpy as np  # Laspy is a python library for reading, modifying and creating LAS LiDAR files.
import laspy  # Open3D is an open-source library that supports rapid development of software that deals with 3D data
import open3d as o3d  # NumPy is the fundamental package for scientific computing in Python.

#%%
# import lidar .las data and assign to variable
las = laspy.read('lidar/las_data/points1.las')

#%%
# examine the available features for the lidar file we have read
list(las.point_format.dimension_names)

#%%
set(list(las.classification))

#%%
# Creating, Filtering, and Writing Point Cloud Data
# To create 3D point cloud data, we can stack together with the X, Y, and Z dimensions, using Numpy like this.
point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))

#%%
# 3D Point Cloud Visualization
# Laspy has no visualization methods so that we will use the open3d library. We first create the open3D geometries and pass the point data we have created earlier. Finally, we use the open3d visualization to draw geometries.
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])


